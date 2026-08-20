# Document

**Definition identifier:** `symk.document`
**Status:** Proposed
**Normative effect:** None
**Candidate owner/layer:** SymK / S2

## Human-semantic nucleus

### DOC-001 — Working definition

A **Document** is a governed knowledge-bearing Representation whose content and
organization are treated as a recognizable documentary whole within a declared
Context and Scope.

### DOC-002 — Representation boundary

A Document is not identical to the Knowledge it may represent, communicate, or
support. The current proposal treats Document as a specialization of
Representation, not as a specialization of Knowledge Object.

### DOC-003 — Realization boundary

A Document is not identical to a physical or digital file occurrence. One
Document may have several file occurrences, formats, versions, or repository
bindings. One file may also require segmentation when it contains several
documentary wholes.

### DOC-004 — Identity

Document identity must be stated independently of a storage provider identifier
or path. A SharePoint item ID, S3 key, filesystem path, hash, and database key
may identify particular records or occurrences without alone determining
Document identity.

## Constitutive candidate conditions

- it is a Representation;
- it bears or organizes content as a recognizable documentary whole;
- its interpretation is bounded by relevant Context and Scope; and
- its identity can remain distinguishable from its file occurrences and
  repository bindings.

## Prohibited conflations

A Document must not be silently equated with:

- Knowledge or a Knowledge Object;
- a byte sequence or file occurrence;
- a repository record or SharePoint list item;
- a MIME type or filename extension;
- a document classification; or
- the truth, validity, or authority of its content.

## Boundary examples

- A prescription represented by both PDF and DOCX may be one Document with two
  file occurrences.
- A scanned bundle containing a prescription and an examination request may
  contain two Documents despite being stored as one file.
- A database row describing a clinical report is not automatically the rendered
  report Document.

## Known open questions

- Minimum criteria for documentary-whole identity remain to be tested.
- The boundary among Document, record, message, dataset, and audiovisual work
  remains outside this initial slice.
- Final admission and artifact form belong to the governed 2.1 and 2.5 process.
