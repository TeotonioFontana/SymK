# LB-DRAFT-003
# Knowledge Attributes Specification

**Status:** Working Draft
**Version:** 0.2
**Maturity:** Exploratory Baseline

---

# 1. Purpose

This specification defines the foundational attributes that characterize Knowledge Primitives.

An Attribute describes a Knowledge Primitive.

It does not define its identity.

It does not relate it to another Primitive.

---

# 2. Engineering Model

SymK distinguishes three orthogonal concepts:

- Primitive → What the knowledge is.
- Attribute → Characteristics of the knowledge.
- Relationship → Connections between knowledge.

---

# 3. Attribute Taxonomy

Attributes are classified into four categories.

## A. Scalar Attributes

Represent a single value.

Examples:

- Confidence
- Version
- Status
- Priority

---

## B. Composite Attributes

Represent a structured object composed of multiple fields.

Examples:

- Authorship
- Provenance
- Identification

---

## C. Multidimensional Attributes

Represent a semantic space rather than a single value.

The first multidimensional attribute recognized by SymK is:

### Applicability

Applicability answers:

> Under which conditions may this Knowledge Object be correctly applied?

Applicability SHALL be extensible.

The Core defines the concept, not the complete list of dimensions.

Possible dimensions include:

- Time
- Jurisdiction
- Organization
- Domain
- Subject
- Audience
- Product
- Role
- Process
- Preconditions
- Exceptions

Projects MAY introduce additional applicability dimensions without changing the SymK Core.

---

## D. Derived Attributes

Derived from other attributes or relationships.

Examples:

- Overall confidence
- Completeness
- Maturity
- Coverage

---

# 4. Applicability

Applicability SHALL NOT be modeled as a scalar property.

Applicability SHALL be modeled as a multidimensional semantic attribute.

Example:

Knowledge Object

    Employer Commission Rule

Applicability

- Time: 2020-01-01 onward
- Organization: Employer X
- Product: Product A
- Role: Sales Representative

Another example:

Knowledge Object

    Osteoporosis Guideline

Applicability

- Domain: Medicine
- Sex: Female
- Menopausal Status: Post-menopause
- Age: ≥ 50 years

---

# 5. Context

Context is intentionally NOT recognized as a Core Primitive.

Context describes the interpretative environment in which a Knowledge Object is analyzed.

Context is independent from Applicability.

Applicability answers:

    "May I apply this Knowledge Object?"

Context answers:

    "How should I interpret this Knowledge Object?"

Future versions may formalize Context as a specialized attribute or as a higher-level semantic construct.

---

# 6. Extensibility Rule

SymK SHALL define attribute classes rather than exhaustive attribute lists.

This allows Domain Cores and Organization Cores to introduce specialized attributes without modifying the SymK Core.

---

# Closing

Knowledge grows in complexity primarily through its attributes and relationships, not by continuously introducing new primitives.

The SymK Core therefore favors a small, stable set of Knowledge Primitives enriched by expressive and extensible Knowledge Attributes.
