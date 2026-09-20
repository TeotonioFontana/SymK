# SymK — Observation-Led Property Discovery Upstream Proposal v0.1

**Status:** Proposed upstream learning; not accepted, not normative  
**Date:** 16 September 2026  
**Source project:** SPServices / LexBrain property and vocabulary work  
**Target:** SymK project-steward review  
**Interfaces with:** accepted GMC Package D; DR-012 Knowledge Engineering and epistemic distinctions; later competent Methodology, Evidence, Property and Vocabulary work  
**Normative effect:** None

## 1. Purpose

This proposal returns a qualified learning from recent SPServices and LexBrain work:

> Controlled observation was not merely a validation step after a property model had
> been designed. It was a constitutive discovery mechanism that revealed relevant
> property dimensions, exposed invalid semantic shortcuts and changed the model of
> what a property assertion must preserve.

The proposal asks SymK to recognize an explicit **scientific lane** for knowledge-model
formation and evolution. It does not claim that observation alone creates Knowledge,
that empirical frequency determines ontology, or that one project establishes a
universal method.

## 2. Source evidence and bounded claim

The source project inspected a controlled SharePoint sample and preserved distinct
signals for document family, procedural stage, actor role, jurisdiction, legal
identifier and date. The work also exposed important non-entailments:

- a filename token does not entail document meaning;
- a folder position does not entail legal context;
- a technical timestamp does not entail a legal or clinical date;
- a mentioned name does not entail resolved identity;
- an observed signal does not entail a confirmed classification;
- missing evidence does not entail property absence; and
- persistence does not convert a hypothesis into an authoritative assertion.

The preserved public evidence contains aggregate signals and explicit limits rather
than all source literals. The bounded conclusion is therefore methodological: the
observation process improved the property model and its treatment rules. It does not
validate every candidate term or transfer the source vocabulary into SymK.

## 3. Proposed scientific lane

For material knowledge-model work, SymK should keep this lane independently
inspectable:

```text
question / object of inquiry
  → observation design
  → source observation
  → signal or pattern
  → hypothesis
  → controlled test or comparison
  → evidence assessment
  → supported, contradicted or unresolved result
  → qualified upstream learning
```

This lane is reciprocal with, but non-substitutable for, three other lanes:

```text
Scientific lane:  observation → hypothesis → test → evidence
Semantic lane:    concept → property → vocabulary → relationship
Governance lane:  candidate → review → decision → version → validity
Operational lane: extraction → storage → search → automation → publication
```

The lanes are projections over one governed undertaking, not necessarily separate
organizations or sequential departments. Work may iterate across them. Their
distinctions prevent semantic design, authority and implementation from silently
substituting for evidence.

## 4. Proposed rule

For a material property, vocabulary term or mapping, SymK should require a
proportionate account of:

1. the observed or proposed object;
2. the source and source layer;
3. the acquisition or derivation method;
4. the observation, signal or value obtained;
5. the interpretation applied;
6. observation reliability and interpretation confidence separately;
7. uncertainty, missingness, contradiction and alternatives;
8. sensitivity and value-handling constraints;
9. the epistemic state;
10. the reviewing or deciding authority;
11. version and provenance lineage; and
12. permitted and prohibited downstream uses.

The record may be compact where consequence and uncertainty are low. The rule does
not require maximum instrumentation or retention.

## 5. Epistemic transition discipline

The scientific lane should preserve at least these distinctions:

```text
observed
derived
inferred
classified
candidate
verified
contradicted
unresolved
unsupported
asserted
```

These labels are proposed working states, not a final universal SymK enumeration.
The important requirement is that transitions remain explicit. In particular:

- `observed` does not automatically become `classified`;
- `classified` does not automatically become `verified`;
- `verified` does not automatically imply authorization for operational use;
- `asserted` identifies an attributable claim, not truth by declaration; and
- `unresolved` or `not_observed` must not be rewritten as `absent`.

## 6. Property assertion consequence

The source learning challenges the thin representation `property = value`. A
material property assertion may need the following envelope:

```text
property_id
subject_ref
value | protected_value_ref | unresolved
source_layer
acquisition_method
evidence_refs[]
observed_at
confidence
epistemic_state
sensitivity
authority_state
method_or_classifier_version
contradiction_refs[]
```

This is a conceptual requirement proposal, not an implementation schema. SymK should
decide which elements belong to the Property concept, Assertion, Evidence, Context,
Provenance, governance envelope or projection rather than flattening them into one
object.

## 7. Relationship to accepted Package D

This proposal is an upstream evidence bundle under Package D. It reinforces Package
D's separation of observation, signal, Ground, Evidence, assessment and decision,
while adding a narrower finding about **model discovery**:

- observation can reveal candidate property dimensions, not only report progress;
- failed or incomplete observation can reveal method and schema defects;
- contradictions are research inputs rather than noise to discard;
- observation design affects what can responsibly be claimed;
- semantic and operational layers must preserve observation lineage; and
- derived-project learning requires qualified transfer, not silent universality.

Package D already provides the authority boundary: transmission to SymK does not
amend SymK. This proposal therefore remains pending competent review.

## 8. Candidate implications for SymK

If accepted after review, this learning may justify:

1. recognizing the scientific lane in SymK's Knowledge Engineering account;
2. evaluating Observation, Signal, Hypothesis, Evidence and Property as a connected
   but non-collapsed concept cluster;
3. requiring source-layer and acquisition-method provenance for material assertions;
4. preserving negative, contradictory and missing evidence;
5. distinguishing intrinsic semantic character from acquisition origin;
6. introducing observation-led vocabulary discovery guidance;
7. testing whether current Property and Vocabulary artifacts overemphasize semantic
   declaration relative to empirical formation; and
8. adding derived-project cases to future validation of the scientific lane.

## 9. Prohibited inferences

This proposal does not establish that:

- empirical observation is the only route to Knowledge;
- ontology is reducible to corpus statistics;
- frequency establishes truth, importance or authority;
- one SharePoint corpus generalizes to every Domain;
- filenames, folders or technical metadata are reliable semantic authorities;
- every property requires content inspection;
- all proposed epistemic states must become universal SymK primitives;
- the proposed assertion envelope is an accepted schema;
- SPServices or LexBrain may amend SymK by implementation;
- the legal vocabulary is complete or validated; or
- this proposal opens any SymK evolution stage or authorizes implementation.

## 10. Transfer tests required before acceptance

Competent review should test the proposal against at least:

1. a Domain where observation is primarily experimental;
2. a historical or interpretive Domain where source criticism dominates;
3. a mathematical or formal Domain where proof is not ordinary empirical observation;
4. a high-sensitivity Domain where literals cannot be retained;
5. a sparse-data case where `unknown` is common;
6. a conflicting-source case;
7. an adversarial or manipulated-data case;
8. an operational system where inference is useful before verification; and
9. a low-consequence case where the full envelope would be disproportionate.

These tests should determine scope, exceptions, proportionality and whether
“scientific lane” is the correct term across Domains.

## 11. Open questions

- Is the scientific lane a universal SymK view, a Knowledge Engineering method, or a
  Domain-configurable profile?
- Does Observation require a separate primitive, or is it a qualified Event/Record?
- How should Evidence relate to Observation, Ground, Assertion and Authority?
- Which epistemic states are primitive, profiles or lifecycle labels?
- How should absence, non-observation, unsupported format and failed access differ?
- Where should contradiction live: Evidence, Assertion, assessment or all through
  linked records?
- How should privacy-preserving fingerprints participate in evidence without being
  mistaken for the source value?
- What is the minimum sufficient observation envelope under proportional governance?

## 12. Requested disposition

The project steward is asked to choose one of:

- **admit for governed evaluation** as a qualified Package D upstream proposal;
- **return for correction** with stated deficiencies;
- **defer** to a named competent stage or work package; or
- **reject** with preserved rationale.

Admission would authorize evaluation only. It would not accept the scientific lane,
amend a Foundation Paper, create a primitive, open a stage or authorize implementation.

## 13. Source references

- `lauramendonca_property_audit.md` — local evidence reconstruction and gaps.
- `lexbrain_legal_vocabulary_stage_handoff_v0_1.md` — downstream consolidation and
  controlled next-stage proposal.
- SPServices `SPS_SPP1A_A3_SECOND_LIVE_EXECUTION_EVIDENCE_v0_1.md` — bounded legal
  sample observation.
- SPServices `SPS_SPP1B_M3_STAGE2_EXACT_ONE_RUN_EXECUTION_EVIDENCE_v0_1.md` —
  fail-closed metadata observation and response-shape learning.
- SymK `SYMK_GMC_PACKAGE_D_OBSERVATION_PAUSE_PIVOT_AND_UPSTREAM_LEARNING_PROPOSAL_v0.1.md`
  — accepted upstream-learning boundary.

