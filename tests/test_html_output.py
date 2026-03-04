"""
tests/test_html_output.py
Validates the generated HTML files in docs/.
Run: python tests/test_html_output.py
"""
import sys
from pathlib import Path

DOCS = Path(__file__).parent.parent / "docs"
ERRORS = []

def err(msg):
    ERRORS.append(msg)
    print(f"  ✗ {msg}")

def ok(msg):
    print(f"  ✓ {msg}")

# ─── Check file existence ──────────────────────────────────────────────────
print("\n── Checking file existence ──────────────────────────────────────────")
for fname in ("index.html", "taxonomy.html", "timeline.html"):
    path = DOCS / fname
    if path.exists():
        size_kb = path.stat().st_size // 1024
        ok(f"{fname}  ({size_kb} KB)")
        min_size = 3 if fname == "index.html" else 10
        if size_kb < min_size:
            err(f"{fname} seems too small ({size_kb} KB)!")
    else:
        err(f"{fname} NOT FOUND in docs/")

# ─── Content checks ────────────────────────────────────────────────────────
checks = {
    "index.html": [
        ("D3.js CDN", "d3js.org"),
        ("Title present", "Awesome Native Multimodal Models"),
        ("Taxonomy link", "taxonomy.html"),
        ("Timeline link",  "timeline.html"),
        ("GitHub link",    "github.com"),
    ],
    "taxonomy.html": [
        ("D3 import",         'd3js.org'),
        ("Tree data",         'RAW_TREE'),
        ("initTree function", 'function update('),
        ("Tooltip element",   'id="tooltip"'),
        ("BAGEL entry",       'BAGEL'),
        ("Show-o2 entry",     'Show-o2'),
        ("Search input",      'id="search"'),
        ("Expand button",     'expandAll()'),
    ],
    "timeline.html": [
        ("D3 import",          'd3js.org'),
        ("Data array",         'const DATA ='),
        ("CAT_META config",    'CAT_META'),
        ("assignLanes func",   'function assignLanes('),
        ("Minimap SVG",        'id="mini-svg"'),
        ("Tooltip element",    'id="tooltip"'),
        ("Category filter",    'id="cat-filters"'),
        ("BAGEL entry",        'BAGEL'),
        ("Gemini 3.1 Pro",     'Gemini 3.1 Pro'),
        ("GPT-4o entry",       'GPT-4o'),
        ("Qwen2.5-Omni",       'Qwen2.5-Omni'),
        ("Today line",         'Mar 2026'),
        ("Year jump buttons",  'jumpYear('),
    ],
}

for fname, tests in checks.items():
    path = DOCS / fname
    if not path.exists():
        continue
    content = path.read_text(encoding="utf-8")
    print(f"\n── {fname} ────────────────────────────────────────────────────────")
    for label, needle in tests:
        if needle in content:
            ok(label)
        else:
            err(f"{label}: '{needle}' not found in {fname}")

# ─── Model count check ────────────────────────────────────────────────────
print("\n── Model count heuristics ───────────────────────────────────────────")
tl_path = DOCS / "timeline.html"
if tl_path.exists():
    content = tl_path.read_text()
    import re
    # Count "name" occurrences in data array as proxy
    hits = len(re.findall(r'"name":', content))
    ok(f"Model 'name' entries in timeline.html: {hits}")
    if hits < 60:
        err(f"Too few models in timeline.html: {hits}")

# ─── Summary ──────────────────────────────────────────────────────────────
print("\n── Summary ──────────────────────────────────────────────────────────")
if ERRORS:
    print(f"❌ {len(ERRORS)} error(s):")
    for e in ERRORS:
        print(f"   • {e}")
    sys.exit(1)
else:
    print("✅ All HTML output checks passed!")
