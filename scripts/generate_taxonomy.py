"""
generate_taxonomy.py
Generates docs/taxonomy.html — an interactive D3.js collapsible taxonomy tree.
Run: python scripts/generate_taxonomy.py
"""

import json
import os
import sys
from pathlib import Path

# ── allow sibling import when run from repo root ──────────────────────────────
sys.path.insert(0, str(Path(__file__).parent))
from data import TAXONOMY_TREE, META  # noqa: E402

DOCS_DIR = Path(__file__).parent.parent / "docs"
DOCS_DIR.mkdir(exist_ok=True)

OUTPUT = DOCS_DIR / "taxonomy.html"

# ──────────────────────────────────────────────────────────────────────────────
# Embed the Python dict as JSON for D3
# ──────────────────────────────────────────────────────────────────────────────
tree_json = json.dumps(TAXONOMY_TREE, ensure_ascii=False, indent=2)
meta_json = json.dumps(META, ensure_ascii=False)

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{META['title']} — Taxonomy Tree</title>
<style>
  :root {{
    --bg: #0d1117; --surface: #161b22; --border: #30363d;
    --text: #e6edf3; --muted: #8b949e; --accent: #58a6ff;
    --link: #79c0ff;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: var(--bg); color: var(--text); font-family: 'Segoe UI', system-ui, sans-serif; }}

  header {{
    padding: 20px 32px; border-bottom: 1px solid var(--border);
    display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;
  }}
  header h1 {{ font-size: 1.35rem; font-weight: 700; }}
  header h1 span {{ color: var(--accent); }}
  .badges {{ display: flex; gap: 8px; flex-wrap: wrap; }}
  .badge {{
    padding: 3px 10px; border-radius: 20px; font-size: 0.75rem;
    background: #21262d; border: 1px solid var(--border); color: var(--muted);
  }}
  .badge b {{ color: var(--text); }}

  .toolbar {{
    padding: 12px 24px; background: var(--surface); border-bottom: 1px solid var(--border);
    display: flex; gap: 10px; flex-wrap: wrap; align-items: center;
  }}
  .toolbar input {{
    flex: 1; min-width: 180px; max-width: 320px;
    background: var(--bg); border: 1px solid var(--border); border-radius: 6px;
    color: var(--text); padding: 6px 12px; font-size: 0.85rem; outline: none;
  }}
  .toolbar input:focus {{ border-color: var(--accent); }}
  .btn {{
    padding: 5px 14px; border-radius: 6px; font-size: 0.8rem; cursor: pointer;
    border: 1px solid var(--border); background: var(--surface); color: var(--text);
    transition: background 0.15s, border-color 0.15s;
  }}
  .btn:hover {{ background: #21262d; border-color: var(--accent); color: var(--accent); }}
  .btn.primary {{ background: var(--accent); color: #0d1117; border-color: var(--accent); font-weight: 600; }}
  .btn.primary:hover {{ background: #79c0ff; }}

  #canvas {{ width: 100%; overflow: hidden; cursor: grab; }}
  #canvas:active {{ cursor: grabbing; }}
  svg text {{ user-select: none; }}

  .node circle {{
    stroke-width: 2px; cursor: pointer;
    filter: drop-shadow(0 2px 4px rgba(0,0,0,.5));
    transition: r 0.2s;
  }}
  .node circle:hover {{ r: 11 !important; }}
  .node text {{ font-size: 12px; fill: var(--text); }}
  .node text.muted {{ fill: var(--muted); font-size: 10px; }}
  .link {{ fill: none; stroke: #30363d; stroke-width: 1.5px; stroke-opacity: .7; }}
  .node.highlight circle {{ stroke: #f0c040 !important; stroke-width: 3px; }}
  .node.highlight text {{ fill: #f0c040 !important; }}
  .node.faded {{ opacity: 0.25; }}

  #tooltip {{
    position: fixed; background: #1c2128; border: 1px solid var(--border);
    border-radius: 10px; padding: 12px 16px; pointer-events: none;
    max-width: 300px; font-size: 0.82rem; line-height: 1.6;
    z-index: 9999; box-shadow: 0 8px 24px rgba(0,0,0,.6);
    display: none;
  }}
  #tooltip h4 {{ color: var(--accent); margin-bottom: 4px; font-size: 0.9rem; }}
  #tooltip a {{ color: var(--link); text-decoration: none; }}
  #tooltip a:hover {{ text-decoration: underline; }}
  .pill {{
    display: inline-block; padding: 1px 8px; border-radius: 12px;
    font-size: 0.7rem; margin: 2px 2px 0 0; font-weight: 600;
  }}

  footer {{
    text-align: center; padding: 16px; font-size: 0.75rem; color: var(--muted);
    border-top: 1px solid var(--border); margin-top: 8px;
  }}
  footer a {{ color: var(--link); }}
</style>
</head>
<body>
<header>
  <h1>🌐 <span>{META['title']}</span> — Architecture Taxonomy</h1>
  <div class="badges">
    <span class="badge">📄 <b>{META['paper_count']}</b> papers</span>
    <span class="badge">🗓 Last updated <b>{META['last_updated']}</b></span>
    <span class="badge">📜 MIT License</span>
    <a href="{META['github_url']}" target="_blank" class="badge">⭐ GitHub</a>
    <a href="timeline.html" class="badge" style="color:var(--accent)">📅 Timeline →</a>
  </div>
</header>

<div class="toolbar">
  <input id="search" type="text" placeholder="🔍  Search models, categories…" />
  <button class="btn" onclick="expandAll()">Expand All</button>
  <button class="btn" onclick="collapseToLevel(2)">L2 View</button>
  <button class="btn" onclick="collapseToLevel(1)">L1 View</button>
  <button class="btn primary" onclick="resetView()">⌂ Reset</button>
  <span id="match-count" style="font-size:0.78rem;color:var(--muted);margin-left:6px;"></span>
</div>

<div id="canvas"></div>

<div id="tooltip"></div>

<footer>
  Auto-generated by <code>generate_taxonomy.py</code> ·
  Data: <a href="{META['github_url']}" target="_blank">Awesome-Native-Multimodal-Models</a> ·
  Visualized with <a href="https://d3js.org" target="_blank">D3.js v7</a>
</footer>

<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
<script>
// ── Embedded data ─────────────────────────────────────────────────────────
const RAW_TREE = {tree_json};

// ── Layout constants ─────────────────────────────────────────────────────
const W = window.innerWidth || 1400;
const H = Math.max(window.innerHeight - 160, 700);
const MARGIN = {{top: 40, right: 240, bottom: 40, left: 180}};

// ── SVG setup ────────────────────────────────────────────────────────────
const svg = d3.select("#canvas").append("svg")
  .attr("width", W).attr("height", H)
  .style("background", "#0d1117");

const g = svg.append("g")
  .attr("transform", `translate(${{MARGIN.left}},${{H/2}})`);

const zoom = d3.zoom()
  .scaleExtent([0.15, 3])
  .on("zoom", (event) => g.attr("transform", event.transform.translate(MARGIN.left, H / 2)));

svg.call(zoom);

// ── D3 tree layout ───────────────────────────────────────────────────────
const treeFn = d3.tree().nodeSize([28, 240]);
let root = d3.hierarchy(RAW_TREE);
root.x0 = 0; root.y0 = 0;

// Collapse nodes at depth >= 3 initially
root.each(d => {{ if (d.depth >= 3) d._children = d.children, d.children = null; }});

// ── Color mapping ────────────────────────────────────────────────────────
function getColor(d) {{
  let n = d;
  while (n) {{
    if (n.data.color) return n.data.color;
    n = n.parent;
  }}
  return "#58a6ff";
}}

// ── Link path ────────────────────────────────────────────────────────────
const linkGen = d3.linkHorizontal().x(d => d.y).y(d => d.x);

let i = 0; // node id counter

function update(source) {{
  treeFn(root);
  const nodes = root.descendants();
  const links = root.links();

  // ── Links ──────────────────────────────────────────────────────────────
  const link = g.selectAll("path.link").data(links, d => d.target.id);

  const linkEnter = link.enter().append("path")
    .attr("class", "link")
    .attr("d", () => {{
      const o = {{x: source.x0, y: source.y0}};
      return linkGen({{source: o, target: o}});
    }});

  link.merge(linkEnter).transition().duration(400)
    .attr("d", linkGen);

  link.exit().transition().duration(400)
    .attr("d", () => {{
      const o = {{x: source.x, y: source.y}};
      return linkGen({{source: o, target: o}});
    }}).remove();

  // ── Nodes ──────────────────────────────────────────────────────────────
  const node = g.selectAll("g.node").data(nodes, d => d.id || (d.id = ++i));

  const nodeEnter = node.enter().append("g")
    .attr("class", "node")
    .attr("transform", d => `translate(${{source.y0}},${{source.x0}})`)
    .on("click", (event, d) => {{ toggle(d); update(d); }})
    .on("mouseenter", showTooltip)
    .on("mousemove", moveTooltip)
    .on("mouseleave", hideTooltip);

  nodeEnter.append("circle")
    .attr("r", 0)
    .style("fill", d => (d._children || d.children) ? getColor(d) : "#1c2128")
    .style("stroke", getColor);

  nodeEnter.append("text")
    .attr("dy", "0.31em")
    .attr("x", d => (d.children || d._children) ? -14 : 14)
    .style("text-anchor", d => (d.children || d._children) ? "end" : "start")
    .text(d => d.data.name);

  nodeEnter.filter(d => d.data.year)
    .append("text")
    .attr("class", "muted")
    .attr("dy", "1.4em")
    .attr("x", d => (d.children || d._children) ? -14 : 14)
    .style("text-anchor", d => (d.children || d._children) ? "end" : "start")
    .text(d => d.data.year ? `${{d.data.year}}` : "");

  const nodeUpdate = node.merge(nodeEnter);

  nodeUpdate.transition().duration(400)
    .attr("transform", d => `translate(${{d.y}},${{d.x}})`);

  nodeUpdate.select("circle").transition().duration(400)
    .attr("r", d => d.depth === 0 ? 12 : d.depth === 1 ? 9 : 7)
    .style("fill", d => (d._children || d.children) ? getColor(d) : "#1c2128")
    .style("stroke", getColor);

  node.exit().transition().duration(400)
    .attr("transform", d => `translate(${{source.y}},${{source.x}})`).remove();

  nodes.forEach(d => {{ d.x0 = d.x; d.y0 = d.y; }});
}}

function toggle(d) {{
  if (d.children) {{ d._children = d.children; d.children = null; }}
  else {{ d.children = d._children; d._children = null; }}
}}

function expandAll() {{
  root.each(d => {{ if (d._children) {{ d.children = d._children; d._children = null; }} }});
  update(root);
}}

function collapseAll(node) {{
  if (node.children) {{
    node.children.forEach(collapseAll);
    node._children = node.children;
    node.children = null;
  }}
}}

function collapseToLevel(level) {{
  root.each(d => {{
    if (d.depth >= level) {{
      if (d.children) {{ d._children = d.children; d.children = null; }}
    }} else {{
      if (d._children) {{ d.children = d._children; d._children = null; }}
    }}
  }});
  update(root);
}}

function resetView() {{
  svg.transition().duration(500).call(zoom.transform, d3.zoomIdentity);
  collapseToLevel(2);
}}

// ── Tooltip ──────────────────────────────────────────────────────────────
const tooltip = document.getElementById("tooltip");

function showTooltip(event, d) {{
  const nd = d.data;
  let html = `<h4>${{nd.name}}</h4>`;
  if (nd.description) html += `<div style="color:var(--muted);margin-bottom:6px">${{nd.description}}</div>`;
  if (nd.year) html += `<span class="pill" style="background:#21262d;color:#58a6ff">📅 ${{nd.year}}</span>`;
  if (nd.arxiv) html += `<span class="pill" style="background:#21262d;color:#ffa657">
      <a href="https://arxiv.org/abs/${{nd.arxiv}}" target="_blank">📄 arXiv:${{nd.arxiv}}</a></span>`;
  if (nd.github) html += `<span class="pill" style="background:#21262d;color:#3fb950">
      <a href="${{nd.github}}" target="_blank">💻 GitHub</a></span>`;
  if (d.children || d._children) {{
    const cnt = (d.children || d._children).length;
    html += `<div style="margin-top:6px;color:var(--muted);font-size:0.75rem">${{cnt}} sub-node(s) — click to toggle</div>`;
  }}
  tooltip.innerHTML = html;
  tooltip.style.display = "block";
  moveTooltip(event);
}}

function moveTooltip(event) {{
  const tw = tooltip.offsetWidth, th = tooltip.offsetHeight;
  let x = event.clientX + 16, y = event.clientY + 16;
  if (x + tw > window.innerWidth - 10) x = event.clientX - tw - 16;
  if (y + th > window.innerHeight - 10) y = event.clientY - th - 16;
  tooltip.style.left = x + "px"; tooltip.style.top = y + "px";
}}

function hideTooltip() {{ tooltip.style.display = "none"; }}

// ── Search ───────────────────────────────────────────────────────────────
document.getElementById("search").addEventListener("input", function() {{
  const q = this.value.trim().toLowerCase();
  const cnt = document.getElementById("match-count");
  if (!q) {{
    g.selectAll("g.node").classed("highlight", false).classed("faded", false);
    cnt.textContent = "";
    return;
  }}
  let hits = 0;
  g.selectAll("g.node").each(function(d) {{
    const match = d.data.name.toLowerCase().includes(q) ||
                  (d.data.description || "").toLowerCase().includes(q) ||
                  String(d.data.year || "").includes(q);
    d3.select(this).classed("highlight", match).classed("faded", !match);
    if (match) hits++;
  }});
  cnt.textContent = hits ? `${{hits}} match${{hits > 1 ? "es" : ""}}` : "No matches";
}});

// ── Initial render ───────────────────────────────────────────────────────
update(root);
</script>
</body>
</html>
"""

OUTPUT.write_text(HTML, encoding="utf-8")
print(f"✅  {OUTPUT}  ({OUTPUT.stat().st_size // 1024} KB)")
