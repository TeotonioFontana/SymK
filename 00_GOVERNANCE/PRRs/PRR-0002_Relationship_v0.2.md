# PRR-0002 --- Primitive Review Record: Relationship

**Target:** FC-002 --- Relationship\
**Status:** In Progress\
**Revision:** 0.2

# Review Summary

Relationship has survived the initial elimination attacks and currently
remains the strongest candidate for a foundational concept.

No engineering replacement (pointer, reference, foreign key,
containment, property) successfully eliminated the underlying semantic
association.

# Attacks Performed

## Attack 1 --- Elimination

Attempted replacements:

-   Reference
-   Pointer
-   Foreign Key
-   Property
-   Containment

**Result:** Failed.

Each replacement represented an implementation mechanism rather than the
semantic concept.

------------------------------------------------------------------------

## Attack 2 --- Candidate Substitutes

Two meaningful alternatives remain under investigation:

-   Association
-   Connection

Neither has yet demonstrated greater explanatory power than
Relationship.

------------------------------------------------------------------------

## Attack 3 --- Dependency

Relationship requires participants.

Entity does not require Relationships to exist.

Current conclusion:

Relationship depends upon Entity.

------------------------------------------------------------------------

## Attack 4 --- Self Participation

A Relationship appears capable of participating in another Relationship.

Example:

A supports B

contradicts

C supports D

This strengthens the hypothesis that Relationship behaves as a
first-class engineering object.

------------------------------------------------------------------------

# Critical Observation CO-001

## Question

Can scalar values participate in Relationships?

Examples:

37 greater_than 12

Pressure depends_on Temperature

If scalar values may participate directly, the current definition of
Entity requires revision.

If they may not, a formal criterion separating first-class engineering
objects from scalar values must be established.

This investigation affects:

-   FC-001 Entity
-   FC-002 Relationship
-   FC-003 Identity

Status: OPEN

Priority: CRITICAL

------------------------------------------------------------------------

# Interim Conclusion

Relationship remains provisionally accepted as a candidate foundational
concept.

Further review is suspended pending resolution of CO-001.
