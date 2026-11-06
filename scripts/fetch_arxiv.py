#!/usr/bin/env python3
"""从 arXiv（可选 HuggingFace Daily Papers）抓取原生多模态相关论文。

流程：抓取 → 负向过滤 → 关键词加权打分 → 归类到赛道 → 与历史库去重
      → 仅把「首次出现」的论文写入 docs/<赛道>.md 的标记表格。

用法：
  python scripts/fetch_arxiv.py                 # 增量（默认回溯 45 天）
  python scripts/fetch_arxiv.py --days 365      # 首次建库，回填一年
  python scripts/fetch_arxiv.py --dry-run       # 只看会写什么，不动文件
  python scripts/fetch_arxiv.py --category video-reasoning
  python scripts/fetch_arxiv.py --sources arxiv,hf
"""

from __future__ import annotations

import argparse
import re
import sys
import time
from datetime import timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from common import (
    ARXIV_API,
    DATA,
    DOCS,
    HF_PAPERS_API,
    arxiv_date_range,
    clean_text,
    http_get,
    insert_table_rows,
    load_config,
    log,
    md_escape,
    parse_arxiv_feed,
    parse_date,
    read_json,
    short_authors,
    shorten,
    today_utc,
    warn,
    write_json,
)

PAPER_STORE = DATA / "papers.json"


# ─── 打分与分类 ────────────────────────────────────────────────────────────

def score_paper(
    paper: Dict[str, Any], category: Dict[str, Any], weights: Dict[str, Any]
) -> Tuple[float, int]:
    """返回 (加权总分, strong 命中次数)。strong 命中数用于质量闸门。"""
    title = paper["title"].lower()
    abstract = paper["abstract"].lower()
    score = 0.0
    strong_hits = 0
    for level, terms in (category.get("keywords") or {}).items():
        w = weights.get(level) or {}
        w_title, w_abs = float(w.get("title", 0)), float(w.get("abstract", 0))
        for term in terms:
            t = term.lower()
            if t in title:
                score += w_title
                strong_hits += 1 if level == "strong" else 0
            elif t in abstract:
                score += w_abs
                strong_hits += 1 if level == "strong" else 0
    return score, strong_hits


def is_negative(paper: Dict[str, Any], negatives: List[str]) -> bool:
    text = f"{paper['title']} {paper['abstract']}".lower()
    return any(n.lower() in text for n in negatives)


def has_modality_anchor(paper: Dict[str, Any], anchors: List[str]) -> bool:
    text = f"{paper['title']} {paper['abstract']}".lower()
    return any(a.lower() in text for a in anchors)


def classify(
    paper: Dict[str, Any], config: Dict[str, Any], allowed: Optional[set[str]] = None
) -> Optional[Tuple[str, float]]:
    """返回 (赛道 id, 最高分)；不过闸门则返回 None。

    三道闸门：模态锚点 → strong 关键词命中 → 最低分。
    allowed 限定候选赛道——单赛道运行时必须传，否则论文会被分到没在跑的赛道里丢掉。
    """
    filters = (config["meta"].get("filters") or {})
    anchors = filters.get("modality_anchors") or []
    require_strong = bool(filters.get("require_strong", False))
    if anchors and not has_modality_anchor(paper, anchors):
        return None

    weights = config["weights"]
    best: Optional[Tuple[str, float, int]] = None
    for cat in config["categories"]:
        if allowed is not None and cat["id"] not in allowed:
            continue
        s, strong_hits = score_paper(paper, cat, weights)
        if best is None or s > best[1]:
            best = (cat["id"], s, strong_hits)

    if best is None:
        return None
    cat_id, score, strong_hits = best
    if require_strong and strong_hits == 0:
        return None
    if score < float(config["meta"]["min_score"]):
        return None
    return cat_id, round(score, 2)


# ─── 抓取 ──────────────────────────────────────────────────────────────────

def fetch_arxiv_for_category(
    category: Dict[str, Any], config: Dict[str, Any], days: int
) -> List[Dict[str, Any]]:
    date_filter = arxiv_date_range(days)
    per_query = int(config["meta"]["arxiv_max_per_query"])
    collected: Dict[str, Dict[str, Any]] = {}

    for query in category.get("arxiv_queries", []):
        params = {
            "search_query": f"({query}) AND {date_filter}",
            "start": 0,
            "max_results": per_query,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        resp = http_get(ARXIV_API, params=params, timeout=40)
        if resp is None:
            warn(f"[{category['id']}] 查询失败，跳过: {query}")
            continue

        papers = parse_arxiv_feed(resp.content)
        fresh = 0
        for p in papers:
            if p["arxiv_id"] not in collected:
                collected[p["arxiv_id"]] = p
                fresh += 1
        log(f"  [{category['id']}] {len(papers):>3} 条 / 新增 {fresh:>3} ← {query}")
        time.sleep(3)  # arXiv 建议请求间隔 ≥3s

    return list(collected.values())


def fetch_hf_daily(days: int) -> List[Dict[str, Any]]:
    """HuggingFace Daily Papers：提供社区热度（upvotes）这一额外信号。"""
    papers: List[Dict[str, Any]] = []
    seen: set[str] = set()
    today = today_utc()

    for offset in range(days):
        date_str = (today - timedelta(days=offset)).strftime("%Y-%m-%d")
        resp = http_get(HF_PAPERS_API, params={"date": date_str}, retries=2, base_wait=1.5)
        if resp is None:
            continue
        try:
            payload = resp.json()
        except ValueError:
            continue
        if not isinstance(payload, list):
            continue

        for item in payload:
            info = item.get("paper", item) if isinstance(item, dict) else {}
            pid = (info.get("id") or "").strip()
            if not pid or pid in seen:
                continue
            seen.add(pid)
            papers.append(
                {
                    "arxiv_id": pid,
                    "title": info.get("title", ""),
                    "abstract": info.get("summary", ""),
                    "published": (info.get("publishedAt") or date_str)[:10],
                    "primary_category": "",
                    "categories": [],
                    "authors": [a.get("name", "") for a in info.get("authors", []) if isinstance(a, dict)],
                    "url": f"https://arxiv.org/abs/{pid}",
                    "hf_upvotes": int(item.get("upvotes") or 0),
                    "github_repo": info.get("githubRepo") or "",
                }
            )
        if papers and offset > 3 and len(papers) > 400:
            break

    log(f"  [hf] 取回 {len(papers)} 条 Daily Papers")
    return papers


# ─── 渲染 ──────────────────────────────────────────────────────────────────

_BOILERPLATE = re.compile(
    r"^(in this (paper|work|study)|we (propose|present|introduce|study|develop)|"
    r"this (paper|work|study) (proposes|presents|introduces)|here,? we)\b[,:]?\s*",
    re.I,
)


def contribution_of(paper: Dict[str, Any], limit: int = 95) -> str:
    """把摘要压成一句"核心贡献"：去掉套话开头，再按句子边界截断。"""
    text = _BOILERPLATE.sub("", clean_text(paper.get("abstract", "")), count=1).strip()
    if text:
        text = text[0].upper() + text[1:]
    return shorten(text or paper.get("title", ""), limit)


def render_row(paper: Dict[str, Any], category_id: str) -> Tuple[str, str]:
    date = paper.get("published") or "—"
    title = md_escape(paper["title"])
    authors = md_escape(short_authors(paper.get("authors", [])))
    contribution = md_escape(contribution_of(paper))

    primary = (paper.get("primary_category") or "").strip()
    link = f"[📄 {paper['arxiv_id']}]({paper['url']})"
    meta = [f"`{primary}`"] if primary else []
    if paper.get("hf_upvotes"):
        meta.append(f"🔥{paper['hf_upvotes']}")
    if paper.get("github_repo"):
        meta.append(f"[💻]({paper['github_repo']})")
    if paper.get("via") == "hf":
        meta.append("🤗")

    row = f"| {date} | **{title}** | {authors} | {contribution} | {link} {' '.join(meta)} |".rstrip()
    # 用完整 URL 作去重键：arXiv ID 之间存在前缀关系（2610.1056 / 2610.10563）
    return f"(https://arxiv.org/abs/{paper['arxiv_id']})", row


# ─── 主流程 ────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(description="抓取 arXiv 原生多模态论文并写入 docs/")
    parser.add_argument("--days", type=int, default=None, help="回溯天数（默认取配置 lookback_days）")
    parser.add_argument("--category", action="append", help="只跑指定赛道（可多次指定）")
    parser.add_argument("--sources", default="arxiv,hf", help="数据源：arxiv,hf")
    parser.add_argument("--dry-run", action="store_true", help="不写文件")
    parser.add_argument("--force", action="store_true", help="忽略历史库，全部重新插入")
    args = parser.parse_args()

    config = load_config()
    days = args.days or int(config["meta"]["lookback_days"])
    categories = config["categories"]
    if args.category:
        wanted = {c.lower() for c in args.category}
        categories = [c for c in categories if c["id"] in wanted]
        if not categories:
            warn(f"未找到赛道: {args.category}")
            return 1

    sources = {s.strip() for s in args.sources.split(",") if s.strip()}
    negatives = config.get("negative") or []
    log(f"回溯 {days} 天｜赛道 {len(categories)} 个｜数据源 {sorted(sources)}")

    store = read_json(PAPER_STORE, {"updated": "", "papers": {}})
    known: Dict[str, Any] = store.get("papers", {})
    today_str = today_utc().strftime("%Y-%m-%d")

    # 1) 按赛道抓取 + 打分归类
    by_category: Dict[str, List[Dict[str, Any]]] = {c["id"]: [] for c in categories}
    seen_ids: set[str] = set()
    allowed_ids = {c["id"] for c in categories}
    total_fetched = 0

    for cat in categories:
        if "arxiv" not in sources:
            continue
        log(f"━━ {cat['emoji']} {cat['name']} ({cat['id']}) ━━")
        papers = fetch_arxiv_for_category(cat, config, days)
        total_fetched += len(papers)

        for p in papers:
            if p["arxiv_id"] in seen_ids:
                continue
            seen_ids.add(p["arxiv_id"])
            if is_negative(p, negatives):
                continue
            verdict = classify(p, config, allowed_ids)
            if verdict is None:
                continue
            best_id, score = verdict
            p["score"] = score
            p["via"] = "arxiv"
            if best_id in by_category:
                by_category[best_id].append(p)

    # 2) HuggingFace 作为补充信号（同样走一遍分类，命中已抓到的论文则合并 upvotes）
    if "hf" in sources:
        log("━━ 🤗 HuggingFace Daily Papers ━━")
        indexed = {p["arxiv_id"]: p for lst in by_category.values() for p in lst}
        for p in fetch_hf_daily(min(days, 14)):
            if p["arxiv_id"] in indexed:
                indexed[p["arxiv_id"]]["hf_upvotes"] = p.get("hf_upvotes", 0)
                indexed[p["arxiv_id"]].setdefault("github_repo", p.get("github_repo", ""))
                continue
            if is_negative(p, negatives):
                continue
            verdict = classify(p, config, allowed_ids)
            if verdict is None:
                continue
            best_id, score = verdict
            p["score"], p["via"] = score, "hf"
            if best_id in by_category:
                by_category[best_id].append(p)
                seen_ids.add(p["arxiv_id"])

    # 3) 去重 + 落表
    cat_by_id = {c["id"]: c for c in categories}
    total_new = 0
    per_cat_new: Dict[str, int] = {}

    for cat_id, papers in by_category.items():
        cat = cat_by_id[cat_id]
        papers.sort(key=lambda p: (p.get("published", ""), p.get("score", 0)), reverse=True)

        new_papers = [p for p in papers if args.force or p["arxiv_id"] not in known]
        per_cat_new[cat_id] = len(new_papers)

        for p in papers:
            record = known.get(p["arxiv_id"], {})
            record.update(
                {
                    "title": p["title"],
                    "published": p.get("published", ""),
                    "url": p["url"],
                    "categories": sorted(set(record.get("categories", []) + [cat_id])),
                    "score": max(float(record.get("score", 0)), float(p.get("score", 0))),
                    "primary_category": p.get("primary_category", ""),
                    "first_seen": record.get("first_seen") or (p.get("published") or today_str),
                }
            )
            known[p["arxiv_id"]] = record

        if not new_papers:
            log(f"  {cat_id}: 无新增")
            continue

        rows = [render_row(p, cat_id) for p in new_papers]
        doc_path = Path(DOCS / Path(cat["doc"]).name)
        inserted = insert_table_rows(
            doc_path,
            "papers",
            rows,
            max_rows=int(config["meta"]["max_rows_per_doc"]),
            dry_run=args.dry_run,
        )
        total_new += inserted
        log(f"  {cat_id}: 命中 {len(papers)} 篇，新增写入 {inserted} 行 → {doc_path.name}")

    if not args.dry_run:
        store["updated"] = today_utc().strftime("%Y-%m-%dT%H:%M:%SZ")
        store["papers"] = known
        write_json(PAPER_STORE, store)

    log("")
    log(f"抓取 {total_fetched} 篇｜入库总量 {len(known)}｜本次新增 {total_new}")
    for cat_id, n in per_cat_new.items():
        log(f"  · {cat_id}: +{n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
