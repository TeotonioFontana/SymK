# -*- coding: utf-8 -*-
"""
Console entrypoints:
  sym-init     → drop .symbiotic.yaml + common shim (+ CI/pre-commit)
  sym-check    → run static checks
  sym-decorate → run codemod (mirror-friendly)
"""
from __future__ import annotations
import argparse
from pathlib import Path
from typing import Optional
import yaml

def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else {}

def cmd_init(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Initialize a repo with Symbiotic config and shim.")
    ap.add_argument("--dir", default=".")
    args = ap.parse_args(argv)
    target = Path(args.dir).resolve()
    (target / "common").mkdir(parents=True, exist_ok=True)
    (target / ".github/workflows").mkdir(parents=True, exist_ok=True)
    # Core files
    (target / ".symbiotic.yaml").write_text(DEFAULT_CFG, encoding="utf-8")
    (target / "common" / "result_envelope.py").write_text("from symbiotic_devkit.envelope import enveloped\n__all__=['enveloped']\n", encoding="utf-8")
    (target / ".pre-commit-config.yaml").write_text(DEFAULT_PRECOMMIT, encoding="utf-8")
    (target / ".github" / "workflows" / "symbiotic.yml").write_text(DEFAULT_GHA, encoding="utf-8")
    print(f"[sym-init] Initialized at {target}")
    return 0

def cmd_check(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Run Symbiotic checks")
    ap.add_argument("--config", default=".symbiotic.yaml")
    ap.add_argument("--root", default=None)
    ap.add_argument("--allow", default=None)
    ap.add_argument("--out-json", default=None)
    ap.add_argument("--out-report", default=None)
    args = ap.parse_args(argv)
    cfg = _load_yaml(Path(args.config))
    root = Path(args.root or cfg.get("root", ".")).resolve()
    allow = args.allow or ",".join(cfg.get("cross_pkg_allow", ["common"]))
    out_json = args.out_json or cfg.get("report_json")
    out_report = args.out_report or cfg.get("report_md")
    from symbiotic_devkit.codemods.symbiotic_checks import main as check_main
    argv2 = ["--root", str(root), "--allow", allow]
    if out_json: argv2 += ["--out-json", out_json]
    if out_report: argv2 += ["--out-report", out_report]
    return check_main(argv2)

def cmd_decorate(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Run codemod to enforce @enveloped")
    ap.add_argument("--config", default=".symbiotic.yaml")
    ap.add_argument("--root", default=None)
    ap.add_argument("--schema", choices=("minimal","hints"), default=None)
    ap.add_argument("--write-mode", choices=("mirror","inplace"), default=None)
    ap.add_argument("--out-dir", default=None)
    ap.add_argument("--copy-others", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--name-pattern", default=None)
    ap.add_argument("--pkg-top", default=None)
    args = ap.parse_args(argv)
    cfg = _load_yaml(Path(args.config))
    root = Path(args.root or cfg.get("root", ".")).resolve()
    schema = args.schema or cfg.get("schema_mode", "minimal")
    write_mode = args.write_mode or cfg.get("write_mode", "mirror")
    out_dir = args.out_dir or cfg.get("out_dir")
    copy_others = args.copy_others or bool(cfg.get("copy_others", False))
    force = args.force or True
    name_pattern = args.name_pattern or cfg.get("boundary_name_regex", "(run|execute|perform|backup|restore|handle|process)")
    pkg_top = args.pkg_top or cfg.get("pkg_top", "common")
    from symbiotic_devkit.codemods import decorate_enforcer as de
    argv2 = ["--root", str(root), "--schema", schema, "--write-mode", write_mode, "--name-pattern", name_pattern, "--pkg-top", pkg_top]
    if out_dir: argv2 += ["--out-dir", out_dir]
    if copy_others: argv2 += ["--copy-others"]
    if force: argv2 += ["--force"]
    return de.main(argv2)

DEFAULT_CFG = """pkg_top: "common"
boundary_name_regex: "(run|execute|perform|backup|restore|handle|process)"
schema_mode: "hints"
write_mode: "mirror"
out_dir: ".sym-mirror"
copy_others: true
exclude_dirs: ["tests", ".venv", "venv", "__pycache__"]
cross_pkg_allow: ["common"]
bounce_exempt: []
report_json: "reports/symbiotic_report.json"
report_md:   "reports/symbiotic_report.md"
"""

DEFAULT_PRECOMMIT = """repos:
  - repo: local
    hooks:
      - id: symbiotic-check
        name: symbiotic-check
        entry: sym-check --config .symbiotic.yaml
        language: system
        pass_filenames: false
"""

DEFAULT_GHA = """name: symbiotic-guardrails
on: [push, pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install libcst pyyaml .
      - run: mkdir -p reports
      - run: sym-check --config .symbiotic.yaml --out-json reports/symbiotic_report.json --out-report reports/symbiotic_report.md
      - uses: actions/upload-artifact@v4
        with:
          name: symbiotic-reports
          path: reports/*
"""
