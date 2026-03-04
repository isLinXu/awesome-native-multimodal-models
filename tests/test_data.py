"""
tests/test_data.py
Validates the structure and integrity of data.py.
Run: python tests/test_data.py
"""
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from data import TAXONOMY_TREE, TIMELINE_MODELS, META  # noqa: E402

ERRORS = []

def err(msg):
    ERRORS.append(msg)
    print(f"  ✗ {msg}")

def ok(msg):
    print(f"  ✓ {msg}")


print("\n── Validating META ──────────────────────────────────────────────────")
for key in ("title", "paper_count", "last_updated", "github_url", "categories"):
    if key in META:
        ok(f"META.{key} present")
    else:
        err(f"META.{key} missing!")

print("\n── Validating TAXONOMY_TREE ─────────────────────────────────────────")
assert isinstance(TAXONOMY_TREE, dict), "TAXONOMY_TREE must be a dict"
assert "name" in TAXONOMY_TREE, "TAXONOMY_TREE must have 'name'"
assert "children" in TAXONOMY_TREE, "TAXONOMY_TREE must have 'children'"
ok(f"Root node: '{TAXONOMY_TREE['name']}'")
ok(f"Top-level branches: {len(TAXONOMY_TREE['children'])}")

# JSON serializable
try:
    json.dumps(TAXONOMY_TREE)
    ok("TAXONOMY_TREE is JSON-serializable")
except Exception as e:
    err(f"TAXONOMY_TREE JSON error: {e}")

# Leaf nodes
def collect_leaves(node, depth=0):
    leaves = []
    for child in node.get("children", []):
        if not child.get("children"):
            leaves.append((child["name"], depth))
        else:
            leaves.extend(collect_leaves(child, depth + 1))
    return leaves

leaves = collect_leaves(TAXONOMY_TREE)
ok(f"Leaf models in taxonomy: {len(leaves)}")
if len(leaves) < 50:
    err(f"Too few leaf models: {len(leaves)} (expected >= 50)")

print("\n── Validating TIMELINE_MODELS ───────────────────────────────────────")
assert isinstance(TIMELINE_MODELS, list), "TIMELINE_MODELS must be a list"
ok(f"Total timeline models: {len(TIMELINE_MODELS)}")
if len(TIMELINE_MODELS) < 60:
    err(f"Too few timeline models: {len(TIMELINE_MODELS)} (expected >= 60)")

REQUIRED_FIELDS = ("name", "year", "category")
valid_cats = set(META["categories"].keys())
for m in TIMELINE_MODELS:
    for f in REQUIRED_FIELDS:
        if f not in m:
            err(f"Model '{m.get('name', '?')}' missing field '{f}'")
    if m.get("category") not in valid_cats:
        err(f"Model '{m['name']}' has unknown category '{m.get('category')}'")
    if not (2010 <= int(m.get("year", 0)) <= 2030):
        err(f"Model '{m['name']}' has suspicious year {m.get('year')}")

# JSON serializable
try:
    json.dumps(TIMELINE_MODELS)
    ok("TIMELINE_MODELS is JSON-serializable")
except Exception as e:
    err(f"TIMELINE_MODELS JSON error: {e}")

# Check landmark count
lm = [m for m in TIMELINE_MODELS if m.get("landmark")]
ok(f"Landmark models: {len(lm)}")
if len(lm) < 10:
    err("Too few landmark models (expected >= 10)")

print("\n── Summary ─────────────────────────────────────────────────────────")
if ERRORS:
    print(f"❌ {len(ERRORS)} error(s) found:")
    for e in ERRORS:
        print(f"   • {e}")
    sys.exit(1)
else:
    print(f"✅ All checks passed! ({len(TIMELINE_MODELS)} timeline models, {len(leaves)} taxonomy leaves)")
