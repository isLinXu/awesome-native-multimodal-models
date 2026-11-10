"""
generate_repos.py
Generates docs/repos.html — GitHub radar browser.
Run: python scripts/generate_repos.py
"""

from __future__ import annotations

import json
import sys
from html import escape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from pages_common import (  # noqa: E402
    NAV_CSS,
    TRACK_COLOR,
    live_meta,
    prepare_pages,
    site_footer,
    site_nav,
    track_catalog,
)

DOCS_DIR = Path(__file__).parent.parent / "docs"
OUTPUT = DOCS_DIR / "repos.html"

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
  main { width: min(1120px, 100%); margin: 0 auto; padding: 28px 20px 64px; flex: 1; }
  h1 { font-size: 1.6rem; margin-bottom: 6px; }
  h1 span { color: var(--accent); }
  .lead { color: var(--muted); font-size: 0.9rem; margin-bottom: 16px; line-height: 1.7; }
  .chart-card {
    background: var(--surface); border: 1px solid var(--border); border-radius: 16px;
    padding: 8px; overflow: hidden; margin-bottom: 16px;
  }
  .chart-card img { width: 100%; height: auto; display: block; border-radius: 10px; }
  .toolbar {
    display: flex; flex-wrap: wrap; gap: 8px; align-items: center;
    background: var(--surface); border: 1px solid var(--border);
    border-radius: 14px; padding: 12px; margin-bottom: 14px;
  }
  .toolbar input, .toolbar select {
    background: var(--bg); border: 1px solid var(--border); border-radius: 8px;
    color: var(--text); padding: 8px 12px; font-size: 0.88rem; outline: none;
  }
  .toolbar input { flex: 1; min-width: 200px; }
  .chips { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 14px; }
  .chip {
    border: 1px solid var(--border); background: #21262d; color: var(--muted);
    border-radius: 999px; padding: 5px 12px; font-size: 0.78rem; cursor: pointer;
  }
  .chip.active { color: #0d1117; font-weight: 700; border-color: transparent; }
  .meta-line { color: var(--muted); font-size: 0.8rem; margin-bottom: 12px; }
  table { width: 100%; border-collapse: collapse; font-size: 0.86rem; }
  th, td { text-align: left; padding: 9px 8px; border-bottom: 1px solid #21262d; vertical-align: top; }
  th { color: var(--muted); font-weight: 600; font-size: 0.75rem; }
  td a { color: var(--text); text-decoration: none; font-weight: 600; }
  td a:hover { color: var(--accent); }
  .num { font-variant-numeric: tabular-nums; white-space: nowrap; }
  .pill { display: inline-block; font-size: 0.68rem; padding: 1px 8px; border-radius: 999px; color: #0d1117; font-weight: 700; }
  .desc { color: var(--muted); font-size: 0.78rem; margin-top: 2px; }
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
    tracks = track_catalog()
    track_js = json.dumps(
        {t["id"]: {"name": t["name"], "zh": t["zh"], "color": TRACK_COLOR.get(t["id"], "#58a6ff")} for t in tracks},
        ensure_ascii=False,
    )
    chips = ['<button class="chip active" data-track="">全部</button>']
    for t in tracks:
        chips.append(
            f'<button class="chip" data-track="{escape(t["id"])}" data-color="{t["color"]}">{t["emoji"]} {escape(t["zh"])}</button>'
        )

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{escape(meta['title'])} — Repos</title>
<style>
{NAV_CSS}
{CSS}
</style>
</head>
<body>
{site_nav("repos", github)}
<main>
  <h1>🚀 仓库雷达 <span>Repos</span></h1>
  <p class="lead">跟踪 {meta['repos_total']} 个仓库，累计 ⭐ {meta['repos_stars_total']:,}。
     默认按 7 日增速排；快照不足一周时用日均折算（≈）。</p>
  <div class="chart-card"><img src="assets/ranking-dark.svg" alt="项目 star 增速 Top 12" /></div>
  <div class="chips" id="chips">{''.join(chips)}</div>
  <div class="toolbar">
    <input id="q" type="search" placeholder="搜索 owner/repo 或简介…" />
    <select id="sort">
      <option value="speed">按 7 日增速</option>
      <option value="stars">按 Stars</option>
      <option value="name">按名字</option>
    </select>
  </div>
  <div class="meta-line" id="status">加载中…</div>
  <div style="overflow-x:auto">
    <table>
      <thead>
        <tr><th>#</th><th>项目</th><th>赛道</th><th>⭐</th><th>7d Δ</th></tr>
      </thead>
      <tbody id="body"></tbody>
    </table>
  </div>
</main>
{site_footer(github)}
<script>
const TRACKS = {track_js};
let ALL = [];
let track = "";
function pill(cid) {{
  const t = TRACKS[cid] || {{zh: cid, color: "#58a6ff"}};
  return `<span class="pill" style="background:${{t.color}}">${{t.zh || cid}}</span>`;
}}
function apply() {{
  const q = document.getElementById("q").value.trim().toLowerCase();
  const sort = document.getElementById("sort").value;
  let view = ALL.filter(r => {{
    if (track && !(r.c || []).includes(track)) return false;
    const blob = ((r.n||"") + " " + (r.d||"")).toLowerCase();
    if (q && !blob.includes(q)) return false;
    return true;
  }});
  view.sort((a,b) => {{
    if (sort === "stars") return (b.s||0) - (a.s||0);
    if (sort === "name") return (a.n||"").localeCompare(b.n||"");
    return (b.v||0) - (a.v||0);
  }});
  const body = document.getElementById("body");
  body.innerHTML = view.map((r, i) => `
    <tr>
      <td class="num">${{i+1}}</td>
      <td><a href="${{r.u}}" target="_blank" rel="noopener">${{r.n}}</a>
          <div class="desc">${{r.d || ""}}</div></td>
      <td>${{(r.c||[]).map(pill).join(" ")}}</td>
      <td class="num">${{(r.s||0).toLocaleString()}}</td>
      <td class="num">${{r.est ? "≈" : ""}}+${{Math.round(r.v||0)}}</td>
    </tr>`).join("") || `<tr><td colspan="5">没有匹配的仓库</td></tr>`;
  document.getElementById("status").textContent = `显示 ${{view.length}} / ${{ALL.length}} 个仓库`;
  document.querySelectorAll(".chip").forEach(el => {{
    const on = el.dataset.track === track;
    el.classList.toggle("active", on);
    el.style.background = on && el.dataset.color ? el.dataset.color : "";
    el.style.color = on && el.dataset.color ? "#0d1117" : "";
  }});
}}
document.getElementById("q").addEventListener("input", apply);
document.getElementById("sort").addEventListener("change", apply);
document.getElementById("chips").addEventListener("click", e => {{
  const btn = e.target.closest(".chip");
  if (!btn) return;
  track = btn.dataset.track || "";
  apply();
}});
fetch("data/live-repos.json")
  .then(r => r.json())
  .then(rows => {{ ALL = rows; apply(); }})
  .catch(() => {{ document.getElementById("status").textContent = "无法加载 data/live-repos.json"; }});
</script>
</body>
</html>
"""
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"✅  {OUTPUT}  ({OUTPUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
