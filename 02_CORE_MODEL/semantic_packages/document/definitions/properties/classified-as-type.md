# Document classified as type

**Definition identifier:** `symk.document.classified_as_type`
**Status:** Proposed
**Normative effect:** None
**Semantic kind:** Qualified relation presented as a Document property
**Candidate owner/layer:** SymK / S2
**Property semantics dependency:** `symk.semantic.property@0.1.0-proposed`

## Human-semantic nucleus

### DCLASS-001 — Working definition

`symk.document.classified_as_type` relates a Document to a domain-governed
DocumentType concept through a qualified classification assertion.

### DCLASS-002 — Assertion boundary

The PropertyDefinition exists independently of any assignment. A concrete
PropertyAssertion exists only when an assertion relates an identified Document
to an identified DocumentType concept with the required qualifiers.

### DCLASS-003 — Required qualification

An interpretable assertion identifies at least:

- the Document being classified;
- the PropertyDefinition and compatible version;
- the DocumentType concept;
- the governing Domain;
- the classification scheme and version;
- the assertion status; and
- provenance sufficient to identify how or by whom the assertion arose.

Evidence, Context, Scope, effective time, confidence, and purpose are required
when their omission would materially change interpretation or authorized use.

### DCLASS-004 — Multiplicity

The relation is not universally single-valued. A Document may receive several
assignments under different schemes, purposes, times, or competing analyses.
Contradictory or superseded assignments must remain distinguishable rather than
being overwritten silently.

### DCLASS-005 — Primary value

A primary or repository-visible document type is a purpose-specific Projection
over eligible assertions. It is not the full authoritative runtime assertion
state.

### DCLASS-006 — Evidence and acceptance

A filename, folder, classifier result, or extracted phrase may support a
candidate classification. It does not by itself create an accepted assertion.
The transition from proposed to accepted status requires the authority declared
by the adopting Domain or organization.

### DCLASS-007 — Absence

Absence of an assertion does not entail unknown, not collected, not applicable,
rejected, or impossible. Those states require explicit representation when the
distinction matters.

## Generic semantic conformance

This candidate is modeled as:

- a Property represented by a PropertyDefinition;
- applicable to Document through `symk.document.core_properties`;
- asserted through a PropertyAssertion;
- completed by a concept-reference PropertyValue; and
- qualified according to the definition and material Context and Scope.

The generic meanings of those roles belong to `symk.semantic.property`; this
file supplies only the document-classification specialization.

## Prohibited interpretations

- Treating MIME type as a DocumentType assignment.
- Treating a SharePoint Content Type as authoritative without a declared mapping.
- Inferring an accepted type solely from a filename or storage folder.
- Mixing a foreign-domain classification into a declared homogeneous corpus
  without reporting or quarantining the boundary violation.
- Destroying prior accepted, rejected, corrected, or superseded assertions when
  a new assertion is recorded.

## Engineering consequence

Runtime stores should reference this definition by stable identifier and exact
definition version or package digest. They should store assertion instances
separately from installed definition records and repository projections.
