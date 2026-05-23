"""\n===============================================================================
 cli.py — Bootstrap a SymK-compliant Python project (PyCharm-aware)
===============================================================================
 Version..............: v0.0.1-alpha
 Author...............: Teotonio Fontana — Architect
 Programmed by........: Duke (GPT-5.1 Thinking, OpenAI)
 Project..............: SymK - Human-AI Symbiotic Cooperation Protocol
 Layer/Context........: CLI / Project initialization
-------------------------------------------------------------------------------
 Description
 -------------------------------------------------------------------------------
 Creates the minimal structure and files aligned with the SymK coding rules:
 - Boundaries as functions with @enveloped
 - SQLAlchemy confined to adapters/models
 - purpose.md, .symbiotic.yaml, pyproject.toml, tests, optional pre-commit/CI
 - Validates --dest looks like a PyCharm project unless --skip-ide-check
 - Scaffolds the project-level PLC structure under PLC/

-------------------------------------------------------------------------------
 Responsibilities
 -------------------------------------------------------------------------------
 - Parse command-line options for project name, package name, destination and optional features
 - Validate that --dest is a PyCharm project unless --skip-ide-check is used
 - Create the Python package layout (common, boundaries, core, adapters, models, optional services)
 - Generate baseline configuration and documentation files (purpose.md, .symbiotic.yaml, pyproject.toml, README.md, .gitignore, .editorconfig)
 - Scaffold the project Product Lifecycle (PLC) folders and stub README files
 - Optionally create tests, pre-commit config, CI workflow and initialize a git repository

-------------------------------------------------------------------------------
 Inputs & Outputs
 -------------------------------------------------------------------------------
 Inputs:
   - CLI flags: --name, --package, --dest, --services, --init-git, --precommit, --ci, --force, --inplace, --skip-ide-check, --ide-report
   - Existing PyCharm project structure at --dest (unless --skip-ide-check is provided)

 Outputs:
   - Scaffolded project directory tree with Python packages and PLC folders
   - Baseline configuration and documentation files (purpose.md, .symbiotic.yaml, pyproject.toml, README.md, .gitignore, .editorconfig)
   - Optional pre-commit and CI configuration files
   - Optional initialized git repository with initial commit
   - Console summary of created files and suggested next steps

-------------------------------------------------------------------------------
 Change Log
 -------------------------------------------------------------------------------
 v0.0.1-alpha:
   • Initial implementation of SymK project initialization CLI.
   • Scaffolds SymK-compliant Python package, PLC structure and core config files.
   • Includes PyCharm project validation and optional pre-commit, CI and git initialization.
===============================================================================\n"""
from __future__ import annotations

import argparse
from pathlib import Path

from .pycharm_env import require_pycharm
from .scaffold import initialize_project


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="symk-project-init",
        description="Bootstrap a SymK-compliant Python project (PyCharm-aware).",
    )
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
    return ap


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    dest = Path(args.dest).resolve()
    ide_base = dest

    if not args.skip_ide_check:
        require_pycharm(ide_base, strict=True, report=args.ide_report)
    else:
        if args.ide_report:
            require_pycharm(ide_base, strict=False, report=True)

    return initialize_project(args)


if __name__ == "__main__":
    raise SystemExit(main())
