"""
generate_index.py
Generates docs/index.html — live observatory landing page.
Run: python scripts/generate_index.py
"""

from __future__ import annotations

import sys
from html import escape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from pages_common import (  # noqa: E402
    NAV_CSS,
    TRACK_COLOR,
    fmt_delta,
    fmt_int,
    latest_papers,
    live_meta,
    prepare_pages,
    site_footer,
    site_nav,
    top_repos,
    track_catalog,
    year_counts,
)

DOCS_DIR = Path(__file__).parent.parent / "docs"
DOCS_DIR.mkdir(exist_ok=True)
OUTPUT = DOCS_DIR / "index.html"

INDEX_CSS = """
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
  main { width: min(1120px, 100%); margin: 0 auto; padding: 36px 20px 64px; }
  .hero { text-align: center; max-width: 820px; margin: 0 auto 36px; }
  .kicker {
    display: inline-block; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.12em;
    text-transform: uppercase; color: var(--accent); background: #21262d;
    border: 1px solid var(--border); border-radius: 999px; padding: 4px 12px; margin-bottom: 16px;
  }
  .hero h1 { font-size: clamp(1.8rem, 4vw, 2.6rem); font-weight: 800; line-height: 1.2; margin-bottom: 8px; }
  .hero h1 span { color: var(--accent); }
  .hero .sub { font-size: 1.02rem; color: var(--muted); margin-bottom: 14px; }
  .hero p { font-size: 0.95rem; color: var(--muted); line-height: 1.8; }
  .badge-row { display: flex; gap: 8px; flex-wrap: wrap; justify-content: center; margin-top: 22px; }
  .badge {
    padding: 5px 14px; border-radius: 20px; font-size: 0.8rem;
    background: #21262d; border: 1px solid var(--border); color: var(--muted);
    text-decoration: none;
  }
  .badge:hover { border-color: var(--accent); color: var(--accent); }
  .badge b { color: var(--text); }

  .stats-row {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 12px; margin: 8px 0 36px;
  }
  .stat-box {
    background: var(--surface); border: 1px solid var(--border);
    border-radius: 14px; padding: 18px 14px; text-align: center;
  }
  .stat-box .num { font-size: 1.7rem; font-weight: 800; color: var(--accent); }
  .stat-box .lab { font-size: 0.75rem; color: var(--muted); margin-top: 4px; }

  h2.sec { font-size: 1.15rem; margin: 8px 0 14px; }
  h2.sec span { color: var(--muted); font-weight: 500; font-size: 0.85rem; margin-left: 8px; }

  .charts { display: grid; grid-template-columns: 1.4fr 1fr; gap: 16px; margin-bottom: 36px; }
  .chart-card {
    background: var(--surface); border: 1px solid var(--border); border-radius: 16px;
    padding: 8px; overflow: hidden;
  }
  .chart-card img { width: 100%; height: auto; display: block; border-radius: 10px; }

  .years { display: flex; align-items: flex-end; gap: 8px; height: 120px; margin: 0 0 36px; }
  .ybar { flex: 1; display: flex; flex-direction: column; align-items: center; height: 100%; justify-content: flex-end; gap: 4px; }
  .yfill { width: 100%; max-width: 42px; border-radius: 6px 6px 2px 2px; background: linear-gradient(#58a6ff, #1f6feb); min-height: 4px; }
  .ylab { font-size: 0.68rem; color: var(--muted); }
  .yn { font-size: 0.68rem; color: var(--text); font-weight: 600; }

  .tracks { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; margin-bottom: 36px; }
  a.track {
    background: var(--surface); border: 1px solid var(--border); border-radius: 16px;
    padding: 18px; text-decoration: none; color: var(--text);
    transition: transform 0.15s, border-color 0.15s;
    display: flex; flex-direction: column; gap: 8px;
  }
  a.track:hover { transform: translateY(-3px); border-color: var(--accent); }
  a.track .row { display: flex; justify-content: space-between; align-items: center; }
  a.track .emoji { font-size: 1.5rem; }
  a.track h3 { font-size: 0.98rem; }
  a.track .en { font-size: 0.75rem; color: var(--muted); }
  a.track .nums b { font-size: 1.25rem; }
  a.track .delta { font-size: 0.75rem; color: var(--accent); }

  .split { display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 16px; margin-bottom: 36px; }
  .panel {
    background: var(--surface); border: 1px solid var(--border); border-radius: 16px; padding: 18px 20px;
  }
  .panel h2 { font-size: 1rem; margin-bottom: 12px; }
  .paper {
    display: grid; grid-template-columns: 88px 1fr auto; gap: 10px; align-items: baseline;
    padding: 8px 0; border-bottom: 1px solid #21262d; font-size: 0.84rem;
  }
  .paper:last-child { border-bottom: 0; }
  .paper .date { color: var(--muted); font-variant-numeric: tabular-nums; }
  .paper a { color: var(--text); text-decoration: none; }
  .paper a:hover { color: var(--accent); }
  .pill { font-size: 0.68rem; color: #0d1117; padding: 1px 8px; border-radius: 999px; font-weight: 700; white-space: nowrap; }

  .repo { padding: 8px 0; border-bottom: 1px solid #21262d; }
  .repo:last-child { border-bottom: 0; }
  .repo a { color: var(--text); text-decoration: none; font-weight: 650; font-size: 0.86rem; }
  .repo a:hover { color: var(--accent); }
  .repo p { color: var(--muted); font-size: 0.75rem; margin-top: 2px; line-height: 1.45; }
  .repo .meta { color: var(--muted); font-size: 0.75rem; margin-top: 2px; }

  .maps { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 36px; }
  a.card {
    background: var(--surface); border: 1px solid var(--border); border-radius: 16px;
    padding: 24px; text-decoration: none; color: var(--text);
    transition: transform 0.15s, border-color 0.15s; position: relative;
  }
  a.card:hover { transform: translateY(-3px); border-color: var(--accent); }
  a.card .tag {
    position: absolute; top: 16px; right: 16px;
    background: var(--accent); color: #0d1117;
    font-size: 0.68rem; font-weight: 700; padding: 2px 8px; border-radius: 12px;
  }
  a.card .icon { font-size: 1.8rem; display: block; margin-bottom: 8px; }
  a.card h2 { font-size: 1.15rem; margin-bottom: 6px; }
  a.card p { font-size: 0.84rem; color: var(--muted); line-height: 1.65; }

  .definition {
    background: var(--surface); border-left: 3px solid var(--accent);
    border-radius: 8px; padding: 18px 22px;
    font-size: 0.88rem; color: var(--muted); line-height: 1.8;
  }
  .definition strong { color: var(--text); }

  footer {
    margin-top: auto; padding: 20px; font-size: 0.75rem; color: var(--muted); text-align: center;
    border-top: 1px solid var(--border);
  }
  footer a { color: var(--link); }

  @media (max-width: 800px) {
    .charts, .split, .maps { grid-template-columns: 1fr; }
    .paper { grid-template-columns: 72px 1fr; }
    .paper .pill { display: none; }
  }
"""


def _year_bars() -> str:
    rows = year_counts()
    if not rows:
        return ""
    mx = max(n for _, n in rows) or 1
    parts = ['<h2 class="sec">按年覆盖 <span>2017 地基 → 今天</span></h2>', '<div class="years">']
    for year, n in rows:
        h = max(6, round(100 * n / mx))
        parts.append(
            f'<div class="ybar"><div class="yn">{n}</div>'
            f'<div class="yfill" style="height:{h}%"></div>'
            f'<div class="ylab">{escape(year)}</div></div>'
        )
    parts.append("</div>")
    return "\n".join(parts)


def _track_cards() -> str:
    parts = ['<h2 class="sec">五条赛道 <span>点进去按赛道浏览自动跟踪论文</span></h2>', '<div class="tracks">']
    for t in track_catalog():
        intro = escape((t["intro"] or "")[:90])
        parts.append(
            f'<a class="track" href="papers.html#{escape(t["id"])}">'
            f'<div class="row"><span class="emoji">{t["emoji"]}</span>'
            f'<span class="delta">{fmt_delta(t["new_7d"])} / 7d</span></div>'
            f'<h3>{escape(t["zh"])}</h3>'
            f'<div class="en">{escape(t["name"])}</div>'
            f'<div class="nums"><b>{fmt_int(t["papers"])}</b> 篇</div>'
            f'<div class="en">{intro}</div>'
            "</a>"
        )
    parts.append("</div>")
    return "\n".join(parts)


def _latest() -> str:
    parts = ["<h2>最新入库</h2>"]
    for pid, p in latest_papers(14):
        cats = p.get("categories") or ["—"]
        cid = cats[0]
        color = TRACK_COLOR.get(cid, "#58a6ff")
        title = escape(p.get("title") or pid)
        date = escape((p.get("published") or "—")[:10])
        url = escape(p.get("url") or f"https://arxiv.org/abs/{pid}")
        parts.append(
            f'<div class="paper"><span class="date">{date}</span>'
            f'<a href="{url}" target="_blank" rel="noopener">{title}</a>'
            f'<span class="pill" style="background:{color}">{escape(cid)}</span></div>'
        )
    parts.append('<p style="margin-top:12px;font-size:0.8rem"><a href="papers.html" style="color:var(--link)">浏览全部论文 →</a></p>')
    return "\n".join(parts)


def _repos() -> str:
    parts = ["<h2>仓库雷达</h2>"]
    for r in top_repos(8):
        name = escape(r.get("full_name") or "")
        url = escape(r.get("url") or "#")
        desc = escape((r.get("description") or "")[:110])
        stars = fmt_int(r.get("stars"))
        parts.append(
            f'<div class="repo"><a href="{url}" target="_blank" rel="noopener">{name}</a>'
            f'<div class="meta">⭐ {stars}</div>'
            f'<p>{desc}</p></div>'
        )
    return "\n".join(parts)


def main() -> None:
    prepare_pages()
    meta = live_meta()
    github = meta["github_url"]

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{escape(meta['title'])}</title>
<meta name="description" content="原生多模态模型观测台：自动跟踪 tokenizer、统一理解与生成、Any-to-Any、Omni 与预训练底座。" />
<style>
{NAV_CSS}
{INDEX_CSS}
</style>
</head>
<body>
{site_nav("index", github)}
<main>
  <div class="hero">
    <div class="kicker">Live Observatory</div>
    <h1>🤖 <span>Awesome</span> Native<br/>Multimodal Models</h1>
    <div class="sub">原生多模态模型观测台</div>
    <p>每天从 arXiv 抓取、打分、归类。覆盖从 <strong>2017 VQ-VAE</strong> 到今天的
       tokenizer / 统一理解+生成 / Any-to-Any / Omni / 预训练底座。
       精选谱系与时间线仍由人工目录驱动，长尾新论文由自动跟踪补上。</p>
    <div class="badge-row">
      <span class="badge">📄 <b>{escape(str(meta['paper_count']))}</b> Papers</span>
      <span class="badge">🗓 Updated <b>{escape(str(meta['last_updated']))}</b></span>
      <span class="badge">🔥 7d <b>{fmt_delta(meta['papers_new_7d'])}</b></span>
      <a href="{escape(github)}" target="_blank" rel="noopener" class="badge">⭐ GitHub</a>
      <a href="papers.html" class="badge">📚 论文库</a>
    </div>
  </div>

  <div class="stats-row">
    <div class="stat-box"><div class="num">{escape(str(meta['paper_count']))}</div><div class="lab">自动跟踪论文</div></div>
    <div class="stat-box"><div class="num">{fmt_delta(meta['papers_new_7d'])}</div><div class="lab">近 7 天新论文</div></div>
    <div class="stat-box"><div class="num">{fmt_int(meta['repos_total'])}</div><div class="lab">跟踪仓库</div></div>
    <div class="stat-box"><div class="num">{fmt_int(meta['repos_stars_total'])}</div><div class="lab">累计 Stars</div></div>
    <div class="stat-box"><div class="num">{fmt_int(meta['curated_models'])}</div><div class="lab">精选模型 / 谱系</div></div>
    <div class="stat-box"><div class="num">{fmt_int(meta['landmarks'])}</div><div class="lab">Landmark</div></div>
  </div>

  <h2 class="sec">动态趋势 <span>近 12 周 · 来自 data/papers.json</span></h2>
  <div class="charts">
    <div class="chart-card"><img src="assets/trend-dark.svg" alt="近 12 周论文发布趋势" /></div>
    <div class="chart-card"><img src="assets/distribution-dark.svg" alt="赛道论文分布" /></div>
  </div>

  {_year_bars()}
  {_track_cards()}

  <div class="split">
    <div class="panel">{_latest()}</div>
    <div class="panel">{_repos()}</div>
  </div>

  <h2 class="sec">精选地图 <span>人工目录，不含自动跟踪长尾</span></h2>
  <div class="maps">
    <a href="taxonomy.html" class="card">
      <span class="tag">Interactive</span>
      <span class="icon">🌐</span>
      <h2>Architecture Taxonomy</h2>
      <p>Hierarchical D3.js collapsible tree — 5 primary branches,
         12+ sub-categories, 100+ leaf models. Search, expand, hover for paper links.</p>
    </a>
    <a href="timeline.html" class="card">
      <span class="tag">Interactive</span>
      <span class="icon">📅</span>
      <h2>Model Timeline</h2>
      <p>Swim-lane timeline from 2017 to 2026. Zoom, pan, category filters,
         year jump, landmark highlighting.</p>
    </a>
  </div>

  <div class="definition">
    <strong>What is "Native Multimodal"?</strong><br/>
    A native multimodal model processes multiple modalities through
    <strong>shared computation paths</strong> (not separate encoders bridged by adapters),
    <strong>unified tokenization</strong> (all modalities in a common token space),
    and <strong>end-to-end cross-modal training</strong> — as opposed to modular
    "adapter" architectures like LLaVA or InstructBLIP.
  </div>
</main>
{site_footer(github, 'Visualized with <a href="https://d3js.org" target="_blank" rel="noopener">D3.js v7</a>')}
</body>
</html>
"""
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"✅  {OUTPUT}  ({OUTPUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
