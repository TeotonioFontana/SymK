# PropertyAssertion

**Definition identifier:** `symk.property_assertion`
**Status:** Proposed
**Normative effect:** None
**Candidate owner/layer:** Semantic minimum at S2; domain and operational authority at narrower layers

## Human-semantic nucleus

### PAST-001 — Working definition

A **PropertyAssertion** is a governed claim that applies an identified Property
to an identified eligible Bearer, with the value or predicate state and
qualifiers required by the PropertyDefinition.

### PAST-002 — Minimum semantic roles

An interpretable assertion identifies:

- the Bearer or subject;
- the PropertyDefinition and compatible version;
- the value, target, or predicate state required by that Property;
- material Domain, Scope, Context, and time dimensions;
- assertion status; and
- provenance sufficient to understand how the assertion arose.

Evidence, confidence, authorization, and purpose are required when their
absence would materially change interpretation or permitted reliance.

### PAST-003 — Assertion status is not truth

Proposed, accepted, rejected, corrected, superseded, or another governance
status describes treatment of the assertion by an authority or process. It
does not by itself establish truth, validity, certainty, or permission to rely.

### PAST-004 — Provenance and evidence

An assertion must preserve the distinction among who or what produced it, the
activity that produced it, the evidence offered for it, and the authority that
changed its governance status.

### PAST-005 — Revision and coexistence

Materially distinct assertion states and revisions must remain recoverable.
Conflicting assertions may coexist when their provenance, status, Scope,
Context, scheme, purpose, or time differs. An effective current view is a
Projection over the assertion history, not a license to destroy it.

### PAST-006 — Absence

Absence of an assertion does not entail unknown, not collected, unavailable,
not applicable, rejected, false, or impossible. Those meanings require an
explicit assertion or governed status when the distinction matters.

### PAST-007 — Runtime and repository boundary

Production assertions belong to project or neutral operational stores.
Repository columns, tags, indexes, caches, and search fields are derived
projections unless the applicable authority explicitly establishes otherwise.

## Prohibited interpretations

- An assertion is identical to a PropertyDefinition.
- Acceptance status proves the assertion true.
- A missing row has one universal epistemic meaning.
- Updating an effective value authorizes destruction of prior assertions.
- A repository projection silently becomes the authoritative assertion record.
