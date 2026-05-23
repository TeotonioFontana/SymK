#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
 symbiotic_check.py — Symbiotic static rules auditor (Rules 2–5)
===============================================================================
 Author.............: Teotonio Fontana — Architect
 Programmed by......: Duke (GPT-5, OpenAI)
 Project............: SymK / Symbiotic DevKit
 Purpose............: Scan a Python tree and enforce lightweight guardrails for
                      AI–human collaboration: docstring hygiene, stable dict
                      contracts, limited cross-package coupling, and no A↔B
                      “bounce” between functions.

 Contract
 --------
 Invoke against a project root to produce a machine-readable JSON payload and an
 optional Markdown report. Findings are classified as warnings (rule 2) or
 errors (rules 3–5). Exit codes are CI-friendly.

 JSON payload (printed to stdout):
   {
     "root": "<absolute-path>",
     "stats": {
       "modules": <int>,
       "functions": <int>,
       "errors": <int>,
       "warnings": <int>
     },
     "warnings": [ {kind, rule, file, line, msg}, ... ],
     "errors":   [ {kind, rule, file, line, msg}, ... ]
   }

 CLI Parameters
 --------------
 --root PATH         (required) Project root to scan.
 --allow CSV         Comma-separated list of cross-package imports to allow.
                     Default: "common"
 --out-json PATH     Write the JSON payload to PATH (in addition to stdout).
 --out-report PATH   Write a Markdown summary to PATH.

 Rules Enforced
 --------------
 (2) Argument documentation present (warning)
     - Each function should document parameters in the docstring, with a section
       named "Args:", "Arguments:", or "Parameters:".

 (3) Static per-key return types (error)
     - For dict *literal* returns, each key must have a consistent value type
       across returns. Mixed types mean unstable contracts.

 (4) No cross-package imports except allowlist (error)
     - Disallow absolute imports into other top-level packages (dirs with
       __init__.py) unless explicitly allowed via --allow.

 (5) No A<->B bounce within a module (error)
     - Flag mutual calls (A calls B and B calls A) as a design smell.

 Exit Codes
 ----------
 0 — clean
 1 — warnings only
 2 — errors present OR invalid root path

 Notes
 -----
 • Fast, syntax-tree only; no imports executed.
 • Rule 3 inspects only dict *literals* (not variables), by design.
 • Keep these checks cheap and ubiquitous—run in pre-commit and CI.
===============================================================================
"""
from __future__ import annotations
import argparse, ast, json, sys
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Set, Optional, Dict
from collections import defaultdict


@dataclass
class Issue:
    """A single finding produced by the checker.

    Attributes
    ----------
    kind : str
        Either "error" or "warning".
    rule : int
        Rule number (2, 3, 4, or 5).
    file : str
        Path of the file where the issue was found.
    line : int
        1-based line number associated with the finding.
    msg : str
        Human-readable message describing the issue.
    """
    kind: str
    rule: int
    file: str
    line: int
    msg: str


def _load(path: Path) -> Optional[ast.AST]:
    """Parse a Python file into an AST.

    Returns
    -------
    ast.AST | None
        The parsed tree, or None if the file has syntax errors.
    """
    try:
        return ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except SyntaxError:
        return None


def _doc_has_args(doc: Optional[str]) -> bool:
    """Heuristically check if a docstring documents parameters.

    We keep it deliberately simple and fast: we search for a section
    header containing one of:
      - "Args:"
      - "Arguments:"
      - "Parameters:"

    Parameters
    ----------
    doc : str | None
        The function or method docstring.

    Returns
    -------
    bool
        True if a likely parameter section is present, False otherwise.
    """
    if not doc:
        return False
    low = doc.lower()
    return "args:" in low or "arguments:" in low or "parameters:" in low


def _collect_top_packages(root: Path) -> Set[str]:
    """Return names of top-level packages under `root`.

    A “top-level package” is any direct child directory that contains
    an `__init__.py`. These are used to detect cross-package imports.

    Parameters
    ----------
    root : Path
        Project root to inspect.

    Returns
    -------
    set[str]
        Set of directory names that are importable top-level packages.
    """
    return {
        p.name
        for p in root.iterdir()
        if p.is_dir() and (p / "__init__.py").exists()
    }


def rule2_docstrings(mod: ast.Module, path: Path, issues: List[Issue]) -> None:
    """Rule 2 — Warn when functions lack an 'Args:'-style section.

    Parameters
    ----------
    mod : ast.Module
        Parsed module.
    path : Path
        File path for reporting.
    issues : list[Issue]
        Accumulator for findings.
    """
    for n in ast.walk(mod):
        if isinstance(n, ast.FunctionDef):
            if not _doc_has_args(ast.get_docstring(n)):
                issues.append(
                    Issue(
                        "warning",
                        2,
                        str(path),
                        n.lineno,
                        f"Function '{n.name}' missing Args:/Arguments:/Parameters: section",
                    )
                )


def rule3_static_return_types(mod: ast.Module, path: Path, issues: List[Issue]) -> None:
    """Rule 3 — Enforce consistent types per dict key in literal returns.

    We collect dict *literal* returns and track the type name of each key's
    value (e.g., 'str', 'list', 'dict'). If the same key appears with multiple
    types across returns, we report an error.

    Limitations
    -----------
    - Only inspects dict literals (`return {'k': value, ...}`), not variables.
    - Type names come from AST node classes, not runtime evaluation.

    Parameters
    ----------
    mod : ast.Module
        Parsed module.
    path : Path
        File path for reporting.
    issues : list[Issue]
        Accumulator for findings.
    """
    per_key: Dict[str, Set[str]] = defaultdict(set)

    class V(ast.NodeVisitor):
        def visit_Return(self, n: ast.Return):
            v = n.value
            if isinstance(v, ast.Dict):
                for k, val in zip(v.keys, v.values):
                    if isinstance(k, ast.Constant) and isinstance(k.value, str):
                        per_key[k.value].add(type(val).__name__)

    V().visit(mod)

    for k, ts in per_key.items():
        if len(ts) > 1:
            issues.append(
                Issue(
                    "error",
                    3,
                    str(path),
                    1,
                    f"Key '{k}' returns multiple types: {sorted(ts)}",
                )
            )


def rule4_cross_pkg_imports(
    mod: ast.Module, path: Path, root: Path, allow: Set[str], issues: List[Issue]
) -> None:
    """Rule 4 — Disallow cross-package imports except an allowlist.

    This discourages accidental coupling and cyclic dependencies between
    top-level packages. Relative imports are fine. Absolute imports into
    other top-level packages must be allowed explicitly.

    Parameters
    ----------
    mod : ast.Module
        Parsed module.
    path : Path
        File path for reporting.
    root : Path
        Project root to discover top-level packages.
    allow : set[str]
        Packages that are allowed to be imported into others.
    issues : list[Issue]
        Accumulator for findings.
    """
    top = _collect_top_packages(root)
    rel = path.relative_to(root)
    me = rel.parts[0] if len(rel.parts) else None

    for n in ast.walk(mod):
        if isinstance(n, ast.Import):
            for a in n.names:
                head = a.name.split(".")[0]
                if head in top and head != me and head not in allow:
                    issues.append(
                        Issue(
                            "error",
                            4,
                            str(path),
                            n.lineno,
                            f"Cross-package import '{a.name}' not allowed",
                        )
                    )
        elif isinstance(n, ast.ImportFrom):
            if n.level == 0 and n.module:
                head = n.module.split(".")[0]
                if head in top and head != me and head not in allow:
                    issues.append(
                        Issue(
                            "error",
                            4,
                            str(path),
                            n.lineno,
                            f"Cross-package import-from '{n.module}' not allowed",
                        )
                    )


def rule5_bounce(mod: ast.Module, path: Path, issues: List[Issue]) -> None:
    """Rule 5 — Detect A<->B “bounce” (mutual calls) within the same module.

    We consider it a bounce when function A calls B and function B calls A,
    and A != B. This is typically a smell of split responsibilities or
    accidental recursion-by-committee.

    Parameters
    ----------
    mod : ast.Module
        Parsed module.
    path : Path
        File path for reporting.
    issues : list[Issue]
        Accumulator for findings.
    """
    funcs: Dict[str, ast.FunctionDef] = {}
    calls: Dict[str, Set[str]] = defaultdict(set)

    class C(ast.NodeVisitor):
        def __init__(self, name: str):
            self.name = name

        def visit_Call(self, n: ast.Call):
            if isinstance(n.func, ast.Name):
                calls[self.name].add(n.func.id)
            self.generic_visit(n)

    for n in mod.body:
        if isinstance(n, ast.FunctionDef):
            funcs[n.name] = n

    for name, fn in funcs.items():
        C(name).visit(fn)

    for a, bs in calls.items():
        for b in bs:
            if b in calls and a in calls[b] and a != b:
                issues.append(
                    Issue(
                        "error",
                        5,
                        str(path),
                        funcs[a].lineno,
                        f"Bouncing calls between '{a}' and '{b}'",
                    )
                )


def _markdown(issues: List[Issue], stats) -> str:
    """Render findings into a compact Markdown report.

    Parameters
    ----------
    issues : list[Issue]
        All warnings and errors.
    stats : dict
        A small dictionary with counts:
        - modules
        - functions
        - errors
        - warnings

    Returns
    -------
    str
        Markdown text.
    """
    out: List[str] = []
    out += ["# Symbiotic Checks Report", ""]
    out += [
        f"- Modules scanned: {stats['modules']}",
        f"- Functions seen:  {stats['functions']}",
        f"- Errors:          {stats['errors']}",
        f"- Warnings:        {stats['warnings']}",
        "",
    ]
    if not issues:
        out += ["✅ No issues found."]
        return "\n".join(out)

    out += ["## Findings"]
    for i in issues:
        icon = "❗" if i.kind == "error" else "⚠️"
        out += [f"- {icon} **Rule {i.rule}** — {i.file}:{i.line} — {i.msg}"]
    return "\n".join(out)


def main(argv=None) -> int:
    """CLI entrypoint.

    Parameters
    ----------
    argv : list[str] | None
        Optional argument vector for programmatic use. If None, uses sys.argv.

    Behavior
    --------
    - Scans all `*.py` under --root recursively.
    - Prints a summary to stderr and the JSON payload to stdout.
    - Returns:
        0 if clean,
        1 if warnings (no errors),
        2 if errors or invalid root.

    Returns
    -------
    int
        Exit code as described above.
    """
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--allow", default="common")
    ap.add_argument("--out-json", default=None)
    ap.add_argument("--out-report", default=None)
    args = ap.parse_args(argv)

    root = Path(args.root).resolve()
    if not root.exists():
        print(f"[symbiotic_checks] ERROR: root not found: {root}", file=sys.stderr)
        return 2

    allow = {a.strip() for a in args.allow.split(",") if a.strip()}

    issues: List[Issue] = []
    mods = 0
    fns = 0

    for p in root.rglob("*.py"):
        mod = _load(p)
        if not mod:
            continue
        mods += 1
        fns += sum(1 for n in ast.walk(mod) if isinstance(n, ast.FunctionDef))
        rule2_docstrings(mod, p, issues)
        rule3_static_return_types(mod, p, issues)
        rule4_cross_pkg_imports(mod, p, root, allow, issues)
        rule5_bounce(mod, p, issues)

    errors = [i for i in issues if i.kind == "error"]
    warnings = [i for i in issues if i.kind == "warning"]

    stats = {
        "modules": mods,
        "functions": fns,
        "errors": len(errors),
        "warnings": len(warnings),
    }

    payload = {
        "root": str(root),
        "stats": stats,
        "warnings": [asdict(w) for w in warnings],
        "errors": [asdict(e) for e in errors],
    }

    print(
        f"[symbiotic_checks] root={root}\n"
        f"  modules={mods}  functions={fns}  errors={len(errors)}  warnings={len(warnings)}",
        file=sys.stderr,
    )
    print(json.dumps(payload, indent=2))

    if args.out_json:
        Path(args.out_json).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out_json).write_text(json.dumps(payload, indent=2), encoding="utf-8")

    if args.out_report:
        md = _markdown(issues, stats)
        Path(args.out_report).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out_report).write_text(md, encoding="utf-8")

    return 2 if errors else (1 if warnings else 0)


if __name__ == "__main__":
    raise SystemExit(main())
