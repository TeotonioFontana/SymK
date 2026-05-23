#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scaffold_plc.py

Scaffold a SymK-style PLC documentation structure into a project root.

What it does
------------
- Creates <project_root>/plc/ with phase folders and starter .md docs
- Does NOT overwrite existing files unless --force
- Writes a scaffold_manifest.json with created/skipped/errors

Usage
-----
python3 scaffold_plc.py /path/to/new_project
python3 scaffold_plc.py /path/to/new_project --force
python3 scaffold_plc.py /path/to/new_project --project-name "My Project"

Notes
-----
- You can customize the PLC spec in PLC_SPEC below (single source of truth).
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple


# =============================================================================
# PLC Spec (edit this to match your canonical PLC)
# =============================================================================

# Each entry: (relative_path_under_plc, kind)
# kind: "dir" or "md" or "txt" or "json" or "yaml"
PLC_SPEC: List[Tuple[str, str]] = [
    ("README.md", "md"),
    ("00_Meta", "dir"),
    ("00_Meta/00.0_PLC_Overview.md", "md"),
    ("00_Meta/00.1_Glossary.md", "md"),
    ("00_Meta/00.2_Decisions_Log.md", "md"),

    ("01_Discovery", "dir"),
    ("01_Discovery/01.0_Discovery_Index.md", "md"),
    ("01_Discovery/01.1_Product_Vision.md", "md"),
    ("01_Discovery/01.2_Market_Research.md", "md"),
    ("01_Discovery/01.3_Target_Segments.md", "md"),
    ("01_Discovery/01.4_SWOT.md", "md"),
    ("01_Discovery/01.5_Requirements.md", "md"),
    ("01_Discovery/01.6_Discovery_Outcomes.md", "md"),

    ("02_Architecture", "dir"),
    ("02_Architecture/02.0_Architecture_Index.md", "md"),
    ("02_Architecture/02.1_System_Context.md", "md"),
    ("02_Architecture/02.2_Topology.md", "md"),
    ("02_Architecture/02.3_Data_Model.md", "md"),
    ("02_Architecture/02.4_Security.md", "md"),
    ("02_Architecture/02.5_Integration.md", "md"),

    ("03_Planning", "dir"),
    ("03_Planning/03.0_Planning_Index.md", "md"),
    ("03_Planning/03.1_Roadmap.md", "md"),
    ("03_Planning/03.2_Backlog.md", "md"),
    ("03_Planning/03.3_Risks.md", "md"),

    ("04_Design", "dir"),
    ("04_Design/04.0_Design_Index.md", "md"),
    ("04_Design/04.1_UX_UI.md", "md"),
    ("04_Design/04.2_API_Spec.md", "md"),
    ("04_Design/04.3_DB_Schema.md", "md"),

    ("05_Implementation", "dir"),
    ("05_Implementation/05.0_Implementation_Index.md", "md"),
    ("05_Implementation/05.1_Dev_Environment.md", "md"),
    ("05_Implementation/05.2_Coding_Standards.md", "md"),

    ("06_Testing", "dir"),
    ("06_Testing/06.0_Testing_Index.md", "md"),
    ("06_Testing/06.1_Test_Plan.md", "md"),
    ("06_Testing/06.2_Test_Cases.md", "md"),

    ("07_Deployment", "dir"),
    ("07_Deployment/07.0_Deployment_Index.md", "md"),
    ("07_Deployment/07.1_Deployment_Guide.md", "md"),
    ("07_Deployment/07.2_Runbook.md", "md"),

    ("08_Operations", "dir"),
    ("08_Operations/08.0_Operations_Index.md", "md"),
    ("08_Operations/08.1_Monitoring.md", "md"),
    ("08_Operations/08.2_Incident_Response.md", "md"),
    ("08_Operations/08.3_Maintenance.md", "md"),

    # Optional machine-readable layer (keep if you want)
    ("contracts", "dir"),
    ("contracts/plc.yaml", "yaml"),
    ("scaffold_manifest.json", "json"),
]


# =============================================================================
# Templates
# =============================================================================

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def md_header(title: str, project_name: str) -> str:
    return (
        f"# {title}\n\n"
        f"**Project:** {project_name}\n\n"
        f"**Last updated (UTC):** {utc_now_iso()}\n\n"
        f"---\n\n"
    )


def md_section(prompt: str) -> str:
    return f"## Notes\n\n{prompt}\n"


def render_md(relpath: str, project_name: str) -> str:
    name = Path(relpath).stem.replace("_", " ")
    title = name

    # Slightly smarter titles for a few known files
    if relpath.endswith("README.md"):
        title = "PLC Workspace"
        return (
            md_header(title, project_name)
            + "This folder is the Product Life Cycle (PLC) workspace.\n\n"
              "Rules of engagement:\n"
              "- Keep it readable.\n"
              "- Keep it auditable.\n"
              "- If it matters, write it down. If it doesn’t, don’t.\n\n"
              "If you want to change the structure, edit the scaffold spec and re-run.\n"
        )

    if relpath.endswith("_Index.md"):
        return (
            md_header(title, project_name)
            + "This is the index page for this PLC phase.\n\n"
              "### Contents\n"
              "- (Add links to the documents in this folder)\n\n"
              "### Status\n"
              "- Owner:\n"
              "- Current state:\n"
              "- Next decision:\n"
        )

    # Default per-doc skeleton
    return (
        md_header(title, project_name)
        + md_section(
            "Capture:\n"
            "- What is the goal of this document?\n"
            "- What decisions does it support?\n"
            "- What assumptions are we making?\n"
            "- What evidence do we have?\n"
        )
        + "## Open Questions\n\n- \n\n"
          "## Decisions\n\n- \n"
    )


def render_yaml(project_name: str) -> str:
    # Minimal stub — replace with your canonical contract if you have one.
    return (
        f"# plc.yaml\n"
        f"# Minimal PLC contract stub\n"
        f"project:\n"
        f"  name: {project_name!r}\n"
        f"plc:\n"
        f"  version: 1.0\n"
        f"  root: plc/\n"
        f"  phases:\n"
        f"    - id: 00_Meta\n"
        f"    - id: 01_Discovery\n"
        f"    - id: 02_Architecture\n"
        f"    - id: 03_Planning\n"
        f"    - id: 04_Design\n"
        f"    - id: 05_Implementation\n"
        f"    - id: 06_Testing\n"
        f"    - id: 07_Deployment\n"
        f"    - id: 08_Operations\n"
    )


# =============================================================================
# Scaffolder
# =============================================================================

@dataclass
class Result:
    created: List[str]
    skipped: List[str]
    errors: List[str]

    def to_dict(self) -> Dict[str, object]:
        return {
            "created": self.created,
            "skipped": self.skipped,
            "errors": self.errors,
            "created_count": len(self.created),
            "skipped_count": len(self.skipped),
            "errors_count": len(self.errors),
            "timestamp_utc": utc_now_iso(),
        }


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_text_file(path: Path, content: str, force: bool) -> str:
    if path.exists() and not force:
        return "skipped"
    ensure_dir(path.parent)
    path.write_text(content, encoding="utf-8")
    return "created"


def scaffold(project_root: Path, project_name: str, force: bool) -> Result:
    res = Result(created=[], skipped=[], errors=[])

    try:
        ensure_dir(project_root)
    except Exception as e:
        res.errors.append(f"Failed to create project_root '{project_root}': {e}")
        return res

    plc_root = project_root / "plc"
    try:
        ensure_dir(plc_root)
    except Exception as e:
        res.errors.append(f"Failed to create plc root '{plc_root}': {e}")
        return res

    # Create everything from spec
    for rel, kind in PLC_SPEC:
        target = plc_root / rel

        try:
            if kind == "dir":
                ensure_dir(target)
                res.created.append(str(target))
                continue

            if kind == "md":
                status = write_text_file(target, render_md(rel, project_name), force)
            elif kind == "yaml":
                status = write_text_file(target, render_yaml(project_name), force)
            elif kind == "json":
                # We'll write manifest at the end (but create placeholder if needed)
                status = write_text_file(target, "{}", force)
            elif kind == "txt":
                status = write_text_file(target, "", force)
            else:
                res.errors.append(f"Unknown kind '{kind}' for '{rel}'")
                continue

            if status == "created":
                res.created.append(str(target))
            else:
                res.skipped.append(str(target))

        except Exception as e:
            res.errors.append(f"Failed on '{target}': {e}")

    # Write final manifest (always updates unless you want strict mode)
    manifest_path = plc_root / "scaffold_manifest.json"
    try:
        ensure_dir(manifest_path.parent)
        manifest_path.write_text(json.dumps(res.to_dict(), indent=2), encoding="utf-8")
        if str(manifest_path) not in res.created and str(manifest_path) not in res.skipped:
            res.created.append(str(manifest_path))
    except Exception as e:
        res.errors.append(f"Failed writing manifest '{manifest_path}': {e}")

    return res


# =============================================================================
# CLI
# =============================================================================

def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Scaffold a PLC folder/files structure into a new project root."
    )
    p.add_argument(
        "project_root",
        help="Path to the new project root (will be created if missing).",
    )
    p.add_argument(
        "--project-name",
        default=None,
        help="Project name used inside generated docs (default: folder name).",
    )
    p.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files.",
    )
    return p.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    project_root = Path(args.project_root).expanduser().resolve()
    project_name = args.project_name or project_root.name

    result = scaffold(project_root=project_root, project_name=project_name, force=args.force)

    # Human-readable summary
    print(f"PLC scaffold root: {project_root / 'plc'}")
    print(f"Created: {len(result.created)} | Skipped: {len(result.skipped)} | Errors: {len(result.errors)}")

    if result.errors:
        print("\nErrors:")
        for e in result.errors:
            print(f"- {e}")
        return 2

    # If nothing created and everything skipped, still success.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
