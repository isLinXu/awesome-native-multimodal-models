#!/usr/bin/env python3
"""汇总统计：刷新 README 的数字、生成 docs/digest.md 周报、导出 data/stats.json。

数据全部来自 data/papers.json 与 data/repos.json，不重复请求网络，
所以这个脚本可以随时安全地重跑。

用法：
  python scripts/update_metadata.py
  python scripts/update_metadata.py --digest-days 14
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List

from common import (
    DATA,
    DOCS,
    ROOT,
    count_table_rows,
    load_config,
    log,
    read_json,
    replace_marked,
    today_utc,
    write_if_changed,
    write_json,
)

PAPER_STORE = DATA / "papers.json"
REPO_STORE = DATA / "repos.json"
STATS_PATH = DATA / "stats.json"
DIGEST = DOCS / "digest.md"
README = ROOT / "README.md"


def days_ago_str(days: int) -> str:
    return (today_utc() - timedelta(days=days)).strftime("%Y-%m-%d")


def fmt_delta(delta: Any) -> str:
    if delta is None:
        return "—"
    return f"+{delta:,}" if delta > 0 else f"{delta:,}"


def print_summary() -> None:
    """把 data/stats.json 渲染成 GitHub Actions 的 markdown 摘要。"""
    stats = read_json(STATS_PATH, {})
    if not stats:
        print("_未生成 stats.json_")
        return
    print("### 抓取结果")
    print("")
    print(f"- 论文总量：**{stats.get('papers_total', 0):,}**（文档内 {stats.get('papers_in_docs', 0):,}）")
    print(f"- 近 7 天新增：**{stats.get('papers_new_7d', 0):,}**")
    print(
        f"- 跟踪仓库：**{stats.get('repos_total', 0):,}**，"
        f"累计 star **{stats.get('repos_stars_total', 0):,}**"
    )
    print("")
    print("| 赛道 | 库内 | 文档内 | 7 日新增 |")
    print("| :-- | --: | --: | --: |")
    for d in (stats.get("categories") or {}).values():
        print(f"| {d['name']} | {d['papers']:,} | {d['rows_in_doc']:,} | {d['papers_new_7d']:,} |")


def main() -> int:
    parser = argparse.ArgumentParser(description="刷新统计、徽章与周报")
    parser.add_argument("--digest-days", type=int, default=7)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--summary", action="store_true", help="只打印 markdown 摘要（给 CI 用）")
    args = parser.parse_args()

    if args.summary:
        print_summary()
        return 0

    config = load_config()
    paper_store = read_json(PAPER_STORE, {"papers": {}})
    repo_store = read_json(REPO_STORE, {"repos": {}})
    papers: Dict[str, Any] = paper_store.get("papers", {})
    repos: Dict[str, Any] = repo_store.get("repos", {})

    cat_by_id = {c["id"]: c for c in config["categories"]}
    today = today_utc()
    since_7 = days_ago_str(args.digest_days)
    since_30 = days_ago_str(30)

    # ── 论文统计 ──
    per_cat: Dict[str, Dict[str, int]] = {
        c["id"]: {"total": 0, "recent": 0, "new": 0} for c in config["categories"]
    }
    recent_total = new_total = 0
    for pid, p in papers.items():
        cats = p.get("categories") or []
        first_seen = p.get("first_seen", "")
        published = p.get("published", "")
        is_new = first_seen >= since_7
        is_recent = published >= since_30
        if is_new:
            new_total += 1
        if is_recent:
            recent_total += 1
        for cid in cats:
            if cid in per_cat:
                per_cat[cid]["total"] += 1
                per_cat[cid]["recent"] += 1 if is_recent else 0
                per_cat[cid]["new"] += 1 if is_new else 0

    doc_rows = {
        c["id"]: count_table_rows(Path(DOCS / Path(c["doc"]).name), "papers")
        for c in config["categories"]
    }
    total_doc_rows = sum(doc_rows.values())

    # ── 仓库统计 ──
    repo_list = list(repos.values())
    total_stars = sum(r.get("stars", 0) for r in repo_list)
    movers = sorted(
        [r for r in repo_list if (r.get("delta_7d") or 0) > 0],
        key=lambda r: r.get("delta_7d") or 0,
        reverse=True,
    )[:10]

    stats = {
        "generated_at": today.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "papers_total": len(papers),
        "papers_in_docs": total_doc_rows,
        "papers_new_7d": new_total,
        "papers_last_30d": recent_total,
        "repos_total": len(repo_list),
        "repos_stars_total": total_stars,
        "categories": {
            cid: {
                "name": cat_by_id[cid]["name"],
                "papers": per_cat[cid]["total"],
                "papers_last_30d": per_cat[cid]["recent"],
                "papers_new_7d": per_cat[cid]["new"],
                "rows_in_doc": doc_rows.get(cid, 0),
            }
            for cid in per_cat
        },
    }
    write_json(STATS_PATH, stats)

    # ── 周报 ──
    lines: List[str] = [
        "# 📬 自动周报 / Digest",
        "",
        f"> 本文件由 `scripts/update_metadata.py` 自动生成，最后更新 **{today:%Y-%m-%d}**。",
        f"> 统计窗口：收录「论文发布日」落在近 {args.digest_days} 天内的条目（不是抓取日）。",
        "",
        "## 概览",
        "",
        "| 指标 | 数值 |",
        "| :-- | --: |",
        f"| 收录论文（全量库） | {len(papers):,} |",
        f"| 文档内可浏览条目 | {total_doc_rows:,} |",
        f"| 近 {args.digest_days} 天新发布 | {new_total:,} |",
        f"| 跟踪仓库 | {len(repo_list):,} |",
        f"| 跟踪仓库总 star | {total_stars:,} |",
        "",
    ]

    for cat in config["categories"]:
        cid = cat["id"]
        fresh = [
            (pid, p)
            for pid, p in papers.items()
            if cid in (p.get("categories") or []) and p.get("first_seen", "") >= since_7
        ]
        fresh.sort(key=lambda kv: (kv[1].get("published", ""), kv[1].get("score", 0)), reverse=True)
        lines.append(f"## {cat['emoji']} {cat['name']} · 近 {args.digest_days} 天新发布 {len(fresh)} 篇")
        lines.append("")
        if not fresh:
            lines += ["_本周没有新发布的命中论文，赛道可能进入平台期，或关键词需要补充。_", ""]
            continue
        for pid, p in fresh[:12]:
            title = p.get("title", pid)
            url = p.get("url", f"https://arxiv.org/abs/{pid}")
            lines.append(f"- [{title}]({url}) · `{p.get('published', '—')}` · score {p.get('score', 0)}")
        if len(fresh) > 12:
            lines.append(f"- …… 另有 {len(fresh) - 12} 篇，见 [{cat['doc']}]({Path(cat['doc']).name})")
        lines.append("")

    lines += ["## 🚀 仓库增速榜（近 7 天 star 增量）", ""]
    if movers:
        lines += ["| 项目 | ⭐ | 7 日 Δ | 30 日 Δ | 赛道 |", "| :-- | --: | --: | --: | :-- |"]
        for r in movers:
            cats = ", ".join(r.get("categories", [])[:2])
            lines.append(
                f"| [**{r['full_name']}**]({r.get('url', '')}) | {r.get('stars', 0):,} | "
                f"{fmt_delta(r.get('delta_7d'))} | {fmt_delta(r.get('delta_30d'))} | {cats} |"
            )
    else:
        lines.append("_增速数据需要至少两天的 star 快照，明天起开始累积。_")
    lines.append("")

    if not args.dry_run:
        write_if_changed(DIGEST, "\n".join(lines))

    # ── README 数字刷新 ──
    if README.exists():
        content = README.read_text(encoding="utf-8")
        content = replace_marked(content, "papers", f"{len(papers):,}")
        content = replace_marked(content, "papers_new", f"+{new_total:,}")
        content = replace_marked(content, "repos", f"{len(repo_list):,}")
        content = replace_marked(content, "stars", f"{total_stars:,}")
        content = replace_marked(content, "updated", today.strftime("%Y-%m-%d"))
        for cid, n in doc_rows.items():
            content = replace_marked(content, f"cat_{cid}", f"{n:,}")
        if not args.dry_run:
            write_if_changed(README, content)

    log(f"论文 {len(papers):,}（文档内 {total_doc_rows:,}）｜近 {args.digest_days} 天新增 {new_total:,}")
    log(f"仓库 {len(repo_list):,}（总 star {total_stars:,}）｜增速榜 {len(movers)} 个")
    for cid, d in stats["categories"].items():
        log(f"  · {cid}: 库内 {d['papers']:,} / 文档 {d['rows_in_doc']:,} / 7 日新增 {d['papers_new_7d']}")
    log(f"已更新: {STATS_PATH.name}, {DIGEST.name}, README.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
