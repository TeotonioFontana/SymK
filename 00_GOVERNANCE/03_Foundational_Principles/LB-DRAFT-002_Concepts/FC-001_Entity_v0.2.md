# FC-001 --- Entity

**Version:** 0.2\
**Status:** Under Evaluation\
**Primitive Review Record:** PRR-0001\
**Confidence:** Medium

------------------------------------------------------------------------

# 1. Purpose

This document defines the SymK concept **Entity**.

It is the canonical engineering specification for the Entity concept.
Its content evolves only through approved Primitive Review Records
(PRRs).

------------------------------------------------------------------------

# 2. Current Definition

> **An Entity is a first-class engineering object within the SymK
> conceptual model that may possess its own identity, lifecycle,
> metadata, relationships, and representations.**

------------------------------------------------------------------------

# 3. Motivation

Entity provides a common abstraction for every first-class engineering
object managed by SymK.

Without this abstraction, every concept would need to independently
define identity, lifecycle, governance, versioning, provenance, metadata
and representation.

Entity centralizes these concerns.

------------------------------------------------------------------------

# 4. Engineering Characteristics

An Entity may possess:

-   Identity
-   Metadata
-   Lifecycle
-   Relationships
-   Representations
-   Version History
-   Provenance
-   Governance Information

None of these characteristics are individually mandatory.

------------------------------------------------------------------------

# 5. What an Entity is NOT

The following are **not** Entities:

-   Numbers
-   Strings
-   Boolean values
-   Literal values
-   Simple attributes
-   Scalar values

Examples:

    37

    Confidence = 0.82

These values belong to engineering objects but are not engineering
objects themselves.

------------------------------------------------------------------------

# 6. Examples

Current examples include:

-   Intelligence
-   Knowledge
-   Relationship *(under evaluation)*
-   Context *(under evaluation)*
-   Representation *(under evaluation)*

------------------------------------------------------------------------

# 7. Counterexamples

-   Integer
-   String
-   Timestamp value
-   UUID literal
-   Floating-point number

------------------------------------------------------------------------

# 8. Definition Evolution

## Initial Definition

> Anything that exists.

### Result

Rejected.

Reason:

Too broad. It incorrectly classified literals and scalar values as
Entities.

------------------------------------------------------------------------

## Current Definition

> A first-class engineering object...

Status:

Current working definition.

------------------------------------------------------------------------

# 9. Primitive Evaluation History

**PRR-0001**

Results:

-   Survived First Attack
-   Survived Second Attack
-   Survived Third Attack

The third attack refined the definition from an existential concept to a
first-class engineering object.

------------------------------------------------------------------------

# 10. Engineering Consequences

Accepting Entity implies:

-   Uniform governance
-   Uniform lifecycle
-   Uniform versioning
-   Uniform provenance
-   Common abstraction across the ontology

------------------------------------------------------------------------

# 11. Open Questions

Current open questions include:

-   Is Relationship an Entity?
-   Is Context an Entity?
-   Are Representations themselves Entities?

------------------------------------------------------------------------

# 12. Related Concepts

-   FC-002 Relationship
-   FC-003 Identity
-   FC-004 Context
-   FC-005 Intelligence
-   FC-006 Knowledge

------------------------------------------------------------------------

# 13. Engineering Invariants

**INV-001**

Every Entity is a first-class engineering object.

**INV-002**

An Entity may participate in one or more Relationships.

**INV-003**

An Entity may possess Identity.

**INV-004**

An Entity may have one or more Representations.

**INV-005**

Scalar values are not Entities.

------------------------------------------------------------------------

# 14. Reference Engineering Model

## Semantic Model

``` text
Entity
 ├── has Identity
 ├── has Metadata
 ├── participates in Relationship
 ├── has Lifecycle
 ├── has Representation
 └── has Version
```

## JSON Contract

``` json
{
  "entity": {
    "id": "entity-001",
    "identity": {},
    "metadata": {},
    "relationships": [],
    "representations": [],
    "lifecycle": {},
    "version": {},
    "provenance": {}
  }
}
```

## YAML Contract

``` yaml
entity:
  id: entity-001
  identity: {}
  metadata: {}
  relationships: []
  representations: []
  lifecycle: {}
  version: {}
  provenance: {}
```

## Design Notes

-   This engineering model is a reference contract, not an
    implementation.
-   The structure is expected to evolve as additional primitives are
    evaluated.
-   JSON, YAML and graph views are alternative representations of the
    same concept.

------------------------------------------------------------------------

# 15. References

-   Primitive Evaluation Standard
-   PRR-0001
-   Foundational Principles
-   SYMK-NOTE-001 --- Multi-Layer Concept Specification
