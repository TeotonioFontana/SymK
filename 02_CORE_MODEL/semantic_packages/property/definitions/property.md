# Property

**Definition identifier:** `symk.property`
**Status:** Proposed
**Normative effect:** None
**Candidate owner/layer:** SymK / S2

## Human-semantic nucleus

### PROP-001 — Working definition

A **Property** is a quality, state, predicate, or relation attributable to an
eligible Bearer within declared Scope and relevant Context.

### PROP-002 — Semantic forms

A Property may be expressed as:

- a quality or characteristic;
- a state that may change over time;
- a unary predicate that holds or does not hold;
- a relation to another identified subject or concept; or
- a qualified relation whose interpretation depends on additional dimensions.

These forms must not be forced into one scalar-value model merely because a
programming language or database makes scalar fields convenient.

### PROP-003 — Attribution boundary

A Property is interpreted only with an eligible Bearer and the Scope, Context,
and Applicability conditions material to the attribution. The same term may
refer to different Properties when bearer, jurisdiction, or meaning differs.

### PROP-004 — Representation boundary

A Property is not identical to its name, definition file, YAML declaration,
class attribute, database column, extracted value, or repository metadata
field. Those are representations or implementations of selected dimensions.

### PROP-005 — Identity

A governed Property requires an identity stable enough to distinguish a label
change from a semantic change. A material change in meaning, bearer, value role,
scope, or constitutive constraints requires explicit version and lineage
treatment.

## Prohibited interpretations

- Every technical field is automatically a governed Property.
- Every Property has exactly one scalar value.
- A Property exists only after it is asserted of an instance.
- Properties sharing a label are necessarily identical.
- Storage-layer constraints silently determine semantic meaning.

## Open questions

- Final disposition of Property as a concept or supporting distinction remains
  subject to the governed 2.1 process.
- The minimum formal relation among Property, predicate, quality, state, and
  Relationship remains to be tested in 2.1.4 and 2.5.
