#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
plc_scaffold_from_meta.py — v0.1.1

Generate or update a PLC/ folder structure for a project from a Meta PLC JSON
definition (phases + leaves).

OVERVIEW
--------
This script reads a Meta PLC JSON file (the "meta PLC" definition) and
translates it into a concrete folder and file structure inside a project
root (typically the PyCharm project root).

For each phase/leaf defined in the JSON, it will:

  - Create a phase directory:
        <root>/<plc-dir>/<phase_id>_<Phase_Name_Slug>/

  - Create a leaf directory:
        <root>/<plc-dir>/<phase_dir>/<leaf_id>_<Leaf_Name_Slug>/

  - Generate a leaf README.md using the canonical Meta PLC leaf schema:
        1. Purpose / Objective
        2. Description
        3. Input
        4. Outcomes
        5. Tools / Methodology
        6. AI Support / Symbiotic Role

  - Optionally create empty placeholder files for doc/data outcomes declared
    in the Meta PLC JSON.

Existing files are preserved by default and only created when missing,
unless you explicitly use --force (see below).

META PLC FORMAT (HIGH LEVEL)
----------------------------
The JSON file can be either:

  - a plain object with "phases": [...]
  - or an object with a "meta_plc" top-level key containing "phases": [...]

Each phase entry has at least:
  {
    "id": "1",
    "name": "Discovery",
    "description": "...",
    "leaves": [ ... ]
  }

Each leaf entry has at least:
  {
    "id": "1.1",
    "phase": 1,
    "name": "Product Vision",
    "purpose": "...",
    "description": "...",
    "inputs": [ ... ],
    "outcomes": [ ... ],
    "tools": { ... },
    "ai_contract": { ... }
  }

The script does not validate the full schema, but expects those keys to
exist if you want rich README content.

CLI FLAGS
---------
--meta PATH        (required)
    Path to the Meta PLC JSON file.
    Examples:
      --meta templates/meta_plc.json
      --meta PLC/meta_plc_1to3.json

    This file defines the phases and leaves that will be scaffolded.
    If the file is missing or invalid, the script exits with code 2.

--root PATH        (default: ".")
    Project root directory where the PLC/ structure will be created.
    In your methodology this should be the PyCharm project root.

    Examples:
      --root .
      --root /Users/you/Projects/MyApp

    The script will create (or reuse) the PLC directory under this root:
      <root>/<plc-dir>/...

--plc-dir NAME     (default: "PLC")
    Name of the top-level PLC directory under the project root.

    Examples:
      --plc-dir PLC
      --plc-dir docs/PLC

    If you use "--plc-dir docs/PLC", the effective path becomes:
      <root>/docs/PLC/

--create-outcomes  (flag, default: off)
    When provided, the script will also create **empty placeholder files**
    for each outcome of type "doc" or "data" declared in the Meta PLC
    for that leaf.

    Outcome resolution rules:
      - If the "ref" field of the outcome starts with "PLC/", it is
        treated as a path relative to the project root:
          ref: "PLC/1_Discovery/1.1_Product_Vision/product_vision.md"
          => <root>/PLC/1_Discovery/1.1_Product_Vision/product_vision.md

      - Otherwise, it is treated as a path relative to the leaf directory:
          ref: "product_vision.md"
          => <leaf_dir>/product_vision.md

    Existing files are never overwritten by this flag; it only creates
    missing files.

--force            (flag, default: off)
    When provided, the script will **overwrite** existing README.md files
    for phases and leaves with freshly generated content from the Meta PLC.

    Behaviour summary:
      - Phase README.md:
          * overwritten if --force, otherwise created only if missing.
      - Leaf README.md:
          * overwritten if --force, otherwise created only if missing.
      - Outcome files (doc/data):
          * never overwritten, only created when missing (even with --force).

    Use this when you update the Meta PLC JSON and want to realign the
    leaf/phase README files to the new definitions.

EXIT CODES
----------
  0  Success
  2  Invalid arguments or missing paths (meta file or root dir not found)

TYPICAL USAGE
-------------
From the project root (PyCharm project directory):

  # Basic scaffold (phases/leaves + README.md), no placeholders
  python plc_scaffold_from_meta.py \
      --meta templates/meta_plc_1to3.json \
      --root . \
      --plc-dir PLC

  # Scaffold + create placeholder outcome files for docs/data
  python plc_scaffold_from_meta.py \
      --meta templates/meta_plc_1to3.json \
      --root . \
      --plc-dir PLC \
      --create-outcomes

  # Regenerate all README.md files after changing the Meta PLC
  python plc_scaffold_from_meta.py \
      --meta templates/meta_plc_1to3.json \
      --root . \
      --plc-dir PLC \
      --force
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from textwrap import dedent
from typing import Any, Dict, List, Tuple


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def slugify(name: str) -> str:
    """Turn a phase/leaf name into a filesystem-friendly slug."""
    s = re.sub(r"[^\w]+", "_", name.strip(), flags=re.IGNORECASE)
    s = re.sub(r"_+", "_", s).strip("_")
    return s or "item"


def write_file(path: Path, content: str, *, force: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        return
    path.write_text(content, encoding="utf-8")


def touch(path: Path, *, force: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        return
    path.write_text("", encoding="utf-8")


def format_inputs(inputs: List[Dict[str, Any]]) -> Tuple[List[str], List[str]]:
    """Split inputs into required / optional lines for the README."""
    req: List[str] = []
    opt: List[str] = []
    for item in inputs or []:
        t = item.get("type", "unknown")
        ref = item.get("ref", "")
        required = bool(item.get("required", False))
        line = f"- type={t}, ref={ref}"
        (req if required else opt).append(line)
    return req, opt


def format_outcomes(outcomes: List[Dict[str, Any]]) -> List[str]:
    lines: List[str] = []
    for item in outcomes or []:
        t = item.get("type", "unknown")
        ref = item.get("ref", "")
        required = bool(item.get("required", False))
        flag = "required" if required else "optional"
        lines.append(f"- [{flag}] type={t}, ref={ref}")
    return lines


def render_leaf_readme(phase: Dict[str, Any], leaf: Dict[str, Any]) -> str:
    """Generate README.md content for a leaf from meta PLC."""
    phase_id = phase.get("id", "")
    phase_name = phase.get("name", "")
    leaf_id = leaf.get("id", "")
    leaf_name = leaf.get("name", "")

    title = f"{leaf_id} {leaf_name}".strip()
    purpose = leaf.get("purpose", "").strip()
    description = leaf.get("description", "").strip()

    inputs = leaf.get("inputs", []) or []
    outcomes = leaf.get("outcomes", []) or []
    tools = leaf.get("tools", {}) or {}
    ai = leaf.get("ai_contract", {}) or {}

    req_inputs, opt_inputs = format_inputs(inputs)
    outcome_lines = format_outcomes(outcomes)

    methods = tools.get("methods", []) or []
    tools_list = tools.get("tools", []) or []
    templates = tools.get("templates", []) or []

    ai_enabled = bool(ai.get("enabled", False))
    ai_roles = ai.get("roles", []) or []
    ai_prompts = ai.get("prompt_ids", []) or []
    ai_input_docs = (ai.get("input_spec") or {}).get("documents", []) or []
    ai_input_data = (ai.get("input_spec") or {}).get("data", []) or []
    ai_output_docs = (ai.get("output_spec") or {}).get("documents", []) or []
    ai_output_data = (ai.get("output_spec") or {}).get("data", []) or []

    lines: List[str] = []

    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"_Phase {phase_id} — {phase_name}_")
    lines.append("")

    # 1. Purpose / Objective
    lines.append("## 1. Purpose / Objective")
    lines.append(purpose or "TBD.")
    lines.append("")

    # 2. Description
    lines.append("## 2. Description")
    lines.append(description or "TBD.")
    lines.append("")

    # 3. Input
    lines.append("## 3. Input")
    if req_inputs:
        lines.append("- **Required:**")
        lines.extend(req_inputs)
    else:
        lines.append("- **Required:** none explicitly defined.")
    if opt_inputs:
        lines.append("- **Optional:**")
        lines.extend(opt_inputs)
    lines.append("")

    # 4. Outcomes
    lines.append("## 4. Outcomes")
    if outcome_lines:
        lines.extend(outcome_lines)
    else:
        lines.append("- No outcomes defined yet in meta PLC.")
    lines.append("")

    # 5. Tools / Methodology
    lines.append("## 5. Tools / Methodology")
    if methods:
        lines.append("- **Methods:**")
        for m in methods:
            lines.append(f"  - {m}")
    if tools_list:
        lines.append("- **Tools:**")
        for t in tools_list:
            lines.append(f"  - {t}")
    if templates:
        lines.append("- **Templates:**")
        for tpl in templates:
            lines.append(f"  - {tpl}")
    if not (methods or tools_list or templates):
        lines.append("No specific methods/tools/templates registered yet in meta PLC.")
    lines.append("")

    # 6. AI Support / Symbiotic Role
    lines.append("## 6. AI Support / Symbiotic Role")
    if not ai_enabled:
        lines.append("AI support not explicitly defined for this leaf in the meta PLC.")
    else:
        if ai_roles:
            lines.append("- **Roles:**")
            for r in ai_roles:
                lines.append(f"  - {r}")
        if ai_prompts:
            lines.append("- **Prompt contracts:**")
            for pid in ai_prompts:
                lines.append(f"  - `{pid}`")

        if ai_input_docs or ai_input_data:
            lines.append("- **Input context:**")
            for d in ai_input_docs:
                lines.append(f"  - doc: {d}")
            for d in ai_input_data:
                lines.append(f"  - data: {d}")

        if ai_output_docs or ai_output_data:
            lines.append("- **Expected outputs (AI-assisted):**")
            for d in ai_output_docs:
                lines.append(f"  - doc: {d}")
            for d in ai_output_data:
                lines.append(f"  - data: {d}")

    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------------

def scaffold_from_meta(
    meta_path: Path,
    root: Path,
    plc_dir_name: str,
    *,
    create_outcomes: bool,
    force: bool,
) -> None:
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    meta_plc = meta.get("meta_plc") or meta

    phases = meta_plc.get("phases", [])
    plc_root = root / plc_dir_name
    plc_root.mkdir(parents=True, exist_ok=True)

    created: List[Path] = []

    for phase in phases:
        phase_id = str(phase.get("id", "")).strip()
        phase_name = str(phase.get("name", "")).strip() or "Phase"
        phase_dir = phase.get("dir") or f"{phase_id}_{slugify(phase_name)}"
        phase_path = plc_root / phase_dir
        phase_path.mkdir(parents=True, exist_ok=True)

        # Optional phase-level README
        phase_readme = phase_path / "README.md"
        if not phase_readme.exists() or force:
            desc = phase.get("description", "").strip()
            content = dedent(f"""\
            # {phase_id} {phase_name}

            {desc or "TBD: phase description."}

            This folder contains all PLC leaves for this phase.
            """)
            write_file(phase_readme, content, force=True)
            created.append(phase_readme)

        for leaf in phase.get("leaves", []):
            leaf_id = str(leaf.get("id", "")).strip()
            leaf_name = str(leaf.get("name", "")).strip() or "Leaf"
            leaf_dir = leaf.get("dir") or f"{leaf_id}_{slugify(leaf_name)}"
            leaf_path = phase_path / leaf_dir
            leaf_path.mkdir(parents=True, exist_ok=True)

            # Leaf README
            readme_path = leaf_path / "README.md"
            content = render_leaf_readme(phase, leaf)
            write_file(readme_path, content, force=force)
            created.append(readme_path)

            # Optional: create outcome files (empty placeholders)
            if create_outcomes:
                for outcome in leaf.get("outcomes", []) or []:
                    ref = outcome.get("ref")
                    if not ref:
                        continue
                    ref_path = Path(ref)
                    if str(ref_path).startswith("PLC/"):
                        out_path = root / ref_path
                    else:
                        out_path = leaf_path / ref_path
                    if outcome.get("type") in {"doc", "data"}:
                        touch(out_path, force=False)
                        created.append(out_path)

    print(f"[OK] PLC scaffold generated under: {plc_root}")
    if created:
        print("Created/updated:")
        for p in created:
            rel = p.relative_to(root)
            print(f"  - {rel}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="Generate PLC/ folder structure from a Meta PLC JSON definition."
    )
    ap.add_argument("--meta", required=True, help="Path to meta_plc.json")
    ap.add_argument("--root", default=".", help="Project root (PyCharm project root)")
    ap.add_argument("--plc-dir", default="PLC", help="Relative PLC root directory name")
    ap.add_argument(
        "--create-outcomes",
        action="store_true",
        help="Create empty files for doc/data outcomes defined in meta_plc.json",
    )
    ap.add_argument(
        "--force",
        action="store_true",
        help="Overwrite README.md files if they already exist.",
    )

    args = ap.parse_args(argv)

    meta_path = Path(args.meta).resolve()
    root = Path(args.root).resolve()

    if not meta_path.is_file():
        print(f"[ERROR] Meta PLC file not found: {meta_path}", file=sys.stderr)
        return 2
    if not root.is_dir():
        print(f"[ERROR] Project root is not a directory: {root}", file=sys.stderr)
        return 2

    scaffold_from_meta(
        meta_path=meta_path,
        root=root,
        plc_dir_name=args.plc_dir,  # <-- fixed here
        create_outcomes=args.create_outcomes,
        force=args.force,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

