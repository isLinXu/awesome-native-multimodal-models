"""
generate_papers.py
Generates docs/papers.html — searchable live paper browser.
Run: python scripts/generate_papers.py
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
OUTPUT = DOCS_DIR / "papers.html"

PAGE_CSS = """
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
  .lead { color: var(--muted); font-size: 0.9rem; margin-bottom: 20px; line-height: 1.7; }

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
  .toolbar input:focus, .toolbar select:focus { border-color: var(--accent); }
  .chips { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 14px; }
  .chip {
    border: 1px solid var(--border); background: #21262d; color: var(--muted);
    border-radius: 999px; padding: 5px 12px; font-size: 0.78rem; cursor: pointer;
  }
  .chip.active { color: #0d1117; font-weight: 700; border-color: transparent; }
  .meta-line { color: var(--muted); font-size: 0.8rem; margin-bottom: 12px; }

  table { width: 100%; border-collapse: collapse; font-size: 0.86rem; }
  th, td { text-align: left; padding: 9px 8px; border-bottom: 1px solid #21262d; vertical-align: top; }
  th { color: var(--muted); font-weight: 600; font-size: 0.75rem; cursor: pointer; user-select: none; }
  th:hover { color: var(--accent); }
  td a { color: var(--text); text-decoration: none; font-weight: 600; }
  td a:hover { color: var(--accent); }
  .date { color: var(--muted); font-variant-numeric: tabular-nums; white-space: nowrap; width: 108px; }
  .score { color: var(--muted); width: 56px; font-variant-numeric: tabular-nums; }
  .pill { display: inline-block; font-size: 0.68rem; padding: 1px 8px; border-radius: 999px; color: #0d1117; font-weight: 700; }
  .pager { display: flex; gap: 8px; align-items: center; justify-content: center; margin-top: 18px; }
  .pager button {
    background: var(--surface); border: 1px solid var(--border); color: var(--text);
    border-radius: 8px; padding: 6px 12px; cursor: pointer;
  }
  .pager button:disabled { opacity: 0.4; cursor: default; }
  .empty { color: var(--muted); padding: 32px 0; text-align: center; }
  footer {
    padding: 20px; font-size: 0.75rem; color: var(--muted); text-align: center;
    border-top: 1px solid var(--border);
  }
  footer a { color: var(--link); }
  @media (max-width: 720px) {
    .score, .hide-sm { display: none; }
  }
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
<title>{escape(meta['title'])} — Papers</title>
<style>
{NAV_CSS}
{PAGE_CSS}
</style>
</head>
<body>
{site_nav("papers", github)}
<main>
  <h1>📚 论文库 <span>Live papers</span></h1>
  <p class="lead">自动跟踪库，当前 <b>{escape(str(meta['paper_count']))}</b> 篇，从 2017 回填到今天。
     点赛道或搜标题；数据来自 <code>data/papers.json</code>，每日更新。</p>
  <div class="chips" id="chips">{''.join(chips)}</div>
  <div class="toolbar">
    <input id="q" type="search" placeholder="搜索标题或 arXiv ID…" />
    <select id="year">
      <option value="">全部年份</option>
    </select>
    <select id="sort">
      <option value="date">按日期</option>
      <option value="score">按相关分</option>
    </select>
  </div>
  <div class="meta-line" id="status">加载中…</div>
  <div style="overflow-x:auto">
    <table>
      <thead>
        <tr>
          <th data-sort="date">日期</th>
          <th>论文</th>
          <th class="hide-sm">赛道</th>
          <th class="score" data-sort="score">分</th>
        </tr>
      </thead>
      <tbody id="body"></tbody>
    </table>
  </div>
  <div class="pager">
    <button id="prev">上一页</button>
    <span id="pageinfo"></span>
    <button id="next">下一页</button>
  </div>
</main>
{site_footer(github)}
<script>
const TRACKS = {track_js};
const PAGE = 40;
let ALL = [];
let view = [];
let page = 0;
let track = decodeURIComponent((location.hash || "").replace("#","")).trim();
if (track && !(track in TRACKS)) track = "";

function pill(cid) {{
  const t = TRACKS[cid] || {{zh: cid, color: "#58a6ff"}};
  return `<span class="pill" style="background:${{t.color}}">${{t.zh || cid}}</span>`;
}}
function apply() {{
  const q = document.getElementById("q").value.trim().toLowerCase();
  const year = document.getElementById("year").value;
  const sort = document.getElementById("sort").value;
  view = ALL.filter(p => {{
    if (track && !(p.c || []).includes(track)) return false;
    if (year && !(p.d || "").startsWith(year)) return false;
    if (q && !((p.t || "").toLowerCase().includes(q) || (p.id || "").includes(q))) return false;
    return true;
  }});
  view.sort((a,b) => sort === "score" ? (b.s||0) - (a.s||0) : (b.d||"").localeCompare(a.d||""));
  page = 0;
  render();
}}
function render() {{
  const start = page * PAGE;
  const slice = view.slice(start, start + PAGE);
  const body = document.getElementById("body");
  if (!slice.length) {{
    body.innerHTML = `<tr><td colspan="4" class="empty">没有匹配的论文</td></tr>`;
  }} else {{
    body.innerHTML = slice.map(p => `
      <tr>
        <td class="date">${{p.d || "—"}}</td>
        <td><a href="https://arxiv.org/abs/${{p.id}}" target="_blank" rel="noopener">${{p.t}}</a></td>
        <td class="hide-sm">${{(p.c||[]).map(pill).join(" ")}}</td>
        <td class="score">${{p.s || "—"}}</td>
      </tr>`).join("");
  }}
  const pages = Math.max(1, Math.ceil(view.length / PAGE));
  document.getElementById("status").textContent =
    `显示 ${{view.length.toLocaleString()}} / ${{ALL.length.toLocaleString()}} 篇` + (track ? ` · ${{TRACKS[track]?.zh || track}}` : "");
  document.getElementById("pageinfo").textContent = `${{page+1}} / ${{pages}}`;
  document.getElementById("prev").disabled = page <= 0;
  document.getElementById("next").disabled = page >= pages - 1;
  document.querySelectorAll(".chip").forEach(el => {{
    const on = el.dataset.track === track;
    el.classList.toggle("active", on);
    el.style.background = on && el.dataset.color ? el.dataset.color : "";
    el.style.color = on && el.dataset.color ? "#0d1117" : "";
  }});
}}
document.getElementById("q").addEventListener("input", apply);
document.getElementById("year").addEventListener("change", apply);
document.getElementById("sort").addEventListener("change", apply);
document.getElementById("prev").onclick = () => {{ page = Math.max(0, page-1); render(); window.scrollTo(0,0); }};
document.getElementById("next").onclick = () => {{ page += 1; render(); window.scrollTo(0,0); }};
document.getElementById("chips").addEventListener("click", e => {{
  const btn = e.target.closest(".chip");
  if (!btn) return;
  track = btn.dataset.track || "";
  history.replaceState(null, "", track ? "#"+track : "papers.html");
  apply();
}});
window.addEventListener("hashchange", () => {{
  track = decodeURIComponent((location.hash || "").replace("#","")).trim();
  if (track && !(track in TRACKS)) track = "";
  apply();
}});
fetch("data/live-papers.json")
  .then(r => r.json())
  .then(rows => {{
    ALL = rows;
    const years = [...new Set(rows.map(p => (p.d||"").slice(0,4)).filter(y => /^\\d{{4}}$/.test(y)))].sort().reverse();
    const sel = document.getElementById("year");
    years.forEach(y => {{
      const o = document.createElement("option"); o.value = y; o.textContent = y; sel.appendChild(o);
    }});
    apply();
  }})
  .catch(() => {{
    document.getElementById("status").textContent = "无法加载 data/live-papers.json";
  }});
</script>
</body>
</html>
"""
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"✅  {OUTPUT}  ({OUTPUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
