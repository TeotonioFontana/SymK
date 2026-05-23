# -*- coding: utf-8 -*-
"""
Shared utilities for symk-project-init:
- time helpers
- name slugification
- filesystem helpers
- reporting of created files
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict


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


def as_dict(obj) -> Dict:
    """Tiny helper for type hints; not used yet but handy if needed."""
    if isinstance(obj, dict):
        return obj
    return dict(obj)
