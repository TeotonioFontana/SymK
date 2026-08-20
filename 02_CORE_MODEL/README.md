# SymK Core Model

**Status:** Proposed scaffold
**Normative effect:** None
**Target decision stage:** SymK 2.5 — Semantic packaging and projection architecture

## Purpose

This directory is the candidate home of SymK-owned semantic definitions whose
minimum meaning has cross-project reach.

It separates four things that must not be collapsed:

1. a governed semantic definition;
2. a machine-semantic projection of selected claims from that definition;
3. a domain-owned specialization or vocabulary;
4. runtime assertions and implementation records.

The Core Model stores the first two only when their owning layer and authority
are explicit. It may contain examples of the other two, but examples acquire no
authority through repository placement.

## Current authority boundary

The contents are scaffolding for review. They do not open, complete, or accept
SymK 2.5; do not migrate historical `FC-*`, `FP-*`, or `SYMK-P-*` artifacts; and
do not select a final serialization or formal language.

Promotion from Proposed to a governing status requires the applicable SymK
decision and preserved lineage.

## Structure

```text
02_CORE_MODEL/
└── semantic_packages/
    ├── README.md
    └── <semantic-family>/
        ├── manifest.yaml
        ├── README.md
        ├── definitions/
        ├── semantics/
        ├── examples/
        └── CHANGELOG.md
```

Packages are organized by coherent semantic family, not by runtime object,
database row, source file, tenant, or customer.

## Candidate package index

| Package | Purpose | Status |
|---|---|---|
| `symk.semantic.property` | Defines the candidate distinction among Property, PropertyDefinition, PropertyApplicabilityProfile, PropertyAssertion, and PropertyValue | Proposed |
| `symk.semantic.document` | Tests a vertical slice from Document semantics through a machine-inspectable document-type classification relation | Proposed |

## Non-goals

This directory is not:

- a database of document instances or property values;
- a domain vocabulary for Legal, Medical, or another derived project;
- a Python package or API model;
- a repository-native metadata definition;
- evidence that every contained concept is foundational; or
- evidence that a machine representation exhausts a governed concept.
