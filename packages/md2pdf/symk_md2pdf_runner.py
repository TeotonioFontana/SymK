#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
symk_md2pdf_runner.py — Use md2pdf to render a Markdown manual to PDF
with a simple white-book style.

Usage:
    python symk_md2pdf_runner.py input.md output.pdf [--css symk_whitebook.css]

Requirements:
    pip install md2pdf weasyprint

Notes:
    - This is a thin wrapper around md2pdf.core.md2pdf so you can keep the
      conversion deterministic and scriptable inside your toolchain.
"""

import argparse
from pathlib import Path

from md2pdf.core import md2pdf


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert Markdown to PDF using md2pdf with optional CSS."
    )
    parser.add_argument("input_md", help="Path to the input Markdown file.")
    parser.add_argument("output_pdf", help="Path to the output PDF file.")
    parser.add_argument(
        "--css",
        help="Optional CSS file to control layout (e.g., symk_whitebook.css).",
        default=None,
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    md_path = Path(args.input_md)
    if not md_path.is_file():
        raise SystemExit(f"Input Markdown file not found: {md_path}")

    pdf_path = Path(args.output_pdf)
    css_path = Path(args.css) if args.css else None

    # base_url ensures relative links (images, etc.) resolve correctly
    base_url = str(md_path.parent.resolve())

    md2pdf(
        pdf_file_path=str(pdf_path),
        md_file_path=str(md_path),
        css_file_path=str(css_path) if css_path else None,
        base_url=base_url,
    )

    print(f"PDF written to: {pdf_path}")


if __name__ == "__main__":
    main()
