"""
generate_index.py
Generates docs/index.html — landing page linking taxonomy + timeline.
Run: python scripts/generate_index.py
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from data import TIMELINE_MODELS, META  # noqa: E402

DOCS_DIR = Path(__file__).parent.parent / "docs"
DOCS_DIR.mkdir(exist_ok=True)
OUTPUT = DOCS_DIR / "index.html"

total = len(TIMELINE_MODELS)
landmarks = sum(1 for m in TIMELINE_MODELS if m.get("landmark"))

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{META['title']}</title>
<style>
  :root {{
    --bg: #0d1117; --surface: #161b22; --border: #30363d;
    --text: #e6edf3; --muted: #8b949e; --accent: #58a6ff; --link: #79c0ff;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background: var(--bg); color: var(--text);
    font-family: 'Segoe UI', system-ui, sans-serif;
    min-height: 100vh; display: flex; flex-direction: column; align-items: center;
    padding: 60px 20px;
  }}
  .hero {{ text-align: center; max-width: 760px; }}
  .hero h1 {{ font-size: 2.4rem; font-weight: 800; line-height: 1.2; margin-bottom: 16px; }}
  .hero h1 span {{ color: var(--accent); }}
  .hero p {{ font-size: 1.05rem; color: var(--muted); line-height: 1.8; margin-bottom: 28px; }}

  .badge-row {{ display: flex; gap: 10px; flex-wrap: wrap; justify-content: center; margin-bottom: 40px; }}
  .badge {{
    padding: 5px 16px; border-radius: 20px; font-size: 0.82rem;
    background: #21262d; border: 1px solid var(--border); color: var(--muted);
    text-decoration: none;
  }}
  .badge:hover {{ border-color: var(--accent); color: var(--accent); }}
  .badge b {{ color: var(--text); }}

  .cards {{ display: flex; gap: 24px; flex-wrap: wrap; justify-content: center; width: 100%; max-width: 900px; }}
  .card {{
    background: var(--surface); border: 1px solid var(--border); border-radius: 16px;
    padding: 32px 28px; flex: 1; min-width: 260px; max-width: 400px;
    text-decoration: none; color: var(--text);
    transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
    position: relative; overflow: hidden;
  }}
  .card:hover {{
    transform: translateY(-4px);
    border-color: var(--accent);
    box-shadow: 0 12px 36px rgba(88,166,255,.15);
  }}
  .card .icon {{ font-size: 2.8rem; margin-bottom: 14px; display: block; }}
  .card h2 {{ font-size: 1.4rem; font-weight: 700; margin-bottom: 8px; }}
  .card p {{ font-size: 0.88rem; color: var(--muted); line-height: 1.7; }}
  .card .tag {{
    position: absolute; top: 20px; right: 20px;
    background: var(--accent); color: #0d1117;
    font-size: 0.7rem; font-weight: 700; padding: 2px 8px; border-radius: 12px;
  }}

  .stats-row {{
    display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 16px; width: 100%; max-width: 900px; margin: 48px 0 32px;
  }}
  .stat-box {{
    background: var(--surface); border: 1px solid var(--border);
    border-radius: 12px; padding: 20px; text-align: center;
  }}
  .stat-box .num {{ font-size: 2rem; font-weight: 800; color: var(--accent); }}
  .stat-box .lab {{ font-size: 0.78rem; color: var(--muted); margin-top: 4px; }}

  .definition {{
    background: var(--surface); border-left: 3px solid var(--accent);
    border-radius: 8px; padding: 18px 22px; max-width: 760px; width: 100%;
    margin: 40px 0; font-size: 0.88rem; color: var(--muted); line-height: 1.8;
  }}
  .definition strong {{ color: var(--text); }}

  footer {{
    margin-top: auto; padding-top: 48px;
    font-size: 0.75rem; color: var(--muted); text-align: center;
  }}
  footer a {{ color: var(--link); }}
</style>
</head>
<body>

<div class="hero">
  <h1>🤖 <span>Awesome</span> Native<br/>Multimodal Models</h1>
  <p>A curated collection of <strong>{META['paper_count']} papers</strong> on models that handle
     text, image, audio, and video within a <em>unified architecture</em> —
     shared computation paths, unified tokenization, and end-to-end cross-modal training.</p>
  <div class="badge-row">
    <span class="badge">📄 <b>{META['paper_count']}</b> Papers</span>
    <span class="badge">🗓 Updated <b>{META['last_updated']}</b></span>
    <span class="badge">📜 MIT License</span>
    <a href="{META['github_url']}" target="_blank" class="badge">⭐ GitHub</a>
    <span class="badge">🤝 PRs Welcome</span>
  </div>
</div>

<div class="stats-row">
  <div class="stat-box"><div class="num">{total}</div><div class="lab">Models Tracked</div></div>
  <div class="stat-box"><div class="num">{landmarks}</div><div class="lab">Landmark Models</div></div>
  <div class="stat-box"><div class="num">5</div><div class="lab">Categories</div></div>
  <div class="stat-box"><div class="num">2017</div><div class="lab">Start Year (VQ-VAE)</div></div>
  <div class="stat-box"><div class="num">2026</div><div class="lab">Through Year</div></div>
</div>

<div class="cards">
  <a href="taxonomy.html" class="card">
    <span class="tag">Interactive</span>
    <span class="icon">🌐</span>
    <h2>Architecture Taxonomy</h2>
    <p>Hierarchical D3.js collapsible tree — explore 5 primary branches,
       12+ sub-categories, and 100+ leaf models. Click nodes to expand/collapse,
       hover for paper/GitHub links, search by name or keyword.</p>
  </a>
  <a href="timeline.html" class="card">
    <span class="tag">Interactive</span>
    <span class="icon">📅</span>
    <h2>Model Timeline</h2>
    <p>Swim-lane timeline from 2017 to 2026 across 5 technology lanes.
       Greedy lane assignment, minimap overview, zoom & pan, category filters,
       year jump buttons, and landmark highlighting.</p>
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

<footer>
  Auto-generated · Data &amp; code: <a href="{META['github_url']}" target="_blank">Awesome-Native-Multimodal-Models</a> ·
  Visualized with <a href="https://d3js.org" target="_blank">D3.js v7</a>
</footer>

</body>
</html>
"""

OUTPUT.write_text(HTML, encoding="utf-8")
print(f"✅  {OUTPUT}  ({OUTPUT.stat().st_size // 1024} KB)")
