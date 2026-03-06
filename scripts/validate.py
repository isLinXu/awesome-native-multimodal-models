"""
validate.py — Comprehensive data validation engine for Awesome-Native-Multimodal-Models.

Checks performed
────────────────
TIMELINE_MODELS
  [E] TL-001  Duplicate model names
  [E] TL-002  Duplicate arXiv IDs  (non-empty IDs only)
  [E] TL-003  Missing required fields  (name / year / category)
  [E] TL-004  Unknown category  (not in META.categories)
  [E] TL-005  Year out of valid range  [2010, 2027]
  [E] TL-006  Month out of valid range  [1, 12]
  [E] TL-007  Malformed arXiv ID  (must match YYMM.NNNNN or YYYYMM.NNNNN pattern)
  [W] TL-008  Empty desc field
  [W] TL-009  No arXiv AND no github  (model has no reference link)
  [W] TL-010  GitHub URL not starting with https://
  [W] TL-011  arXiv year inconsistency  (arXiv YYMM vs declared year mismatch > 1y)
  [I] TL-012  No GitHub link  (arXiv exists but github empty)

TAXONOMY_TREE (leaf nodes)
  [E] TX-001  Duplicate leaf name within same sub-category
  [E] TX-002  Duplicate arXiv ID across all leaves
  [W] TX-003  Leaf appears in multiple sub-categories  (same name, different paths)
  [W] TX-004  Year out of valid range
  [W] TX-005  Malformed arXiv ID
  [W] TX-006  No arxiv AND no github on leaf

CROSS-VALIDATION
  [W] CV-001  Model in TIMELINE but not in any TAXONOMY leaf
  [W] CV-002  Model in TAXONOMY leaf but not in TIMELINE
  [I] CV-003  arXiv ID mismatch between TIMELINE and TAXONOMY for the same model name

META / STRUCTURE
  [E] MT-001  META missing required key
  [E] MT-002  TAXONOMY_TREE missing 'name' or 'children'
  [W] MT-003  Category in META not referenced by any TIMELINE model
  [W] MT-004  Invalid hex color on taxonomy node

Usage
─────
  python scripts/validate.py                  # print report to stdout
  python scripts/validate.py --json           # also write docs/validation.json
  python scripts/validate.py --strict         # exit 1 on any WARNING or ERROR
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import List, Optional

# ── allow sibling import ──────────────────────────────────────────────────────
sys.path.insert(0, str(Path(__file__).parent))
from data import TAXONOMY_TREE, TIMELINE_MODELS, META  # noqa: E402

# ─────────────────────────────────────────────────────────────────────────────
# Data structures
# ─────────────────────────────────────────────────────────────────────────────

SEVERITY_RANK = {"ERROR": 0, "WARNING": 1, "INFO": 2}
SEVERITY_EMOJI = {"ERROR": "🔴", "WARNING": "🟡", "INFO": "🔵"}

@dataclass
class Issue:
    code: str
    severity: str          # ERROR | WARNING | INFO
    location: str          # e.g. "TIMELINE[42]" or "TAXONOMY > Unified U+G > AR Semantic"
    model: str             # model name or empty
    message: str
    suggestion: str = ""

    @property
    def emoji(self) -> str:
        return SEVERITY_EMOJI.get(self.severity, "⚪")

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class ValidationReport:
    generated_at: str = field(default_factory=lambda: datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"))
    total_timeline: int = 0
    total_taxonomy_leaves: int = 0
    issues: List[Issue] = field(default_factory=list)

    # ── computed properties ───────────────────────────────────────────────────
    @property
    def errors(self)   -> List[Issue]: return [i for i in self.issues if i.severity == "ERROR"]
    @property
    def warnings(self) -> List[Issue]: return [i for i in self.issues if i.severity == "WARNING"]
    @property
    def infos(self)    -> List[Issue]: return [i for i in self.issues if i.severity == "INFO"]

    @property
    def quality_score(self) -> int:
        """0-100 quality score: starts at 100, deducts per issue."""
        score = 100
        score -= len(self.errors)   * 5   # each ERROR  costs 5 pts
        score -= len(self.warnings) * 2   # each WARNING costs 2 pts
        score -= len(self.infos)    * 0   # INFO = informational only
        return max(0, min(100, score))

    @property
    def quality_label(self) -> str:
        s = self.quality_score
        if s >= 95: return "Excellent"
        if s >= 85: return "Good"
        if s >= 70: return "Fair"
        if s >= 50: return "Poor"
        return "Critical"

    def add(self, code: str, severity: str, location: str,
            model: str, message: str, suggestion: str = "") -> None:
        self.issues.append(Issue(code, severity, location, model, message, suggestion))

    def to_dict(self) -> dict:
        return {
            "generated_at": self.generated_at,
            "summary": {
                "total_timeline":       self.total_timeline,
                "total_taxonomy_leaves":self.total_taxonomy_leaves,
                "errors":               len(self.errors),
                "warnings":             len(self.warnings),
                "infos":                len(self.infos),
                "quality_score":        self.quality_score,
                "quality_label":        self.quality_label,
            },
            "issues": [i.to_dict() for i in self.issues],
        }


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

# arXiv IDs: old style "YYMM.NNNNN" or new "YYMM.NNNNN"  (digits only, dot in middle)
_ARXIV_RE = re.compile(r"^\d{4}\.\d{4,5}$")
_HEX_RE   = re.compile(r"^#[0-9A-Fa-f]{6}$")
_YEAR_MIN, _YEAR_MAX = 2010, 2027
_MONTH_MIN, _MONTH_MAX = 1, 12


def _arxiv_ok(arxiv_id: str) -> bool:
    return bool(_ARXIV_RE.match(arxiv_id.strip()))


def _arxiv_year(arxiv_id: str) -> Optional[int]:
    """Extract 4-digit year from arXiv ID like '2405.09818' → 2024."""
    m = _ARXIV_RE.match(arxiv_id.strip())
    if not m:
        return None
    yymm = arxiv_id[:4]
    yy = int(yymm[:2])
    return 2000 + yy if yy <= 99 else None


def _collect_leaves(node: dict, path: str = "") -> list[tuple[str, dict, str]]:
    """Recursively collect all leaf nodes → [(name, node_dict, path), ...]"""
    results = []
    for child in node.get("children", []):
        child_path = f"{path} > {child['name']}" if path else child["name"]
        if child.get("children"):
            results.extend(_collect_leaves(child, child_path))
        else:
            results.append((child.get("name", "??"), child, child_path))
    return results


# ─────────────────────────────────────────────────────────────────────────────
# Validator
# ─────────────────────────────────────────────────────────────────────────────

def run_validation() -> ValidationReport:
    report = ValidationReport()

    valid_categories = set(META.get("categories", {}).keys())
    timeline = TIMELINE_MODELS
    report.total_timeline = len(timeline)

    # ── META / STRUCTURE ─────────────────────────────────────────────────────
    _check_meta(report, valid_categories)

    # ── TIMELINE checks ──────────────────────────────────────────────────────
    _check_timeline(report, timeline, valid_categories)

    # ── TAXONOMY checks ──────────────────────────────────────────────────────
    leaves = _collect_leaves(TAXONOMY_TREE)
    report.total_taxonomy_leaves = len(leaves)
    _check_taxonomy(report, leaves)

    # ── CROSS-VALIDATION ─────────────────────────────────────────────────────
    _check_cross(report, timeline, leaves)

    # Sort: ERROR first, then WARNING, then INFO; within same severity by code
    report.issues.sort(key=lambda i: (SEVERITY_RANK[i.severity], i.code, i.model))
    return report


# ── META ─────────────────────────────────────────────────────────────────────

def _check_meta(report: ValidationReport, valid_cats: set) -> None:
    loc = "META"

    # MT-001: required keys
    required_meta_keys = ("title", "paper_count", "last_updated", "github_url", "categories")
    for k in required_meta_keys:
        if k not in META:
            report.add("MT-001", "ERROR", loc, "", f"META missing required key '{k}'",
                       f"Add '{k}' to META dict in data.py")

    # MT-002: TAXONOMY_TREE structure
    if not isinstance(TAXONOMY_TREE, dict):
        report.add("MT-002", "ERROR", "TAXONOMY_TREE", "", "TAXONOMY_TREE must be a dict", "")
    else:
        for key in ("name", "children"):
            if key not in TAXONOMY_TREE:
                report.add("MT-002", "ERROR", "TAXONOMY_TREE", "",
                           f"TAXONOMY_TREE missing required key '{key}'", "")

    # MT-003: unused categories
    used_cats = {m.get("category") for m in TIMELINE_MODELS}
    for cat in valid_cats:
        if cat not in used_cats:
            report.add("MT-003", "WARNING", loc, cat,
                       f"Category '{cat}' defined in META.categories but not used by any timeline model",
                       "Remove unused category or add models for it")

    # MT-004: invalid hex colors in taxonomy
    def _walk_colors(node: dict, path: str = "") -> None:
        color = node.get("color", "")
        if color and not _HEX_RE.match(color):
            report.add("MT-004", "WARNING", path or "TAXONOMY_TREE",
                       node.get("name", "?"),
                       f"Invalid hex color '{color}'",
                       "Use 6-digit hex like #FF6B6B")
        for child in node.get("children", []):
            _walk_colors(child, f"{path} > {child.get('name','?')}")

    _walk_colors(TAXONOMY_TREE)


# ── TIMELINE ─────────────────────────────────────────────────────────────────

def _check_timeline(report: ValidationReport, timeline: list, valid_cats: set) -> None:
    name_counter   = Counter(m.get("name", "") for m in timeline)
    arxiv_seen: dict[str, int] = {}   # arxiv_id → first index

    for idx, m in enumerate(timeline):
        name = m.get("name", "")
        loc  = f"TIMELINE[{idx}]"

        # TL-003: missing required fields
        for field_name in ("name", "year", "category"):
            if field_name not in m or m[field_name] == "" or m[field_name] is None:
                report.add("TL-003", "ERROR", loc, name,
                           f"Missing required field '{field_name}'",
                           f"Add '{field_name}' to TIMELINE_MODELS[{idx}]")

        # TL-001: duplicate names (report only at first occurrence)
        if name_counter[name] > 1 and name:
            indices = [i for i, x in enumerate(timeline) if x.get("name") == name]
            if idx == indices[0]:
                report.add("TL-001", "ERROR", loc, name,
                           f"Duplicate model name '{name}' appears {name_counter[name]}× "
                           f"at indices {indices}",
                           "Each model name must be unique; use version suffixes if needed")

        year  = m.get("year")
        month = m.get("month")
        arxiv = str(m.get("arxiv", "") or "").strip()
        github = str(m.get("github", "") or "").strip()
        category = m.get("category", "")

        # TL-004: unknown category
        if category and category not in valid_cats:
            report.add("TL-004", "ERROR", loc, name,
                       f"Unknown category '{category}' (valid: {sorted(valid_cats)})",
                       "Fix category to one of the keys in META.categories")

        # TL-005: year range
        if year is not None:
            try:
                yr = int(year)
                if not (_YEAR_MIN <= yr <= _YEAR_MAX):
                    report.add("TL-005", "ERROR", loc, name,
                               f"Year {yr} out of valid range [{_YEAR_MIN}, {_YEAR_MAX}]",
                               "Check if the year is correct")
            except (TypeError, ValueError):
                report.add("TL-005", "ERROR", loc, name,
                           f"Year value '{year}' is not an integer", "Use an integer year")

        # TL-006: month range
        if month is not None:
            try:
                mo = int(month)
                if not (_MONTH_MIN <= mo <= _MONTH_MAX):
                    report.add("TL-006", "ERROR", loc, name,
                               f"Month {mo} out of valid range [1, 12]",
                               "Use 1–12 for month")
            except (TypeError, ValueError):
                report.add("TL-006", "ERROR", loc, name,
                           f"Month value '{month}' is not an integer", "Use an integer 1–12")

        # TL-007: arXiv format
        if arxiv and not _arxiv_ok(arxiv):
            report.add("TL-007", "ERROR", loc, name,
                       f"Malformed arXiv ID '{arxiv}' (expected pattern YYMM.NNNNN)",
                       "Use format like '2405.09818'")

        # TL-002: duplicate arXiv
        if arxiv:
            if arxiv in arxiv_seen:
                report.add("TL-002", "ERROR", loc, name,
                           f"Duplicate arXiv ID '{arxiv}' also used by "
                           f"TIMELINE[{arxiv_seen[arxiv]}] "
                           f"({timeline[arxiv_seen[arxiv]].get('name','')})",
                           "Each arXiv ID should map to exactly one model entry")
            else:
                arxiv_seen[arxiv] = idx

        # TL-011: arXiv year vs declared year inconsistency
        if arxiv and year and _arxiv_ok(arxiv):
            ax_year = _arxiv_year(arxiv)
            if ax_year is not None and abs(ax_year - int(year)) > 1:
                report.add("TL-011", "WARNING", loc, name,
                           f"arXiv ID '{arxiv}' implies year {ax_year} "
                           f"but declared year is {year} (gap > 1 year)",
                           "Double-check the year field or arXiv ID")

        # TL-008: empty desc
        desc = str(m.get("desc", "") or "").strip()
        if not desc:
            report.add("TL-008", "WARNING", loc, name,
                       "Empty 'desc' field — tooltip will show no description",
                       "Add a one-line description")

        # TL-009: no reference at all
        if not arxiv and not github:
            report.add("TL-009", "WARNING", loc, name,
                       "No arXiv ID and no GitHub URL — model has no reference link",
                       "Add at least one of 'arxiv' or 'github'")

        # TL-010: bad GitHub URL
        if github and not github.startswith("https://"):
            report.add("TL-010", "WARNING", loc, name,
                       f"GitHub URL '{github}' does not start with 'https://'",
                       "Use full https:// URL")

        # TL-012: no GitHub (info only)
        if arxiv and not github:
            report.add("TL-012", "INFO", loc, name,
                       "arXiv present but no GitHub URL",
                       "Consider adding a GitHub link if available")


# ── TAXONOMY ─────────────────────────────────────────────────────────────────

def _check_taxonomy(report: ValidationReport, leaves: list) -> None:
    name_to_paths: dict[str, list[str]] = defaultdict(list)
    arxiv_to_names: dict[str, list[str]] = defaultdict(list)

    for name, node, path in leaves:
        name_to_paths[name].append(path)
        arxiv = str(node.get("arxiv", "") or "").strip()
        if arxiv:
            arxiv_to_names[arxiv].append(name)

    # TX-003: same name in multiple paths
    for name, paths in name_to_paths.items():
        if len(paths) > 1:
            report.add("TX-003", "WARNING", f"TAXONOMY > multiple paths",
                       name,
                       f"Leaf '{name}' appears in {len(paths)} sub-categories: "
                       + " | ".join(paths),
                       "Remove duplicate or use a more specific name")

    # TX-002: duplicate arXiv across leaves
    for arxiv_id, names in arxiv_to_names.items():
        if len(names) > 1:
            report.add("TX-002", "ERROR", "TAXONOMY",
                       ", ".join(names),
                       f"arXiv ID '{arxiv_id}' shared by {len(names)} leaves: {names}",
                       "Each arXiv ID should appear only once in the taxonomy tree")

    # Per-leaf checks
    seen_in_subcat: dict[str, set] = defaultdict(set)  # subcat_path → set of names

    for name, node, path in leaves:
        arxiv  = str(node.get("arxiv",  "") or "").strip()
        github = str(node.get("github", "") or "").strip()
        year   = node.get("year")
        subcat = " > ".join(path.split(" > ")[:2])   # top 2 levels as sub-category key

        # TX-001: duplicate within same sub-category
        if name in seen_in_subcat[subcat]:
            report.add("TX-001", "ERROR", path, name,
                       f"Duplicate leaf name '{name}' in sub-category '{subcat}'",
                       "Remove or rename the duplicate entry")
        seen_in_subcat[subcat].add(name)

        # TX-004: year range
        if year is not None:
            try:
                yr = int(year)
                if not (_YEAR_MIN <= yr <= _YEAR_MAX):
                    report.add("TX-004", "WARNING", path, name,
                               f"Year {yr} out of valid range [{_YEAR_MIN}, {_YEAR_MAX}]",
                               "Check the year field")
            except (TypeError, ValueError):
                report.add("TX-004", "WARNING", path, name,
                           f"Year value '{year}' is not an integer", "Use an integer")

        # TX-005: arXiv format
        if arxiv and not _arxiv_ok(arxiv):
            report.add("TX-005", "WARNING", path, name,
                       f"Malformed arXiv ID '{arxiv}'",
                       "Expected format: YYMM.NNNNN")

        # TX-006: no reference
        if not arxiv and not github:
            report.add("TX-006", "WARNING", path, name,
                       "No arXiv ID and no GitHub URL on taxonomy leaf",
                       "Add at least one reference link")


# ── CROSS-VALIDATION ─────────────────────────────────────────────────────────

def _check_cross(report: ValidationReport, timeline: list, leaves: list) -> None:
    tl_names  = {m.get("name", ""): m for m in timeline}
    tx_names  = {name: (node, path) for name, node, path in leaves}

    tl_arxiv  = {str(m.get("arxiv","") or "").strip(): m.get("name","")
                 for m in timeline if m.get("arxiv")}
    tx_arxiv  = {str(n.get("arxiv","") or "").strip(): name
                 for name, n, _ in leaves if n.get("arxiv")}

    # CV-001: in TIMELINE but not in TAXONOMY
    for name in tl_names:
        if name and name not in tx_names:
            report.add("CV-001", "WARNING",
                       f"TIMELINE vs TAXONOMY",
                       name,
                       f"'{name}' is in TIMELINE_MODELS but has no leaf in TAXONOMY_TREE",
                       "Add a leaf node under the appropriate sub-category")

    # CV-002: in TAXONOMY but not in TIMELINE
    for name in tx_names:
        if name and name not in tl_names:
            report.add("CV-002", "WARNING",
                       f"TAXONOMY vs TIMELINE",
                       name,
                       f"'{name}' is in TAXONOMY_TREE leaves but not in TIMELINE_MODELS",
                       "Add a timeline entry or remove the taxonomy leaf")

    # CV-003: arXiv mismatch for same model name
    for name in set(tl_names) & set(tx_names):
        tl_ax = str(tl_names[name].get("arxiv", "") or "").strip()
        tx_ax = str(tx_names[name][0].get("arxiv", "") or "").strip()
        if tl_ax and tx_ax and tl_ax != tx_ax:
            report.add("CV-003", "INFO",
                       "TIMELINE vs TAXONOMY",
                       name,
                       f"arXiv ID differs: TIMELINE='{tl_ax}' vs TAXONOMY='{tx_ax}'",
                       "Ensure both lists use the same arXiv ID")


# ─────────────────────────────────────────────────────────────────────────────
# Terminal printer
# ─────────────────────────────────────────────────────────────────────────────

_RESET  = "\033[0m"
_BOLD   = "\033[1m"
_RED    = "\033[91m"
_YELLOW = "\033[93m"
_CYAN   = "\033[96m"
_GREEN  = "\033[92m"
_GRAY   = "\033[90m"
_WHITE  = "\033[97m"
_MAG    = "\033[95m"

SEV_COLOR = {"ERROR": _RED, "WARNING": _YELLOW, "INFO": _CYAN}

_BAR_WIDTH = 72

def _hline(char: str = "─") -> str:
    return char * _BAR_WIDTH

def _center(text: str, char: str = " ") -> str:
    pad = max(0, _BAR_WIDTH - len(text))
    lpad = pad // 2
    return " " * lpad + text

def print_report(report: ValidationReport, *, use_color: bool = True) -> None:
    """Pretty-print the full validation report to stdout."""

    def c(color: str, text: str) -> str:
        return f"{color}{text}{_RESET}" if use_color else text

    print()
    print(c(_BOLD + _WHITE, _hline("═")))
    print(c(_BOLD + _WHITE, _center("🔍  DATA VALIDATION REPORT")))
    print(c(_BOLD + _WHITE, _center(f"Awesome-Native-Multimodal-Models  ·  {report.generated_at}")))
    print(c(_BOLD + _WHITE, _hline("═")))

    # ── Summary row ────────────────────────────────────────────────────────
    errors   = len(report.errors)
    warnings = len(report.warnings)
    infos    = len(report.infos)
    score    = report.quality_score
    label    = report.quality_label
    score_color = _GREEN if score >= 85 else (_YELLOW if score >= 70 else _RED)

    print()
    print(c(_BOLD, f"  📊 Dataset size"))
    print(f"     Timeline models   : {c(_WHITE, str(report.total_timeline))}")
    print(f"     Taxonomy leaves   : {c(_WHITE, str(report.total_taxonomy_leaves))}")
    print()
    print(c(_BOLD, f"  📋 Issue summary"))
    print(f"     {c(_RED,    '🔴 ERRORs  ')}: {c(_RED,    str(errors).rjust(4))}")
    print(f"     {c(_YELLOW, '🟡 WARNINGs')}: {c(_YELLOW, str(warnings).rjust(4))}")
    print(f"     {c(_CYAN,   '🔵 INFOs   ')}: {c(_CYAN,   str(infos).rjust(4))}")
    print()
    print(f"  🏆 Quality score    : {c(score_color + _BOLD, str(score) + ' / 100')}  "
          f"({c(score_color, label)})")
    print()
    print(c(_BOLD + _WHITE, _hline()))

    if not report.issues:
        print(c(_GREEN + _BOLD, _center("✅  No issues found — data is clean!")))
        print(c(_WHITE, _hline("═")))
        return

    # ── Per-code stats ──────────────────────────────────────────────────────
    code_counts: Counter = Counter(i.code for i in report.issues)
    print(c(_BOLD, "\n  Issue breakdown by code:\n"))
    by_code: dict[str, list[Issue]] = defaultdict(list)
    for iss in report.issues:
        by_code[iss.code].append(iss)

    header_printed = False
    prev_sev = None
    for code, issues_for_code in sorted(by_code.items(),
                                         key=lambda kv: (SEVERITY_RANK[kv[1][0].severity], kv[0])):
        sev = issues_for_code[0].severity
        col = SEV_COLOR.get(sev, _RESET)
        if sev != prev_sev:
            print(c(_BOLD, f"  {'─'*14} {sev} {'─'*14}"))
            prev_sev = sev
        print(f"  {c(col, code.ljust(8))}  {c(_GRAY, issues_for_code[0].message[:50].ljust(52))}  "
              f"× {c(_WHITE, str(len(issues_for_code)))}")

    # ── Detailed issue list ─────────────────────────────────────────────────
    print()
    print(c(_BOLD + _WHITE, _hline()))
    print(c(_BOLD, "  Detailed issues:\n"))

    for iss in report.issues:
        col = SEV_COLOR.get(iss.severity, _RESET)
        print(f"  {iss.emoji}  {c(col + _BOLD, iss.code.ljust(8))} "
              f"{c(_GRAY, iss.location[:36].ljust(36))} "
              f"{c(_WHITE, iss.model[:24].ljust(24))}")
        print(f"     {c(_WHITE, iss.message)}")
        if iss.suggestion:
            print(f"     {c(_GRAY, '↳ ' + iss.suggestion)}")
        print()

    print(c(_BOLD + _WHITE, _hline("═")))

    # ── Final verdict ───────────────────────────────────────────────────────
    if errors:
        print(c(_RED + _BOLD,   _center(f"❌  {errors} ERROR(s) must be fixed before release")))
    elif warnings:
        print(c(_YELLOW + _BOLD, _center(f"⚠️  {warnings} WARNING(s) — recommended fixes")))
    else:
        print(c(_GREEN + _BOLD,  _center("✅  No critical issues — good to go!")))
    print(c(_BOLD + _WHITE, _hline("═")))
    print()


# ─────────────────────────────────────────────────────────────────────────────
# CLI entry-point
# ─────────────────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate Awesome-Native-Multimodal-Models data")
    parser.add_argument("--json",   action="store_true",
                        help="Write docs/validation.json in addition to stdout")
    parser.add_argument("--strict", action="store_true",
                        help="Exit 1 on any WARNING or ERROR (default: only ERROR)")
    parser.add_argument("--no-color", action="store_true",
                        help="Disable ANSI color codes")
    args = parser.parse_args()

    report = run_validation()
    use_color = not args.no_color and sys.stdout.isatty()
    print_report(report, use_color=use_color)

    # Optionally write JSON
    if args.json:
        docs_dir = Path(__file__).parent.parent / "docs"
        docs_dir.mkdir(exist_ok=True)
        out = docs_dir / "validation.json"
        out.write_text(json.dumps(report.to_dict(), ensure_ascii=False, indent=2))
        print(f"📄 Validation JSON written to {out}")

    # Exit code
    if args.strict:
        return 1 if (report.errors or report.warnings) else 0
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
