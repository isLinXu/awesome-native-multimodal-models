#!/usr/bin/env python3
"""公共工具：配置加载、带退避的网络请求、arXiv 解析、markdown 表格标记写入。

设计原则：所有脚本只依赖 requests + pyyaml，任何一步失败都只降级不崩溃，
保证 GitHub Actions 里单点故障不会让整个定时任务红掉。
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple
from xml.etree import ElementTree as ET

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
DATA = ROOT / "data"
CONFIG_PATH = ROOT / "config" / "taxonomy.yml"

UA = "awesome-native-multimodal-models-bot/1.0 (+https://github.com/isLinXu/awesome-native-multimodal-models)"

ARXIV_API = "https://export.arxiv.org/api/query"
HF_PAPERS_API = "https://huggingface.co/api/daily_papers"
GITHUB_API = "https://api.github.com"

ATOM = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


# ─── 基础 IO ────────────────────────────────────────────────────────────────

def log(msg: str) -> None:
    print(msg, flush=True)


def warn(msg: str) -> None:
    print(f"  [warn] {msg}", file=sys.stderr, flush=True)


def load_config(path: Path = CONFIG_PATH) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        warn(f"读取 {path.name} 失败（{e}），使用默认值")
        return default


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2, sort_keys=False)
        f.write("\n")


def today_utc() -> datetime:
    return datetime.now(timezone.utc)


# ─── 网络 ──────────────────────────────────────────────────────────────────

def http_get(
    url: str,
    params: Optional[Dict[str, Any]] = None,
    *,
    headers: Optional[Dict[str, str]] = None,
    retries: int = 4,
    timeout: int = 30,
    base_wait: float = 2.0,
    accept_status: Iterable[int] = (200,),
) -> Optional[requests.Response]:
    """GET + 指数退避。4xx（除 429）直接放弃，避免无意义重试。"""
    hdrs = {"User-Agent": UA}
    if headers:
        hdrs.update(headers)

    last_err: Optional[str] = None
    for attempt in range(retries):
        if attempt:
            wait = base_wait * (2 ** (attempt - 1))
            time.sleep(min(wait, 30))
        try:
            resp = requests.get(url, params=params, headers=hdrs, timeout=timeout)
        except requests.RequestException as e:
            last_err = str(e)
            continue

        if resp.status_code in accept_status:
            return resp
        if resp.status_code == 429:
            last_err = "429 rate limited"
            continue
        if 400 <= resp.status_code < 500:
            warn(f"HTTP {resp.status_code} for {url} — 放弃（不重试）")
            return None
        last_err = f"HTTP {resp.status_code}"

    warn(f"请求失败 {url}: {last_err}")
    return None


# ─── 文本处理 ──────────────────────────────────────────────────────────────

def clean_text(text: str) -> str:
    """收敛空白。注意不要做 NFKC 归一化——它会把中文全角标点（，：）压成半角，
    而本仓库大量正文是中文，压完读起来很别扭。"""
    text = (text or "").replace("\u3000", " ").replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def md_escape(text: str) -> str:
    return clean_text(text).replace("|", "\\|")


def shorten(text: str, limit: int = 110) -> str:
    """按句子边界截断，避免在词中间切断，也不会留下"…,"这种残句。"""
    text = clean_text(text)
    if len(text) <= limit:
        return text
    window = text[: limit + 40]
    cut = limit
    for sep in (". ", "; ", ", "):
        idx = window.rfind(sep, 0, limit)
        if idx > limit * 0.5:
            cut = idx
            break
    result = re.sub(r"[\s,;:.!?、，；：]+$", "", window[:cut])
    return result + "…"


def short_authors(authors: List[str], keep: int = 2) -> str:
    if not authors:
        return "—"
    if len(authors) <= keep:
        return ", ".join(authors)
    return ", ".join(authors[:keep]) + " et al."


def parse_date(value: str) -> Optional[datetime]:
    try:
        return datetime.strptime(value[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except (ValueError, TypeError):
        return None


# ─── arXiv 解析 ────────────────────────────────────────────────────────────

def parse_arxiv_feed(xml_bytes: bytes) -> List[Dict[str, Any]]:
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError as e:
        warn(f"arXiv XML 解析失败: {e}")
        return []

    papers: List[Dict[str, Any]] = []
    for entry in root.findall("atom:entry", ATOM):
        raw_id = (entry.findtext("atom:id", default="", namespaces=ATOM) or "").strip()
        # 兼容新旧两种 id 形式：abs/2610.10563v1 与 abs/cs/0601001v1
        m = re.search(r"abs/(.+?)(?:v\d+)?$", raw_id)
        arxiv_id = m.group(1) if m else ""
        if not arxiv_id:
            continue

        title = clean_text(entry.findtext("atom:title", default="", namespaces=ATOM))
        summary = clean_text(entry.findtext("atom:summary", default="", namespaces=ATOM))
        published = (entry.findtext("atom:published", default="", namespaces=ATOM) or "")[:10]
        updated = (entry.findtext("atom:updated", default="", namespaces=ATOM) or "")[:10]
        primary = ""
        pc = entry.find("arxiv:primary_category", ATOM)
        if pc is not None:
            primary = pc.get("term", "")
        categories = [c.get("term", "") for c in entry.findall("atom:category", ATOM)]
        authors = [
            clean_text(a.findtext("atom:name", default="", namespaces=ATOM))
            for a in entry.findall("atom:author", ATOM)
        ]
        comment = clean_text(entry.findtext("arxiv:comment", default="", namespaces=ATOM))

        papers.append(
            {
                "arxiv_id": arxiv_id,
                "title": title,
                "abstract": summary,
                "published": published,
                "updated": updated,
                "primary_category": primary,
                "categories": categories,
                "authors": [a for a in authors if a],
                "comment": comment,
                "url": f"https://arxiv.org/abs/{arxiv_id}",
            }
        )
    return papers


def arxiv_date_range(days_back: int) -> str:
    end = today_utc()
    start = end - timedelta(days=days_back)
    return f"submittedDate:[{start:%Y%m%d}0000 TO {end:%Y%m%d}2359]"


# ─── markdown 表格（标记块写入） ────────────────────────────────────────────
#
# 文档里这样写：
#   <!-- table:start papers -->
#   | 日期 | 论文 | ... |
#   | :-- | ... |
#   <!-- table:end papers -->
#
# 脚本只在两个标记之间做「新增置顶 + 按 key 去重 + 截断」，
# 永远不会碰标记外面的正文，所以人和机器可以同时改同一个文件。

_START = "<!-- table:start {} -->"
_END = "<!-- table:end {} -->"


def insert_table_rows(
    doc_path: Path,
    table_id: str,
    rows: List[Tuple[str, str]],
    *,
    max_rows: int = 300,
    dry_run: bool = False,
) -> int:
    """rows: [(dedupe_key, markdown_row), ...]，按给定顺序插入表体顶部。"""
    if not doc_path.exists():
        warn(f"文档不存在，跳过: {doc_path}")
        return 0

    content = doc_path.read_text(encoding="utf-8")
    start_marker, end_marker = _START.format(table_id), _END.format(table_id)

    start = content.find(start_marker)
    if start == -1:
        warn(f"{doc_path.name} 缺少 {start_marker}")
        return 0
    end = content.find(end_marker, start)
    if end == -1:
        warn(f"{doc_path.name} 缺少 {end_marker}")
        return 0

    block = content[start + len(start_marker) : end]
    lines = [ln for ln in block.split("\n") if ln.strip()]

    if len(lines) < 2:
        warn(f"{doc_path.name} 表格 {table_id} 缺少表头")
        return 0

    header, separator, body = lines[0], lines[1], lines[2:]

    inserted: List[str] = []
    for key, row in rows:
        # key 必须是行内独一无二的片段（如 "[**owner/repo**]"），不能用裸名字：
        # "bytedance/UI-TARS" 是 "bytedance/UI-TARS-desktop" 的子串，裸名字会误判成重复。
        if key and any(key in ln for ln in body):
            continue
        if any(key in ln for ln in inserted):
            continue
        inserted.append(row)

    if not inserted:
        return 0

    new_body = inserted + body
    dropped = max(0, len(new_body) - max_rows)
    new_body = new_body[:max_rows]

    new_block = "\n" + "\n".join([header, separator] + new_body) + "\n"
    content = content[: start + len(start_marker)] + new_block + content[end:]
    if not dry_run:
        doc_path.write_text(content, encoding="utf-8")

    if dropped:
        log(f"  {doc_path.name}: 表格超限，{dropped} 条较早条目移出文档（仍保留在 data/papers.json）")
    return len(inserted)


def replace_table_body(
    doc_path: Path, table_id: str, rows: List[str], *, dry_run: bool = False
) -> int:
    """整表重写（榜单类用：每次都是全量快照，排名会变，不能增量追加）。"""
    if not doc_path.exists():
        warn(f"文档不存在，跳过: {doc_path}")
        return 0
    content = doc_path.read_text(encoding="utf-8")
    start_marker, end_marker = _START.format(table_id), _END.format(table_id)
    start = content.find(start_marker)
    end = content.find(end_marker, start) if start != -1 else -1
    if start == -1 or end == -1:
        warn(f"{doc_path.name} 缺少表格标记 {table_id}")
        return 0

    block = content[start + len(start_marker) : end]
    lines = [ln for ln in block.split("\n") if ln.strip().startswith("|")]
    if len(lines) < 2:
        warn(f"{doc_path.name} 表格 {table_id} 缺少表头")
        return 0
    header, separator = lines[0], lines[1]

    new_block = "\n" + "\n".join([header, separator] + rows) + "\n"
    if not dry_run:
        doc_path.write_text(
            content[: start + len(start_marker)] + new_block + content[end:], encoding="utf-8"
        )
    return len(rows)


def replace_marked(content: str, marker: str, value: str) -> str:
    """替换 <!--STATS:xxx-->旧值<!--/STATS:xxx--> 之间的内容。"""
    pattern = re.compile(
        r"(<!--\s*STATS:" + re.escape(marker) + r"\s*-->)(.*?)(<!--\s*/STATS:" + re.escape(marker) + r"\s*-->)",
        re.S,
    )
    return pattern.sub(lambda m: m.group(1) + value + m.group(3), content)


def count_table_rows(doc_path: Path, table_id: Optional[str] = None) -> int:
    """统计数据行数。table_id 为空则统计文档内所有标记表格。"""
    if not doc_path.exists():
        return 0
    content = doc_path.read_text(encoding="utf-8")
    total = 0
    pattern = r"<!-- table:start (\S+) -->(.*?)<!-- table:end \1 -->"
    for m in re.finditer(pattern, content, re.S):
        if table_id and m.group(1) != table_id:
            continue
        lines = [ln for ln in m.group(2).split("\n") if ln.strip().startswith("|")]
        total += max(0, len(lines) - 2)
    return total


def write_if_changed(path: Path, content: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True
