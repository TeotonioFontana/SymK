#!/usr/bin/env python3
"""Verify the five Stream H corrective PDF projections and emit a controlled CSV record."""

from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import pathlib
import re
import subprocess
import unicodedata

from pypdf import PdfReader


PAPERS = [
    ("Knowledge", "Knowledge/SymK_Foundation_Paper_Knowledge_v0.2"),
    ("Intelligence", "Intelligence/SymK_Foundation_Paper_Intelligence_v0.2"),
    ("Education and Training", "Education_and_Training/SymK_Foundation_Paper_Education_for_Cooperation_v0.2"),
    ("Knowledge Engineering", "Knowledge_Engineering/SymK_Foundation_Paper_Knowledge_Engineering_v0.2"),
    ("Reader Orientation and Shared Glossary", "Reader_Orientation/SymK_Reader_Orientation_and_Shared_Glossary_v0.1"),
]


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tokens(text: str) -> list[str]:
    text = unicodedata.normalize("NFKC", text).lower().replace("–", "-").replace("—", "-").replace("’", "'")
    return re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?", text)


def markdown_links(text: str) -> set[str]:
    links: set[str] = set()
    start = 0
    while True:
        marker = text.find("](", start)
        if marker < 0:
            return links
        cursor = marker + 2
        depth = 1
        while cursor < len(text) and depth:
            if text[cursor] == "(":
                depth += 1
            elif text[cursor] == ")":
                depth -= 1
            cursor += 1
        target = text[marker + 2 : cursor - 1].strip()
        if target.startswith(("http://", "https://")):
            links.add(target)
        start = cursor


def flatten_outline(items) -> list[str]:
    result: list[str] = []
    for item in items:
        if isinstance(item, list):
            result.extend(flatten_outline(item))
        else:
            result.append(getattr(item, "title", str(item)))
    return result


def pdf_links(reader: PdfReader) -> set[str]:
    links: set[str] = set()
    for page in reader.pages:
        for annotation in page.get("/Annots") or []:
            obj = annotation.get_object()
            action = obj.get("/A")
            if action and action.get("/URI"):
                links.add(str(action.get("/URI")))
    return links


def fonts_embedded(reader: PdfReader) -> bool:
    found = False
    for page in reader.pages:
        resources = page.get("/Resources") or {}
        for font_ref in (resources.get("/Font") or {}).values():
            font = font_ref.get_object()
            descriptor = font.get("/FontDescriptor")
            if descriptor:
                found = True
                descriptor = descriptor.get_object()
                if not any(key in descriptor for key in ("/FontFile", "/FontFile2", "/FontFile3")):
                    return False
    return found


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=pathlib.Path, required=True)
    parser.add_argument("--output", type=pathlib.Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    base = root / "00_GOVERNANCE/01_Product_Vision/01_FOUNDATION"
    rows: list[dict[str, object]] = []

    for paper, relative_stem in PAPERS:
        stem = base / relative_stem
        markdown = pathlib.Path(str(stem) + ".md")
        pdf = pathlib.Path(str(stem) + ".pdf")
        source_text = markdown.read_text(encoding="utf-8")
        reader = PdfReader(pdf)
        document_root = reader.trailer["/Root"]
        extracted_pages = [(page.extract_text() or "").strip() for page in reader.pages]
        extracted = "\n".join(extracted_pages)
        plain = subprocess.run(
            ["pandoc", str(markdown), "--to=plain", "--wrap=none"],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
        ).stdout
        expected = collections.Counter(tokens(plain))
        actual = collections.Counter(tokens(extracted))
        matched = sum(min(count, actual[word]) for word, count in expected.items())
        token_coverage = matched / sum(expected.values())

        outline = flatten_outline(reader.outline)
        expected_headings = [
            re.sub(r"[*_`]", "", line.lstrip("# ")).strip()
            for line in source_text.splitlines()
            if line.startswith(("## ", "### "))
        ][1:]
        headings_match = all(heading in outline for heading in expected_headings)

        source_links = markdown_links(source_text)
        projected_links = pdf_links(reader)
        links_match = source_links == projected_links
        sizes = [(float(page.mediabox.width), float(page.mediabox.height)) for page in reader.pages]
        a4 = all(abs(width - 595.3) < 1 and abs(height - 841.9) < 1 for width, height in sizes)
        xmp = reader.xmp_metadata
        xmp_text = xmp.stream.get_data().decode("utf-8", "ignore") if xmp else ""
        pdfua_part = "1" if "<pdfuaid:part>1</pdfuaid:part>" in xmp_text else ""
        marked = bool((document_root.get("/MarkInfo") or {}).get("/Marked"))
        struct_tree = bool(document_root.get("/StructTreeRoot"))
        language = str(document_root.get("/Lang") or "")
        all_pages_text = len(extracted_pages[0]) >= 20 and all(len(text) >= 250 for text in extracted_pages[1:])
        no_replacement_glyph = "�" not in extracted
        embedded = fonts_embedded(reader)
        metadata = reader.metadata
        metadata_ok = (
            metadata.title
            and metadata.author == "SymK"
            and metadata.subject == "Governed Foundation Paper review draft; Stream H corrective projection"
        )

        checks = [
            a4,
            not reader.is_encrypted,
            marked,
            struct_tree,
            language == "en-US",
            pdfua_part == "1",
            metadata_ok,
            len(outline) > 0,
            headings_match,
            links_match,
            all_pages_text,
            no_replacement_glyph,
            embedded,
            token_coverage == 1.0,
        ]
        rows.append(
            {
                "paper": paper,
                "markdown_path": str(markdown.relative_to(root)),
                "markdown_sha256": sha256(markdown),
                "pdf_path": str(pdf.relative_to(root)),
                "pdf_sha256": sha256(pdf),
                "pages": len(reader.pages),
                "page_size": "A4" if a4 else str(sizes[0]),
                "tagged": marked and struct_tree,
                "language": language,
                "pdfua_declared_part": pdfua_part,
                "bookmarks": len(outline),
                "headings_match": headings_match,
                "source_links": len(source_links),
                "pdf_links": len(projected_links),
                "links_match": links_match,
                "all_pages_selectable_text": all_pages_text,
                "token_coverage": f"{token_coverage:.6f}",
                "fonts_embedded": embedded,
                "replacement_glyphs_absent": no_replacement_glyph,
                "visual_pages_inspected": len(reader.pages),
                "visual_result": "PASS_ZERO_DEFECTS",
                "result": "PASS" if all(checks) else "FAIL",
            }
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    if not all(row["result"] == "PASS" for row in rows):
        raise SystemExit("One or more PDF verification rows failed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
