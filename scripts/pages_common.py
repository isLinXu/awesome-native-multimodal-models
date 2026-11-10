#!/usr/bin/env python3
"""GitHub Pages 共用：导航、live 数据、把图表/精简 JSON 拷进 docs/。"""

from __future__ import annotations

import json
import shutil
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from html import escape
from pathlib import Path
from typing import Any, Dict, List, Tuple

sys.path.insert(0, str(Path(__file__).parent))
from common import DATA, DOCS, ROOT, load_config, read_json  # noqa: E402
from data import META, TIMELINE_MODELS  # noqa: E402

ASSETS = ROOT / "assets"
PAGES_DATA = DOCS / "data"
PAGES_ASSETS = DOCS / "assets"

TRACK_EMOJI = {
    "tokenizers": "🔢",
    "unified-ug": "🖼️",
    "any-to-any": "🌐",
    "omni": "🎙️",
    "pretraining": "🧠",
}
TRACK_COLOR = {
    "tokenizers": "#4ECDC4",
    "unified-ug": "#FF6B6B",
    "any-to-any": "#A8E6CF",
    "omni": "#DDA0DD",
    "pretraining": "#FAD7A0",
}

NAV_CSS = """
.site-nav {
  position: sticky; top: 0; z-index: 80;
  display: flex; align-items: center; justify-content: space-between;
  gap: 12px; flex-wrap: wrap;
  padding: 10px 24px;
  background: rgba(13,17,23,.92);
  backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--border, #30363d);
}
.site-nav .brand {
  font-weight: 800; color: var(--text, #e6edf3); text-decoration: none;
  letter-spacing: -0.02em; font-size: 0.95rem;
}
.site-nav .brand span { color: var(--accent, #58a6ff); }
.site-nav .links { display: flex; gap: 4px; flex-wrap: wrap; align-items: center; }
.site-nav a.link {
  color: var(--muted, #8b949e); text-decoration: none;
  padding: 6px 11px; border-radius: 8px; font-size: 0.8rem;
  display: inline-flex; flex-direction: row; align-items: baseline; gap: 5px;
}
.site-nav a.link small { font-size: 0.68rem; opacity: 0.7; font-weight: 400; }
.site-nav a.link:hover { color: var(--text, #e6edf3); background: #21262d; }
.site-nav a.link.active { color: var(--accent, #58a6ff); background: #21262d; }
.site-nav a.ext { color: var(--muted, #8b949e); text-decoration: none; font-size: 0.8rem; padding: 6px 10px; }
.site-nav a.ext:hover { color: var(--accent, #58a6ff); }
"""


def load_stats() -> Dict[str, Any]:
    return read_json(DATA / "stats.json", {})


def load_papers() -> Dict[str, Any]:
    store = read_json(DATA / "papers.json", {"papers": {}})
    return store.get("papers") or {}


def load_repos() -> Dict[str, Any]:
    store = read_json(DATA / "repos.json", {"repos": {}})
    return store.get("repos") or {}


def live_meta() -> Dict[str, Any]:
    meta = dict(META)
    stats = load_stats()
    if stats.get("papers_total"):
        meta["paper_count"] = f"{int(stats['papers_total']):,}"
    if stats.get("generated_at"):
        meta["last_updated"] = str(stats["generated_at"])[:10]
    meta["papers_new_7d"] = int(stats.get("papers_new_7d") or 0)
    meta["papers_last_30d"] = int(stats.get("papers_last_30d") or 0)
    meta["repos_total"] = int(stats.get("repos_total") or 0)
    meta["repos_stars_total"] = int(stats.get("repos_stars_total") or 0)
    meta["curated_models"] = len(TIMELINE_MODELS)
    meta["landmarks"] = sum(1 for m in TIMELINE_MODELS if m.get("landmark"))
    return meta


def fmt_int(n: Any) -> str:
    try:
        return f"{int(n):,}"
    except (TypeError, ValueError):
        return "—"


def fmt_delta(n: Any) -> str:
    try:
        v = int(n)
    except (TypeError, ValueError):
        return "—"
    return f"+{v:,}" if v > 0 else f"{v:,}"


def site_nav(active: str, github_url: str) -> str:
    items = [
        ("index.html", "index", "观测台", "Observatory"),
        ("papers.html", "papers", "论文库", "Papers"),
        ("digest.html", "digest", "周报", "Digest"),
        ("repos.html", "repos", "仓库", "Repos"),
        ("taxonomy.html", "taxonomy", "谱系", "Taxonomy"),
        ("timeline.html", "timeline", "时间线", "Timeline"),
    ]
    links = []
    for href, key, zh, en in items:
        cls = "link active" if key == active else "link"
        links.append(f'<a class="{cls}" href="{href}">{escape(zh)}<small>{escape(en)}</small></a>')
    return (
        '<nav class="site-nav">'
        '<a class="brand" href="index.html">🤖 <span>Native MM</span></a>'
        f'<div class="links">{"".join(links)}'
        f'<a class="ext" href="{escape(github_url)}" target="_blank" rel="noopener">GitHub ↗</a>'
        "</div></nav>"
    )


def site_footer(github_url: str, extra: str = "") -> str:
    bits = [
        "每日从 arXiv / GitHub 自动观测 · ",
        f'Data &amp; code: <a href="{escape(github_url)}" target="_blank" rel="noopener">isLinXu/awesome-native-multimodal-models</a>',
    ]
    if extra:
        bits.append(" · " + extra)
    return f"<footer>{''.join(bits)}</footer>"


def track_catalog() -> List[Dict[str, Any]]:
    config = load_config()
    stats = load_stats().get("categories") or {}
    rows = []
    for cat in config.get("categories") or []:
        cid = cat["id"]
        st = stats.get(cid) or {}
        rows.append(
            {
                "id": cid,
                "name": cat.get("name") or cid,
                "zh": cat.get("zh") or cat.get("name") or cid,
                "emoji": cat.get("emoji") or TRACK_EMOJI.get(cid, "📄"),
                "color": TRACK_COLOR.get(cid, "#58a6ff"),
                "intro": (cat.get("intro") or "").strip().split("\n")[0],
                "papers": int(st.get("papers") or 0),
                "new_7d": int(st.get("papers_new_7d") or 0),
            }
        )
    return rows


def latest_papers(limit: int = 16) -> List[Tuple[str, Dict[str, Any]]]:
    papers = load_papers()
    items = list(papers.items())
    items.sort(key=lambda kv: (kv[1].get("published") or "", kv[1].get("score") or 0), reverse=True)
    return items[:limit]


def featured_papers(limit: int = 12, days: int = 45, min_score: float = 6.0) -> List[Tuple[str, Dict[str, Any]]]:
    """近 N 天里分数够高的论文；不够条数就按分数回退，避免首页被噪声标题占满。"""
    cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")
    items = [
        (pid, p)
        for pid, p in load_papers().items()
        if (p.get("published") or "") >= cutoff
    ]
    items.sort(
        key=lambda kv: (float(kv[1].get("score") or 0), kv[1].get("published") or ""),
        reverse=True,
    )
    strong = [x for x in items if float(x[1].get("score") or 0) >= min_score]
    picked = strong[:limit] if len(strong) >= 6 else items[:limit]
    return picked


def papers_since(days: int = 7) -> List[Tuple[str, Dict[str, Any]]]:
    cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")
    items = [
        (pid, p)
        for pid, p in load_papers().items()
        if (p.get("published") or "") >= cutoff
    ]
    items.sort(
        key=lambda kv: (float(kv[1].get("score") or 0), kv[1].get("published") or ""),
        reverse=True,
    )
    return items


def landmark_models() -> List[Dict[str, Any]]:
    rows = [m for m in TIMELINE_MODELS if m.get("landmark")]
    rows.sort(key=lambda m: (int(m.get("year") or 0), int(m.get("month") or 0), m.get("name") or ""))
    return rows


def repo_speed(rec: Dict[str, Any]) -> float:
    d7 = rec.get("delta_7d")
    if d7 is not None:
        try:
            return float(d7)
        except (TypeError, ValueError):
            pass
    try:
        return float(rec.get("velocity") or 0) * 7
    except (TypeError, ValueError):
        return 0.0


def top_repos(limit: int = 8) -> List[Dict[str, Any]]:
    repos = list(load_repos().values())
    repos.sort(key=lambda r: (repo_speed(r), int(r.get("stars") or 0)), reverse=True)
    return repos[:limit]


def year_counts() -> List[Tuple[str, int]]:
    papers = load_papers()
    c = Counter()
    for p in papers.values():
        y = (p.get("published") or "")[:4]
        if y.isdigit():
            c[y] += 1
    return sorted(c.items())


def prepare_pages() -> None:
    """把图表和精简 JSON 拷到 docs/，Pages 才能同源读取。"""
    DOCS.mkdir(exist_ok=True)
    PAGES_ASSETS.mkdir(parents=True, exist_ok=True)
    PAGES_DATA.mkdir(parents=True, exist_ok=True)
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")

    if ASSETS.exists():
        for src in ASSETS.glob("*.svg"):
            shutil.copy2(src, PAGES_ASSETS / src.name)

    papers = load_papers()
    slim_papers = [
        {
            "id": pid,
            "t": rec.get("title") or pid,
            "d": rec.get("published") or "",
            "c": rec.get("categories") or [],
            "s": rec.get("score") or 0,
        }
        for pid, rec in papers.items()
    ]
    slim_papers.sort(key=lambda r: r["d"], reverse=True)
    (PAGES_DATA / "live-papers.json").write_text(
        json.dumps(slim_papers, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )

    slim_repos = []
    for rec in load_repos().values():
        speed = repo_speed(rec)
        slim_repos.append(
            {
                "n": rec.get("full_name") or "",
                "s": rec.get("stars") or 0,
                "u": rec.get("url") or "",
                "d": rec.get("description") or "",
                "c": rec.get("categories") or [],
                "v": round(speed, 1),
                "est": rec.get("delta_7d") is None,
                "lang": rec.get("language") or "",
            }
        )
    slim_repos.sort(key=lambda r: (r["v"], r["s"]), reverse=True)
    (PAGES_DATA / "live-repos.json").write_text(
        json.dumps(slim_repos, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )

    stats = load_stats()
    if stats:
        (PAGES_DATA / "stats.json").write_text(
            json.dumps(stats, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
