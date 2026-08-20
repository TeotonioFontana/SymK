# PropertyValue

**Definition identifier:** `symk.property_value`
**Status:** Proposed
**Normative effect:** None
**Candidate owner/layer:** Meaning follows the governing PropertyDefinition and value source

## Human-semantic nucleus

### PVAL-001 — Working definition

A **PropertyValue** is the semantic role occupied by the value, target, or
structured content through which a PropertyAssertion completes the form
declared by its PropertyDefinition.

### PVAL-002 — Value families

A PropertyDefinition may permit one or more value families, including:

- a governed concept reference;
- an identified subject reference;
- a literal with datatype, unit, language, or format where relevant;
- a structured value with declared internal meaning; or
- a predicate state when no separate value is semantically required.

The allowed family is part of the PropertyDefinition, not inferred from a
currently convenient serialization.

### PVAL-003 — Concept reference

A concept-valued assertion must preserve concept identity, governing scheme,
scheme version, Domain, and source authority. A display label alone is not a
stable concept reference.

### PVAL-004 — Literal interpretation

A literal value is not self-interpreting. Datatype, unit, language, scale,
format, uncertainty, or normalization rules must be present whenever their
omission would change meaning.

### PVAL-005 — Multiplicity

Multiplicity belongs to the PropertyDefinition and applicable profile. Several
values or assertions may be valid under different schemes, purposes, times,
Contexts, Scopes, or provenance. A selected primary value is a Projection unless
the governing semantics establish otherwise.

## Prohibited interpretations

- Every PropertyValue is a string.
- A human-readable label is always a concept identity.
- JSON structure provides meaning without a governed definition.
- Multiple values are necessarily an error.
