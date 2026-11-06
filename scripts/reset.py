#!/usr/bin/env python3
"""清空指定表格与状态库，用于重建。

典型用法：改了分类关键词、想重新按新规则收一遍时。

  python scripts/reset.py --papers          # 清空 5 个赛道的论文表 + data/papers.json
  python scripts/reset.py --repos           # 清空项目榜 + data/repos.json（会丢 star 历史）
  python scripts/reset.py --papers --repos
  python scripts/reset.py --papers --dry-run

注意：--repos 会丢掉历史快照，增速要重新累积，慎用。
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from common import DATA, DOCS, load_config, log

TABLES = {
    "papers": ("docs", "papers"),
    "repos": ("docs/projects.md", "repos"),
}


def clear_table(doc_path: Path, table_id: str, dry_run: bool) -> bool:
    if not doc_path.exists():
        return False
    content = doc_path.read_text(encoding="utf-8")
    pattern = re.compile(
        r"(<!-- table:start " + table_id + r" -->)(.*?)(<!-- table:end " + table_id + r" -->)", re.S
    )
    m = pattern.search(content)
    if not m:
        return False
    lines = [ln for ln in m.group(2).split("\n") if ln.strip().startswith("|")]
    if len(lines) < 2:
        return False
    body = "\n" + "\n".join(lines[:2]) + "\n"
    new = m.group(1) + body + m.group(3)
    if not dry_run:
        doc_path.write_text(content[: m.start()] + new + content[m.end():], encoding="utf-8")
    log(f"  清空 {doc_path.name} :: {table_id}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="清空表格与状态库以便重建")
    parser.add_argument("--papers", action="store_true")
    parser.add_argument("--repos", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not (args.papers or args.repos):
        parser.print_help()
        return 1

    if args.papers:
        log("清空论文表与 data/papers.json")
        for cat in load_config()["categories"]:
            clear_table(Path(DOCS / Path(cat["doc"]).name), "papers", args.dry_run)
        if not args.dry_run and (DATA / "papers.json").exists():
            (DATA / "papers.json").unlink()
            log("  删除 data/papers.json")

    if args.repos:
        log("清空项目榜与 data/repos.json（star 历史将丢失）")
        clear_table(Path(DOCS / "projects.md"), "repos", args.dry_run)
        if not args.dry_run and (DATA / "repos.json").exists():
            (DATA / "repos.json").unlink()
            log("  删除 data/repos.json")

    log("完成" + ("（dry-run，未改动）" if args.dry_run else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
