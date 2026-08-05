# -*- coding: utf-8 -*-
"""
===============================================================================
 python_init.py — SymK Python Script Header Generator
===============================================================================
 Version.............: v0.1.0-alpha
 Author..............: Teotoniio Fontana — Architect
 Programmed by.......: Duke (GPT-5.1 Thinking, OpenAI)
 Project.............: SymK Devkit / Tools
-------------------------------------------------------------------------------
 Description
 ------------------------------------------------------------------------------
 Generate a standardized Python script heading docstring from a JSON
 specification. This is the first building block for SymK-compliant
 Python script initialization.

 For now:
   • Load a script specification from JSON
   • Render a header docstring with the official layout
   • Print to stdout or write to a target file

 Later:
   • Integrate with project_init
   • Auto-insert/patch headers in existing Python files
   • Enforce versioning / change-log consistency
===============================================================================
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from textwrap import dedent
from typing import Any, Dict, Iterable, List, Mapping, Optional

DOC_BORDER = "=" * 79
SECTION_BORDER = "-" * 79


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------
def _ensure_list(value: Any) -> List[str]:
    """Normalize value into a list of strings."""
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    return [str(v) for v in value]


def _fmt_field(label: str, value: str, width: int = 21) -> str:
    """
    Format a header field as:
      ' Label.............: value'
    Width controls the total length of label + dots before ':'.
    """
    label = label.strip()
    dots = "." * max(1, width - len(label))
    return f" {label}{dots}: {value}"


def load_spec(path: Path) -> Dict[str, Any]:
    """Load and minimally validate a script spec JSON file."""
    data = json.loads(path.read_text(encoding="utf-8"))

    required = [
        "module_name",
        "short_purpose",
        "version",
        "author",
        "programmed_by",
        "project",
    ]
    missing = [k for k in required if k not in data]
    if missing:
        raise ValueError(f"Missing required keys in spec: {', '.join(missing)}")

    return data


# ---------------------------------------------------------------------------
# Header rendering
# ---------------------------------------------------------------------------
def render_script_header(spec: Mapping[str, Any]) -> str:
    """
    Render a full Python header docstring from a spec dict.

    Expected keys (JSON):
      - module_name: str (e.g., "orchestrator.py")
      - short_purpose: str (short human title)
      - version: str (e.g., "v0.7.7-alpha")
      - author: str
      - programmed_by: str
      - project: str
      - layer_context: str (optional, defaults to "-")
      - description: str | [str, ...]
      - responsibilities: [str, ...] (optional)
      - inputs: [str, ...] (optional)
      - outputs: [str, ...] (optional)
      - change_log: [
            {
              "version": "v0.7.7-alpha",
              "items": ["...", "..."]
            },
            ...
        ] (optional)
    """
    module_name = str(spec["module_name"])
    short_purpose = str(spec["short_purpose"])
    version = str(spec["version"])
    author = str(spec["author"])
    programmed_by = str(spec["programmed_by"])
    project = str(spec["project"])
    layer_context = str(spec.get("layer_context", "-"))

    description_lines = _ensure_list(spec.get("description"))
    responsibilities = _ensure_list(spec.get("responsibilities"))
    inputs = _ensure_list(spec.get("inputs"))
    outputs = _ensure_list(spec.get("outputs"))
    change_log = spec.get("change_log") or []

    lines: List[str] = []

    # Top block
    lines.append(DOC_BORDER)
    lines.append(f" {module_name} — {short_purpose}")
    lines.append(DOC_BORDER)
    lines.append(_fmt_field("Version", version))
    lines.append(_fmt_field("Author", author))
    lines.append(_fmt_field("Programmed by", programmed_by))
    lines.append(_fmt_field("Project", project))
    lines.append(_fmt_field("Layer/Context", layer_context))
    lines.append(SECTION_BORDER)

    # Description
    lines.append(" Description")
    lines.append(f" {SECTION_BORDER}")
    if description_lines:
        for line in description_lines:
            lines.append(f" {line}")
    else:
        lines.append(" (no description provided)")
    lines.append("")

    # Responsibilities
    if responsibilities:
        lines.append(SECTION_BORDER)
        lines.append(" Responsibilities")
        lines.append(f" {SECTION_BORDER}")
        for item in responsibilities:
            lines.append(f" - {item}")
        lines.append("")

    # Inputs / Outputs
    if inputs or outputs:
        lines.append(SECTION_BORDER)
        lines.append(" Inputs & Outputs")
        lines.append(f" {SECTION_BORDER}")

        if inputs:
            lines.append(" Inputs:")
            for item in inputs:
                lines.append(f"   - {item}")
        if outputs:
            if inputs:
                lines.append("")  # blank line between sections
            lines.append(" Outputs:")
            for item in outputs:
                lines.append(f"   - {item}")
        lines.append("")

    # Change log
    if change_log:
        lines.append(SECTION_BORDER)
        lines.append(" Change Log")
        lines.append(f" {SECTION_BORDER}")
        for entry in change_log:
            v = str(entry.get("version", "")).strip()
            items = _ensure_list(entry.get("items"))
            if v:
                lines.append(f" {v}:")
            else:
                lines.append(" (version unspecified):")
            for item in items:
                lines.append(f"   • {item}")
        lines.append(DOC_BORDER)
    else:
        # Close if there is no change log section
        lines.append(DOC_BORDER)

    # Wrap into a Python docstring
    header = '"""\\n' + "\n".join(lines) + '\\n"""'
    return header


# ---------------------------------------------------------------------------
# Spec template / scaffold
# ---------------------------------------------------------------------------
def default_spec_template() -> Dict[str, Any]:
    """Return a generic spec template with placeholder values."""
    return {
        "module_name": "module.py",
        "short_purpose": "Short one-line purpose",
        "version": "v0.1.0-alpha",
        "author": "Teotoniio Fontana — Architect",
        "programmed_by": "Duke (GPT-5.1 Thinking, OpenAI)",
        "project": "SymK / Your Project",
        "layer_context": "Layer / Context (e.g., CLI Orchestrator, Adapter, Core Helper)",
        "description": [
            "One or more lines describing what this script does.",
            "Keep it high-level and focused on responsibilities, not implementation details.",
        ],
        "responsibilities": [
            "Responsibility 1",
            "Responsibility 2",
        ],
        "inputs": [
            "Input 1 (e.g., CLI flags, config files, env vars)",
        ],
        "outputs": [
            "Output 1 (e.g., logs, files, stdout, DB writes)",
        ],
        "change_log": [
            {
                "version": "v0.1.0-alpha",
                "items": [
                    "Initial version generated from SymK python_init template.",
                ],
            }
        ],
    }


def write_spec_template(path: Path, *, force: bool = False) -> None:
    """Write a default script spec template JSON."""
    if path.exists() and not force:
        raise SystemExit(f"[ERROR] Spec file already exists: {path} (use --force to overwrite)")
    path.parent.mkdir(parents=True, exist_ok=True)
    data = default_spec_template()
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"[OK] Wrote script spec template to: {path}")


def write_header(path: Path, header: str, *, force: bool = False) -> None:
    """
    Write the rendered header to a file.

    For now this simply writes the header as-is. Later we can add modes like:
      - 'insert' (prepend to existing file)
      - 'patch'  (replace existing header block)
    """
    if path.exists() and not force:
        raise SystemExit(f"[ERROR] Target file already exists: {path} (use --force to overwrite)")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(header + "\n", encoding="utf-8")
    print(f"[OK] Wrote header to: {path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="python_init",
        description="Generate SymK-style Python script headers from JSON specs.",
    )

    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--spec",
        help="Path to a JSON script specification to render into a header docstring.",
    )
    group.add_argument(
        "--init-spec",
        help="Path to write a template script specification JSON, then exit.",
    )

    p.add_argument(
        "--out",
        help="Optional output file path. If omitted, header is printed to stdout.",
    )
    p.add_argument(
        "--force",
        action="store_true",
        help="Allow overwriting existing files (spec or header).",
    )

    return p


def main(argv: Optional[Iterable[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.init_spec:
        write_spec_template(Path(args.init_spec), force=args.force)
        return 0

    # Normal mode: render header from spec
    spec_path = Path(args.spec)
    spec = load_spec(spec_path)
    header = render_script_header(spec)

    if args.out:
        write_header(Path(args.out), header, force=args.force)
    else:
        print(header)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
