"""
tests/test_data.py
Data integrity tests powered by the validate.py engine.
Run: python tests/test_data.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from validate import run_validation  # noqa: E402

PASS, FAIL = [], []

def ok(msg):  PASS.append(msg); print(f"  ✓ {msg}")
def err(msg): FAIL.append(msg); print(f"  ✗ {msg}")

print("\n── Running validation engine ────────────────────────────────────────")
report = run_validation()

print(f"  Total timeline models   : {report.total_timeline}")
print(f"  Total taxonomy leaves   : {report.total_taxonomy_leaves}")
print(f"  🔴 Errors               : {len(report.errors)}")
print(f"  🟡 Warnings             : {len(report.warnings)}")
print(f"  🔵 Infos                : {len(report.infos)}")
print(f"  🏆 Quality score        : {report.quality_score}/100  ({report.quality_label})")

print("\n── Assertions ───────────────────────────────────────────────────────")

# Must have zero ERRORs
if len(report.errors) == 0:
    ok("Zero ERRORs — data is structurally valid")
else:
    for issue in report.errors:
        err(f"[{issue.code}] {issue.model}: {issue.message}")

# Minimum dataset size
if report.total_timeline >= 60:
    ok(f"Timeline size sufficient ({report.total_timeline} models)")
else:
    err(f"Timeline too small: {report.total_timeline} (expected ≥ 60)")

if report.total_taxonomy_leaves >= 50:
    ok(f"Taxonomy leaves sufficient ({report.total_taxonomy_leaves} leaves)")
else:
    err(f"Taxonomy leaves too few: {report.total_taxonomy_leaves} (expected ≥ 50)")

# Landmark models
from data import TIMELINE_MODELS, META  # noqa: E402
lm_count = sum(1 for m in TIMELINE_MODELS if m.get("landmark"))
if lm_count >= 10:
    ok(f"Landmark count OK ({lm_count})")
else:
    err(f"Too few landmarks: {lm_count} (expected ≥ 10)")

# All categories used
used_cats = {m.get("category") for m in TIMELINE_MODELS}
valid_cats = set(META.get("categories", {}).keys())
missing_cats = valid_cats - used_cats
if not missing_cats:
    ok("All categories have at least one model")
else:
    err(f"Unused categories: {missing_cats}")

# JSON serializable
import json  # noqa: E402
try:
    json.dumps(report.to_dict())
    ok("Full report is JSON-serializable")
except Exception as e:
    err(f"JSON serialization failed: {e}")

# Quality score > 0
if report.quality_score > 0:
    ok(f"Quality score > 0 ({report.quality_score})")
else:
    err("Quality score is 0 — too many errors!")

print("\n── Summary ──────────────────────────────────────────────────────────")
if FAIL:
    print(f"❌ {len(FAIL)} test(s) FAILED:")
    for f in FAIL:
        print(f"   • {f}")
    sys.exit(1)
else:
    print(f"✅ All {len(PASS)} test(s) passed!")
