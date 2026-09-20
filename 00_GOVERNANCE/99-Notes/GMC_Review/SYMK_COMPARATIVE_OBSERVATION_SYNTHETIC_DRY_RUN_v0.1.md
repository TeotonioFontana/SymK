# SymK Comparative Observation Protocol — Synthetic Dry Run v0.1

**Status:** Completed synthetic evidence; no vocabulary or execution authority  
**Date:** 16 September 2026  
**Protocol under test:** `SYMK_COMPARATIVE_OBSERVATION_AND_VOCABULARY_ADJUDICATION_PROTOCOL_v0.1.md`  
**Fixture:** `SYMK_COMPARATIVE_OBSERVATION_SYNTHETIC_FIXTURE_v0.1.json`

## 1. Purpose

Test whether the proposed protocol prevents ad-hoc semantic decisions when a larger
sample and a changed instrument produce materially different results.

No record in this dry run represents a real document, person, client, proceeding,
library or SharePoint item. The scenario and all counts are synthetic.

## 2. Pre-result controls

The fixture represents a design accepted before result visibility. It freezes:

- prior sample `S1` with 20 synthetic documents;
- new sample `S2` with 200 synthetic documents in three source strata;
- prior instrument `I1`;
- context-aware instrument `I2`;
- prior vocabulary `V1`;
- three primary questions;
- the complete permitted divergence-class set; and
- the non-authoritative purpose of the dry run.

The dry run therefore tests prospective rules rather than inventing categories after
the results.

## 3. Crossed design

All four sample/instrument cells are present:

| | S1 prior sample | S2 new sample |
|---|---|---|
| I1 prior instrument | baseline reproduction | corpus-change view under constant instrument |
| I2 new instrument | instrument-change view under constant sample | candidate improved observation |

This design exposed conclusions that a simple old-versus-new comparison would have
missed.

## 4. Case C1 — `INI` alias

### Observed synthetic result

I1 classified every `INI` token as `initial_petition`. Under I2, the same token split
among `initial_petition`, `initial_bundle_document` and `unresolved`. In S2/I2 the
interpretation also varied materially by source stratum: `court_exports` used the
token predominantly for an initial document in a bundle rather than for a petition.

### Comparative judgment

- primary: `scope_restriction`;
- secondary: `source_heterogeneity`, `instrument_drift`,
  `unsupported_generalization`.

### Dry-run disposition

The observation “token `INI` occurred” remains intact. The global semantic mapping is
restricted. `INI` may continue only as a context-qualified candidate alias pending
Domain adjudication; automatic global mapping is prohibited.

### What the protocol prevented

- choosing S2 merely because it is larger;
- retaining I1 merely because it reproduces the baseline;
- declaring I2 correct merely because it is newer;
- averaging away the source strata; and
- deleting the original token observations when the interpretation changed.

## 5. Case C2 — “initial” phase, event or state

### Observed synthetic result

I1 mapped all relevant signals to `initial_phase`. I2 separated them into procedural
phase, filing event, initial document state and unresolved cases in both samples.

### Comparative judgment

- primary: `specialization`;
- secondary: `semantic_contradiction`, `instrument_drift`.

### Dry-run disposition

The prior concept is not simply renamed. Three candidate semantic dimensions are
opened for review. Prior assertions remain tied to their original vocabulary version
until reviewed or explicitly superseded.

### What the protocol prevented

- treating a lexical similarity as conceptual identity;
- changing the meaning of `initial_phase` without changing its version;
- migrating historical assertions by implication; and
- forcing unresolved cases into one of the new classes.

## 6. Case C3 — technical timestamp versus legal date

### Observed synthetic result

I1 interpreted every source modification timestamp as an issue date. I2 preserved all
timestamps as `source_modified_at` and found no independent evidence supporting an
issue date.

### Comparative judgment

- primary: `unsupported_generalization`;
- secondary: `instrument_drift`.

### Dry-run disposition

The native timestamp remains valid technical metadata. Its legal interpretation is
rejected unless independent evidence supports `issue_date`.

### What the protocol prevented

- deleting a technically correct observation because its interpretation was wrong;
- treating availability of a value as proof of semantic relevance; and
- allowing an operational convenience mapping to become legal meaning.

## 7. Gate results

| Gate | Result | Evidence |
|---|---|---|
| G0 baseline freeze | PASS | S1/I1/V1 and supported/unsupported claims frozen |
| G1 comparative design | PASS | questions, strata, alternatives and classes declared pre-result |
| G2 sample/instrument readiness | PASS for synthetic scope | four comparison cells defined |
| G3 controlled observation | PARTIAL | aggregate synthetic records exist; per-document records intentionally omitted |
| G4 comparative assessment | PASS | three divergences classified with qualifiers |
| G5 Domain adjudication | NOT TESTED | synthetic disposition is not competent legal review |
| G6 vocabulary decision | NOT AUTHORIZED | no vocabulary effect |
| G7 migration/publication | NOT AUTHORIZED | no migration or publication effect |
| G8 monitoring | NOT APPLICABLE | nothing was published |

## 8. Defects and improvements found

### 8.1 Per-observation evidence must be exercised

This fixture uses aggregate synthetic results. Before a live application, a second
dry run should include individual observation records and contradiction links to test
lineage, protected values and recomputation.

### 8.2 Materiality needs an application profile

The general protocol intentionally avoids universal numeric thresholds. The legal
application must define consequence-sensitive criteria before result access.

### 8.3 Reviewer independence needs a concrete rule

The protocol permits proportional role combination. The legal application should
state which divergences require a second reviewer and how disagreement is preserved.

### 8.4 Vocabulary identity rules need machine validation

The dry run preserved historical identities conceptually. A future contract should
test that a term identity cannot retain materially changed meaning without version or
supersession metadata.

### 8.5 Protocol deviations need a tested fail-closed path

No deviation was injected. A subsequent negative-control test should alter a rule
after result visibility and verify that confirmatory conclusions are blocked.

## 9. Assessment of anti-ad-hoc protection

The protocol materially reduced discretion by forcing:

- baseline preservation;
- prospective questions and categories;
- crossed sample/instrument comparison;
- source-stratum inspection;
- separate observation and interpretation;
- explicit alternatives;
- constrained divergence vocabulary;
- independent Domain adjudication before semantic change; and
- separate vocabulary and migration decisions.

It did not eliminate judgment, nor should it. It converted judgment from an implicit
reaction into an attributable, challengeable decision over preserved evidence.

## 10. Dry-run conclusion

**PROVISIONAL PASS WITH OPEN CORRECTIONS.** The proposed protocol successfully prevents
the three tested forms of ad-hoc semantic change. It is not yet ready to govern the
large legal sample because per-observation lineage, negative protocol deviations,
legal materiality and reviewer-independence rules remain untested.

No SharePoint or Graph access, document read, vocabulary change, stage opening,
migration, publication or operational authorization occurred.

