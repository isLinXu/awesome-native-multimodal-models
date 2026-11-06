#!/usr/bin/env python3
"""文档自检：表格列数一致、相对链接可达、标记表格齐全、统计标记成对。

放在 CI 里跑，防止"脚本写坏了一张表"这种事悄悄合进主干。

  python scripts/check_md.py
  python scripts/check_md.py --quiet
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import List

from common import DOCS, ROOT, load_config

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
STATS_RE = re.compile(r"<!--\s*STATS:([\w-]+)\s*-->(.*?)<!--\s*/STATS:\1\s*-->", re.S)


def check_tables(path: Path) -> List[str]:
    errors: List[str] = []
    lines = path.read_text(encoding="utf-8").split("\n")
    block: List[str] = []
    start_line = 0

    def flush() -> None:
        if len(block) < 2:
            return
        widths = {row.count("|") for row in block}
        if len(widths) > 1:
            errors.append(
                f"{path.name}:{start_line} 表格列数不一致（出现 {sorted(widths)} 种竖线数量）"
            )

    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith("|"):
            if not block:
                start_line = i
            block.append(line.strip())
        else:
            flush()
            block = []
    flush()
    return errors


def check_links(path: Path) -> List[str]:
    errors: List[str] = []
    for target in LINK_RE.findall(path.read_text(encoding="utf-8")):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean = target.split("#")[0]
        if not clean:
            continue
        if not (path.parent / clean).exists():
            errors.append(f"{path.name}: 相对链接失效 → {target}")
    return errors


def check_markers(path: Path) -> List[str]:
    errors: List[str] = []
    content = path.read_text(encoding="utf-8")
    for table_id in ("papers",):
        if f"<!-- table:start {table_id} -->" not in content:
            errors.append(f"{path.name}: 缺少 table:start {table_id} 标记")
        if f"<!-- table:end {table_id} -->" not in content:
            errors.append(f"{path.name}: 缺少 table:end {table_id} 标记")
    for m in re.finditer(r"<!--\s*STATS:([\w-]+)\s*-->", content):
        if not re.search(rf"<!--\s*/STATS:{m.group(1)}\s*-->", content):
            errors.append(f"{path.name}: 统计标记未闭合 → {m.group(1)}")
    return errors


IMG_RE = re.compile(r'(?:src|srcset)="([^"]+\.svg)"')
PICTURE_RE = re.compile(r"<picture>(.*?)</picture>", re.S)


def check_images(path: Path) -> List[str]:
    """校验内嵌 SVG 是否存在，以及 <picture> 的深浅两套是否齐全。

    图是脚本生成的，很容易出现"改了文件名但忘了改引用"或"只生成了浅色版"。
    GitHub 上图片挂了不会报错，只会显示一个破图标——所以必须在这里挡住。
    """
    errors: List[str] = []
    content = path.read_text(encoding="utf-8")

    for target in IMG_RE.findall(content):
        if target.startswith(("http://", "https://", "data:")):
            continue
        if not (path.parent / target).exists():
            errors.append(f"{path.name}: 图片不存在 → {target}")

    for block in PICTURE_RE.findall(content):
        has_dark = 'prefers-color-scheme: dark' in block
        has_img = "<img" in block
        if has_img and not has_dark:
            errors.append(f"{path.name}: <picture> 缺少深色版 <source>，深色主题下会显示浅色图")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="文档自检")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    config = load_config()
    files = [ROOT / "README.md", ROOT / "CONTRIBUTING.md"]
    files += [DOCS / Path(c["doc"]).name for c in config["categories"]]
    files += [DOCS / "projects.md", DOCS / "digest.md"]

    all_errors: List[str] = []
    checked = 0
    for path in files:
        if not path.exists():
            all_errors.append(f"{path.name}: 文件不存在")
            continue
        checked += 1
        all_errors += check_tables(path)
        all_errors += check_links(path)
        all_errors += check_images(path)
        if path.parent == DOCS and path.name not in ("projects.md", "digest.md"):
            all_errors += check_markers(path)

    if all_errors:
        print(f"发现 {len(all_errors)} 个问题：")
        for e in all_errors:
            print(f"  ✗ {e}")
        return 1

    if not args.quiet:
        print(f"✓ {checked} 个文件全部通过：表格列数一致、链接可达、图片齐全、标记完整")
    return 0


if __name__ == "__main__":
    sys.exit(main())
