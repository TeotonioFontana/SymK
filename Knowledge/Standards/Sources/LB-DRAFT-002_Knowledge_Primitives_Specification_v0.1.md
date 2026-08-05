# LB-DRAFT-002
# Knowledge Primitives Specification

**Status:** Working Draft
**Version:** 0.1

## Purpose

This specification defines the foundational Knowledge Primitives of the SymK Core.

A Knowledge Primitive is an irreducible engineering construct used to describe, organize and evolve knowledge.

## Primitive Criteria

A Knowledge Primitive SHALL:

- represent a fundamental concept;
- not be expressible as a Property;
- not be expressible as a Relationship;
- not be merely a specialization;
- have long-term architectural value.

## Initial Primitive Set

### KP-001 — Knowledge Object

The fundamental unit of knowledge recognized by SymK.

Recognition criteria:

- identifiable;
- describable;
- reusable;
- representable;
- related to other Knowledge Objects.

Knowledge Objects are the conceptual center of SymK.

### KP-002 — Representation

A manifestation of one or more Knowledge Objects.

Examples:

- document
- legal pleading
- presentation
- report
- diagram
- training material

Representations are projections of knowledge.

### KP-003 — Knowledge Source

The origin from which a Knowledge Object is acquired.

Examples:

- legislation
- scientific literature
- expert knowledge
- organizational experience
- operational practice

### KP-004 — Context

The environment in which a Knowledge Object is interpreted or applied.

Examples:

- time
- jurisdiction
- organization
- process
- audience
- domain

## Primitive Selection Rule

Every candidate primitive SHALL answer:

1. Is it universal?
2. Is it irreducible?
3. Will multiple domains use it?
4. Is it expected to remain stable over time?

Otherwise it SHOULD remain outside the SymK Core.

## Deferred to Domain Cores

The following are intentionally excluded from the SymK Core:

- Thesis
- Argument
- Evidence
- Legal Strategy
- Legal Fragment
- Petition

These are expected to belong to the Legal Core.

## Candidates Under Evaluation

- Knowledge Network
- Decision
- Event
- Observation
- Knowledge Process

## Closing

The SymK Core seeks the smallest stable vocabulary capable of supporting long-term symbiotic cooperation between human and artificial intelligence.
