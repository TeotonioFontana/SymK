# FC-002 --- Relationship

**Version:** 0.1\
**Status:** Under Evaluation\
**Primitive Review Record:** PRR-0002\
**Confidence:** Medium

------------------------------------------------------------------------

# 1. Purpose

This document defines the SymK concept **Relationship**.

It is the canonical engineering specification for the current
understanding of Relationship and evolves only through approved
Primitive Review Records.

------------------------------------------------------------------------

# 2. Current Definition

> **A Relationship is a first-class engineering object that expresses a
> semantic association between two or more first-class engineering
> objects.**

This is the current working definition and remains subject to future
review.

------------------------------------------------------------------------

# 3. Motivation

Relationship exists to connect first-class engineering objects.

Without Relationship, a collection of Entities becomes merely a
collection of isolated objects.

Knowledge emerges not only from objects themselves, but also from the
semantic structure connecting them.

------------------------------------------------------------------------

# 4. Engineering Characteristics

A Relationship may possess:

-   Identity
-   Metadata
-   Lifecycle
-   Version History
-   Provenance
-   One or more Representations

A Relationship connects two or more first-class engineering objects.

The connected objects are called **Participants**.

------------------------------------------------------------------------

# 5. What a Relationship is NOT

A Relationship is not:

-   a pointer
-   a database foreign key
-   an object reference
-   containment
-   an implementation artifact

These are merely engineering representations.

The Relationship exists independently of how it is represented.

------------------------------------------------------------------------

# 6. Examples

Examples include:

-   supports
-   contradicts
-   depends_on
-   belongs_to
-   references
-   generates
-   owns
-   author_of

## Cross-domain examples

### LexBrain

-   Fragment supports Thesis
-   Document belongs_to Case

### SSHConnectivity

-   Tunnel connects Service
-   Service runs_on Server

### Osteolab

-   Patient has Exam
-   Exam generates Report

### HyperAdm

-   User belongs_to Organization
-   Account owns Application

------------------------------------------------------------------------

# 7. Counterexamples

These are not Relationships:

-   Integer
-   String
-   UUID
-   Timestamp
-   Color

Likewise, a database foreign key is not itself a Relationship.

It is one possible implementation.

------------------------------------------------------------------------

# 8. Definition Evolution

## Initial Definition

> A semantic association between two objects.

**Observation**

Too implementation-oriented.

It ignored metadata, lifecycle and governance.

## Current Definition

> A first-class engineering object that expresses a semantic association
> between two or more first-class engineering objects.

Status:

Current working definition.

------------------------------------------------------------------------

# 9. Primitive Evaluation History

**PRR-0002**

Current findings:

-   Elimination attempt failed.
-   Every attempted replacement recreated Relationship under another
    name.
-   Cross-domain evidence collected.

Current conclusion:

Relationship appears indispensable.

------------------------------------------------------------------------

# 10. Engineering Consequences

Accepting Relationship implies:

-   semantic associations become first-class citizens
-   relationships may possess metadata
-   relationships may evolve independently
-   relationships may be governed independently
-   relationships become versionable

------------------------------------------------------------------------

# 11. Open Questions

Current open questions include:

-   Is every Relationship an Entity?
-   Is Connection more primitive than Relationship?
-   Should Relationship always have at least two Participants?
-   Can Relationships relate other Relationships?
-   Can Relationships possess Context?

------------------------------------------------------------------------

# 12. Related Concepts

-   FC-001 Entity
-   FC-003 Identity
-   FC-004 Context
-   FC-005 Intelligence
-   FC-006 Knowledge

------------------------------------------------------------------------

# 13. Engineering Invariants

**INV-001**

Every Relationship connects two or more first-class engineering objects.

**INV-002**

A Relationship is independent of its engineering representation.

**INV-003**

Replacing a Relationship with pointers or references does not eliminate
the underlying Relationship.

**INV-004**

A Relationship may possess metadata.

**INV-005**

A Relationship may evolve independently of the connected objects.

------------------------------------------------------------------------

# 14. Reference Engineering Model

## Semantic Model

``` text
Relationship
├── Participants*
├── Identity
├── Metadata
├── Lifecycle
├── Version
├── Provenance
└── Representation*
```

## JSON Contract

``` json
{
  "relationship": {
    "id": "relationship-001",
    "type": "supports",
    "participants": [
      {
        "role": "source",
        "entity": "entity-001"
      },
      {
        "role": "target",
        "entity": "entity-002"
      }
    ],
    "metadata": {},
    "context": {},
    "lifecycle": {},
    "version": {},
    "provenance": {},
    "representations": []
  }
}
```

## YAML Contract

``` yaml
relationship:
  id: relationship-001
  type: supports
  participants:
    - role: source
      entity: entity-001
    - role: target
      entity: entity-002
  metadata: {}
  context: {}
  lifecycle: {}
  version: {}
  provenance: {}
  representations: []
```

## Design Notes

Current engineering assumptions:

-   Participants are represented explicitly.
-   Roles are independent of the participant.
-   Context is modeled separately from the relationship itself.
-   Relationship type is treated as semantic information.
-   This structure is expected to evolve.

------------------------------------------------------------------------

# 15. References

-   Primitive Evaluation Standard
-   PRR-0002
-   FC-001 Entity
-   SYMK-NOTE-001 --- Multi-Layer Concept Specification

# 16. Review Notes (Added after PRR-0002 Revision 0.2)

## Current Primitive Review Status

Relationship has survived:

-   Elimination Attack
-   Dependency Attack
-   Self-Participation Attack

Two conceptual alternatives remain under investigation:

-   Association
-   Connection

## Critical Observation CO-001

The review uncovered a higher-level question:

> Can scalar values participate directly in Relationships?

Resolving this question may require refinement of the current definition
of Entity before the Relationship review can continue.

For this reason, FC-002 remains **Under Evaluation**, and its current
definition should be interpreted as a working engineering hypothesis
rather than a final foundational definition.
