# SymK Comparative Observation and Vocabulary Adjudication Protocol v0.1

**Status:** Proposed; not accepted; not operational authority  
**Date:** 16 September 2026  
**Purpose:** convert observation-led learning into a repeatable Knowledge Engineering process  
**Source learning:** SPServices / LexBrain property and vocabulary discovery  
**Depends on:** SymK Package D; prohibited-inference controls; observation-led property-discovery upstream proposal  
**Normative effect:** None until separately accepted by competent authority

## 1. Decision problem

When a later observation produces results that differ materially from an earlier
observation, Knowledge Engineering must not silently prefer the newer, larger, more
convenient or already operational result. It must determine whether the difference
is caused by:

- increased coverage;
- population or sample composition;
- source heterogeneity;
- acquisition or instrument change;
- interpretation or vocabulary change;
- temporal or contextual drift;
- error, bias or unsupported inference;
- genuine contradiction; or
- insufficient evidence.

This protocol governs that determination for material property and vocabulary work.

## 2. Governing rule

> No material observation result may directly rewrite a prior observation, governed
> vocabulary or accepted assertion. A difference must first become a versioned
> comparative assessment with explicit evidence, uncertainty, alternatives and
> competent adjudication.

The protocol preserves three independent objects:

```text
Prior observation O1
New observation O2
Comparative assessment C(O1,O2)
```

An adjudication may change the status or permitted use of an interpretation. It does
not change the historical bytes, identity or declared result of either observation.

## 3. Scope

Apply this protocol when a new observation may materially affect:

- a Property definition;
- a Vocabulary concept or hierarchy;
- an alias or lexical mapping;
- an evidence-to-concept mapping;
- a classifier, extractor or observation rule;
- a profile-specific interpretation;
- an accepted or published assertion class;
- a source-population generalization; or
- an operational dependency on any of the above.

Routine repetition with no material difference may use a proportionate short-form
receipt. Privacy, safety, legal and Domain-specific requirements remain independently
applicable.

## 4. Non-substitution boundaries

The protocol keeps distinct:

- source value and protected representation;
- observation and interpretation;
- observation reliability and semantic confidence;
- sample frequency and conceptual importance;
- population difference and temporal drift;
- instrument drift and source drift;
- contradiction and heterogeneity;
- statistical materiality and Domain materiality;
- reviewer agreement and truth;
- adjudication and implementation;
- accepted vocabulary change and migration authority; and
- `absent`, `not_observed`, `unknown`, `inaccessible` and `unsupported`.

## 5. Required lifecycle

```text
G0 baseline freeze
  → G1 comparative-design acceptance
  → G2 instrument and sample readiness
  → G3 controlled observation
  → G4 comparison and divergence classification
  → G5 Domain adjudication
  → G6 vocabulary decision
  → G7 migration/publication decision
  → G8 post-decision monitoring
```

No gate entails the next gate. Vocabulary acceptance does not authorize migration,
publication or retrospective reclassification.

## 6. G0 — Baseline freeze

Before examining the new result, preserve:

1. prior observation identities and checksums;
2. prior sample definition and known exclusions;
3. prior instrument, rules, configuration and versions;
4. prior vocabulary and mappings;
5. prior hypotheses and decisions;
6. unresolved cases, contradictions and unsupported formats;
7. known privacy-driven evidence losses;
8. current operational consumers and reliance; and
9. the exact claims that the prior evidence does and does not support.

The freeze does not declare the baseline correct. It prevents retrospective editing.

## 7. G1 — Comparative-design acceptance

The design must be recorded before semantic results are inspected. It declares:

- question and decision purpose;
- target population;
- sampling frame and method;
- stratification variables;
- inclusion and exclusion rules;
- expected sources of heterogeneity;
- primary and secondary comparisons;
- hypotheses and credible alternatives;
- possible falsifying or restricting outcomes;
- missingness and unsupported-format treatment;
- planned uncertainty assessment;
- materiality criteria;
- stopping conditions;
- privacy and retention controls; and
- authorized uses of the result.

Exploratory observation is permitted, but it must be labeled exploratory and cannot
be retrospectively presented as confirmatory.

## 8. G2 — Instrument and sample readiness

The readiness record freezes:

- sample manifest or reproducible sample-selection method;
- stable opaque subject identities;
- extractor, classifier, parser and rule versions;
- vocabulary version used during interpretation;
- environment and relevant dependencies;
- expected input and output shapes;
- known false-positive and false-negative modes;
- access, privacy and retention controls;
- reviewer instructions and blinding where applicable;
- comparison implementation and tests; and
- rollback/stop behavior.

### 8.1 Instrument/source separation

Where practicable, use the crossed design:

| | Prior sample S1 | New sample S2 |
|---|---:|---:|
| Prior instrument I1 | required baseline | required source-change comparison |
| New instrument I2 | required instrument-change comparison | candidate improved observation |

This distinguishes changes caused by the corpus from changes caused by the method.
If one cell cannot be run, the resulting limitation must constrain the conclusion.

## 9. G3 — Per-observation scientific record

Each material observation must preserve, directly or through resolvable references:

```text
observation_id
subject_ref
observation_target
source_layer
source_property_or_region
observed_value | protected_value_ref | value_not_retained
outcome
acquisition_method
instrument_version
observation_time
scope_ref
evidence_refs[]
sensitivity
value_handling
observation_reliability
candidate_interpretations[]
semantic_confidence
epistemic_state
limitations[]
contradiction_refs[]
```

Allowed outcomes must distinguish at least:

- `present`;
- `absent_within_observation_scope`;
- `not_observed`;
- `unknown`;
- `inaccessible`;
- `unsupported`;
- `malformed`; and
- `observation_failed`.

The source literal may be deleted or withheld when required. Its scientific handling,
existence, method, protected reference, loss and limitations must remain inspectable.

## 10. G4 — Comparative assessment

Comparison occurs at both aggregate and observation levels. Aggregate totals must not
erase strata, rare but consequential cases, contradictions or missingness.

For each material difference, the assessor records:

1. affected property, term, mapping or method;
2. prior and new results;
3. absolute and relative change where meaningful;
4. distribution across declared strata;
5. missingness and unsupported cases;
6. instrument contribution;
7. source-population contribution;
8. temporal/contextual contribution;
9. credible alternative explanations;
10. consequence if accepted, ignored or misclassified;
11. confidence and residual uncertainty; and
12. proposed divergence class.

## 11. Divergence classes

Each material difference receives one primary class and zero or more secondary
qualifiers.

| Class | Meaning | Default consequence |
|---|---|---|
| `replication` | compatible result under comparable conditions | strengthen evidence; no automatic semantic change |
| `coverage_extension` | new observations within the prior concept's scope | expand support/coverage |
| `alias_extension` | new expression for an existing concept | review alias mapping |
| `specialization` | one concept separates into justified narrower concepts | propose hierarchy change |
| `scope_restriction` | prior definition or mapping is too broad | restrict claim/use; assess affected assertions |
| `semantic_contradiction` | comparable evidence supports incompatible interpretations | suspend automatic promotion; adjudicate |
| `observational_contradiction` | comparable observations disagree about the source phenomenon | investigate provenance/instrument/source |
| `source_heterogeneity` | differences follow stable source strata | create contextual profile or qualified scope |
| `temporal_drift` | differences follow time under comparable method | version temporal validity |
| `instrument_drift` | difference follows method/version | validate instrument; do not attribute to corpus |
| `sampling_effect` | difference is explained by sampling frame/composition | qualify generalization |
| `data_quality_failure` | malformed, duplicated, inaccessible or corrupted source materially affects result | correct or constrain result |
| `unsupported_generalization` | evidence does not justify claimed wider scope | retract/restrict general claim |
| `inconclusive` | available evidence cannot distinguish credible explanations | retain unresolved state |

No numeric majority automatically selects a class.

## 12. Materiality

Materiality is multidimensional. The design must consider proportionately:

- magnitude and frequency;
- uncertainty and reliability;
- distribution across strata;
- legal, clinical or Domain significance;
- reversibility;
- consequence of false positive and false negative;
- number and importance of dependent assertions;
- affected persons and rights;
- operational reliance;
- security and privacy impact; and
- cost of delayed versus premature change.

A rare result may be material. A statistically visible result may be semantically
irrelevant. Materiality is an assessment requiring declared authority.

## 13. G5 — Domain adjudication

The Domain adjudicator does not rerun the observation implicitly. The adjudicator
reviews the comparative record and decides among:

- accept divergence classification;
- correct classification;
- request additional evidence;
- retain competing interpretations;
- declare context-specific profiles;
- suspend a mapping or term from automatic use;
- preserve unresolved status; or
- reject the proposed semantic consequence.

The record must include rationale, dissent, conflicts of interest, scope and expiry or
review conditions. Human agreement is evidence about review, not proof of truth.

## 14. G6 — Vocabulary decision

Vocabulary change decisions are limited to:

- no change;
- evidential support strengthened or weakened;
- alias added, restricted, deprecated or rejected;
- definition clarified without semantic change;
- scope restricted;
- concept specialized or generalized;
- concept added;
- concept deprecated but retained for lineage;
- mapping relation changed;
- mapping suspended;
- term retained as unresolved; or
- proposal rejected.

Every change must identify the prior version, new version, evidence and adjudication.
Previously published identities must not be silently repurposed.

## 15. G7 — Migration and publication

Semantic acceptance and operational migration are separate decisions. Migration must
assess:

- existing assertions and packages;
- search and automation behavior;
- compatibility mappings;
- reprocessing scope;
- rollback;
- affected users;
- auditability;
- communication; and
- whether historical assertions remain valid under their original version.

Default rule: historical observations remain fixed; historical assertions retain
their original vocabulary reference unless an explicit, recorded migration creates a
new assertion or supersession relation.

## 16. G8 — Monitoring

After publication or migration, monitor proportionately for:

- unexpected unclassified rates;
- new contradictions;
- distribution shifts;
- reviewer disagreement;
- operational misclassification;
- affected-subject challenge;
- privacy or retention failures;
- excessive governance cost; and
- evidence that the adjudication's scope was too broad.

Monitoring can trigger review. It does not automatically amend the vocabulary.

## 17. Roles and separation of authority

| Role | Responsibility | Cannot alone |
|---|---|---|
| Observation designer | defines question and method | accept vocabulary change |
| Sample custodian | establishes population/sample lineage | interpret legal meaning |
| Instrument owner | versions and validates extraction | adjudicate its own semantic result alone |
| Observation operator | executes approved procedure | change criteria after result |
| Comparative assessor | classifies differences and alternatives | publish vocabulary change |
| Domain reviewer | evaluates Domain meaning | rewrite observations |
| Vocabulary steward | decides versioned vocabulary disposition | authorize operational migration by implication |
| Operational authority | decides migration/publication | manufacture semantic acceptance |
| Challenge reviewer | hears conflicts and correction requests | erase dissent or source evidence |

One person may occupy multiple roles in a small project, but the record must identify
which role and authority supports each act. High-consequence cases require independent
review proportionate to risk.

## 18. Anti-ad-hoc controls

The following are prohibited unless recorded as a protocol deviation and separately
reviewed:

- changing hypotheses after seeing results without marking them exploratory;
- changing inclusion rules to obtain a preferred distribution;
- changing instrument versions mid-run without partitioning results;
- merging `unknown`, `unsupported` or `failed` into `absent`;
- selecting only favorable strata;
- using sample size alone to settle semantic disagreement;
- replacing prior observation bytes or identity;
- promoting a classifier output directly to governed truth;
- resolving disagreement by unrecorded consensus;
- changing a concept's meaning while retaining its identity without versioning; and
- presenting operational adoption as scientific validation.

## 19. Minimum artifact set

Every material application produces:

1. Baseline Freeze Record;
2. Comparative Observation Plan;
3. Sample and Instrument Manifest;
4. Observation Batch;
5. Comparative Assessment Report;
6. Divergence Register;
7. Domain Adjudication Record;
8. Vocabulary Change Decision;
9. Migration/Publication Decision, when applicable; and
10. Monitoring/Challenge Record, when applicable.

Templates accompanying this proposal define minimum fields but carry no execution
authority.

## 20. Quality and acceptance tests

A comparative package fails closed if:

- the baseline was changed after G0;
- sample or instrument identity is unavailable;
- observation and interpretation cannot be separated;
- material missingness is concealed;
- the comparison merges incompatible populations without qualification;
- divergence is classified without credible alternatives;
- Domain adjudication lacks attributable authority;
- a vocabulary decision lacks evidence lineage;
- publication is treated as automatic after semantic acceptance; or
- protected evidence was handled outside its declared policy.

## 21. Initial SPServices/LexBrain application

For the planned larger legal-document sample:

- the existing 11-document evidence becomes the frozen prior baseline;
- the current extractor/rule release becomes I1;
- the larger sample becomes S2 with declared strata;
- any improved instrument becomes I2;
- the four-cell crossed comparison is attempted;
- the six observed legal dimensions are compared independently;
- aliases such as `Ini`, `Manif` and `Contest` remain hypotheses until observed and
  adjudicated;
- the unsupported legacy `.doc` and prior contradiction remain visible; and
- no vocabulary change occurs before G5/G6.

## 22. Prohibited inferences

This proposal does not establish that:

- the prior baseline is scientifically sufficient;
- a larger sample is automatically more representative;
- every Domain requires the same sampling or statistical method;
- every material decision requires quantitative significance testing;
- the listed divergence classes are exhaustive forever;
- Human review is infallible;
- an accepted vocabulary is true outside its scope;
- preservation requires retaining prohibited literals;
- this protocol authorizes SharePoint access or a new observation run; or
- this document is already accepted SymK methodology.

## 23. Requested disposition

The project steward is asked to admit, correct, defer or reject this protocol. If
admitted, the first authorized use should be a dry run with synthetic or already
permitted evidence before any large live legal-document observation.

