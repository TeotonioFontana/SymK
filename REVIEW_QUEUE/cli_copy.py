#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
symk-project-init — Bootstrap a SymK-compliant Python project (PyCharm-aware)

Creates the minimal structure + files aligned with the coding rules:
- Boundaries as functions with @enveloped
- SQLAlchemy confined to adapters/models
- purpose.md, .symbiotic.yaml, pyproject.toml, tests, optional pre-commit/CI
- Validates --dest looks like a PyCharm project unless --skip-ide-check

Usage examples:
  python -m project_init --inplace --package myapp --precommit --ci
  symk-init --name MyApp --dest /path/to/PyCharmProject --services
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from textwrap import dedent
from typing import Any, Dict, List

# ------------------------- helpers -------------------------
def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def slugify_name(name: str) -> str:
    s = re.sub(r"[^\w]+", "_", name, flags=re.IGNORECASE).strip("_")
    if not s:
        return "app"
    if re.match(r"^\d", s):
        s = "p_" + s
    return s.lower()


def write_file(path: Path, content: str, *, force: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        return
    path.write_text(content, encoding="utf-8")


def touch(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text("", encoding="utf-8")


def print_created(root: Path) -> None:
    print("\nProject layout:")
    for p in sorted(root.rglob("*")):
        if p.is_dir():
            continue
        rel = p.relative_to(root)
        print(f"  - {rel} ({p.stat().st_size} bytes)")


# ------------------------- PyCharm validator -------------------------
def _collect_iml_paths(base: Path) -> List[Path]:
    imls: List[Path] = []
    imls.extend(base.glob("*.iml"))
    idea = base / ".idea"
    if idea.is_dir():
        imls.extend(idea.glob("*.iml"))
    return imls


def detect_pycharm_project(base: Path) -> Dict[str, Any]:
    idea = base / ".idea"
    misc = idea / "misc.xml"
    modules_xml = idea / "modules.xml"
    workspace_xml = idea / "workspace.xml"
    imls = _collect_iml_paths(base)
    venv_ok = (base / ".venv" / "pyvenv.cfg").exists() or (base / "venv" / "pyvenv.cfg").exists()
    ok = idea.is_dir() and (misc.exists() or modules_xml.exists() or workspace_xml.exists()) and bool(imls)
    return {
        "base": str(base),
        "idea_dir": idea.is_dir(),
        "misc_xml": misc.exists(),
        "modules_xml": modules_xml.exists(),
        "workspace_xml": workspace_xml.exists(),
        "iml_found": bool(imls),
        "iml_list": [str(p) for p in imls],
        "venv_present": venv_ok,
        "ok": ok,
    }


def require_pycharm(base: Path, *, strict: bool = True, report: bool = False) -> None:
    diag = detect_pycharm_project(base)
    if report:
        print("[PyCharm check]")
        for k in ["idea_dir", "modules_xml", "misc_xml", "workspace_xml", "iml_found", "venv_present"]:
            print(f"  - {k}: {diag[k]}")
        if diag["iml_found"]:
            for p in diag["iml_list"]:
                print(f"    * {p}")
    if strict and not diag["ok"]:
        print(
            f"[ERROR] --dest doesn’t look like a PyCharm project: {base}\n"
            f"  Expect .idea/ plus one of modules.xml/misc.xml/workspace.xml and at least one .iml.\n"
            f"  Use --skip-ide-check to bypass if you know what you’re doing.",
            file=sys.stderr,
        )
        raise SystemExit(3)


# ------------------------- options -------------------------
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


# ------------------------- templates -------------------------
def tpl_purpose_md(name: str) -> str:
    return dedent(
        f"""\
        # Purpose

        **Application**: {name}
        **Effective**: {utc_now_iso()}

        ## Objective
        Concise description of the product’s goal and the problem it solves.

        ## Scope
        - **In**: Core use cases the app MUST address.
        - **Out**: What the app explicitly will not do.

        ## Assumptions
        List critical assumptions (tech, users, data).

        ## Non-Functional
        Performance, reliability, security, compliance, accessibility.

        ## Traceability
        Everything in the codebase should map back to this purpose.
        """
    )


def tpl_symbiotic_yaml(pkg: str) -> str:
    return dedent(
        f"""\
        spec_version: "1.0.0"
        pkg_top: "common"
        boundary_name_regex: "(run|execute|perform|backup|restore|handle|process)"
        schema_mode: "hints"          # or "minimal"
        write_mode: "mirror"          # or "inplace"
        out_dir: ".sym-mirror"
        copy_others: true
        exclude_dirs: ["tests", ".venv", "venv", "__pycache__"]
        cross_pkg_allow: ["common"]
        bounce_exempt: []
        report_json: "reports/symbiotic_report.json"
        report_md:   "reports/symbiotic_report.md"
        autofix_mode: "off"           # "off" | "safe"
        autofix_review: false
        """
    )


def tpl_gitignore() -> str:
    return dedent(
        """\
        # Python
        __pycache__/
        *.py[cod]
        *.pyo
        .Python
        .venv/
        venv/
        build/
        dist/
        .pytest_cache/
        .mypy_cache/
        .ruff_cache/
        .idea/
        .DS_Store
        reports/
        """
    )


def tpl_editorconfig() -> str:
    return dedent(
        """\
        root = true

        [*]
        charset = utf-8
        end_of_line = lf
        insert_final_newline = true
        indent_style = space
        indent_size = 4
        trim_trailing_whitespace = true

        [*.md]
        trim_trailing_whitespace = false
        """
    )


def tpl_pyproject(name: str, pkg: str) -> str:
    return dedent(
        f"""\
        [project]
        name = "{name}"
        version = "0.1.0"
        description = "SymK project scaffold"
        readme = "README.md"
        requires-python = ">=3.11"
        authors = [{{ name = "Teotoniio Fontana" }}]
        dependencies = [
            "SQLAlchemy>=2.0",
        ]

        [project.optional-dependencies]
        dev = ["pytest>=8", "pre-commit>=3.6", "ruff>=0.4"]

        [tool.ruff]
        line-length = 100
        target-version = "py311"
        select = ["E","F","W","I","B","UP"]
        """
    )


def tpl_readme(name: str) -> str:
    return dedent(
        f"""\
        # {name}

        Minimal SymK-compliant project scaffold.

        ## Quick start
        - Create venv, install dev deps:
          ```
          python -m venv .venv && source .venv/bin/activate
          pip install -e '.[dev]'
          ```
        - Run tests:
          ```
          pytest -q
          ```
        - (Optional) Set up pre-commit:
          ```
          pre-commit install
          ```
        """
    )


def tpl_precommit() -> str:
    return dedent(
        """\
        repos:
          - repo: https://github.com/astral-sh/ruff-pre-commit
            rev: v0.7.0
            hooks:
              - id: ruff
                args: [--fix]
              - id: ruff-format
          - repo: local
            hooks:
              - id: sym-check
                name: sym-check
                entry: python -m tools.symbiotic_check --root . --report-json reports/symbiotic_report.json --report-md reports/symbiotic_report.md
                language: system
                pass_filenames: false
        """
    )


def tpl_ci_yaml() -> str:
    return dedent(
        """\
        name: CI
        on: [push, pull_request]
        jobs:
          symbiotic:
            runs-on: ubuntu-latest
            steps:
              - uses: actions/checkout@v4
              - uses: actions/setup-python@v5
                with:
                  python-version: '3.11'
              - run: pip install -e '.[dev]'
              - run: ruff check --output-format=github .
              - run: pytest -q
              # Optional: run sym-check if your tools package is present
              - run: python -m tools.symbiotic_check --root . --report-json reports/symbiotic_report.json --report-md reports/symbiotic_report.md || true
        """
    )


def tpl_common_init() -> str:
    return ""


def tpl_result_envelope_py() -> str:
    return dedent(
        """\
        # -*- coding: utf-8 -*-
        """
        '"""'
        """
        result_envelope.py — Symbiotic result envelope & validation

        Decorator `@enveloped(schema=...)` wraps boundary functions to:
          • validate inputs against a simple schema (type/min/max/allowed/non_empty/required/default)
          • enforce a standard envelope with status triad (success|invalid|error)
          • attach meta (fn, UTC ISO ts, duration_ms, args)

        Contract:
          The decorated function MUST return a payload dict. We keep per-key
          types stable. The decorator wraps it into:

            {
              "ok": bool,
              "status": "success" | "invalid" | "error",
              "code": int,
              "msg": str | None,
              "data": dict,
              "errors": list[str],
              "exception": {"type": str, "message": str, "trace": str} | None,
              "meta": {"fn": str, "ts": str, "duration_ms": int, "args": dict}
            }

        Notes:
          - Keep heavy validation at boundaries. Private helpers remain simple.
          - `include_trace=True` attaches traceback for status=error.
        """
        '"""'
        """
        from __future__ import annotations
        from functools import wraps
        from typing import Any, Callable, Dict, Optional
        from datetime import datetime, timezone
        import traceback
        import time

        def _iso_utc() -> str:
            return datetime.now(timezone.utc).isoformat()

        def _validate(schema: Optional[Dict[str, dict]], bound_args: Dict[str, Any]) -> list[str]:
            \"""
            Validate arguments by a tiny rule set:
              type, required, default, non_empty, min, max, allowed, pattern (regex str)
            Returns a list of error messages. It also fills defaults into bound_args.
            \"""
            if not schema:
                return []
            import re
            errors: list[str] = []
            for name, rules in schema.items():
                has = name in bound_args
                value = bound_args.get(name, None)
                if not has and rules.get("required", True) and "default" not in rules:
                    errors.append(f"Missing required param: {name}")
                    continue
                if not has and "default" in rules:
                    bound_args[name] = rules["default"]
                    value = bound_args[name]
                    has = True
                if not has:
                    continue
                typ = rules.get("type")
                if typ and not isinstance(value, typ):
                    errors.append(f"Param {name}: expected {getattr(typ, '__name__', typ)}, got {type(value).__name__}")
                    continue
                if rules.get("non_empty") and (value == '' or value == [] or value == {}):
                    errors.append(f"Param {name}: must be non-empty")
                if isinstance(value, (int, float)):
                    if "min" in rules and value < rules["min"]:
                        errors.append(f"Param {name}: {value} < min {rules['min']}")
                    if "max" in rules and value > rules["max"]:
                        errors.append(f"Param {name}: {value} > max {rules['max']}")
                if "allowed" in rules and value not in set(rules["allowed"]):
                    errors.append(f"Param {name}: {value} not in allowed set")
                if "pattern" in rules:
                    if not re.match(rules["pattern"], str(value)):
                        errors.append(f"Param {name}: does not match pattern")
            return errors

        def enveloped(
            *,
            schema: Optional[Dict[str, dict]] = None,
            require_payload_dict: bool = True,
            success_code: int = 200,
            invalid_code: int = 422,
            error_code: int = 500,
            include_trace: bool = False,
        ):
            \"""Wrap a boundary function so it always returns an envelope.\"""
            def deco(fn):
                @wraps(fn)
                def wrapper(*args, **kwargs):
                    started = time.perf_counter()
                    from inspect import signature
                    sig = signature(fn)
                    bound = sig.bind_partial(*args, **kwargs)
                    bound.apply_defaults()
                    bound_args = dict(bound.arguments)

                    val_errs = _validate(schema, bound_args)
                    if val_errs:
                        return {
                            "ok": False,
                            "status": "invalid",
                            "code": invalid_code,
                            "msg": "Input validation failed",
                            "data": {},
                            "errors": val_errs,
                            "exception": None,
                            "meta": {"fn": f"{fn.__module__}.{fn.__name__}", "ts": _iso_utc(), "duration_ms": int((time.perf_counter()-started)*1000), "args": bound_args},
                        }
                    try:
                        payload = fn(**bound_args)
                        if require_payload_dict and not isinstance(payload, dict):
                            raise TypeError("Boundary payload must be a dict")
                        return {
                            "ok": True,
                            "status": "success",
                            "code": success_code,
                            "msg": None,
                            "data": payload,
                            "errors": [],
                            "exception": None,
                            "meta": {"fn": f"{fn.__module__}.{fn.__name__}", "ts": _iso_utc(), "duration_ms": int((time.perf_counter()-started)*1000), "args": bound_args},
                        }
                    except Exception as ex:
                        exc = {"type": type(ex).__name__, "message": str(ex), "trace": traceback.format_exc() if include_trace else ""}
                        return {
                            "ok": False,
                            "status": "error",
                            "code": error_code,
                            "msg": "Unhandled exception",
                            "data": {},
                            "errors": [],
                            "exception": exc,
                            "meta": {"fn": f"{fn.__module__}.{fn.__name__}", "ts": _iso_utc(), "duration_ms": int((time.perf_counter()-started)*1000), "args": bound_args},
                        }
                return wrapper
            return deco
        """
    )


def tpl_boundaries_healthcheck(pkg: str) -> str:
    return dedent(
        f"""\
        # -*- coding: utf-8 -*-
        \"\"\"Boundary: simple healthcheck (pure, stateless, envelope-wrapped).\"\"\"
        from {pkg}.common.result_envelope import enveloped

        @enveloped(schema={{"ping": {{"type": bool, "required": False, "default": True}}}})
        def run_healthcheck(ping: bool = True) -> dict:
            payload = {{"service": "ok", "ping": bool(ping), "found": True}}
            return payload
        """
    )


def tpl_core_example() -> str:
    return dedent(
        """\
        # -*- coding: utf-8 -*-
        \"\"\"Core: pure, deterministic helpers (no IO/logging/db).\"\"\"
        def add(a: int, b: int) -> int:
            return int(a) + int(b)
        """
    )


def tpl_adapters_db_session() -> str:
    return dedent(
        """\
        # -*- coding: utf-8 -*-
        \"\"\"Adapters: SQLAlchemy session/engine factory (R-960/R-980).\"\"\"
        from __future__ import annotations
        from typing import Generator
        import os
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker

        _DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///:memory:")
        _engine = create_engine(_DATABASE_URL, future=True)
        SessionLocal = sessionmaker(bind=_engine, autoflush=False, autocommit=False, future=True)

        def get_engine():
            return _engine

        def session_scope() -> Generator:
            session = SessionLocal()
            try:
                yield session
                session.commit()
            except Exception:
                session.rollback()
                raise
            finally:
                session.close()
        """
    )


def tpl_models_init() -> str:
    return ""


def tpl_tests_healthcheck(pkg: str) -> str:
    return dedent(
        f"""\
        # -*- coding: utf-8 -*-
        from {pkg}.boundaries.run_healthcheck import run_healthcheck

        def test_healthcheck_envelope_success():
            env = run_healthcheck(ping=True)
            assert env["ok"] is True
            assert env["status"] == "success"
            assert env["code"] == 200
            assert isinstance(env["data"], dict)
            assert env["data"]["service"] == "ok"
            assert env["data"]["ping"] is True
            assert "meta" in env and "ts" in env["meta"]
        """
    )


def tpl_readme_services() -> str:
    return "# services/\n\nOptional thin orchestration layer. Compose adapters and core; no direct IO."


# ------------------------- PLC structure (project PLC) -------------------------
def create_plc_structure(root: Path, project_name: str) -> None:
    """
    Create the project PLC skeleton under root/PLC.

    This is the *instance* PLC for this project (not the meta PLC template).
    It follows the agreed phase structure and drops a tiny README.md into
    each subfolder so the tree is visible and ready to be filled.
    """
    plc_root = root / "PLC"
    phases: Dict[str, List[str]] = {
        "1_Discovery": [
            "1.1_Product_Vision",
            "1.2_Market_Research",
            "1.3_Stakeholder_Map",
        ],
        "2_Architecture": [
            "2.1_System_Blueprints",
            "2.2_Reference_Stacks",
            "2.3_Security_Model",
        ],
        "3_Planning": [
            "3.1_Roadmap",
            "3.2_Release_Trains",
            "3.3_Scope_Definition",
        ],
        "4_Design": [
            "4.1_UX_Flows",
            "4.2_IA_Diagrams",
            "4.3_Design_System",
        ],
        "5_Development": [
            "5.1_Backend",
            "5.2_Frontend",
            "5.3_Infrastructure",
        ],
        "6_Testing": [
            "6.1_Test_Plans",
            "6.2_QA_Suites",
            "6.3_Security_Tests",
        ],
        "7_Deployment": [
            "7.1_Runtime_Configs",
            "7.2_CICD_Pipelines",
            "7.3_Observability",
        ],
        "8_Operations": [
            "8.1_SRE_Procedures",
            "8.2_Incident_Response",
            "8.3_Performance_Tuning",
        ],
        "9_GTM": [
            "9.1_Positioning",
            "9.2_Sales_Enablement",
            "9.3_Pricing",
        ],
        "10_Documentation": [
            "10.1_Technical_Docs",
            "10.2_User_Docs",
            "10.3_Release_Notes",
        ],
    }

    plc_root.mkdir(parents=True, exist_ok=True)

    # Root README for PLC
    write_file(
        plc_root / "README.md",
        dedent(
            f"""\
            # Product Lifecycle (PLC) — {project_name}

            This folder contains the *project-level* PLC instance for this product.
            Each phase folder groups the working artifacts for that phase.
            """
        ),
        force=False,
    )

    for phase, subfolders in phases.items():
        phase_dir = plc_root / phase
        phase_dir.mkdir(parents=True, exist_ok=True)

        # Simple phase README
        pretty_phase = phase.replace("_", " ")
        write_file(
            phase_dir / "README.md",
            dedent(
                f"""\
                # {pretty_phase}

                Project PLC phase for **{project_name}**.
                """
            ),
            force=False,
        )

        for sub in subfolders:
            sub_dir = phase_dir / sub
            sub_dir.mkdir(parents=True, exist_ok=True)
            pretty_sub = sub.replace("_", " ")
            write_file(
                sub_dir / "README.md",
                dedent(
                    f"""\
                    # {pretty_sub}

                    TODO: fill in for project **{project_name}**.
                    """
                ),
                force=False,
            )


# ------------------------- main -------------------------
def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", default="my_app")
    ap.add_argument("--package", default=None)
    ap.add_argument("--dest", default=".")
    ap.add_argument("--services", action="store_true")
    ap.add_argument("--init-git", action="store_true")
    ap.add_argument("--precommit", action="store_true")
    ap.add_argument("--ci", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--inplace", action="store_true")
    ap.add_argument(
        "--skip-ide-check",
        action="store_true",
        help="Allow scaffolding even if --dest is not a detected PyCharm project",
    )
    ap.add_argument(
        "--ide-report",
        action="store_true",
        help="Print PyCharm project diagnostics",
    )
    args = ap.parse_args(argv)

    name = args.name.strip()
    pkg = args.package.strip() if args.package else slugify_name(name)
    dest = Path(args.dest).resolve()

    # Validate PyCharm project at --dest (or current dir if --inplace)
    ide_base = dest
    if not args.skip_ide_check:
        require_pycharm(ide_base, strict=True, report=args.ide_report)
    else:
        if args.ide_report:
            require_pycharm(ide_base, strict=False, report=True)

    # Determine root for scaffold
    root = dest if args.inplace else dest / name
    root.mkdir(parents=True, exist_ok=True)

    # Directories
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
        if key == "services" and not args.services:
            continue
        p.mkdir(parents=True, exist_ok=True)

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


if __name__ == "__main__":
    raise SystemExit(main())
