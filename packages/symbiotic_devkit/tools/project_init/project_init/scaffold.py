# -*- coding: utf-8 -*-
"""
Core scaffolding logic for symk-project-init.
"""

from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict

from .utils import write_file, touch, print_created, slugify_name
from .templates import (
    tpl_purpose_md,
    tpl_symbiotic_yaml,
    tpl_gitignore,
    tpl_editorconfig,
    tpl_pyproject,
    tpl_readme,
    tpl_precommit,
    tpl_ci_yaml,
    tpl_common_init,
    tpl_result_envelope_py,
    tpl_boundaries_healthcheck,
    tpl_core_example,
    tpl_adapters_db_session,
    tpl_models_init,
    tpl_tests_healthcheck,
    tpl_readme_services,
)
from .plc import create_plc_structure


@dataclass
class Options:
    name: str
    package: str
    dest: Path
    services: bool
    init_git: bool
    precommit: bool
    ci: bool
    force: bool
    inplace: bool
    skip_ide_check: bool
    ide_report: bool


def build_paths(root: Path, pkg: str, services: bool) -> Dict[str, Path]:
    paths = {
        "common": root / pkg / "common",
        "boundaries": root / pkg / "boundaries",
        "core": root / pkg / "core",
        "adapters": root / pkg / "adapters",
        "models": root / pkg / "models",
        "services": root / pkg / "services",
        "tests_pkg": root / "tests" / pkg,
        "docs_waivers": root / "docs" / "waivers",
        "github_wf": root / ".github" / "workflows",
    }
    for key, p in paths.items():
        if key == "services" and not services:
            continue
        p.mkdir(parents=True, exist_ok=True)
    return paths


def initialize_project(args) -> int:
    # Normalize args into Options for clarity
    name = args.name.strip()
    pkg = args.package.strip() if args.package else slugify_name(name)
    dest = Path(args.dest).resolve()

    root = dest if args.inplace else dest / name
    root.mkdir(parents=True, exist_ok=True)

    paths = build_paths(root, pkg, services=args.services)

    # __init__.py files
    for p in [
        root / pkg,
        paths["common"],
        paths["boundaries"],
        paths["core"],
        paths["adapters"],
        paths["models"],
    ]:
        touch(p / "__init__.py")
    if args.services:
        touch(paths["services"] / "__init__.py")

    # Baseline files
    write_file(root / "purpose.md", tpl_purpose_md(name), force=args.force)
    write_file(root / ".symbiotic.yaml", tpl_symbiotic_yaml(pkg), force=args.force)
    write_file(root / ".gitignore", tpl_gitignore(), force=args.force)
    write_file(root / ".editorconfig", tpl_editorconfig(), force=args.force)
    write_file(root / "pyproject.toml", tpl_pyproject(name, pkg), force=args.force)
    write_file(root / "README.md", tpl_readme(name), force=args.force)

    # Common envelope
    write_file(paths["common"] / "result_envelope.py", tpl_result_envelope_py(), force=args.force)
    write_file(paths["common"] / "__init__.py", tpl_common_init(), force=args.force)

    # Boundary sample
    write_file(paths["boundaries"] / "run_healthcheck.py", tpl_boundaries_healthcheck(pkg), force=args.force)

    # Core sample
    write_file(paths["core"] / "example.py", tpl_core_example(), force=args.force)

    # Adapters sample (SQLAlchemy factory)
    write_file(paths["adapters"] / "db_session.py", tpl_adapters_db_session(), force=args.force)

    # Models init
    write_file(paths["models"] / "__init__.py", tpl_models_init(), force=args.force)

    # Optional services readme
    if args.services:
        write_file(paths["services"] / "README.md", tpl_readme_services(), force=args.force)

    # Tests
    write_file(paths["tests_pkg"] / "test_healthcheck.py", tpl_tests_healthcheck(pkg), force=args.force)

    # Docs/waivers keeper
    touch(paths["docs_waivers"] / ".gitkeep")

    # Project PLC skeleton
    create_plc_structure(root, name)

    # Optional pre-commit / CI
    if args.precommit:
        write_file(root / ".pre-commit-config.yaml", tpl_precommit(), force=args.force)
    if args.ci:
        write_file(paths["github_wf"] / "ci.yml", tpl_ci_yaml(), force=args.force)

    # Optional git init
    if args.init_git:
        try:
            subprocess.run(
                ["git", "init"],
                cwd=str(root),
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            subprocess.run(["git", "add", "-A"], cwd=str(root), check=False)
            subprocess.run(
                ["git", "commit", "-m", "chore: initial SymK scaffold"],
                cwd=str(root),
                check=False,
            )
        except Exception as e:
            print(f"[warn] git init failed: {e}", file=sys.stderr)

    print_created(root)
    print("\nNext steps:")
    print("  1) python -m venv .venv && source .venv/bin/activate")
    print("  2) pip install -e '.[dev]'")
    if args.precommit:
        print("  3) pre-commit install")
    print("  4) pytest -q")
    print("  5) (optional) export DATABASE_URL before using SQLAlchemy")
    return 0
