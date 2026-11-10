"""
generate_digest.py
Generates docs/digest.html — weekly observatory digest.
Run: python scripts/generate_digest.py
"""

from __future__ import annotations

import sys
from html import escape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from pages_common import (  # noqa: E402
    NAV_CSS,
    TRACK_COLOR,
    live_meta,
    papers_since,
    prepare_pages,
    site_footer,
    site_nav,
    track_catalog,
)

DOCS_DIR = Path(__file__).parent.parent / "docs"
OUTPUT = DOCS_DIR / "digest.html"

CSS = """
  :root {
    --bg: #0d1117; --surface: #161b22; --border: #30363d;
    --text: #e6edf3; --muted: #8b949e; --accent: #58a6ff; --link: #79c0ff;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: var(--bg); color: var(--text);
    font-family: 'Segoe UI', 'Noto Sans SC', 'PingFang SC', system-ui, sans-serif;
    min-height: 100vh; display: flex; flex-direction: column;
  }
  main { width: min(880px, 100%); margin: 0 auto; padding: 28px 20px 64px; flex: 1; }
  h1 { font-size: 1.6rem; margin-bottom: 6px; }
  h1 span { color: var(--accent); }
  .lead { color: var(--muted); font-size: 0.9rem; margin-bottom: 22px; line-height: 1.7; }
  .stats {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 10px; margin-bottom: 28px;
  }
  .stat { background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 14px; text-align: center; }
  .stat b { display: block; font-size: 1.3rem; color: var(--accent); }
  .stat span { font-size: 0.75rem; color: var(--muted); }
  h2 { font-size: 1.05rem; margin: 22px 0 10px; }
  .paper { padding: 8px 0; border-bottom: 1px solid #21262d; font-size: 0.88rem; }
  .paper:last-child { border-bottom: 0; }
  .paper a { color: var(--text); text-decoration: none; font-weight: 600; }
  .paper a:hover { color: var(--accent); }
  .meta { color: var(--muted); font-size: 0.78rem; margin-top: 2px; }
  .empty { color: var(--muted); font-size: 0.88rem; }
  .pill { display: inline-block; font-size: 0.68rem; padding: 1px 8px; border-radius: 999px; color: #0d1117; font-weight: 700; }
  footer {
    padding: 20px; font-size: 0.75rem; color: var(--muted); text-align: center;
    border-top: 1px solid var(--border);
  }
  footer a { color: var(--link); }
"""


def main() -> None:
    prepare_pages()
    meta = live_meta()
    github = meta["github_url"]
    fresh = papers_since(7)
    by_cat: dict[str, list] = {t["id"]: [] for t in track_catalog()}
    for pid, p in fresh:
        for cid in p.get("categories") or []:
            if cid in by_cat:
                by_cat[cid].append((pid, p))
                break

    sections = []
    for t in track_catalog():
        rows = by_cat.get(t["id"]) or []
        sections.append(f'<h2>{t["emoji"]} {escape(t["zh"])} · {len(rows)} 篇</h2>')
        if not rows:
            sections.append('<p class="empty">本周这条赛道没有新发布命中。</p>')
            continue
        for pid, p in rows[:12]:
            title = escape(p.get("title") or pid)
            url = escape(p.get("url") or f"https://arxiv.org/abs/{pid}")
            date = escape((p.get("published") or "—")[:10])
            score = p.get("score") or 0
            color = TRACK_COLOR.get(t["id"], "#58a6ff")
            sections.append(
                f'<div class="paper"><a href="{url}" target="_blank" rel="noopener">{title}</a>'
                f'<div class="meta">{date} · score {score} · '
                f'<span class="pill" style="background:{color}">{escape(t["zh"])}</span></div></div>'
            )
        if len(rows) > 12:
            sections.append(
                f'<p class="empty">另有 {len(rows) - 12} 篇，见 '
                f'<a href="papers.html#{escape(t["id"])}" style="color:var(--link)">论文库</a>。</p>'
            )

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{escape(meta['title'])} — Digest</title>
<style>
{NAV_CSS}
{CSS}
</style>
</head>
<body>
{site_nav("digest", github)}
<main>
  <h1>📬 周报 <span>Digest</span></h1>
  <p class="lead">近 7 天按<strong>论文发布日</strong>统计，不是抓取日。
     高分优先。数据随每日 Actions 更新，最后刷新 {escape(str(meta['last_updated']))}。</p>
  <div class="stats">
    <div class="stat"><b>{escape(str(meta['paper_count']))}</b><span>库内论文</span></div>
    <div class="stat"><b>{len(fresh)}</b><span>本周新发布</span></div>
    <div class="stat"><b>{meta['repos_total']}</b><span>跟踪仓库</span></div>
    <div class="stat"><b>{meta['papers_new_7d']}</b><span>7 日入库</span></div>
  </div>
  {''.join(sections)}
</main>
{site_footer(github)}
</body>
</html>
"""
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"✅  {OUTPUT}  ({OUTPUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
