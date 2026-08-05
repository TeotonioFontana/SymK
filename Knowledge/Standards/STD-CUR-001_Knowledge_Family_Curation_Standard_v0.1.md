# STD-CUR-001 --- Knowledge Family Curation Standard

**Identifier:** STD-CUR-001\
**Status:** Draft v0.1\
**Category:** SymK Standard\
**Scope:** All SymK Knowledge Families

------------------------------------------------------------------------

# 1. Purpose

This standard defines how every SymK Knowledge Family shall be curated,
documented, reviewed and evolved.

Its objective is to ensure that every family follows the same editorial
and engineering process.

------------------------------------------------------------------------

# 2. Guiding Principles

1.  Preserve knowledge.
2.  Preserve provenance.
3.  Separate knowledge from editorial metadata.
4.  Never discard historical artifacts without explicit justification.
5.  One canonical asset per knowledge artifact.
6.  Editorial decisions must be documented.

------------------------------------------------------------------------

# 3. Canonical Knowledge Family Structure

    Family/

        README.md

        Canonical/
        Sources/
        Curation/
        Assets/

### Canonical

Authoritative knowledge assets currently endorsed.

### Sources

Historical drafts, notes, imports and legacy material.

### Curation

Editorial artifacts governing the family.

Typical contents:

-   Inventory
-   Lineage
-   Canonical Assessment
-   Decision Log
-   Roadmap
-   Quality Report
-   Open Questions

### Assets

Supporting resources:

-   images
-   CSS
-   diagrams
-   templates
-   illustrations

------------------------------------------------------------------------

# 4. Mandatory Curation Artifacts

Every Knowledge Family should eventually contain:

-   README
-   INVENTORY
-   LINEAGE
-   CANONICAL_ASSESSMENT
-   DECISION_LOG
-   ROADMAP
-   QUALITY_REPORT
-   OPEN_QUESTIONS

------------------------------------------------------------------------

# 5. Canonical Asset

A canonical asset is the current authoritative representation of a
knowledge artifact.

Selection criteria include:

-   conceptual completeness
-   consistency
-   architectural maturity
-   traceability
-   maintainability

The newest version is not automatically canonical.

------------------------------------------------------------------------

# 6. Historical Assets

Historical assets remain valuable because they preserve the evolution of
ideas.

Historical artifacts should normally remain in Sources.

------------------------------------------------------------------------

# 7. Editorial Decisions

Every significant curation decision shall be recorded with:

-   identifier
-   date
-   decision
-   rationale
-   impact

------------------------------------------------------------------------

# 8. Definition of Done

A Knowledge Family is considered curated when a newcomer can determine:

-   the canonical document;
-   how it evolved;
-   why it is canonical;
-   remaining work;
-   supporting material;
-   documented editorial decisions.

------------------------------------------------------------------------

# 9. Future Evolution

This standard is expected to evolve as SymK matures. Changes shall
preserve backward traceability whenever practical.
