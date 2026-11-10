#!/usr/bin/env python3
"""从 arXiv（可选 HuggingFace Daily Papers）抓取原生多模态相关论文。

流程：抓取 → 负向过滤 → 关键词加权打分 → 归类到赛道 → 与历史库去重
      → 仅把「首次出现」的论文写入 docs/<赛道>.md 的标记表格。

用法：
  python scripts/fetch_arxiv.py                 # 增量（默认回溯 45 天）
  python scripts/fetch_arxiv.py --days 365      # 首次建库，回填一年
  python scripts/fetch_arxiv.py --since 2017-01-01   # 回填到 VQ-VAE 之前
  python scripts/fetch_arxiv.py --rebuild-docs  # 把 papers.json 里被截断的行补回文档
  python scripts/fetch_arxiv.py --dry-run       # 只看会写什么，不动文件
  python scripts/fetch_arxiv.py --category unified-ug
  python scripts/fetch_arxiv.py --sources arxiv,hf
"""

from __future__ import annotations

import argparse
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from common import (
    ARXIV_API,
    DATA,
    DOCS,
    HF_PAPERS_API,
    arxiv_date_span,
    clean_text,
    http_get,
    insert_table_rows,
    iter_date_windows,
    load_config,
    log,
    md_escape,
    parse_arxiv_feed,
    parse_date,
    read_json,
    short_authors,
    shorten,
    sort_table_by_date,
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
    category: Dict[str, Any],
    config: Dict[str, Any],
    days: int,
    *,
    chunk_days: int = 0,
    max_pages: int = 4,
) -> List[Dict[str, Any]]:
    """按时间窗口 + 翻页抓取。

    arXiv 单次最多返回 max_results 条（默认 80），按新到旧排。
    若直接把 --days 拉到数年，最近 80 条会把 2017–2023 全部挤掉，
    所以历史回填必须切窗口，并在窗口内翻页。
    """
    per_query = int(config["meta"]["arxiv_max_per_query"])
    windows = iter_date_windows(days, chunk_days)
    collected: Dict[str, Dict[str, Any]] = {}

    for query in category.get("arxiv_queries", []):
        q_new = 0
        q_hit = 0
        for w_start, w_end in windows:
            date_filter = arxiv_date_span(w_start, w_end)
            for page in range(max(1, max_pages)):
                params = {
                    "search_query": f"({query}) AND {date_filter}",
                    "start": page * per_query,
                    "max_results": per_query,
                    "sortBy": "submittedDate",
                    "sortOrder": "descending",
                }
                resp = http_get(ARXIV_API, params=params, timeout=40)
                if resp is None:
                    warn(f"[{category['id']}] 查询失败，跳过: {query} ({w_start:%Y-%m-%d}–{w_end:%Y-%m-%d})")
                    break

                papers = parse_arxiv_feed(resp.content)
                q_hit += len(papers)
                for p in papers:
                    if p["arxiv_id"] not in collected:
                        collected[p["arxiv_id"]] = p
                        q_new += 1
                time.sleep(3)
                if len(papers) < per_query:
                    break
        log(f"  [{category['id']}] 命中 {q_hit:>4} / 新增 {q_new:>3} ← {query}")

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


def fetch_arxiv_by_ids(arxiv_ids: List[str], batch_size: int = 80) -> Dict[str, Dict[str, Any]]:
    """按 arXiv ID 批量补元数据（历史回填截断后，从 papers.json 回写文档用）。"""
    found: Dict[str, Dict[str, Any]] = {}
    ids = [i.strip() for i in arxiv_ids if i and str(i).strip()]
    for i in range(0, len(ids), batch_size):
        batch = ids[i : i + batch_size]
        resp = http_get(
            ARXIV_API,
            params={"id_list": ",".join(batch), "max_results": len(batch)},
            timeout=40,
        )
        if resp is None:
            warn(f"id_list 查询失败 ({batch[0]} … {batch[-1]})")
        else:
            for p in parse_arxiv_feed(resp.content):
                found[p["arxiv_id"]] = p
        time.sleep(3)
    return found


def ids_in_papers_table(doc_path: Path) -> set[str]:
    if not doc_path.exists():
        return set()
    content = doc_path.read_text(encoding="utf-8")
    start = content.find("<!-- table:start papers -->")
    end = content.find("<!-- table:end papers -->", start)
    if start == -1 or end == -1:
        return set()
    raw = re.findall(r"arxiv\.org/abs/([0-9]+\.[0-9]+(?:v\d+)?)", content[start:end])
    return {m.split("v")[0] for m in raw}


def rebuild_docs_from_store(config: Dict[str, Any], *, dry_run: bool) -> int:
    """把 papers.json 里有、文档表被 max_rows 裁掉的行补回去。"""
    store = read_json(PAPER_STORE, {"papers": {}})
    known: Dict[str, Any] = store.get("papers") or {}
    max_rows = int(config["meta"]["max_rows_per_doc"])
    log(f"从 papers.json 回写文档（库内 {len(known)} 篇，max_rows={max_rows}）")

    for cat in config["categories"]:
        cat_id = cat["id"]
        doc_path = Path(DOCS / Path(cat["doc"]).name)
        present = ids_in_papers_table(doc_path)
        missing = [
            pid
            for pid, rec in known.items()
            if cat_id in (rec.get("categories") or []) and pid not in present
        ]
        log(f"  {cat_id}: 文档 {len(present)} 行，缺口 {len(missing)}")
        if missing:
            fetched = fetch_arxiv_by_ids(missing)
            rows: List[Tuple[str, str]] = []
            for pid in missing:
                p = fetched.get(pid)
                if p is None:
                    rec = known[pid]
                    p = {
                        "arxiv_id": pid,
                        "title": rec.get("title") or pid,
                        "abstract": rec.get("desc") or rec.get("abstract") or "",
                        "published": rec.get("published") or "",
                        "primary_category": rec.get("primary_category") or "",
                        "authors": rec.get("authors") or [],
                        "url": rec.get("url") or f"https://arxiv.org/abs/{pid}",
                        "github_repo": rec.get("github_repo") or "",
                    }
                rows.append(render_row(p, cat_id))
            inserted = insert_table_rows(
                doc_path, "papers", rows, max_rows=max_rows, dry_run=dry_run
            )
            log(f"  {cat_id}: 补写 {inserted} 行")
        sort_table_by_date(doc_path, "papers", max_rows=max_rows, dry_run=dry_run)

    log("文档回写完成")
    return 0


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
    parser.add_argument("--since", default=None, help="从该日期回填到今天，例如 2017-01-01")
    parser.add_argument("--chunk-days", type=int, default=None, help="时间窗口天数；大回溯默认 365")
    parser.add_argument("--max-pages", type=int, default=4, help="每个窗口每条查询最多翻几页")
    parser.add_argument("--category", action="append", help="只跑指定赛道（可多次指定）")
    parser.add_argument("--sources", default="arxiv,hf", help="数据源：arxiv,hf")
    parser.add_argument("--dry-run", action="store_true", help="不写文件")
    parser.add_argument("--force", action="store_true", help="忽略历史库，全部重新插入")
    parser.add_argument("--rebuild-docs", action="store_true", help="按 papers.json 把被截断的行补回文档")
    args = parser.parse_args()

    config = load_config()
    if args.rebuild_docs:
        return rebuild_docs_from_store(config, dry_run=args.dry_run)
    if args.since:
        try:
            since_dt = datetime.strptime(args.since, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        except ValueError:
            warn(f"--since 不是有效日期: {args.since}")
            return 1
        days = max((today_utc() - since_dt).days, 1)
    else:
        days = args.days or int(config["meta"]["lookback_days"])
    chunk_days = args.chunk_days
    if chunk_days is None:
        chunk_days = 365 if days > 120 else 0
    categories = config["categories"]
    if args.category:
        wanted = {c.lower() for c in args.category}
        categories = [c for c in categories if c["id"] in wanted]
        if not categories:
            warn(f"未找到赛道: {args.category}")
            return 1

    sources = {s.strip() for s in args.sources.split(",") if s.strip()}
    negatives = config.get("negative") or []
    windows = iter_date_windows(days, chunk_days)
    log(
        f"回溯 {days} 天｜窗口 {len(windows)} 个"
        f"（{windows[0][0]:%Y-%m-%d} → {windows[-1][1]:%Y-%m-%d}）"
        f"｜赛道 {len(categories)} 个｜数据源 {sorted(sources)}"
    )

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
        papers = fetch_arxiv_for_category(
            cat, config, days, chunk_days=chunk_days, max_pages=args.max_pages
        )
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

    max_rows = int(config["meta"]["max_rows_per_doc"])
    for cat in categories:
        sort_table_by_date(
            Path(DOCS / Path(cat["doc"]).name),
            "papers",
            max_rows=max_rows,
            dry_run=args.dry_run,
        )

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
