# Document Core Property Profile

**Profile identifier:** `symk.document.core_properties`
**Status:** Proposed
**Normative effect:** None
**Candidate owner/layer:** SymK / S2
**Bearer:** `symk.document`
**Property semantics dependency:** `symk.semantic.property@0.1.0-proposed`

## Human-semantic nucleus

### DPROFILE-001 — Working definition

The **Document Core Property Profile** is a governed applicability declaration
identifying the SymK-owned properties for which a Document is an eligible
Bearer, together with any profile-level requirements on their use.

It is a subject-specific candidate specialization of
`symk.property_applicability_profile`.

### DPROFILE-002 — Artifact distinction

The profile is distinct from both a Property Definition and a Property
Assertion:

- a Property Definition states what a property means;
- a Property Applicability Profile states which property definitions are
  applicable to a class of bearers under declared conditions; and
- a Property Assertion relates an identified bearer to a value at runtime.

The profile references property definitions. It does not duplicate their
meaning and does not contain runtime values.

### DPROFILE-003 — Current candidate membership

The current profile contains one candidate member:

| Property | Applicability | Universal assertion requirement | Multiplicity |
|---|---|---|---|
| `symk.document.classified_as_type` | Permitted for Documents | Not universally required | Multiple qualified assignments permitted |

Membership records eligibility and profile constraints. It does not promote a
Proposed property to Stage-Accepted or Ratified status.

### DPROFILE-004 — Applicability is not presence

Saying that a property is applicable to Document means that a valid assertion
may use a Document as its Bearer when the property's conditions are satisfied.
It does not mean that every Document has a value or that absence has one default
epistemic interpretation.

### DPROFILE-005 — Domain extension

A derived Domain may adopt this profile and define a domain profile that adds
domain-owned properties or strengthens constraints within its jurisdiction. It
must pin the adopted parent version, preserve the parent meanings and
invariants, and declare additions, strengthenings, omissions, and conflicts.

Domain extension does not transfer ownership of either the SymK profile or the
domain additions.

### DPROFILE-006 — Bearer separation

Only properties whose appropriate Bearer is Document belong in this profile.
Properties of FileOccurrence, RepositoryBinding, a knowledge claim, a person,
an organization, or another subject belong in profiles for those bearers even
when they are displayed together in one application view.

### DPROFILE-007 — Evolution

Adding, removing, replacing, or changing the applicability of a profile member
is a governed profile revision. It must preserve lineage and state the effect on
derived profiles, assertions, validation, search, and repository projections.

## Current exclusions

This initial profile does not yet define:

- a complete universal catalogue of Document properties;
- final cardinality or constraint language;
- domain-specific properties or DocumentType concepts;
- runtime assertion storage;
- repository-native metadata mappings; or
- final specialization and compatibility mechanics.

Those questions remain routed to SymK 2.5–2.9.
