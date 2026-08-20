# DocumentType

**Definition identifier:** `symk.document_type`
**Status:** Proposed
**Normative effect:** None
**Candidate owner/layer:** SymK minimum at S2; domain concepts and schemes at P2

## Human-semantic nucleus

### DTYPE-001 — Working definition

A **DocumentType** is a governed classification concept used to recognize a
kind of Document under a declared Domain, classification scheme, scheme version,
and classification purpose.

### DTYPE-002 — Domain authority

SymK may govern the generic meaning and minimum boundary of DocumentType. The
substantive concepts, membership criteria, hierarchies, equivalences, and
disjointness rules of a domain scheme belong to the authority that governs that
Domain.

### DTYPE-003 — Concept identity

A DocumentType is referenced through a stable concept identifier. Its human
label may change or have translations without necessarily changing the
concept's identity. A material change of meaning, membership criteria, or
jurisdiction requires explicit version and lineage treatment.

### DTYPE-004 — Purpose dependence

Classification is purpose-dependent. Several defensible type assignments may
coexist when they use different declared schemes or purposes. A single
"primary" type is therefore a projection selected for a stated purpose, not a
universal semantic fact.

## Prohibited conflations

DocumentType must not be silently equated with:

- MIME type or file format;
- filename extension;
- SharePoint Content Type or another provider-native type;
- business Domain;
- document lifecycle or review status;
- an uncontrolled display label; or
- an intrinsic single-valued property of every Document.

## Domain examples

The following identifiers are illustrative only and are not defined by this
package:

- `legal.document_type.initial_pleading`;
- `legal.document_type.appeal`;
- `medical.document_type.prescription`;
- `medical.document_type.examination_request`.

## Known open questions

- The minimum common structure required of a compatible domain scheme remains
  for 2.5–2.7.
- Cross-scheme mappings and equivalence claims require their own authority and
  provenance.
