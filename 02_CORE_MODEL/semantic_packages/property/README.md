# SymK Property Semantics

**Package identifier:** `symk.semantic.property`
**Version:** `0.1.0-proposed`
**Status:** Proposed
**Normative effect:** None
**Target decision stages:** SymK 2.1.4 and 2.5

## Purpose

This package defines the candidate cross-project semantic machinery required to
describe properties without reducing them to programming attributes, database
columns, JSON fields, or repository metadata.

It distinguishes:

```text
Property
    represented by a governed PropertyDefinition

PropertyApplicabilityProfile
    relates PropertyDefinitions to eligible Bearers

PropertyAssertion
    applies a Property to an identified Bearer at runtime

PropertyValue
    occupies the value role required by a particular PropertyDefinition
```

## Dependency direction

Subject-specific packages depend on this package. This package does not depend
on Document, Legal, Medical, SharePoint, S3, Python, or MySQL semantics.

For example:

```text
symk.semantic.property
        ↑ dependency
symk.semantic.document
        ↑ adoption and specialization
LexBrain or Medical semantic packages
```

## Boundary

This package defines candidate semantic distinctions and their bounded
machine-semantic projection. It does not define:

- the complete property set of any bearer;
- a final declaration language or validation schema;
- a universal runtime storage model;
- domain-owned properties or values;
- truth from assertion status; or
- a requirement that every Property be implemented as a scalar field.

## Included candidate definitions

| Identifier | Responsibility |
|---|---|
| `symk.property` | Meaning of a Property as an attributable quality, state, predicate, or relation |
| `symk.property_definition` | Governed semantic representation of a Property |
| `symk.property_applicability_profile` | Applicability of PropertyDefinitions to eligible Bearers |
| `symk.property_assertion` | Runtime claim applying a Property to an identified Bearer |
| `symk.property_value` | Value role governed by a PropertyDefinition |

Creation of this scaffold does not admit these candidates into the accepted
foundational set.
