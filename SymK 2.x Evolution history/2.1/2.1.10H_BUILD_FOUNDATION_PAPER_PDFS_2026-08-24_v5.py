#!/usr/bin/env python3
"""Build the coordinated SymK Foundation Paper v0.3 review set as accessible PDF projections."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Mm, Pt, RGBColor
from docx.text.paragraph import Paragraph


PAPERS = [
    {
        "key": "knowledge",
        "source": "00_GOVERNANCE/01_Product_Vision/01_FOUNDATION/Knowledge/SymK_Foundation_Paper_Knowledge_v0.3.md",
        "output": "00_GOVERNANCE/01_Product_Vision/01_FOUNDATION/Knowledge/SymK_Foundation_Paper_Knowledge_v0.3.pdf",
        "title": "Knowledge as the Shared Epistemic Medium",
        "subtitle": "How claims become challengeable, scoped and fit for responsible reliance",
        "accent": "176B87",
    },
    {
        "key": "intelligence",
        "source": "00_GOVERNANCE/01_Product_Vision/01_FOUNDATION/Intelligence/SymK_Foundation_Paper_Intelligence_v0.3.md",
        "output": "00_GOVERNANCE/01_Product_Vision/01_FOUNDATION/Intelligence/SymK_Foundation_Paper_Intelligence_v0.3.pdf",
        "title": "Intelligence Beyond the Human",
        "subtitle": "Capability without human resemblance, rank or automatic authority",
        "accent": "6A4C93",
    },
    {
        "key": "education",
        "source": "00_GOVERNANCE/01_Product_Vision/01_FOUNDATION/Education_and_Training/SymK_Foundation_Paper_Education_for_Cooperation_v0.3.md",
        "output": "00_GOVERNANCE/01_Product_Vision/01_FOUNDATION/Education_and_Training/SymK_Foundation_Paper_Education_for_Cooperation_v0.3.pdf",
        "title": "Formation, Education, and Training in SymK",
        "subtitle": "How durable change, Learning, Training and Education remain distinct",
        "accent": "A14C33",
    },
    {
        "key": "knowledge_engineering",
        "source": "00_GOVERNANCE/01_Product_Vision/01_FOUNDATION/Knowledge_Engineering/SymK_Foundation_Paper_Knowledge_Engineering_v0.3.md",
        "output": "00_GOVERNANCE/01_Product_Vision/01_FOUNDATION/Knowledge_Engineering/SymK_Foundation_Paper_Knowledge_Engineering_v0.3.pdf",
        "title": "Engineering Epistemic Conditions",
        "subtitle": "Designing conditions for inquiry without pretending to manufacture truth",
        "accent": "2F6F5E",
    },
    {
        "key": "reader_orientation",
        "source": "00_GOVERNANCE/01_Product_Vision/01_FOUNDATION/Reader_Orientation/SymK_Reader_Orientation_and_Shared_Glossary_v0.3.md",
        "output": "00_GOVERNANCE/01_Product_Vision/01_FOUNDATION/Reader_Orientation/SymK_Reader_Orientation_and_Shared_Glossary_v0.3.pdf",
        "title": "SymK Reader Orientation and Shared Glossary",
        "subtitle": "A plain-language map of the Foundation Paper set",
        "cover_call": "SymK is a general framework and engineering discipline for responsible Knowledge Engineering through governed cooperation among different forms and Bearers of Intelligence. It calls us to engineer the conditions in which difficult questions can produce scoped, evidence-grounded, challengeable and revisable knowledge work - while never confusing information with Knowledge, performance with Intelligence, capability with Authority, cooperation with legitimacy, or a successful outcome with proof.",
        "cover_outcome": "The principal practical result SymK is intended to enable is a class of governed, domain-centred, knowledge-intensive systems - principally Domain Intelligence Amplifiers - in which qualified people, AI and other participants cooperate through governed domain Knowledge to answer complex questions. LexBrain is one concrete derived-project example: a legal-domain knowledge system shaped by SymK, not SymK itself.",
        "accent": "176B87",
    },
]


def run(command: list[str], *, cwd: pathlib.Path, log: pathlib.Path | None = None) -> str:
    result = subprocess.run(command, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if log is not None:
        log.write_text(result.stdout, encoding="utf-8")
    if result.returncode:
        raise RuntimeError(f"Command failed ({result.returncode}): {' '.join(command)}\n{result.stdout}")
    return result.stdout


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def publication_markdown(source: pathlib.Path, paper: dict[str, str]) -> str:
    text = source.read_text(encoding="utf-8")
    lines = text.splitlines()
    # The first H1 and first H2 are projected through PDF title metadata. Their
    # exact text is retained there, avoiding a duplicate title in the body.
    removed = 0
    body: list[str] = []
    for line in lines:
        if removed == 0 and line.startswith("# "):
            removed += 1
            continue
        if removed == 1 and line.startswith("## "):
            removed += 1
            continue
        body.append(line)
    if removed != 2:
        raise ValueError(f"Expected title and subtitle headings in {source}")

    # Wide source tables are projected as stacked labelled records. This keeps
    # every header and cell in reading order, avoids A4 clipping, and remains a
    # publication-only transformation: the governed Markdown is untouched.
    projected_body: list[str] = []
    index = 0

    def cells(line: str) -> list[str]:
        return [cell.strip() for cell in line.strip().strip("|").split("|")]

    def is_separator(line: str) -> bool:
        parts = cells(line)
        return bool(parts) and all(re.fullmatch(r":?-{3,}:?", part) for part in parts)

    while index < len(body):
        if (
            body[index].lstrip().startswith("|")
            and index + 1 < len(body)
            and is_separator(body[index + 1])
        ):
            table_lines = [body[index]]
            index += 2
            while index < len(body) and body[index].lstrip().startswith("|"):
                table_lines.append(body[index])
                index += 1

            headers = cells(table_lines[0])
            projected_body.extend(
                [
                    "> **Accessible table projection:** Each source row follows as a labelled record; all source headers and cell wording are preserved.",
                    "",
                ]
            )
            for row_line in table_lines[1:]:
                row = cells(row_line)
                row += [""] * (len(headers) - len(row))
                projected_body.append(f"- **{headers[0]}:** {row[0]}")
                for header, value in zip(headers[1:], row[1:]):
                    projected_body.append(f"  - **{header}:** {value}")
            projected_body.append("")
            continue
        projected_body.append(body[index])
        index += 1

    contents = []
    skipped_subtitle = False
    for line in lines:
        if line.startswith("## "):
            heading = re.sub(r"[*_]", "", line[3:]).strip()
            if not skipped_subtitle:
                skipped_subtitle = True
                continue
            numbered = re.match(r"(\\d+)\\.\\s+(.*)", heading)
            if numbered:
                heading = f"Section {numbered.group(1)} - {numbered.group(2)}"
            if heading:
                contents.append(f"- {heading}")

    yaml = [
        "---",
        f'title: "{paper["title"]}"',
        f'subtitle: "{paper["subtitle"]}"',
        'author: "SymK"',
        'date: "24 August 2026"',
        'lang: "en-US"',
        'subject: "Governed Foundation Paper v0.3 review draft; Stream H projection"',
        'keywords: [SymK, Foundation Paper, Knowledge Engineering, governed review draft]',
        "---",
        "",
        "## Contents",
        "",
        *contents,
        "",
        "---",
        "",
        "> **Publication status:** Coordinated v0.3 Stream H review projection. Human reread, newcomer testing and publication acceptance remain pending.",
        "",
    ]
    return "\n".join(yaml + projected_body) + "\n"


def add_page_field(paragraph) -> None:
    run_element = paragraph.add_run()._r
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instruction = OxmlElement("w:instrText")
    instruction.set(qn("xml:space"), "preserve")
    instruction.text = " PAGE "
    separate = OxmlElement("w:fldChar")
    separate.set(qn("w:fldCharType"), "separate")
    display = OxmlElement("w:t")
    display.text = "1"
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    for element in (begin, instruction, separate, display, end):
        run_element.append(element)


def set_font(style, name: str, size: float, color: str | None = None, bold: bool | None = None) -> None:
    style.font.name = name
    style.font.size = Pt(size)
    if color:
        style.font.color.rgb = RGBColor.from_string(color)
    if bold is not None:
        style.font.bold = bold


def create_reference_docx(path: pathlib.Path, accent: str, root: pathlib.Path, paper_key: str) -> None:
    default = subprocess.run(
        ["pandoc", "--print-default-data-file", "reference.docx"],
        cwd=root,
        check=True,
        stdout=subprocess.PIPE,
    ).stdout
    path.write_bytes(default)
    document = Document(path)
    section = document.sections[0]
    section.page_width = Mm(210)
    section.page_height = Mm(297)
    section.top_margin = Mm(21)
    section.bottom_margin = Mm(20)
    section.left_margin = Mm(21)
    section.right_margin = Mm(21)
    section.header_distance = Mm(8)
    section.footer_distance = Mm(9)
    section.different_first_page_header_footer = True

    styles = document.styles
    set_font(styles["Normal"], "Liberation Serif", 10.5, "17242B")
    styles["Normal"].paragraph_format.space_after = Pt(5)
    styles["Normal"].paragraph_format.line_spacing = 1.08
    set_font(styles["Title"], "Liberation Sans", 26, accent, True)
    styles["Title"].paragraph_format.space_before = Pt(82)
    styles["Title"].paragraph_format.space_after = Pt(14)
    set_font(styles["Subtitle"], "Liberation Sans", 16, "53636B")
    styles["Subtitle"].paragraph_format.space_after = Pt(26)
    set_font(styles["Author"], "Liberation Sans", 10, "53636B")
    set_font(styles["Date"], "Liberation Sans", 9.5, "53636B")
    for name, size in {"Heading 1": 18, "Heading 2": 14, "Heading 3": 11.5, "Heading 4": 10.5}.items():
        if name in styles:
            set_font(styles[name], "Liberation Sans", size, accent, True)
            styles[name].paragraph_format.keep_with_next = True
            styles[name].paragraph_format.space_before = Pt(12 if name == "Heading 1" else 8)
            styles[name].paragraph_format.space_after = Pt(4)
    for name in ("Body Text", "First Paragraph", "Block Text", "List Paragraph"):
        if name in styles:
            set_font(styles[name], "Liberation Serif", 10.5, "17242B")
            styles[name].paragraph_format.space_after = Pt(5)
            styles[name].paragraph_format.line_spacing = 1.08
    # The two reference-heavy papers otherwise leave a single governance-note
    # paragraph stranded on a nearly empty final page. A small list-spacing
    # adjustment keeps the publication balanced without changing source text.
    if paper_key in {"knowledge", "knowledge_engineering"} and "List Paragraph" in styles:
        styles["List Paragraph"].paragraph_format.space_after = Pt(4)
    for name in ("Source Code", "Verbatim Char"):
        if name in styles:
            set_font(styles[name], "DejaVu Sans Mono", 8.5, "17242B")
    if "Hyperlink" in styles:
        set_font(styles["Hyperlink"], "Liberation Sans", 9.5, accent)

    header = section.header
    paragraph = header.paragraphs[0]
    paragraph.clear()
    paragraph.paragraph_format.tab_stops.add_tab_stop(Mm(168), WD_TAB_ALIGNMENT.RIGHT)
    left = paragraph.add_run("SymK Foundation Papers - Human Review")
    left.bold = True
    left.font.name = "Liberation Sans"
    left.font.size = Pt(8.5)
    left.font.color.rgb = RGBColor.from_string(accent)
    right = paragraph.add_run("\tStream H corrective projection")
    right.font.name = "Liberation Sans"
    right.font.size = Pt(8.5)
    right.font.color.rgb = RGBColor.from_string("53636B")

    footer_paragraph = section.footer.paragraphs[0]
    footer_paragraph.clear()
    footer_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_page_field(footer_paragraph)
    for footer_run in footer_paragraph.runs:
        footer_run.font.name = "Liberation Sans"
        footer_run.font.size = Pt(8.5)
        footer_run.font.color.rgb = RGBColor.from_string("53636B")

    document.save(path)


def separate_cover_from_contents(path: pathlib.Path, paper: dict[str, str]) -> pathlib.Path:
    document = Document(path)
    subtitle = next((p for p in document.paragraphs if p.style and p.style.name == "Subtitle"), None)
    cover_call = paper.get("cover_call")
    cover_outcome = paper.get("cover_outcome")
    if subtitle is not None and cover_call:
        call = OxmlElement("w:p")
        subtitle._p.addnext(call)
        paragraph = Paragraph(call, subtitle._parent)
        paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
        paragraph.paragraph_format.left_indent = Mm(18)
        paragraph.paragraph_format.right_indent = Mm(18)
        paragraph.paragraph_format.space_before = Pt(4)
        paragraph.paragraph_format.space_after = Pt(8 if cover_outcome else 20)
        paragraph.paragraph_format.line_spacing = 1.12
        run = paragraph.add_run(cover_call)
        run.font.name = "Liberation Serif"
        run.font.size = Pt(11.5)
        run.font.color.rgb = RGBColor.from_string("17242B")
        if cover_outcome:
            outcome_element = OxmlElement("w:p")
            call.addnext(outcome_element)
            outcome_paragraph = Paragraph(outcome_element, subtitle._parent)
            outcome_paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
            outcome_paragraph.paragraph_format.left_indent = Mm(18)
            outcome_paragraph.paragraph_format.right_indent = Mm(18)
            outcome_paragraph.paragraph_format.space_after = Pt(18)
            outcome_paragraph.paragraph_format.line_spacing = 1.12
            outcome_run = outcome_paragraph.add_run(cover_outcome)
            outcome_run.font.name = "Liberation Serif"
            outcome_run.font.size = Pt(10.5)
            outcome_run.font.color.rgb = RGBColor.from_string("176B87")
    for paragraph in document.paragraphs:
        style_name = paragraph.style.name if paragraph.style else ""
        if style_name == "Date":
            paragraph.add_run().add_break(WD_BREAK.PAGE)
            break
    if paper["key"] in {"knowledge", "knowledge_engineering"}:
        in_references = False
        for paragraph in document.paragraphs:
            label = paragraph.text.strip()
            if label == "References":
                in_references = True
                continue
            if label == "Document governance note":
                in_references = False
            if in_references:
                paragraph.paragraph_format.space_after = Pt(1.5)
                paragraph.paragraph_format.line_spacing = 1.0
                for run in paragraph.runs:
                    run.font.size = Pt(9.5)
    enhanced = path.with_name(path.stem + ".enhanced.docx")
    document.save(enhanced)
    return enhanced


def build(root: pathlib.Path, work: pathlib.Path, *, resume: bool = False, key: str | None = None) -> None:
    work.mkdir(parents=True, exist_ok=True)
    os.environ["XDG_CACHE_HOME"] = str(work / "xdg-cache")
    lo_profile = work / "lo-profile"
    lo_output = work / "lo-output"
    lo_output.mkdir(parents=True, exist_ok=True)
    filter_options = (
        'pdf:writer_pdf_Export:{"UseTaggedPDF":{"type":"boolean","value":"true"},'
        '"PDFUACompliance":{"type":"boolean","value":"true"},'
        '"ExportBookmarks":{"type":"boolean","value":"true"},'
        '"ExportBookmarksToPDFDestination":{"type":"boolean","value":"true"}}'
    )

    manifest: list[dict[str, object]] = []
    papers = [paper for paper in PAPERS if key is None or paper["key"] == key]
    if key is not None and not papers:
        raise ValueError(f"Unknown paper key: {key}")
    for paper in papers:
        source = root / paper["source"]
        output = root / paper["output"]
        output.parent.mkdir(parents=True, exist_ok=True)
        md_path = work / f'{paper["key"]}.publication.md'
        reference_path = work / f'{paper["key"]}.reference.docx'
        docx_path = work / pathlib.Path(paper["output"]).with_suffix(".docx").name
        pandoc_log = work / f'{paper["key"]}.pandoc-docx.log'
        lo_log = work / f'{paper["key"]}.libreoffice.log'
        md_path.write_text(publication_markdown(source, paper), encoding="utf-8")

        if not (resume and output.exists() and pandoc_log.exists() and lo_log.exists()):
            create_reference_docx(reference_path, paper["accent"], root, paper["key"])
            run(
                [
                    "pandoc",
                    str(md_path),
                    "--from=gfm+smart",
                    "--to=docx",
                    f"--reference-doc={reference_path}",
                    f"--output={docx_path}",
                ],
                cwd=root,
                log=pandoc_log,
            )
            docx_path = separate_cover_from_contents(docx_path, paper)
            converted = lo_output / docx_path.with_suffix(".pdf").name
            run(
                [
                    "soffice",
                    "--headless",
                    f"-env:UserInstallation=file://{lo_profile}",
                    "--convert-to",
                    filter_options,
                    "--outdir",
                    str(lo_output),
                    str(docx_path),
                ],
                cwd=root,
                log=lo_log,
            )
            if not converted.exists():
                raise RuntimeError(f"LibreOffice did not create {converted}")
            shutil.copy2(converted, output)

        manifest.append(
            {
                "key": paper["key"],
                "source": paper["source"],
                "source_sha256": sha256(source),
                "projection_markdown": str(md_path.relative_to(work.parent)),
                "intermediate_docx": str(docx_path.relative_to(work.parent)),
                "output": paper["output"],
                "output_sha256": sha256(output),
                "pandoc_log": str(pandoc_log.relative_to(work.parent)),
                "libreoffice_log": str(lo_log.relative_to(work.parent)),
            }
        )

    toolchain = {
        "pandoc": run(["pandoc", "--version"], cwd=root).splitlines()[0],
        "libreoffice": run(["soffice", "--version"], cwd=root).strip(),
        "python": sys.version.split()[0],
        "python_docx": __import__("docx").__version__,
        "pdf_export": "writer_pdf_Export with tagged PDF, PDF/UA compliance and bookmarks enabled",
        "projection_rule": "wide Markdown tables become stacked header-labelled records; the source text remains complete; a dedicated cover precedes the contents",
    }
    (work / "build_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (work / "toolchain.json").write_text(json.dumps(toolchain, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=pathlib.Path, required=True)
    parser.add_argument("--work", type=pathlib.Path, required=True)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--key", choices=[paper["key"] for paper in PAPERS])
    args = parser.parse_args()
    build(args.root.resolve(), args.work.resolve(), resume=args.resume, key=args.key)
    return 0


if __name__ == "__main__":
    sys.exit(main())
