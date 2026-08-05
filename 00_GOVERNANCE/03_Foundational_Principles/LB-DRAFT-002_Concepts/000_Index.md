# LB-DRAFT-002 — Foundational Concepts Index

**Document ID:** LB-DRAFT-002  
**Artifact Type:** Foundational Concept Catalog  
**Version:** 0.2  
**Status:** Living Index  
**Governance Method:** Primitive Evaluation Process

---

# 1. Purpose

This index is the authoritative catalog of the SymK Foundational Concepts.

Each `FC-nnn` file defines one candidate or accepted foundational concept as an independently versioned knowledge asset.

The index provides a consolidated view of:

- concept identity
- current evaluation status
- document version
- confidence level
- supporting Primitive Review Record
- major dependencies
- unresolved questions

The detailed definition, evidence, invariants, and engineering models belong in the corresponding `FC-nnn` document.

---

# 2. Concept Status Model

| Status | Meaning |
|---|---|
| Proposed | Candidate identified but not yet subjected to a formal primitive review. |
| Under Evaluation | Candidate is being tested through one or more Primitive Review Records. |
| Provisionally Accepted | Candidate has survived the required attacks but remains subject to confirmation by dependent reviews. |
| Accepted | Candidate has been admitted to the SymK foundation through the approved governance process. |
| Rejected | Candidate was determined not to be a foundational concept or primitive. |
| Superseded | Concept or definition was replaced by a newer canonical concept or formulation. |

---

# 3. Foundational Concept Catalog

| ID | Concept | Status | Version | Confidence | PRR | Primary Dependency | Current Note |
|---|---|---:|---:|---:|---|---|---|
| FC-001 | Entity | Under Evaluation | 0.2 | Medium | PRR-0001 | None established | Survived three attacks; definition refined to “first-class engineering object.” |
| FC-002 | Relationship | Under Evaluation | 0.1 | Medium | PRR-0002 | Entity | Appears indispensable and currently behaves as an Entity. |
| FC-003 | Identity | Proposed | 0.1 | Low | — | Entity, Relationship | Evaluation pending. |
| FC-004 | Context | Proposed | 0.1 | Low | — | Entity, Relationship, Applicability | Boundary between concept and property remains unresolved. |
| FC-005 | Intelligence | Proposed | 0.1 | Low | — | Entity, Identity, Relationship, Context | Evaluation postponed until lower-level concepts stabilize. |
| FC-006 | Knowledge | Proposed | 0.1 | Low | — | Intelligence, Entity, Context, Representation | Evaluation planned after Intelligence. |

---

# 4. Current Evaluation Order

The present evaluation sequence is:

1. **FC-001 — Entity**
2. **FC-002 — Relationship**
3. **FC-003 — Identity**
4. **Representation** — identifier to be confirmed
5. **FC-004 — Context**
6. **FC-005 — Intelligence**
7. **FC-006 — Knowledge**

This order follows the principle:

> Evaluate the concept whose resolution reduces the greatest amount of uncertainty in the remaining ontology.

---

# 5. Current Foundational Findings

## 5.1 Entity

Current working definition:

> An Entity is a first-class engineering object within the SymK conceptual model that may possess its own identity, lifecycle, metadata, relationships, and representations.

The earlier definition, “anything that exists,” was rejected because it incorrectly included literals, scalar values, and simple attributes.

## 5.2 Relationship

Current working definition:

> A Relationship is a first-class engineering object that expresses a semantic association between two or more first-class engineering objects.

Elimination attempts recreated Relationship under alternative names such as references, pointers, containment, or specialized attributes.

---

# 6. Open Questions

| ID | Question | Raised By | Affected Concepts | Status | Priority |
|---|---|---|---|---|---|
| Q-0001 | Is Connection more fundamental than Relationship? | PRR-0002 | Entity, Relationship | Open | High |
| Q-0002 | Is every Relationship an Entity? | PRR-0002 | Entity, Relationship | Provisionally answered: Yes | High |
| Q-0003 | Is Context a first-class concept or a property of applicability? | Foundation review | Context, Applicability | Open | High |
| Q-0004 | Are Representations themselves Entities? | PRR-0001 | Entity, Representation | Open | Medium |
| Q-0005 | Can an Entity possess multiple identities within different scopes? | FC-001 engineering model | Entity, Identity, Context | Open | High |

---

# 7. Document Conventions

Each foundational concept file should follow this naming convention:

```text
FC-nnn_ConceptName.md
```

Example:

```text
FC-001_Entity.md
```

Each concept specification should contain, where applicable:

1. Purpose
2. Current Definition
3. Motivation
4. Engineering Characteristics
5. Exclusions
6. Examples
7. Counterexamples
8. Definition Evolution
9. Primitive Evaluation History
10. Engineering Consequences
11. Open Questions
12. Related Concepts
13. Engineering Invariants
14. Reference Engineering Model
15. References

---

# 8. Multi-Layer Specification Requirement

Every mature `FC-nnn` specification should describe the concept through three synchronized layers:

1. **Human Definition**
2. **Semantic Model**
3. **Reference Engineering Model**

The Reference Engineering Model may include:

- JSON contract
- YAML contract
- graph view
- database projection
- programming-language projection
- design notes

The concept is primary. Every technical representation is a secondary projection of the same canonical concept.

---

# 9. Governance Rules

1. This index is a consolidated catalog, not the primary source for complete concept definitions.
2. The corresponding `FC-nnn` file is the canonical source for each concept.
3. Concept definitions may change only through evidence recorded in the Primitive Review Process.
4. Every material definition change must update:
   - the concept file
   - this index
   - the associated PRR or review record
   - the Canonical Documents Registry, when applicable
5. Historical definitions must remain traceable.
6. Proposed concepts must not be treated as accepted foundations.
7. Open questions must remain explicit until formally resolved.

---

# 10. Related Governance Artifacts

- Primitive Evaluation Standard
- Primitive Backlog
- Primitive Review Record Template
- PRR-0001 — Entity
- PRR-0002 — Relationship
- SYMK-NOTE-001 — Multi-Layer Concept Specification
- Canonical Documents Registry

---

# 11. Revision History

| Version | Change |
|---|---|
| 0.1 | Initial scaffold. |
| 0.2 | Added catalog, status model, evaluation order, findings, open questions, document conventions, and governance rules. |
