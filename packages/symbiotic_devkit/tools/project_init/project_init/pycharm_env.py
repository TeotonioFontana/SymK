# -*- coding: utf-8 -*-
"""
PyCharm project detection and validation for symk-project-init.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict, List


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
