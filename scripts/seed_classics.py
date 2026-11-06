#!/usr/bin/env python3
"""按 arXiv ID 校验并填充各赛道的「奠基与必读」表格。

为什么用 ID 而不是关键词：关键词会漂移，ID 不会。脚本会拿 arXiv 返回的真实
标题/作者/日期覆盖文档，并用 `expect` 字段做二次校验——如果某个 ID 指向的
论文和预期不符（或已被撤下），会打印警告并跳过，绝不把错的东西写进文档。

用法：
  python scripts/seed_classics.py
  python scripts/seed_classics.py --dry-run
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any, Dict, List

from common import (
    ARXIV_API,
    DOCS,
    http_get,
    load_config,
    log,
    md_escape,
    parse_arxiv_feed,
    short_authors,
    shorten,
    warn,
)

_BLOCK = re.compile(r"(<!-- table:start classics -->)(.*?)(<!-- table:end classics -->)", re.S)
HEADER = "| 日期 | 论文 | 作者 | 为什么必读 | 链接 |\n| :-- | :-- | :-- | :-- | :-- |"


def fetch_by_ids(ids: List[str]) -> Dict[str, Dict[str, Any]]:
    if not ids:
        return {}
    resp = http_get(
        ARXIV_API,
        params={"id_list": ",".join(ids), "max_results": len(ids)},
        retries=3,
    )
    if resp is None:
        return {}
    return {p["arxiv_id"]: p for p in parse_arxiv_feed(resp.content)}


def write_block(doc_path: Path, rows: List[str], dry_run: bool) -> int:
    if not doc_path.exists():
        warn(f"文档不存在: {doc_path}")
        return 0
    content = doc_path.read_text(encoding="utf-8")
    m = _BLOCK.search(content)
    if not m:
        warn(f"{doc_path.name} 缺少 classics 表格标记")
        return 0
    body = "\n".join(rows)
    new = f"{m.group(1)}\n{HEADER}\n{body}\n{m.group(3)}" if rows else f"{m.group(1)}\n{HEADER}\n{m.group(3)}"
    if not dry_run:
        doc_path.write_text(content[: m.start()] + new + content[m.end():], encoding="utf-8")
    return len(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="校验并填充奠基论文表")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    config = load_config()
    all_ids = sorted(
        {
            str(c["id"]).strip()
            for cat in config["categories"]
            for c in (cat.get("classics") or [])
            if c.get("id")
        }
    )
    log(f"待校验 arXiv ID: {len(all_ids)} 个")
    meta = fetch_by_ids(all_ids)
    log(f"arXiv 返回有效记录: {len(meta)} 条\n")

    total = 0
    for cat in config["categories"]:
        classics = cat.get("classics") or []
        if not classics:
            continue
        rows: List[str] = []
        for entry in classics:
            cid = str(entry["id"]).strip()
            paper = meta.get(cid)
            if paper is None:
                warn(f"[{cat['id']}] {cid} 无有效记录，跳过")
                continue
            expect = (entry.get("expect") or "").lower()
            haystack = f"{paper['title']} {paper['abstract']}".lower()
            if expect and expect not in haystack:
                warn(f"[{cat['id']}] {cid} 校验不通过（期望包含 '{expect}'，实际: {paper['title'][:60]}），跳过")
                continue
            note = md_escape(entry.get("note", "")) or md_escape(shorten(paper["abstract"], 90))
            rows.append(
                f"| {paper['published']} | **{md_escape(paper['title'])}** | "
                f"{md_escape(short_authors(paper['authors']))} | {note} | "
                f"[📄 {cid}]({paper['url']}) |"
            )
            log(f"  ✓ [{cat['id']}] {cid}  {paper['title'][:64]}")

        doc = Path(DOCS / Path(cat["doc"]).name)
        n = write_block(doc, rows, args.dry_run)
        total += n
        log(f"  → {doc.name}: {n} 条必读\n")

    log(f"完成，共写入 {total} 条必读条目")
    return 0


if __name__ == "__main__":
    sys.exit(main())
