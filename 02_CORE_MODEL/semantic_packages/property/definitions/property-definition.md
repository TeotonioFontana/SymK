# PropertyDefinition

**Definition identifier:** `symk.property_definition`
**Status:** Proposed
**Normative effect:** None
**Candidate owner/layer:** Placement follows the Property's jurisdiction

## Human-semantic nucleus

### PDEF-001 — Working definition

A **PropertyDefinition** is a governed semantic Representation that identifies
a Property and states the meaning, bearer boundary, value role, applicability,
qualifiers, constraints, authority, status, version, and lineage required for
responsible interpretation and use.

### PDEF-002 — Definition and Property

The PropertyDefinition represents the Property; it is not identical to the
Property. A definition may be challenged, revised, superseded, or projected
without implying that a file format owns the represented meaning.

### PDEF-003 — Independent existence

A PropertyDefinition exists independently of runtime assertions. Creating an
assertion instantiates use of the definition; deleting or withholding an
assertion does not delete the definition.

### PDEF-004 — Minimum governed content

A material PropertyDefinition identifies at least:

- a stable definition identifier;
- human-semantic meaning and prohibited conflations;
- eligible bearer kind or the profile through which eligibility is declared;
- value role or predicate form;
- required and conditional qualifiers;
- owner, jurisdiction, status, version, and lineage; and
- known omissions, uncertainty, and projection boundaries.

### PDEF-005 — Authority and version

The owner governs the definition only within its declared jurisdiction. A
domain definition may specialize a SymK meaning but does not acquire authority
to rewrite the SymK definition. Material semantic changes require a new version
or identity according to their effect, with prior definitions preserved.

### PDEF-006 — Structured declaration

A structured declaration is a machine-semantic projection of selected claims
from the PropertyDefinition. It may be authoritative for incorporated formal
claims within declared scope, but it is not exhaustive and must record
alignment, omissions, strengthening, and semantic loss.

## Prohibited interpretations

- A JSON Schema or SQL column is automatically the PropertyDefinition.
- A runtime value defines the Property from which it was produced.
- Copying a domain definition into SymK transfers semantic ownership.
- Reusing an identifier after a material replacement preserves identity.
