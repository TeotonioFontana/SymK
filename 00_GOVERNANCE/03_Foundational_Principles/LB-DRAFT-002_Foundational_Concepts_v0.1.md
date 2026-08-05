# LB-DRAFT-002 --- Foundational Concepts

**Version:** 0.1 (Living Draft)

## Purpose

This document is the canonical catalog of the foundational concepts of
SymK.

Unlike a traditional glossary, every concept in this document is backed
by the Primitive Evaluation Methodology and corresponding Primitive
Review Records (PRRs). Definitions are therefore expected to evolve as
new evidence is gathered.

------------------------------------------------------------------------

# Concept Status

  -----------------------------------------------------------------------
  Status                              Meaning
  ----------------------------------- -----------------------------------
  Proposed                            Candidate identified but not yet
                                      evaluated.

  Under Evaluation                    Currently being challenged through
                                      the PRR process.

  Accepted                            Survived the evaluation process and
                                      admitted to the foundation.

  Rejected                            Determined not to be a primitive.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Entity

**Status:** Under Evaluation

**Current Definition**

> An **Entity** is a first-class engineering object within the SymK
> conceptual model that can possess its own identity, lifecycle,
> metadata, relationships, and representations.

### Definition Evolution

**v0.1**

> Anything that exists in the SymK conceptual model.

**Result:** Rejected during PRR-0001 Third Attack because the definition
was too broad and incorrectly included literals, scalar values, and
simple attributes.

**v0.2 (Current)**

> A first-class engineering object that may possess identity, metadata,
> relationships, representations, lifecycle and version history.

### Engineering Rationale

The Entity abstraction removes duplication by providing a common subject
for identity, relationships, representation, context, metadata,
versioning and lifecycle.

### Current Evidence

-   Survived First Attack
-   Survived Second Independent Attack
-   Survived Third Attack (definition refined)

**Reference:** PRR-0001

------------------------------------------------------------------------

# Intelligence

**Status:** Proposed

### Working Definition

An engineering object capable of acquiring, creating, interpreting or
applying knowledge.

**Evaluation Status**

Not yet evaluated.

------------------------------------------------------------------------

# Knowledge

**Status:** Proposed

### Working Definition

Structured meaning that can be acquired, represented, transferred and
applied by one or more intelligences.

**Evaluation Status**

Not yet evaluated.

------------------------------------------------------------------------

# Relationship

**Status:** Proposed

### Working Definition

A construct expressing an association between first-class engineering
objects.

**Evaluation Status**

Scheduled for evaluation after Entity.

------------------------------------------------------------------------

# Identity

**Status:** Proposed

### Working Definition

A mechanism that uniquely distinguishes a first-class engineering object
within a defined scope.

------------------------------------------------------------------------

# Context

**Status:** Proposed

### Working Definition

The set of conditions under which a statement, relationship or behavior
is applicable.

------------------------------------------------------------------------

# Representation

**Status:** Proposed

### Working Definition

A concrete manifestation through which a first-class engineering object
is expressed or exchanged.

------------------------------------------------------------------------

# Document Governance

This document is intentionally **living**.

Definitions shall only change through evidence accumulated in Primitive
Review Records. Historical reasoning belongs in the PRRs; this document
always reflects the current agreed definition.
