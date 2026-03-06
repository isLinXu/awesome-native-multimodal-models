"""
generate_report.py — Generates docs/validation_report.html
A fully self-contained dark-themed HTML validation dashboard.

Run:  python scripts/generate_report.py
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate import run_validation, ValidationReport, Issue, SEVERITY_RANK  # noqa: E402
from data import TIMELINE_MODELS, META  # noqa: E402

DOCS_DIR = Path(__file__).parent.parent / "docs"
DOCS_DIR.mkdir(exist_ok=True)
OUTPUT = DOCS_DIR / "validation_report.html"


# ─────────────────────────────────────────────────────────────────────────────
# Build stats for charts
# ─────────────────────────────────────────────────────────────────────────────

def build_stats(report: ValidationReport) -> dict:
    """Aggregate all chart/table data from the report."""
    cats = META.get("categories", {})

    # Category distribution
    cat_counts = Counter(m.get("category", "Unknown") for m in TIMELINE_MODELS)

    # Year distribution
    year_counts = Counter(m.get("year") for m in TIMELINE_MODELS if m.get("year"))

    # Issue by code
    code_counts = Counter(i.code for i in report.issues)
    code_sev = {i.code: i.severity for i in report.issues}

    # Coverage: timeline vs taxonomy cross
    cv001 = [i for i in report.issues if i.code == "CV-001"]
    cv002 = [i for i in report.issues if i.code == "CV-002"]

    # Quality breakdown per check type
    tl_issues = [i for i in report.issues if i.code.startswith("TL")]
    tx_issues = [i for i in report.issues if i.code.startswith("TX")]
    cv_issues = [i for i in report.issues if i.code.startswith("CV")]
    mt_issues = [i for i in report.issues if i.code.startswith("MT")]

    # Field completeness for timeline
    fields = ["arxiv", "github", "desc", "month", "landmark"]
    completeness = {}
    total = len(TIMELINE_MODELS)
    for f in fields:
        filled = sum(1 for m in TIMELINE_MODELS
                     if m.get(f) not in (None, "", False) and m.get(f) is not False)
        # landmark=False is falsy but exists — count differently
        if f == "landmark":
            filled = sum(1 for m in TIMELINE_MODELS if "landmark" in m)
        completeness[f] = round(filled / total * 100) if total else 0

    return {
        "cat_labels":     [cats.get(k, {}).get("label", k) for k in sorted(cat_counts)],
        "cat_values":     [cat_counts[k] for k in sorted(cat_counts)],
        "cat_colors":     [cats.get(k, {}).get("color", "#888") for k in sorted(cat_counts)],
        "year_labels":    sorted(year_counts.keys()),
        "year_values":    [year_counts[y] for y in sorted(year_counts.keys())],
        "code_labels":    sorted(code_counts.keys()),
        "code_values":    [code_counts[c] for c in sorted(code_counts.keys())],
        "code_sevs":      [code_sev.get(c, "INFO") for c in sorted(code_counts.keys())],
        "tl_count":       len(tl_issues),
        "tx_count":       len(tx_issues),
        "cv_count":       len(cv_issues),
        "mt_count":       len(mt_issues),
        "cv001_models":   [i.model for i in cv001][:30],
        "cv002_models":   [i.model for i in cv002][:30],
        "completeness":   completeness,
    }


# ─────────────────────────────────────────────────────────────────────────────
# HTML builder
# ─────────────────────────────────────────────────────────────────────────────

SEV_COLOR = {"ERROR": "#ff7b7b", "WARNING": "#ffc947", "INFO": "#74c0fc"}
SEV_BG    = {"ERROR": "#3d1a1a", "WARNING": "#3d2e00", "INFO": "#0d2d45"}
SEV_ICON  = {"ERROR": "🔴", "WARNING": "🟡", "INFO": "🔵"}


def _issue_rows(issues: list[Issue]) -> str:
    if not issues:
        return '<tr><td colspan="5" class="empty-row">No issues in this category ✅</td></tr>'
    rows = []
    for iss in issues:
        col  = SEV_COLOR.get(iss.severity, "#aaa")
        bg   = SEV_BG.get(iss.severity,   "#111")
        icon = SEV_ICON.get(iss.severity,  "⚪")
        sug  = f'<br/><span class="suggestion">↳ {iss.suggestion}</span>' if iss.suggestion else ""
        rows.append(
            f'<tr class="issue-row" data-sev="{iss.severity}" data-code="{iss.code}">'
            f'<td><span class="sev-badge" style="background:{bg};color:{col}">'
            f'{icon} {iss.severity}</span></td>'
            f'<td><code class="code-tag">{iss.code}</code></td>'
            f'<td class="loc-cell">{iss.location}</td>'
            f'<td class="model-cell"><b>{iss.model}</b></td>'
            f'<td class="msg-cell">{iss.message}{sug}</td>'
            f'</tr>'
        )
    return "\n".join(rows)


def _score_ring_svg(score: int, label: str) -> str:
    """Return an SVG score ring."""
    color = "#3fb950" if score >= 85 else ("#ffc947" if score >= 70 else "#ff7b7b")
    r, cx, cy = 54, 68, 68
    circumference = 2 * 3.14159 * r
    offset = circumference * (1 - score / 100)
    return f"""
<svg width="136" height="136" viewBox="0 0 136 136">
  <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#21262d" stroke-width="12"/>
  <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-width="12"
          stroke-dasharray="{circumference:.1f}" stroke-dashoffset="{offset:.1f}"
          stroke-linecap="round" transform="rotate(-90 {cx} {cy})"/>
  <text x="{cx}" y="{cy-6}" text-anchor="middle" fill="{color}"
        font-size="26" font-weight="800" font-family="Segoe UI,system-ui,sans-serif">{score}</text>
  <text x="{cx}" y="{cy+16}" text-anchor="middle" fill="#8b949e"
        font-size="12" font-family="Segoe UI,system-ui,sans-serif">{label}</text>
</svg>"""


def build_html(report: ValidationReport) -> str:
    stats    = build_stats(report)
    score    = report.quality_score
    label    = report.quality_label
    score_color = "#3fb950" if score >= 85 else ("#ffc947" if score >= 70 else "#ff7b7b")
    errors   = len(report.errors)
    warnings = len(report.warnings)
    infos    = len(report.infos)
    total_issues = len(report.issues)
    ring_svg = _score_ring_svg(score, label)

    all_rows     = _issue_rows(report.issues)
    error_rows   = _issue_rows(report.errors)
    warning_rows = _issue_rows(report.warnings)
    info_rows    = _issue_rows(report.infos)

    # JSON for JS
    stats_js     = json.dumps(stats,             ensure_ascii=False)
    report_js    = json.dumps(report.to_dict(),  ensure_ascii=False)

    # Cross-coverage lists
    cv001_list = ", ".join(stats["cv001_models"]) or "None"
    cv002_list = ", ".join(stats["cv002_models"]) or "None"

    # Completeness bars
    comp_bars = ""
    for fname, pct in stats["completeness"].items():
        bar_color = "#3fb950" if pct >= 90 else ("#ffc947" if pct >= 60 else "#ff7b7b")
        comp_bars += f"""
        <div class="comp-row">
          <span class="comp-label">{fname}</span>
          <div class="comp-bar-bg">
            <div class="comp-bar-fill" style="width:{pct}%;background:{bar_color}"></div>
          </div>
          <span class="comp-pct" style="color:{bar_color}">{pct}%</span>
        </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>Validation Report — Awesome Native Multimodal Models</title>
<style>
:root{{
  --bg:#0d1117;--surface:#161b22;--surface2:#1c2128;--border:#30363d;
  --text:#e6edf3;--muted:#8b949e;--accent:#58a6ff;--link:#79c0ff;
  --green:#3fb950;--yellow:#ffc947;--red:#ff7b7b;--purple:#bc8cff;
}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;min-height:100vh}}
a{{color:var(--link);text-decoration:none}}a:hover{{text-decoration:underline}}

/* ── Header ── */
header{{padding:20px 32px;border-bottom:1px solid var(--border);
  display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px}}
header h1{{font-size:1.3rem;font-weight:700}}header h1 span{{color:var(--accent)}}
.hdr-right{{display:flex;gap:10px;flex-wrap:wrap;align-items:center}}
.badge{{padding:3px 12px;border-radius:20px;font-size:0.75rem;background:var(--surface2);
  border:1px solid var(--border);color:var(--muted)}}
.badge b{{color:var(--text)}}
.btn{{padding:5px 16px;border-radius:6px;font-size:0.8rem;cursor:pointer;
  border:1px solid var(--border);background:var(--surface);color:var(--text);
  transition:all .15s}}
.btn:hover{{border-color:var(--accent);color:var(--accent)}}
.btn.primary{{background:var(--accent);color:#0d1117;border-color:var(--accent);font-weight:700}}

/* ── Layout ── */
.main{{max-width:1320px;margin:0 auto;padding:28px 24px}}

/* ── Dashboard cards ── */
.dash-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:16px;margin-bottom:28px}}
.dash-card{{background:var(--surface);border:1px solid var(--border);border-radius:12px;
  padding:20px 18px;text-align:center;transition:transform .2s}}
.dash-card:hover{{transform:translateY(-2px)}}
.dash-num{{font-size:2.2rem;font-weight:800;line-height:1}}
.dash-label{{font-size:0.75rem;color:var(--muted);margin-top:6px}}
.dash-card.error  .dash-num{{color:var(--red)}}
.dash-card.warn   .dash-num{{color:var(--yellow)}}
.dash-card.info   .dash-num{{color:var(--accent)}}
.dash-card.total  .dash-num{{color:var(--text)}}
.dash-card.score  .dash-num{{color:{score_color}}}

/* ── Score ring ── */
.score-section{{display:flex;align-items:center;gap:32px;
  background:var(--surface);border:1px solid var(--border);border-radius:12px;
  padding:24px 28px;margin-bottom:28px;flex-wrap:wrap}}
.score-meta h2{{font-size:1.2rem;margin-bottom:8px}}
.score-meta p{{font-size:0.85rem;color:var(--muted);line-height:1.7;max-width:420px}}
.breakdown-grid{{display:flex;gap:20px;flex-wrap:wrap;margin-top:12px}}
.bkd-item{{background:var(--surface2);border:1px solid var(--border);border-radius:8px;
  padding:10px 18px;text-align:center}}
.bkd-item .num{{font-size:1.4rem;font-weight:700}}
.bkd-item .lbl{{font-size:0.7rem;color:var(--muted)}}

/* ── Section headings ── */
.section-title{{font-size:1.05rem;font-weight:700;margin:28px 0 14px;
  display:flex;align-items:center;gap:8px}}
.section-title::before{{content:'';display:block;width:4px;height:18px;
  background:var(--accent);border-radius:2px}}

/* ── Charts row ── */
.charts-row{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;margin-bottom:28px}}
.chart-card{{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:20px}}
.chart-card h3{{font-size:0.88rem;font-weight:600;margin-bottom:14px;color:var(--muted)}}
canvas{{max-height:220px}}

/* ── Completeness ── */
.comp-row{{display:flex;align-items:center;gap:10px;margin-bottom:8px}}
.comp-label{{width:80px;font-size:0.8rem;color:var(--muted);text-align:right}}
.comp-bar-bg{{flex:1;background:var(--surface2);border-radius:20px;height:8px;overflow:hidden}}
.comp-bar-fill{{height:100%;border-radius:20px;transition:width .4s}}
.comp-pct{{width:38px;font-size:0.78rem;font-weight:700;text-align:right}}

/* ── Tabs ── */
.tabs{{display:flex;gap:0;border-bottom:1px solid var(--border);margin-bottom:0;overflow-x:auto}}
.tab-btn{{padding:9px 20px;font-size:0.83rem;cursor:pointer;background:none;
  border:none;border-bottom:2px solid transparent;color:var(--muted);
  white-space:nowrap;transition:all .15s}}
.tab-btn:hover{{color:var(--text)}}
.tab-btn.active{{color:var(--accent);border-bottom-color:var(--accent);font-weight:600}}
.tab-panel{{display:none;padding-top:16px}}
.tab-panel.active{{display:block}}

/* ── Filter toolbar ── */
.filter-bar{{display:flex;gap:10px;flex-wrap:wrap;align-items:center;
  padding:10px 0 14px}}
.filter-bar input{{background:var(--bg);border:1px solid var(--border);border-radius:6px;
  color:var(--text);padding:5px 10px;font-size:0.82rem;outline:none;min-width:200px}}
.filter-bar input:focus{{border-color:var(--accent)}}
.filter-btn{{padding:4px 14px;border-radius:20px;font-size:0.75rem;cursor:pointer;
  border:1px solid var(--border);background:transparent;color:var(--muted);transition:all .15s}}
.filter-btn:hover,.filter-btn.active{{border-color:var(--accent);color:var(--accent)}}
.filter-btn[data-sev="ERROR"].active{{border-color:var(--red);color:var(--red);background:#3d1a1a}}
.filter-btn[data-sev="WARNING"].active{{border-color:var(--yellow);color:var(--yellow);background:#3d2e00}}
.filter-btn[data-sev="INFO"].active{{border-color:var(--accent);color:var(--accent);background:#0d2d45}}

/* ── Issue table ── */
.issue-table-wrap{{overflow-x:auto;border:1px solid var(--border);border-radius:10px}}
table{{width:100%;border-collapse:collapse;font-size:0.82rem}}
th{{background:var(--surface2);padding:9px 12px;text-align:left;
  font-size:0.75rem;font-weight:600;color:var(--muted);
  border-bottom:1px solid var(--border)}}
td{{padding:9px 12px;border-bottom:1px solid #21262d;vertical-align:top}}
tr:last-child td{{border-bottom:none}}
tr.issue-row{{transition:background .1s}}
tr.issue-row:hover{{background:var(--surface2)}}
tr.issue-row.hidden{{display:none}}
.empty-row{{color:var(--muted);font-style:italic;text-align:center;padding:20px}}
.sev-badge{{display:inline-block;padding:2px 9px;border-radius:20px;
  font-size:0.7rem;font-weight:700;white-space:nowrap}}
code.code-tag{{background:var(--surface2);border:1px solid var(--border);
  border-radius:4px;padding:1px 7px;font-size:0.78rem;color:var(--purple)}}
.loc-cell{{color:var(--muted);font-size:0.75rem;max-width:180px;word-break:break-all}}
.model-cell{{color:var(--text);min-width:120px}}
.msg-cell{{color:var(--text);line-height:1.6}}
.suggestion{{font-size:0.75rem;color:var(--muted)}}

/* ── Coverage list ── */
.coverage-grid{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:28px}}
.cov-card{{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:16px 18px}}
.cov-card h4{{font-size:0.85rem;font-weight:600;margin-bottom:10px;color:var(--yellow)}}
.cov-card.ok h4{{color:var(--green)}}
.cov-tags{{display:flex;flex-wrap:wrap;gap:6px}}
.cov-tag{{background:var(--surface2);border:1px solid var(--border);border-radius:6px;
  padding:2px 9px;font-size:0.75rem;color:var(--muted)}}

/* ── JSON modal ── */
#json-modal{{display:none;position:fixed;inset:0;background:#000a;z-index:9999;
  align-items:center;justify-content:center}}
#json-modal.open{{display:flex}}
.modal-box{{background:var(--surface);border:1px solid var(--border);border-radius:12px;
  width:min(860px,92vw);max-height:80vh;overflow:hidden;
  display:flex;flex-direction:column}}
.modal-header{{padding:14px 18px;border-bottom:1px solid var(--border);
  display:flex;justify-content:space-between;align-items:center}}
.modal-header h3{{font-size:0.95rem;font-weight:700}}
.modal-body{{overflow-y:auto;padding:16px}}
pre.json-pre{{font-size:0.75rem;color:var(--green);white-space:pre-wrap;word-break:break-all}}

footer{{text-align:center;padding:24px;font-size:0.73rem;color:var(--muted);
  border-top:1px solid var(--border);margin-top:32px}}
</style>
</head>
<body>

<header>
  <h1>🔍 <span>Validation Report</span> — Awesome Native Multimodal Models</h1>
  <div class="hdr-right">
    <span class="badge">Generated <b>{report.generated_at}</b></span>
    <a href="taxonomy.html"  class="badge">🌐 Taxonomy</a>
    <a href="timeline.html"  class="badge">📅 Timeline</a>
    <a href="index.html"     class="badge">🏠 Index</a>
    <button class="btn" onclick="showJson()">📋 Export JSON</button>
    <button class="btn primary" onclick="window.print()">🖨 Print</button>
  </div>
</header>

<div class="main">

  <!-- ── Dashboard cards ─────────────────────────────────────────────── -->
  <div class="dash-grid">
    <div class="dash-card total">
      <div class="dash-num">{report.total_timeline}</div>
      <div class="dash-label">Timeline Models</div>
    </div>
    <div class="dash-card total">
      <div class="dash-num">{report.total_taxonomy_leaves}</div>
      <div class="dash-label">Taxonomy Leaves</div>
    </div>
    <div class="dash-card total">
      <div class="dash-num">{total_issues}</div>
      <div class="dash-label">Total Issues</div>
    </div>
    <div class="dash-card error">
      <div class="dash-num">{errors}</div>
      <div class="dash-label">🔴 Errors</div>
    </div>
    <div class="dash-card warn">
      <div class="dash-num">{warnings}</div>
      <div class="dash-label">🟡 Warnings</div>
    </div>
    <div class="dash-card info">
      <div class="dash-num">{infos}</div>
      <div class="dash-label">🔵 Infos</div>
    </div>
    <div class="dash-card score">
      <div class="dash-num" style="color:{score_color}">{score}</div>
      <div class="dash-label">Quality Score / 100</div>
    </div>
  </div>

  <!-- ── Score ring + breakdown ──────────────────────────────────────── -->
  <div class="score-section">
    {ring_svg}
    <div class="score-meta">
      <h2>Data Quality: <span style="color:{score_color}">{label}</span></h2>
      <p>Score is computed as <code>100 − 5×errors − 2×warnings</code>.
         Fix all ERRORs first, then address WARNINGs for a clean dataset.</p>
      <div class="breakdown-grid">
        <div class="bkd-item">
          <div class="num" style="color:#ffc947">{stats["tl_count"]}</div>
          <div class="lbl">Timeline Issues</div>
        </div>
        <div class="bkd-item">
          <div class="num" style="color:#74c0fc">{stats["tx_count"]}</div>
          <div class="lbl">Taxonomy Issues</div>
        </div>
        <div class="bkd-item">
          <div class="num" style="color:#bc8cff">{stats["cv_count"]}</div>
          <div class="lbl">Cross-Val Issues</div>
        </div>
        <div class="bkd-item">
          <div class="num" style="color:#ff7b7b">{stats["mt_count"]}</div>
          <div class="lbl">Meta Issues</div>
        </div>
      </div>
    </div>
  </div>

  <!-- ── Charts ──────────────────────────────────────────────────────── -->
  <div class="section-title">📊 Dataset Overview</div>
  <div class="charts-row">
    <div class="chart-card">
      <h3>Models by Category</h3>
      <canvas id="catChart"></canvas>
    </div>
    <div class="chart-card">
      <h3>Models by Year</h3>
      <canvas id="yearChart"></canvas>
    </div>
    <div class="chart-card">
      <h3>Issues by Code</h3>
      <canvas id="codeChart"></canvas>
    </div>
  </div>

  <!-- ── Field Completeness ──────────────────────────────────────────── -->
  <div class="section-title">✅ Field Completeness (Timeline Models)</div>
  <div style="background:var(--surface);border:1px solid var(--border);
              border-radius:12px;padding:20px 24px;margin-bottom:28px;max-width:520px">
    {comp_bars}
  </div>

  <!-- ── Cross-Coverage ─────────────────────────────────────────────── -->
  <div class="section-title">🔗 Timeline ↔ Taxonomy Coverage</div>
  <div class="coverage-grid">
    <div class="cov-card {'ok' if not stats['cv001_models'] else ''}">
      <h4>{'✅ All timeline models in taxonomy' if not stats['cv001_models']
           else f'⚠️ In Timeline but NOT in Taxonomy ({len(stats["cv001_models"])})'}</h4>
      <div class="cov-tags">
        {''.join(f'<span class="cov-tag">{m}</span>' for m in stats["cv001_models"])
         or '<span class="cov-tag" style="color:var(--green)">— none —</span>'}
      </div>
    </div>
    <div class="cov-card {'ok' if not stats['cv002_models'] else ''}">
      <h4>{'✅ All taxonomy leaves in timeline' if not stats['cv002_models']
           else f'⚠️ In Taxonomy but NOT in Timeline ({len(stats["cv002_models"])})'}</h4>
      <div class="cov-tags">
        {''.join(f'<span class="cov-tag">{m}</span>' for m in stats["cv002_models"])
         or '<span class="cov-tag" style="color:var(--green)">— none —</span>'}
      </div>
    </div>
  </div>

  <!-- ── Issue Table ─────────────────────────────────────────────────── -->
  <div class="section-title">📋 Issue Details</div>
  <div class="tabs">
    <button class="tab-btn active" onclick="switchTab('all',this)">All ({total_issues})</button>
    <button class="tab-btn" onclick="switchTab('error',this)">🔴 Errors ({errors})</button>
    <button class="tab-btn" onclick="switchTab('warning',this)">🟡 Warnings ({warnings})</button>
    <button class="tab-btn" onclick="switchTab('info',this)">🔵 Infos ({infos})</button>
  </div>

  <div id="panel-all" class="tab-panel active">
    <div class="filter-bar">
      <input type="text" id="search-all" placeholder="🔍 Filter by model, message, code…"
             oninput="filterTable('all', this.value)"/>
      <button class="filter-btn active" data-sev="ALL"
              onclick="toggleSev('all','ALL',this)">All</button>
      <button class="filter-btn" data-sev="ERROR"
              onclick="toggleSev('all','ERROR',this)">ERROR</button>
      <button class="filter-btn" data-sev="WARNING"
              onclick="toggleSev('all','WARNING',this)">WARNING</button>
      <button class="filter-btn" data-sev="INFO"
              onclick="toggleSev('all','INFO',this)">INFO</button>
    </div>
    <div class="issue-table-wrap">
      <table id="table-all"><thead>
        <tr><th>Severity</th><th>Code</th><th>Location</th><th>Model</th><th>Message / Suggestion</th></tr>
      </thead><tbody>{all_rows}</tbody></table>
    </div>
  </div>

  <div id="panel-error" class="tab-panel">
    <div class="issue-table-wrap">
      <table><thead>
        <tr><th>Severity</th><th>Code</th><th>Location</th><th>Model</th><th>Message / Suggestion</th></tr>
      </thead><tbody>{error_rows}</tbody></table>
    </div>
  </div>

  <div id="panel-warning" class="tab-panel">
    <div class="issue-table-wrap">
      <table><thead>
        <tr><th>Severity</th><th>Code</th><th>Location</th><th>Model</th><th>Message / Suggestion</th></tr>
      </thead><tbody>{warning_rows}</tbody></table>
    </div>
  </div>

  <div id="panel-info" class="tab-panel">
    <div class="issue-table-wrap">
      <table><thead>
        <tr><th>Severity</th><th>Code</th><th>Location</th><th>Model</th><th>Message / Suggestion</th></tr>
      </thead><tbody>{info_rows}</tbody></table>
    </div>
  </div>

</div><!-- /main -->

<!-- JSON Modal -->
<div id="json-modal">
  <div class="modal-box">
    <div class="modal-header">
      <h3>📋 Validation Report JSON</h3>
      <div style="display:flex;gap:8px">
        <button class="btn" onclick="copyJson()">📋 Copy</button>
        <button class="btn" onclick="downloadJson()">⬇️ Download</button>
        <button class="btn" onclick="closeJson()">✕ Close</button>
      </div>
    </div>
    <div class="modal-body">
      <pre class="json-pre" id="json-pre"></pre>
    </div>
  </div>
</div>

<footer>
  Auto-generated by <code>generate_report.py</code> ·
  <a href="https://github.com/your-username/Awesome-Native-Multimodal-Models">GitHub</a> ·
  Visualized with <a href="https://cdn.jsdelivr.net/npm/chart.js">Chart.js</a>
</footer>

<script src="https://cdn.jsdelivr.net/npm/chart.js@4/dist/chart.umd.min.js"></script>
<script>
// ── Embedded data ─────────────────────────────────────────────────────────
const STATS = {stats_js};
const REPORT = {report_js};

// ── Charts ────────────────────────────────────────────────────────────────
const CHART_OPTS = {{
  responsive: true,
  plugins: {{ legend: {{ labels: {{ color: '#e6edf3', font: {{ size: 11 }} }} }} }},
  scales: {{
    x: {{ ticks: {{ color: '#8b949e', font: {{ size: 10 }} }}, grid: {{ color: '#21262d' }} }},
    y: {{ ticks: {{ color: '#8b949e', font: {{ size: 10 }} }}, grid: {{ color: '#21262d' }} }}
  }}
}};

// Category chart
new Chart(document.getElementById('catChart'), {{
  type: 'doughnut',
  data: {{
    labels: STATS.cat_labels,
    datasets: [{{ data: STATS.cat_values, backgroundColor: STATS.cat_colors,
                  borderColor: '#0d1117', borderWidth: 2 }}]
  }},
  options: {{
    responsive: true,
    plugins: {{
      legend: {{ position: 'bottom', labels: {{ color: '#e6edf3', font: {{ size: 10 }},
                                               boxWidth: 12, padding: 10 }} }}
    }}
  }}
}});

// Year chart
new Chart(document.getElementById('yearChart'), {{
  type: 'bar',
  data: {{
    labels: STATS.year_labels,
    datasets: [{{ label: 'Models', data: STATS.year_values,
                  backgroundColor: '#58a6ff88', borderColor: '#58a6ff', borderWidth: 1 }}]
  }},
  options: {{ ...CHART_OPTS, plugins: {{ legend: {{ display: false }} }} }}
}});

// Code chart
const SEV_COLORS = {{ ERROR: '#ff7b7b', WARNING: '#ffc947', INFO: '#74c0fc' }};
new Chart(document.getElementById('codeChart'), {{
  type: 'bar',
  data: {{
    labels: STATS.code_labels,
    datasets: [{{
      label: 'Issues',
      data: STATS.code_values,
      backgroundColor: STATS.code_sevs.map(s => SEV_COLORS[s] + '88'),
      borderColor:     STATS.code_sevs.map(s => SEV_COLORS[s]),
      borderWidth: 1
    }}]
  }},
  options: {{
    indexAxis: 'y',
    responsive: true,
    plugins: {{ legend: {{ display: false }} }},
    scales: {{
      x: {{ ticks: {{ color: '#8b949e', font: {{ size: 10 }} }}, grid: {{ color: '#21262d' }} }},
      y: {{ ticks: {{ color: '#e6edf3', font: {{ size: 9 }} }}, grid: {{ color: '#21262d' }} }}
    }}
  }}
}});

// ── Tabs ──────────────────────────────────────────────────────────────────
function switchTab(id, btn) {{
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('panel-' + id).classList.add('active');
  btn.classList.add('active');
}}

// ── Filter ────────────────────────────────────────────────────────────────
let activeSev = 'ALL';
function filterTable(panel, q) {{
  const rows = document.querySelectorAll('#table-' + panel + ' tbody tr.issue-row');
  const lq = q.toLowerCase();
  rows.forEach(row => {{
    const sev = row.dataset.sev;
    const text = row.textContent.toLowerCase();
    const sevOk = activeSev === 'ALL' || sev === activeSev;
    const qOk   = !lq || text.includes(lq);
    row.classList.toggle('hidden', !(sevOk && qOk));
  }});
}}
function toggleSev(panel, sev, btn) {{
  activeSev = sev;
  document.querySelectorAll('.filter-bar .filter-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  filterTable(panel, document.getElementById('search-all')?.value || '');
}}

// ── JSON Modal ────────────────────────────────────────────────────────────
function showJson() {{
  document.getElementById('json-pre').textContent = JSON.stringify(REPORT, null, 2);
  document.getElementById('json-modal').classList.add('open');
}}
function closeJson() {{ document.getElementById('json-modal').classList.remove('open'); }}
function copyJson() {{
  navigator.clipboard.writeText(JSON.stringify(REPORT, null, 2))
    .then(() => alert('Copied to clipboard!'));
}}
function downloadJson() {{
  const blob = new Blob([JSON.stringify(REPORT, null, 2)], {{type: 'application/json'}});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob); a.download = 'validation_report.json'; a.click();
}}
document.getElementById('json-modal').addEventListener('click', e => {{
  if (e.target === e.currentTarget) closeJson();
}});
</script>
</body>
</html>"""


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main() -> None:
    print("🔍 Running validation…")
    report = run_validation()

    errors   = len(report.errors)
    warnings = len(report.warnings)
    infos    = len(report.infos)
    print(f"   🔴 Errors:   {errors}")
    print(f"   🟡 Warnings: {warnings}")
    print(f"   🔵 Infos:    {infos}")
    print(f"   🏆 Score:    {report.quality_score}/100  ({report.quality_label})")

    html = build_html(report)
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"✅  {OUTPUT}  ({OUTPUT.stat().st_size // 1024} KB)")

    # Also write JSON sidecar
    json_path = DOCS_DIR / "validation.json"
    json_path.write_text(json.dumps(report.to_dict(), ensure_ascii=False, indent=2))
    print(f"📄  {json_path}")


if __name__ == "__main__":
    main()
