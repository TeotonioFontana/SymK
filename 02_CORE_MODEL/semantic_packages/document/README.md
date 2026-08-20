# SymK Document Semantics

**Package identifier:** `symk.semantic.document`
**Version:** `0.1.0-proposed`
**Status:** Proposed
**Normative effect:** None
**Target decision stage:** SymK 2.5
**Depends on:** `symk.semantic.property@0.1.0-proposed`

## Purpose

This package is the first vertical-slice test of a SymK semantic package. It
asks whether one cross-domain document property can be expressed coherently
from human meaning through a bounded machine-semantic projection without
allowing that projection to define the meaning by convenience.

The selected property is:

> A Document is classified as a DocumentType under a declared Domain,
> classification scheme, version, status, and provenance.

## Included candidate definitions

- `symk.document` — Document as a governed knowledge-bearing representation;
- `symk.document_type` — a domain-governed classification concept for Documents;
- `symk.document.classified_as_type` — the qualified classification relation.

The candidate `symk.document.core_properties` profile declares which of these
property definitions are applicable to Document. It is an applicability
artifact, not another property and not a container of runtime assertions.

## File responsibilities in this package

| File | Responsibility |
|---|---|
| `manifest.yaml` | Controls package identity, authority, status, contents, dependencies, and release state. |
| `README.md` | Provides package orientation, boundaries, navigation, and review questions. |
| `definitions/document.md` | Carries the proposed human-semantic definition and boundaries of Document. |
| `definitions/document-type.md` | Carries the proposed human-semantic definition and domain-ownership boundary of DocumentType. |
| `definitions/properties/classified-as-type.md` | Carries the proposed human-semantic meaning, generic-property conformance, qualifiers, invariants, and exclusions of the classification relation. |
| `definitions/document-property-profile.md` | Defines the proposed Document property set and distinguishes applicability from assertion presence. |
| `semantics/package.yaml` | Makes the package's candidate Document and DocumentType semantics and structured-member references mechanically inspectable. |
| `semantics/alignment.yaml` | Connects machine claims to human claim identifiers and records omissions, mismatch policy, and verification state. |
| `semantics/properties/classified-as-type.yaml` | Projects the classification PropertyDefinition and declares conformance to the generic Property package. |
| `semantics/profiles/document-core-properties.yaml` | Projects the candidate bearer, property membership, applicability, multiplicity, and extension boundary of the Document profile. |
| `examples/valid-assertions.yaml` | Provides illustrative positive fixtures without creating production assertions or domain authority. |
| `examples/counterexamples.yaml` | Provides negative and boundary fixtures for semantic and engineering validation. |
| `CHANGELOG.md` | Records package revisions while leaving decision authority to the governed decision lineage. |

The machine-readable version of these responsibilities is maintained in
`manifest.yaml`.

## Ownership

SymK would own only the cross-project minimum meaning and invariants.

Derived projects retain authority over domain vocabularies and classification
criteria. For example, Legal may define an initial pleading or appeal, while a
Medical domain may define a prescription or examination request. Those values
do not become SymK-owned merely because they instantiate a SymK relation.

## Runtime boundary

This package defines no production document and stores no production property
assertion. A project or neutral operational store may install a traceable copy
of the definition and record assertions that reference the exact package
version or digest. Repository systems such as SharePoint or S3 may receive
reduced projections, but those projections are not the canonical assertion.

## Review questions

1. Does Document have sufficient cross-project reach to be governed by SymK?
2. Is Document best treated as a specialization of Representation?
3. Is `classified_as_type` correctly modeled as a qualified relation rather
   than a single-valued intrinsic attribute?
4. Which qualifiers are constitutive and which belong to operational profiles?
5. What alignment and version rules should be required of every package?

No positive answer is implied by creation of this scaffold.
