# -*- coding: utf-8 -*-
"""
String templates for symk-project-init:
- purpose.md
- .symbiotic.yaml
- .gitignore
- .editorconfig
- pyproject.toml
- README.md
- pre-commit config
- CI workflow
- code skeletons (result_envelope, healthcheck, core, adapters, etc.)
"""

from __future__ import annotations

from textwrap import dedent

from .utils import utc_now_iso


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
        \"\"\"
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
        \"\"\"
        from __future__ import annotations
        from functools import wraps
        from typing import Any, Callable, Dict, Optional
        from datetime import datetime, timezone
        import traceback
        import time

        def _iso_utc() -> str:
            return datetime.now(timezone.utc).isoformat()

        def _validate(schema: Optional[Dict[str, dict]], bound_args: Dict[str, Any]) -> list[str]:
            \"\"\"
            Validate arguments by a tiny rule set:
              type, required, default, non_empty, min, max, allowed, pattern (regex str)
            Returns a list of error messages. It also fills defaults into bound_args.
            \"\"\"
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
            \"\"\"Wrap a boundary function so it always returns an envelope.\"\"\"
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
