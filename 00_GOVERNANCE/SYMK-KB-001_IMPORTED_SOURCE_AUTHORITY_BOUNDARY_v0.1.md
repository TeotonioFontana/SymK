# SYMK-KB-001 — Imported Source Authority Boundary

**Status:** Canonical repository-control interpretation
**Version:** 0.1
**Effective date:** 2026-09-06
**Authority:** Existing SymK authority and registration rules, made explicit through
project-steward authorization to repair the 2026-09-06 full consistency inspection
findings step by step
**Scope:** Imported, recovered and candidate material under `Knowledge/`,
`REVIEW_QUEUE/`, `Supporting papers/` and equivalent evidence locations
**Constitutional effect:** None

## 1. Purpose

This boundary prevents source text from acquiring SymK authority through its own
labels, wording, filename or directory placement. It applies the existing rule that
canonical location, normative force, epistemic authority, external authority and
implementation fact are distinct.

## 2. Default status of imported sources

A file under a `Sources/` directory is preserved **source evidence**. Unless a
separate governed disposition says otherwise, it is:

- not a canonical SymK policy, standard, method, architecture or vocabulary;
- not constitutionally Ratified or Stage-Accepted;
- not automatically applicable to SymK, a derived project or production;
- not execution, release, deployment or blocking authority; and
- not evidence that the source's claims are true, current or compatible with SymK.

Internal source labels such as “canonical,” “normative,” “mandatory,” “Stable,”
“MUST,” or “blocks production” are preserved as claims made by that source. They do
not activate those effects in SymK.

## 3. Admission gate

Imported content gains a governed SymK role only through a separate disposition
that identifies proportionately:

1. the exact object or immutable locator;
2. its artifact identity, version and status;
3. the accepted scope, jurisdiction and intended use;
4. the competent owner and accepting authority;
5. its effective date and any review or expiry condition;
6. conflicts, prohibited inferences and supersession lineage; and
7. its registration in the applicable canonical index.

Admission may classify all, part or none of a source as evidence, a candidate,
guidance, a policy, a standard, a reference model, a canonical asset or historical
material. One admitted passage does not transfer authority to the remainder.

## 4. Knowledge-family layout

Within each `Knowledge/<Family>/` directory:

- `Sources/` preserves imported or recovered evidence without SymK authority;
- `Curation/` holds inventories, assessments, decisions, lineage and open questions;
- `Canonical/` may hold governed family artifacts only after explicit disposition;
- `Assets/` holds supporting resources and gains no authority by placement; and
- the family `README.md` routes readers to this boundary and the current curation
  state.

A file in `Canonical/` is not authoritative solely because of that directory name.
The governing disposition and canonical registry remain necessary.

## 5. Conflict and precedence rule

When an imported source conflicts with a registered SymK control, the registered
control governs SymK within its scope. The conflict remains visible for curation; it
must not be silently resolved by editing preserved evidence or by choosing the more
forceful wording.

The following source claims therefore have no present repository-wide authority:

- web-product architecture source claims that call themselves canonical policy;
- API-documentation source claims that call OpenAPI mandatory or production-
  blocking;
- PLC reference-manual claims that call a working draft canonical; and
- either imported coding-rules version's claim to govern all repository Python.

They remain available for later review and exact, bounded disposition.

## 6. Preservation and non-effects

This boundary does not delete, rewrite, reject or validate any imported source. It
does not select a canonical Knowledge asset, settle competing source versions,
create a production requirement, amend accepted decisions, open an evolution stage
or create constitutional force.

## 7. Challenge and revision

The boundary remains challengeable through project governance. Any replacement must
preserve this version's lineage and state which source classes, authority tests or
effects change.
