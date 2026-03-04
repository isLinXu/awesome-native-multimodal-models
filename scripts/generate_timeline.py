"""
generate_timeline.py
Generates docs/timeline.html — an interactive D3.js swim-lane timeline.
Run: python scripts/generate_timeline.py
"""

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from data import TIMELINE_MODELS, META  # noqa: E402

DOCS_DIR = Path(__file__).parent.parent / "docs"
DOCS_DIR.mkdir(exist_ok=True)
OUTPUT = DOCS_DIR / "timeline.html"

timeline_json = json.dumps(TIMELINE_MODELS, ensure_ascii=False, indent=2)
meta_json = json.dumps(META, ensure_ascii=False)
cats_json = json.dumps(META["categories"], ensure_ascii=False)

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{META['title']} — Timeline</title>
<style>
  :root {{
    --bg: #0d1117; --surface: #161b22; --border: #30363d;
    --text: #e6edf3; --muted: #8b949e; --accent: #58a6ff; --link: #79c0ff;
    --today: #9b59b6;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: var(--bg); color: var(--text); font-family: 'Segoe UI', system-ui, sans-serif;
         display: flex; flex-direction: column; height: 100vh; overflow: hidden; }}

  header {{
    padding: 14px 28px; border-bottom: 1px solid var(--border); flex-shrink: 0;
    display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;
  }}
  header h1 {{ font-size: 1.25rem; font-weight: 700; }}
  header h1 span {{ color: var(--accent); }}
  .stat-row {{ display: flex; gap: 18px; font-size: 0.8rem; color: var(--muted); }}
  .stat-row b {{ color: var(--text); }}

  .toolbar {{
    padding: 8px 20px; background: var(--surface); border-bottom: 1px solid var(--border);
    display: flex; gap: 8px; flex-wrap: wrap; align-items: center; flex-shrink: 0;
  }}
  .toolbar input {{
    background: var(--bg); border: 1px solid var(--border); border-radius: 6px;
    color: var(--text); padding: 5px 10px; font-size: 0.82rem; outline: none; min-width: 180px;
  }}
  .toolbar input:focus {{ border-color: var(--accent); }}
  .sep {{ width: 1px; height: 22px; background: var(--border); margin: 0 4px; }}
  .btn {{
    padding: 4px 12px; border-radius: 5px; font-size: 0.78rem; cursor: pointer;
    border: 1px solid var(--border); background: var(--surface); color: var(--text);
    transition: all 0.15s;
  }}
  .btn:hover {{ border-color: var(--accent); color: var(--accent); }}
  .cat-btn {{ border-radius: 20px; }}
  .cat-btn.active {{ color: #0d1117 !important; font-weight: 700; }}

  #main-area {{ flex: 1; overflow: hidden; position: relative; }}
  #main-svg {{ width: 100%; height: 100%; }}

  /* minimap */
  #minimap-wrap {{
    position: absolute; bottom: 56px; right: 16px;
    background: #1c2128; border: 1px solid var(--border); border-radius: 8px;
    padding: 6px; z-index: 100;
  }}
  #minimap-title {{ font-size: 0.65rem; color: var(--muted); text-align: center; margin-bottom: 4px; }}
  #mini-svg {{ display: block; }}

  /* zoom controls */
  #zoom-controls {{
    position: absolute; bottom: 16px; right: 16px;
    display: flex; gap: 4px; z-index: 100;
  }}

  #tooltip {{
    position: fixed; background: #1c2128; border: 1px solid var(--border); border-radius: 10px;
    padding: 12px 16px; pointer-events: none; max-width: 300px; font-size: 0.82rem; line-height: 1.6;
    z-index: 9999; box-shadow: 0 8px 24px rgba(0,0,0,.6); display: none;
  }}
  #tooltip h4 {{ color: var(--accent); margin-bottom: 4px; font-size: 0.9rem; }}
  #tooltip a {{ color: var(--link); text-decoration: none; }}
  .pill {{ display: inline-block; padding: 1px 8px; border-radius: 12px;
           font-size: 0.7rem; margin: 2px 2px 0 0; font-weight: 600; }}

  footer {{
    text-align: center; padding: 8px; font-size: 0.72rem; color: var(--muted);
    border-top: 1px solid var(--border); flex-shrink: 0;
  }}
  footer a {{ color: var(--link); }}
</style>
</head>
<body>
<header>
  <h1>📅 <span>{META['title']}</span> — Model Timeline</h1>
  <div class="stat-row">
    <span>Total <b id="total-count">—</b></span>
    <span>Landmarks <b id="lm-count">—</b></span>
    <span>Categories <b>5</b></span>
    <span>Span <b>2017 – 2026</b></span>
    <a href="taxonomy.html" style="color:var(--link)">🌐 Taxonomy →</a>
    <a href="{META['github_url']}" target="_blank" style="color:var(--link)">⭐ GitHub</a>
  </div>
</header>

<div class="toolbar">
  <input id="search" type="text" placeholder="🔍  Search…" />
  <div class="sep"></div>
  <button class="btn" onclick="jumpYear(2021)">2021</button>
  <button class="btn" onclick="jumpYear(2022)">2022</button>
  <button class="btn" onclick="jumpYear(2023)">2023</button>
  <button class="btn" onclick="jumpYear(2024)">2024</button>
  <button class="btn" onclick="jumpYear(2025)">2025</button>
  <button class="btn" onclick="jumpYear(2026)">2026</button>
  <div class="sep"></div>
  <div id="cat-filters"></div>
  <div class="sep"></div>
  <button class="btn" onclick="resetView()" style="color:var(--accent)">⌂ Reset</button>
  <span id="vis-count" style="font-size:0.75rem;color:var(--muted);margin-left:4px;"></span>
</div>

<div id="main-area">
  <svg id="main-svg"></svg>
  <div id="minimap-wrap">
    <div id="minimap-title">Overview</div>
    <svg id="mini-svg" width="220" height="70"></svg>
  </div>
  <div id="zoom-controls">
    <button class="btn" onclick="zoomBy(1.3)">＋</button>
    <button class="btn" onclick="zoomBy(0.77)">－</button>
  </div>
</div>

<div id="tooltip"></div>

<footer>
  Auto-generated by <code>generate_timeline.py</code> ·
  Data: <a href="{META['github_url']}" target="_blank">Awesome-Native-Multimodal-Models</a> ·
  Visualized with <a href="https://d3js.org" target="_blank">D3.js v7</a>
</footer>

<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
<script>
// ── Data ─────────────────────────────────────────────────────────────────
const DATA = {timeline_json};
const META = {meta_json};
const CAT_META = {cats_json};

// ── State ─────────────────────────────────────────────────────────────────
let activeCategories = new Set(Object.keys(CAT_META));
let searchQuery = "";
let currentTransform = d3.zoomIdentity;

// ── Stats ─────────────────────────────────────────────────────────────────
document.getElementById("total-count").textContent = DATA.length;
document.getElementById("lm-count").textContent = DATA.filter(d => d.landmark).length;

// ── Category filter buttons ───────────────────────────────────────────────
const filterDiv = document.getElementById("cat-filters");
Object.entries(CAT_META).forEach(([key, meta]) => {{
  const btn = document.createElement("button");
  btn.className = "btn cat-btn active";
  btn.textContent = meta.label;
  btn.style.borderColor = meta.color;
  btn.style.background = meta.color + "33";
  btn.style.color = meta.color;
  btn.dataset.cat = key;
  btn.onclick = () => {{
    if (activeCategories.has(key)) {{
      activeCategories.delete(key);
      btn.classList.remove("active");
      btn.style.background = "transparent";
    }} else {{
      activeCategories.add(key);
      btn.classList.add("active");
      btn.style.background = meta.color + "33";
    }}
    renderTimeline();
  }};
  filterDiv.appendChild(btn);
}});

// ── Layout ────────────────────────────────────────────────────────────────
const CATEGORIES = Object.keys(CAT_META);
const LANE_HEIGHT = 100;
const LANE_PADDING = 24;
const LABEL_H = 22;
const TOP_PAD = 50;
const LEFT_PAD = 100;
const RIGHT_PAD = 60;

const mainSvg = d3.select("#main-svg");
const miniSvg = d3.select("#mini-svg");
let mainW = 0, mainH = 0;

function resize() {{
  const el = document.getElementById("main-area");
  mainW = el.clientWidth;
  mainH = el.clientHeight;
  mainSvg.attr("width", mainW).attr("height", mainH);
  renderTimeline();
}}
window.addEventListener("resize", resize);

// ── Time scale (2017–2026.3) ──────────────────────────────────────────────
const T_MIN = new Date(2017, 0, 1);
const T_MAX = new Date(2026, 5, 1);
let xScale = d3.scaleTime().domain([T_MIN, T_MAX]);

// ── Zoom ──────────────────────────────────────────────────────────────────
const zoom = d3.zoom()
  .scaleExtent([0.4, 12])
  .translateExtent([[-LEFT_PAD * 4, -100], [99999, 99999]])
  .on("zoom", (event) => {{
    currentTransform = event.transform;
    renderTimeline(false);
  }});
mainSvg.call(zoom);

function zoomBy(k) {{
  mainSvg.transition().duration(300).call(zoom.scaleBy, k);
}}

function jumpYear(y) {{
  const x0 = LEFT_PAD + currentTransform.k *
    (xScale(new Date(y, 0, 1)) - xScale.range()[0]);
  const tx = mainW / 2 - x0;
  mainSvg.transition().duration(500).call(
    zoom.transform,
    d3.zoomIdentity.translate(tx, 0).scale(currentTransform.k)
  );
}}

function resetView() {{
  mainSvg.transition().duration(500).call(zoom.transform, d3.zoomIdentity);
  searchQuery = "";
  document.getElementById("search").value = "";
  activeCategories = new Set(Object.keys(CAT_META));
  document.querySelectorAll(".cat-btn").forEach(btn => {{
    btn.classList.add("active");
    const c = CAT_META[btn.dataset.cat].color;
    btn.style.background = c + "33";
  }});
  renderTimeline();
}}

// ── Lane assignment ───────────────────────────────────────────────────────
function assignLanes(models, xScaleLocal) {{
  // greedy: place in first lane where no label overlap
  const laneEnds = {{}};
  CATEGORIES.forEach(c => laneEnds[c] = []);
  const assigned = models.map(m => {{
    const px = xScaleLocal(new Date(m.year, (m.month || 1) - 1, 1));
    const laneList = laneEnds[m.category] || [];
    let lane = 0;
    while (lane < 8) {{
      const end = laneList[lane];
      if (end === undefined || px - end > (m.landmark ? 70 : 55)) break;
      lane++;
    }}
    if (!laneList[lane] || px > laneList[lane]) laneList[lane] = px + (m.name.length * 6 + 30);
    laneEnds[m.category] = laneList;
    return {{ ...m, lane }};
  }});
  return assigned;
}}

// ── Main render ───────────────────────────────────────────────────────────
function renderTimeline(recomputeZoom = true) {{
  if (!mainW) return;
  const innerW = mainW - LEFT_PAD - RIGHT_PAD;
  xScale = d3.scaleTime()
    .domain([T_MIN, T_MAX])
    .range([0, innerW]);

  const tx = currentTransform;
  const xScaleZ = tx.rescaleX(xScale);

  mainSvg.selectAll("*").remove();

  // defs clip
  const defs = mainSvg.append("defs");
  defs.append("clipPath").attr("id", "clip-main")
    .append("rect").attr("x", 0).attr("y", 0)
    .attr("width", innerW).attr("height", mainH);

  const root = mainSvg.append("g").attr("transform", `translate(${{LEFT_PAD}},0)`);
  const clip = root.append("g").attr("clip-path", "url(#clip-main)");

  // lane backgrounds
  CATEGORIES.forEach((cat, ci) => {{
    const y = TOP_PAD + ci * LANE_HEIGHT;
    const isActive = activeCategories.has(cat);
    clip.append("rect")
      .attr("x", 0).attr("y", y)
      .attr("width", innerW).attr("height", LANE_HEIGHT - 4)
      .attr("rx", 6)
      .attr("fill", isActive ? CAT_META[cat].color + "0d" : "#ffffff05")
      .attr("stroke", isActive ? CAT_META[cat].color + "22" : "#ffffff08")
      .attr("stroke-width", 1);
  }});

  // lane labels (fixed, outside clip)
  CATEGORIES.forEach((cat, ci) => {{
    const y = TOP_PAD + ci * LANE_HEIGHT + LANE_HEIGHT / 2;
    root.append("text")
      .attr("x", -12).attr("y", y)
      .attr("text-anchor", "end").attr("dominant-baseline", "middle")
      .attr("font-size", 11).attr("font-weight", "600")
      .attr("fill", activeCategories.has(cat) ? CAT_META[cat].color : "#444d56")
      .text(CAT_META[cat].label);
  }});

  // year grid lines
  const years = d3.timeYear.range(T_MIN, T_MAX);
  years.forEach(yr => {{
    const x = xScaleZ(yr);
    if (x < -20 || x > innerW + 20) return;
    clip.append("line")
      .attr("x1", x).attr("x2", x)
      .attr("y1", TOP_PAD - 10)
      .attr("y2", TOP_PAD + CATEGORIES.length * LANE_HEIGHT)
      .attr("stroke", "#ffffff10").attr("stroke-width", 1)
      .attr("stroke-dasharray", "4,4");

    root.append("text")
      .attr("x", x).attr("y", TOP_PAD - 14)
      .attr("text-anchor", "middle").attr("font-size", 11)
      .attr("fill", "#8b949e")
      .text(yr.getFullYear());
  }});

  // today line
  const todayX = xScaleZ(new Date(2026, 2, 1));
  clip.append("line")
    .attr("x1", todayX).attr("x2", todayX)
    .attr("y1", TOP_PAD - 10)
    .attr("y2", TOP_PAD + CATEGORIES.length * LANE_HEIGHT)
    .attr("stroke", "#9b59b6").attr("stroke-width", 1.5)
    .attr("stroke-dasharray", "5,4");

  clip.append("text")
    .attr("x", todayX + 4).attr("y", TOP_PAD - 14)
    .attr("font-size", 9).attr("fill", "#9b59b6").text("Mar 2026");

  // filter + assign lanes
  const visible = DATA.filter(m => {{
    const catOk = activeCategories.has(m.category);
    const qOk = !searchQuery || m.name.toLowerCase().includes(searchQuery) ||
                 (m.desc || "").toLowerCase().includes(searchQuery);
    return catOk && qOk;
  }});
  document.getElementById("vis-count").textContent =
    visible.length < DATA.length ? `${{visible.length}} / ${{DATA.length}} shown` : "";

  const assigned = assignLanes(visible, xScaleZ);

  // draw models
  assigned.forEach(m => {{
    const catIdx = CATEGORIES.indexOf(m.category);
    const cx = xScaleZ(new Date(m.year, (m.month || 1) - 1, 1));
    if (cx < -60 || cx > innerW + 60) return;
    const laneBaseY = TOP_PAD + catIdx * LANE_HEIGHT + LANE_HEIGHT / 2;
    const cy = laneBaseY + (m.lane - 1) * LABEL_H;
    const r = m.landmark ? 7 : 4.5;
    const col = CAT_META[m.category].color;
    const alpha = searchQuery && !m.name.toLowerCase().includes(searchQuery) ? "33" : "ff";

    const grp = clip.append("g")
      .style("cursor", "pointer")
      .on("mouseenter", (ev) => showTip(ev, m))
      .on("mousemove", moveTip)
      .on("mouseleave", hideTip)
      .on("click", () => {{
        const url = m.arxiv ? `https://arxiv.org/abs/${{m.arxiv}}` : (m.github || null);
        if (url) window.open(url, "_blank");
      }});

    grp.append("circle")
      .attr("cx", cx).attr("cy", cy).attr("r", r)
      .attr("fill", col + alpha)
      .attr("stroke", col + alpha)
      .attr("stroke-width", m.landmark ? 2 : 1.5)
      .attr("filter", m.landmark ? "drop-shadow(0 0 6px " + col + "88)" : "none");

    const fontSize = m.landmark ? 11 : 9.5;
    const fw = m.landmark ? "700" : "400";
    grp.append("text")
      .attr("x", cx + r + 5).attr("y", cy + 1)
      .attr("dominant-baseline", "middle")
      .attr("font-size", fontSize).attr("font-weight", fw)
      .attr("fill", col + alpha)
      .text(m.name);
  }});

  // ── Minimap ──────────────────────────────────────────────────────────────
  const mm = miniSvg;
  mm.selectAll("*").remove();
  const mmW = 220, mmH = 70;
  const mmX = d3.scaleTime().domain([T_MIN, T_MAX]).range([4, mmW - 4]);
  const mmYstep = (mmH - 8) / CATEGORIES.length;

  DATA.forEach(m => {{
    const ci = CATEGORIES.indexOf(m.category);
    mm.append("circle")
      .attr("cx", mmX(new Date(m.year, (m.month || 1) - 1, 1)))
      .attr("cy", 4 + ci * mmYstep + mmYstep / 2)
      .attr("r", m.landmark ? 2.5 : 1.2)
      .attr("fill", CAT_META[m.category].color + "cc");
  }});

  // viewport rect on minimap
  const vx0 = xScaleZ.invert(0), vx1 = xScaleZ.invert(innerW);
  const mmVx0 = Math.max(0, mmX(vx0)), mmVx1 = Math.min(mmW, mmX(vx1));
  mm.append("rect")
    .attr("x", mmVx0).attr("y", 0)
    .attr("width", Math.max(2, mmVx1 - mmVx0)).attr("height", mmH)
    .attr("fill", "none").attr("stroke", "#58a6ff").attr("stroke-width", 1.5)
    .attr("rx", 2).attr("opacity", 0.6);
}}

// ── Tooltip ───────────────────────────────────────────────────────────────
const tip = document.getElementById("tooltip");
function showTip(ev, m) {{
  const col = CAT_META[m.category]?.color || "#58a6ff";
  let html = `<h4>${{m.name}}</h4>`;
  html += `<div style="color:var(--muted);margin-bottom:6px">${{m.desc || ""}}</div>`;
  html += `<span class="pill" style="background:${{col}}22;color:${{col}}">
           ${{CAT_META[m.category]?.label}}</span> `;
  html += `<span class="pill" style="background:#21262d;color:#58a6ff">📅 ${{m.year}}/${{String(m.month).padStart(2,"0")}}</span>`;
  if (m.landmark) html += ` <span class="pill" style="background:#f0c04022;color:#f0c040">⭐ Landmark</span>`;
  if (m.arxiv) html += `<br/><a href="https://arxiv.org/abs/${{m.arxiv}}" target="_blank">📄 arXiv:${{m.arxiv}}</a>`;
  if (m.github) html += ` · <a href="${{m.github}}" target="_blank">💻 GitHub</a>`;
  html += `<div style="font-size:0.7rem;color:var(--muted);margin-top:6px">Click to open paper/project</div>`;
  tip.innerHTML = html;
  tip.style.display = "block";
  moveTip(ev);
}}
function moveTip(ev) {{
  const tw = tip.offsetWidth, th = tip.offsetHeight;
  let x = ev.clientX + 16, y = ev.clientY + 16;
  if (x + tw > window.innerWidth - 10) x = ev.clientX - tw - 16;
  if (y + th > window.innerHeight - 10) y = ev.clientY - th - 16;
  tip.style.left = x + "px"; tip.style.top = y + "px";
}}
function hideTip() {{ tip.style.display = "none"; }}

// ── Search ────────────────────────────────────────────────────────────────
document.getElementById("search").addEventListener("input", function() {{
  searchQuery = this.value.trim().toLowerCase();
  renderTimeline(false);
}});

// ── Init ──────────────────────────────────────────────────────────────────
resize();
</script>
</body>
</html>
"""

OUTPUT.write_text(HTML, encoding="utf-8")
print(f"✅  {OUTPUT}  ({OUTPUT.stat().st_size // 1024} KB)")
