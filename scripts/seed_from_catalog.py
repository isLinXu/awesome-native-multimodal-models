#!/usr/bin/env python3
"""把 scripts/data.py 里已整理的模型灌进自动跟踪库，作为建库日的基线。

只写 data/papers.json 与赛道文档的 papers 表，不覆盖 classics。
已存在的 arXiv ID 不会重复插入，所以可以安全重跑。
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

from common import (
    DATA,
    DOCS,
    insert_table_rows,
    load_config,
    log,
    md_escape,
    read_json,
    short_authors,
    shorten,
    write_json,
)

sys.path.insert(0, str(Path(__file__).parent))
from data import TIMELINE_MODELS  # noqa: E402

PAPER_STORE = DATA / "papers.json"

CATEGORY_MAP = {
    "Tokenizer": "tokenizers",
    "Unified": "unified-ug",
    "Any2Any": "any-to-any",
    "Omni": "omni",
    "Pretraining": "pretraining",
}


def published_of(model: Dict[str, Any]) -> str:
    year = int(model.get("year") or 0)
    month = int(model.get("month") or 1)
    if year < 2010:
        return ""
    return f"{year:04d}-{month:02d}-01"


def contribution_of(model: Dict[str, Any]) -> str:
    desc = (model.get("desc") or "").strip()
    return shorten(desc or model.get("name", ""), 95)


def main() -> int:
    parser = argparse.ArgumentParser(description="用 data.py 灌入自动跟踪基线")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    config = load_config()
    cat_by_id = {c["id"]: c for c in config["categories"]}
    store = read_json(PAPER_STORE, {"updated": "", "papers": {}})
    known: Dict[str, Any] = store.get("papers", {})

    by_category: Dict[str, list] = {c["id"]: [] for c in config["categories"]}
    skipped = 0
    for model in TIMELINE_MODELS:
        arxiv = (model.get("arxiv") or "").strip()
        if not arxiv:
            skipped += 1
            continue
        cat_id = CATEGORY_MAP.get(model.get("category", ""))
        if cat_id not in by_category:
            skipped += 1
            continue
        published = published_of(model)
        record = known.get(arxiv, {})
        cats = sorted(set(record.get("categories", []) + [cat_id]))
        record.update(
            {
                "title": model.get("name", arxiv),
                "published": record.get("published") or published,
                "url": f"https://arxiv.org/abs/{arxiv}",
                "categories": cats,
                "score": max(float(record.get("score", 0)), 6.0 if model.get("landmark") else 3.0),
                "primary_category": record.get("primary_category", ""),
                "first_seen": record.get("first_seen") or published,
                "via": record.get("via") or "catalog",
                "github_repo": model.get("github") or record.get("github_repo", ""),
                "desc": model.get("desc") or record.get("desc", ""),
            }
        )
        known[arxiv] = record
        by_category[cat_id].append((arxiv, model, record))

    total_new = 0
    for cat_id, items in by_category.items():
        items.sort(key=lambda x: x[2].get("published", ""), reverse=True)
        rows = []
        for arxiv, model, record in items:
            title = md_escape(model.get("name") or record["title"])
            authors = md_escape(short_authors([]))
            contrib = md_escape(contribution_of(model) or contribution_of(record))
            date = record.get("published") or "—"
            link = f"[📄 {arxiv}](https://arxiv.org/abs/{arxiv})"
            extra = []
            if record.get("github_repo"):
                extra.append(f"[💻]({record['github_repo']})")
            extra.append("`catalog`")
            row = f"| {date} | **{title}** | {authors} | {contrib} | {link} {' '.join(extra)} |".rstrip()
            rows.append((f"(https://arxiv.org/abs/{arxiv})", row))

        doc_path = Path(DOCS / Path(cat_by_id[cat_id]["doc"]).name)
        inserted = insert_table_rows(
            doc_path,
            "papers",
            rows,
            max_rows=int(config["meta"]["max_rows_per_doc"]),
            dry_run=args.dry_run,
        )
        total_new += inserted
        log(f" {cat_id}: 目录 {len(items)} 条，新写入 {inserted} 行 → {doc_path.name}")

    if not args.dry_run:
        store["updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        store["papers"] = known
        write_json(PAPER_STORE, store)

    log("")
    log(f"基线入库 {len(known)} 篇｜本次新写入文档 {total_new} 行｜跳过 {skipped} 条（无 arXiv 或类别未知）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
