#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
===============================================================================
 decorate_enforcer.py — Codemod to enforce @enveloped on boundary functions
===============================================================================
 Author.............: Teotoniio Fontana — Architect
 Programmed by......: Duke (GPT-5, OpenAI)
 Project............: SymK / Symbiotic DevKit
 Purpose............: Insert the result-envelope import and decorate boundary
                      functions with @enveloped(schema=...), supporting mirror
                      or in-place writes for safe repo adoption.

 Contract
 --------
 For each target module:
   • Ensure a single import exists:
       from <pkg_top>.result_envelope import enveloped
   • Decorate boundary functions (matched by regex) with:
       @enveloped(schema={...})
   • Leave non-boundary functions untouched and preserve formatting.

 Schema modes
 ------------
 --schema=minimal  → inserts a minimal schema stub per function.
 --schema=hints    → infers basic types from signatures/defaults (best-effort).

 CLI Parameters
 --------------
 --root PATH            Project root to scan.
 --write-mode MODE      "mirror" (default) or "inplace".
 --out-dir PATH         When mirror, write transformed tree here.
 --copy-others          Mirror also non-.py files (directory compare friendly).
 --force                Overwrite out-dir if it exists (mirror).
 --name-pattern REGEX   Boundary function matcher (e.g. "(run|execute|perform|backup|restore|handle|process)").
 --pkg-top NAME         Top package that exposes result_envelope.py (e.g. "common").
 --schema {minimal,hints}
 --verbose              Extra logging.

 Notes
 -----
 • Idempotente: não duplica o import nem reaplica o decorator.
 • Respeita comentários e layout (usa CST, não AST) para preservar estilo.
 • Combine com 'sym-init' para criar 'common/result_envelope.py' shim.
===============================================================================
"""
# (resto do arquivo inalterado)

from __future__ import annotations

import argparse
import re
import sys
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Tuple, Dict

try:
    import libcst as cst
except Exception as e:  # pragma: no cover
    print(
        "[decorate_enforcer] ERROR: LibCST is required. Install with 'pip install libcst'.\n"
        f"Underlying error: {e}",
        file=sys.stderr,
    )
    sys.exit(1)

DEFAULT_PATTERN = r"(run|execute|perform|backup|restore|handle|process)"

@dataclass
class Settings:
    """
    Runtime options for the codemod.

    Attributes:
        root (Path): Root directory to scan.
        pkg_top (str): Top-level package name for the import.
        name_pattern (re.Pattern): Regex to select boundary function names.
        schema_mode (str): 'minimal' | 'hints' for schema generation.
        write_mode (str): 'mirror' | 'inplace'. Mirror is PyCharm-friendly.
        out_dir (Optional[Path]): Destination directory for mirror mode.
        copy_others (bool): Copy non-.py files into mirror.
        force (bool): Allow writing into an existing --out-dir.
        dry_run (bool): No writes; summary only.
        exclude (Tuple[str, ...]): Directory name fragments to exclude.
        verbose (bool): Print per-file updates.
    """
    root: Path
    pkg_top: str
    name_pattern: re.Pattern
    schema_mode: str = "minimal"
    write_mode: str = "mirror"
    out_dir: Optional[Path] = None
    copy_others: bool = False
    force: bool = False
    dry_run: bool = False
    exclude: Tuple[str, ...] = field(default_factory=lambda: ("tests", "test", ".venv", "venv", "__pycache__"))
    verbose: bool = False

@dataclass
class FileResult:
    """
    Per-file transformation result.
    """
    path: Path
    target: Path
    changed: bool
    added_import: bool
    decorated: int
    skipped_existing: int

# ----------------------------- Heuristics ------------------------------------

_INT_POSITIVE_NAMES = {"limit", "count", "max_items", "size", "pages", "maxresults"}
_INT_NONNEG_NAMES   = {"retries", "timeout", "ttl", "age", "offset"}
_PORT_NAMES         = {"port", "listen_port"}
_AWS_ID_PATTERNS: Dict[str, str] = {
    "volume_id": r"^vol-[0-9a-f]+$",
    "snapshot_id": r"^snap-[0-9a-f]+$",
    "instance_id": r"^i-[0-9a-f]+$",
    "ami_id": r"^ami-[0-9a-f]+$",
}
_BUCKET_RX = r"^[a-z0-9][a-z0-9.-]{1,62}$"
_REGION_RX = r"^[a-z]{2}-[a-z]+-\d$"

def _last_name(expr: cst.BaseExpression) -> str:
    if isinstance(expr, cst.Name):
        return expr.value
    if isinstance(expr, cst.Attribute):
        return _last_name(expr.attr)
    return ""

def _ann_to_type_token(ann: Optional[cst.Annotation]) -> Optional[str]:
    if not ann:
        return None
    a = ann.annotation
    if isinstance(a, cst.Name):
        v = a.value.lower()
        if v in ("int", "str", "float", "bool", "dict", "list"):
            return v
    if isinstance(a, cst.Subscript):
        base = _last_name(a.value).lower()
        if base in ("list", "sequence", "tuple"):
            return "list"
        if base in ("dict", "mapping"):
            return "dict"
        if base in ("optional",):
            if a.slice and isinstance(a.slice[0].slice, cst.Index):
                inner = a.slice[0].slice.value
                if isinstance(inner, cst.Name):
                    return inner.value.lower()
        if base in ("union",):
            names = []
            for sl in a.slice:
                v = sl.slice.value
                if isinstance(v, cst.Name):
                    names.append(v.value.lower())
            if "none" in names and len(names) >= 2:
                for n in names:
                    if n != "none":
                        return n
    if isinstance(a, cst.Attribute):
        last = _last_name(a).lower()
        if last in ("list", "dict", "int", "str", "float", "bool"):
            return last
    return None

def _is_nullable(ann: Optional[cst.Annotation]) -> bool:
    if not ann:
        return False
    a = ann.annotation
    if isinstance(a, cst.Subscript):
        base = _last_name(a.value).lower()
        if base == "optional":
            return True
        if base == "union":
            for sl in a.slice:
                v = sl.slice.value
                if isinstance(v, cst.Name) and v.value == "None":
                    return True
    return False

def _default_literal_code(expr: Optional[cst.BaseExpression]) -> Optional[str]:
    if expr is None:
        return None
    if isinstance(expr, (cst.Integer, cst.Float, cst.SimpleString)):
        return expr.value
    if isinstance(expr, cst.Name) and expr.value in ("True", "False", "None"):
        return expr.value
    return None

def _infer_hints_for_param(name: str, type_token: Optional[str]) -> Dict[str, str]:
    n = name.lower()
    out: Dict[str, str] = {}
    if type_token == "int":
        if n in _INT_POSITIVE_NAMES or n.endswith("_count") or n.endswith("_limit"):
            out["min"] = "1"
        elif n in _INT_NONNEG_NAMES or n.startswith("max_") or n.endswith("_timeout"):
            out["min"] = "0"
        elif n in _PORT_NAMES:
            out["min"] = "1"
            out["max"] = "65535"
    if type_token == "str":
        out["non_empty"] = "True"
        if n in _AWS_ID_PATTERNS:
            out["pattern"] = repr(_AWS_ID_PATTERNS[n])
        elif "volume" in n and n.endswith("_id"):
            out["pattern"] = repr(_AWS_ID_PATTERNS["volume_id"])
        elif "snapshot" in n and n.endswith("_id"):
            out["pattern"] = repr(_AWS_ID_PATTERNS["snapshot_id"])
        elif "instance" in n and n.endswith("_id"):
            out["pattern"] = repr(_AWS_ID_PATTERNS["instance_id"])
        elif n in {"ami", "ami_id"}:
            out["pattern"] = repr(_AWS_ID_PATTERNS["ami_id"])
        elif "bucket" in n:
            out["pattern"] = repr(_BUCKET_RX)
        elif "region" in n:
            out["pattern"] = repr(_REGION_RX)
    return out

def _schema_entry_for_param(p: cst.Param, mode: str) -> str:
    name = p.name.value
    ann = p.annotation
    type_token = _ann_to_type_token(ann)
    required = p.default is None
    default_code = _default_literal_code(p.default)

    fields: Dict[str, str] = {}
    if type_token:
        fields["type"] = type_token
    fields["required"] = "True" if required else "False"
    if _is_nullable(ann):
        fields["nullable"] = "True"
    if default_code is not None:
        fields["default"] = default_code

    if mode == "hints":
        hints = _infer_hints_for_param(name, type_token)
        if default_code is not None and type_token == "str":
            hints.pop("non_empty", None)
        fields.update(hints)

    parts = []
    for k, v in fields.items():
        if k == "type":
            parts.append(f"'type': {v}")
        elif k == "pattern":
            parts.append(f"'pattern': r{v[1:] if v.startswith('r') else v}")
        else:
            parts.append(f"'{k}': {v}")
    return f"'{name}': {{{', '.join(parts)}}}"

def _build_schema_for_func(fn: cst.FunctionDef, mode: str) -> str:
    entries: List[str] = []
    ps = fn.params
    all_params = list(ps.posonly_params) + list(ps.params) + list(ps.kwonly_params)
    for p in all_params:
        if isinstance(p, cst.Param) and p.name.value not in ("args", "kwargs"):
            entries.append(_schema_entry_for_param(p, mode))
    return "{" + ", ".join(entries) + "}"

# --------------------------- Transformer -------------------------------------

class DecorateTransformer(cst.CSTTransformer):
    """Insert the import and decorate boundary functions with schema."""
    def __init__(self, settings: Settings):
        self.s = settings
        self._has_import = False
        self._added_import = False
        self._decorated = 0
        self._skipped_existing = 0

    def _is_enveloped_import(self, node: cst.CSTNode) -> bool:
        if not isinstance(node, cst.ImportFrom):
            return False
        if not isinstance(node.module, (cst.Attribute, cst.Name)):
            return False
        def dotted(m: cst.BaseExpression) -> str:
            if isinstance(m, cst.Name):
                return m.value
            if isinstance(m, cst.Attribute):
                return f"{dotted(m.value)}.{m.attr.value}"
            return ""
        full = dotted(node.module)
        if full != f"{self.s.pkg_top}.result_envelope":
            return False
        for alias in node.names:
            if isinstance(alias, cst.ImportAlias) and isinstance(alias.name, cst.Name):
                if alias.name.value == "enveloped":
                    return True
        return False

    def visit_ImportFrom(self, node: cst.ImportFrom) -> Optional[bool]:
        if self._is_enveloped_import(node):
            self._has_import = True
        return True

    def leave_Module(self, original: cst.Module, updated: cst.Module) -> cst.Module:
        if self._has_import:
            return updated
        import_stmt = cst.parse_statement(
            f"from {self.s.pkg_top}.result_envelope import enveloped\n"
        )
        body = list(updated.body)
        insert_index = 0
        if body and isinstance(body[0], cst.SimpleStatementLine):
            first = body[0]
            if first.body and isinstance(first.body[0], cst.Expr) and isinstance(first.body[0].value, cst.SimpleString):
                insert_index = 1
        new_body = body[:insert_index] + [import_stmt] + body[insert_index:]
        self._added_import = True
        return updated.with_changes(body=new_body)

    def leave_FunctionDef(self, original: cst.FunctionDef, updated: cst.FunctionDef) -> cst.FunctionDef:
        name = original.name.value
        if name.startswith("_"):
            return updated
        if any(isinstance(d.decorator, cst.Call) and isinstance(d.decorator.func, cst.Name)
               and d.decorator.func.value == "enveloped" for d in (original.decorators or [])) \
           or any(isinstance(d.decorator, cst.Name) and d.decorator.value == "enveloped"
                  for d in (original.decorators or [])):
            self._skipped_existing += 1
            return updated
        if not self.s.name_pattern.search(name):
            return updated

        schema_literal = _build_schema_for_func(original, self.s.schema_mode)
        dec_code = f"enveloped(schema={schema_literal})"
        dec = cst.Decorator(decorator=cst.parse_expression(dec_code))
        decorators = list(updated.decorators or [])
        decorators.insert(0, dec)
        self._decorated += 1
        return updated.with_changes(decorators=decorators)

    @property
    def metrics(self):
        return self._added_import, self._decorated, self._skipped_existing

# ------------------------------ Runner ---------------------------------------

def should_skip(path: Path, settings: Settings) -> bool:
    lower = str(path).lower()
    return any(f"/{frag.lower()}/" in lower or lower.endswith(f"/{frag.lower()}") for frag in settings.exclude)

def _target_for(path: Path, s: Settings) -> Path:
    if s.write_mode == "inplace":
        return path
    # mirror
    out_root = s.out_dir or path.parents[0] / f"{s.root.name}_decorated"
    rel = path.relative_to(s.root)
    return out_root / rel

def _ensure_out_root(s: Settings) -> Path:
    if s.write_mode == "inplace":
        return s.root
    out_root = s.out_dir or (s.root.parent / f"{s.root.name}_decorated")
    if out_root.exists():
        if not s.force:
            raise SystemExit(f"[decorate_enforcer] ERROR: out-dir exists: {out_root} (use --force to reuse)")
    else:
        if not s.dry_run:
            out_root.mkdir(parents=True, exist_ok=True)
    return out_root

def transform_py_file(path: Path, settings: Settings) -> FileResult:
    src = path.read_text(encoding="utf-8")
    module = cst.parse_module(src)
    tx = DecorateTransformer(settings)
    new_mod = module.visit(tx)
    added_import, decorated, skipped = tx.metrics
    changed = (new_mod.code != src)

    target = _target_for(path, settings)
    target.parent.mkdir(parents=True, exist_ok=True)
    if settings.write_mode == "mirror":
        # Always write the transformed code into the mirror, even if unchanged,
        # to keep the trees aligned for PyCharm compare.
        if not settings.dry_run:
            target.write_text(new_mod.code, encoding="utf-8")
    else:
        # inplace: write only if content changed
        if changed and not settings.dry_run:
            target.write_text(new_mod.code, encoding="utf-8")

    if settings.verbose and (settings.write_mode == "inplace" and changed or settings.write_mode == "mirror"):
        print(f"[decorate_enforcer] {'updated' if changed else 'mirrored'}: {path} -> {target} "
              f"(+import={added_import}, +decorated={decorated}, skipped={skipped})")

    return FileResult(
        path=path,
        target=target,
        changed=changed,
        added_import=added_import,
        decorated=decorated,
        skipped_existing=skipped,
    )

def copy_other_file(path: Path, target: Path, settings: Settings) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    if not settings.dry_run:
        shutil.copy2(path, target)
    if settings.verbose:
        print(f"[decorate_enforcer] copied: {path} -> {target}")

def run(settings: Settings) -> List[FileResult]:
    out_root = _ensure_out_root(settings)
    results: List[FileResult] = []
    for path in settings.root.rglob("*"):
        if path.is_dir():
            continue
        if should_skip(path, settings):
            continue
        if path.suffix == ".py":
            results.append(transform_py_file(path, settings))
        else:
            if settings.write_mode == "mirror" and settings.copy_others:
                target = _target_for(path, settings)
                copy_other_file(path, target, settings)
    # Print where the mirror is
    if settings.write_mode == "mirror":
        print(f"[decorate_enforcer] Mirror written to: {out_root}")
    return results

def summarize(results: List[FileResult], s: Settings) -> None:
    files = len([r for r in results if r.path.suffix == ".py"])
    changed = sum(1 for r in results if r.changed)
    imports = sum(1 for r in results if r.added_import)
    decorated = sum(r.decorated for r in results)
    skipped = sum(r.skipped_existing for r in results)
    mode = s.write_mode
    print(
        "[decorate_enforcer] Summary\n"
        f"  Mode              : {mode}\n"
        f"  Examined .py files: {files}\n"
        f"  Changed (AST diff): {changed}\n"
        f"  Imports added     : {imports}\n"
        f"  Functions decorated : {decorated}\n"
        f"  Already decorated   : {skipped}\n"
    )

def parse_args(argv: Optional[List[str]] = None) -> Settings:
    ap = argparse.ArgumentParser(description="Codemod to add @enveloped(schema={...}) to boundary functions.")
    ap.add_argument("--root", default=str(Path("..") / "backup_orchestrator_pkg"))
    ap.add_argument("--pkg-top", default="backup_orchestrator_pkg")
    ap.add_argument("--name-pattern", default=DEFAULT_PATTERN)
    ap.add_argument("--schema", choices=("minimal", "hints"), default="minimal",
                    help="Schema generation mode: 'minimal' sets type/required/default; 'hints' adds bounds/patterns.")
    ap.add_argument("--write-mode", choices=("inplace", "mirror"), default="mirror",
                    help="Where to write results. 'mirror' writes a full tree you can compare in PyCharm.")
    ap.add_argument("--out-dir", default=None,
                    help="Mirror destination directory (default: <root>_decorated).")
    ap.add_argument("--copy-others", action="store_true",
                    help="In mirror mode, also copy non-.py files.")
    ap.add_argument("--force", action="store_true",
                    help="Allow writing into an existing --out-dir.")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--exclude", default="tests,test,.venv,venv,__pycache__")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args(argv)

    root = Path(args.root).resolve()
    if not root.exists():
        raise SystemExit(f"[decorate_enforcer] ERROR: root not found: {root}")

    try:
        pat = re.compile(args.name_pattern)
    except re.error as e:
        raise SystemExit(f"[decorate_enforcer] ERROR: invalid --name-pattern regex: {e}")

    out_dir = Path(args.out_dir).resolve() if args.out_dir else None

    exclude = tuple([x.strip() for x in args.exclude.split(",") if x.strip()])
    return Settings(
        root=root,
        pkg_top=args.pkg_top.strip(),
        name_pattern=pat,
        schema_mode=args.schema,
        write_mode=args.write_mode,
        out_dir=out_dir,
        copy_others=bool(args.copy_others),
        force=bool(args.force),
        dry_run=bool(args.dry_run),
        exclude=exclude,
        verbose=bool(args.verbose),
    )

def main(argv: Optional[List[str]] = None) -> int:
    try:
        settings = parse_args(argv)
        results = run(settings)
        summarize(results, settings)
        if settings.dry_run:
            print(f"[decorate_enforcer] Dry-run mode (schema={settings.schema_mode}, mode={settings.write_mode}): no files were modified.")
        return 0
    except SystemExit as e:
        if isinstance(e.code, int):
            return 1 if e.code == 2 else e.code
        return 1
    except Exception as e:  # pragma: no cover
        print(f"[decorate_enforcer] ERROR: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
