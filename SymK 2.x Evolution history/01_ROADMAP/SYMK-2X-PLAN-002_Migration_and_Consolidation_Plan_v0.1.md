# SymK 2.x Migration and Consolidation Plan

**Identifier:** SYMK-2X-PLAN-002
**Version:** 0.1
**Status:** Proposed — awaiting project-steward review
**Prepared:** 18 August 2026
**Repository inspected:** `/Users/teotonio/Projetos/SymK`
**Scope:** Recovery and replacement of the working plan from the accepted 2.0 baseline through the 3.0 release gate

---

## 1. Executive decision

SymK should **continue from its accepted 2.0 and 2.1 decisions**, not restart its conceptual work and not treat the current repository layout as authoritative merely because material is stored in a canonical-looking directory.

The recovered sequence remains broadly sound:

1. 2.0 — Identity and Jurisdiction
2. 2.1 — Foundational Conceptual System
3. 2.2 — Constitutional Axiom Set
4. 2.3 — Constitutional Governance
5. 2.4 — Legacy Disposition
6. 2.5 — Foundational Concepts and Principles
7. 2.6 — Derived-Project Governance
8. 2.7 — Grounding Validation
9. 2.8 — Corpus Consolidation
10. 2.9 — Engineering Readiness
11. 3.0 — First consolidated SymK release

The sequence requires one structural correction: **corpus recovery, evidence preservation, lineage reconstruction, and repository hygiene must begin now as a continuous migration-control track**. They cannot safely be deferred until 2.8. Stage 2.8 should be the point at which that work is completed, audited, and published—not the point at which it begins.

This plan therefore establishes three coordinated lanes:

- **Semantic and constitutional lane:** the numbered 2.x stages in dependency order.
- **Corpus-integrity lane:** continuous evidence recovery, classification, lineage, and controlled physical migration.
- **Grounding and verification lane:** counterexamples and project evidence accumulated early, with formal validation at 2.7 and engineering conformance at 2.9.

No SymK repository file was changed while preparing this plan.

---

## 2. Inspection basis

The inspection covered the live working tree, Git history and status, governance records, the complete 2.0 and 2.1 working areas, Knowledge Families, migration reports, the review queue, the nested `SymK/` tree, and the readable content of Markdown, Word, PDF, and workbook artifacts.

The following archives were inspected recursively:

- `00_GOVERNANCE.zip`
- `REVIEW_QUEUE/1_Discovery.zip`
- `REVIEW_QUEUE/project_init.zip`
- `SymK 2.x Evolution history/2.1.zip`

No archive contained another archive. The `2.1.zip` content is byte-equivalent to the live 2.1 directory and is therefore a checkpoint of the current, still-uncommitted 2.1 state. The governance ZIP is an older historical checkpoint containing material no longer aligned with the live governance corpus.

### 2.1 Repository condition at inspection

- The outer repository was on `master`, six commits ahead of `origin/master`.
- The working tree contained ten modified 2.1 control files and two untracked, filename-corrupted standards-source files.
- There were approximately 934 tracked files; about 552 were under `REVIEW_QUEUE`.
- Approximately 449 review-queue files were flattened Git object payloads with hexadecimal filenames, not reviewable SymK documents.
- The root and Knowledge Family structures contained many placeholders: 170 of 344 Markdown files outside `.git` and `REVIEW_QUEUE` contained three lines or fewer.
- The nested `SymK/` directory was not a functioning independent Git repository and did not constitute an engineering-ready implementation.
- No meaningful automated test corpus was found outside historical or quarantined material.

These facts do not invalidate the conceptual work. They do mean that repository location, tracked state, and apparent completeness cannot be used as proxies for authority, maturity, or readiness.

---

## 3. Recovered authority baseline

### 3.1 Decisions that control this plan

| Area | Decision/status | Consequence |
|---|---|---|
| 2.0 | Stage-Accepted on 18 August 2026 through DR-008 | SymK is a discipline for designing Intelligence Amplification systems; its purpose, jurisdiction, layer model, tensions, and migration readiness govern later work. |
| 2.1.1 | DR-009 Stage-Accepted | Foundationality is tested by necessity for SymK coherence; disposition, maturity, and artifact form are separate; human- and machine-semantic lanes must remain distinguishable. |
| 2.1.2 | DR-010 approved by the project steward on 18 August 2026 | Identity, Context, Scope, Domain, and Representation form the structural kernel; Relationship, Applicability, Bearer, and Projection are supporting distinctions; System is imported support; Entity loses foundational status pending a 2.5 engineering/meta-model decision. |
| 2.1.2 repository surfaces | Synchronized as Stage-Accepted on 18 August 2026 | The maturity and authority fields now reflect the project-steward decision without expanding its meaning or migrating canonical concept artifacts. |
| Constitution vNext | Proposed/candidate, not Ratified | Candidate axioms and jurisdictional clauses may be evaluated, but they do not yet possess constitutional authority. |
| Legacy axioms and principles | Registered historical/canonical material pending disposition | They remain evidence and possible inherited authority claims; their location does not immunize them from 2.4 disposition. |
| Foundation papers v0.1 | Working foundation evidence | They must be revised after the integrated 2.1 baseline because several still describe cooperation as SymK's objective rather than a process or mode. |

### 3.2 Authority rule

The governing distinction is:

> **Canonical location is not maturity, and maturity is not constitutional authority.**

Archives, imported files, candidate documents, and registered legacy material are evidence unless and until the appropriate decision process gives them a stronger status.

### 3.3 Transitional authority

Until 2.3 constitutes formal governance, the project steward may Stage-Accept work under the existing evolution-governance process. Ratification must remain unavailable. Stage 2.3 must include a transition clause that:

1. acknowledges the interim project-steward authority used for 2.0–2.3;
2. constitutes the enduring ratification authority;
3. defines whether and how the new authority reviews earlier Stage-Accepted decisions; and
4. prevents a circular claim that the candidate constitution ratified the governance mechanism that gave the constitution its authority.

---

## 4. Structural diagnosis

### 4.1 What should be preserved

- The 2.0 identity, jurisdiction, layer, tension, and migration decisions.
- The 2.1.1 evaluation method and its explicit separation of semantic status from artifact form.
- The 2.1.2 structural kernel and its refusal to make Entity universally foundational.
- The original division between conceptual, constitutional, legacy, packaging, derived-project, validation, consolidation, and engineering stages.
- Historical sources, dissent, abandoned alternatives, and contradictory artifacts as evidence.

### 4.2 What must change

1. **Status synchronization must precede new conceptual work.** Completed on 18 August 2026: DR-010 and all affected 2.1 status surfaces now record Stage-Acceptance.
2. **Corpus integrity cannot wait until 2.8.** The review queue contains both potentially important historical artifacts and hundreds of flattened Git objects; it must be processed by manifest, not treated as one disposable directory.
3. **Knowledge Families cannot be presumed complete.** Their curation sets and canonical claims are mostly placeholders, and one purported canonical white paper is explicitly mock content.
4. **Constitutional candidacy and ratification must be separated.** Stage 2.2 prepares and Stage-Accepts a candidate; Stage 2.3 creates authority and conducts ratification under a transition rule.
5. **Legacy semantic disposition must precede physical consolidation.** Stage 2.4 decides what inherited materials mean and whether they survive; 2.8 completes their placement and publication.
6. **Concept packaging must follow conceptual integration.** Existing FC, FP, primitive-methodology, JSON/YAML, and projection scaffolds cannot dictate the ontology they are supposed to express.
7. **Grounding must produce counterevidence, not ceremonial translations.** LexBrain and sshConnectivity should challenge SymK with materially different systems and failure cases.

---

## 5. Operating model for the migration

### 5.1 The three lanes

```text
Semantic / constitutional lane
M0 → 2.1 → 2.2 → 2.3 → 2.4 → 2.5 → 2.6 → 2.7 → 2.8 → 2.9 → 3.0

Corpus-integrity lane
C0 Inventory → C1 Recovery → C2 Lineage → C3 Curation → C4 Physical migration → C5 Publication

Grounding / verification lane
V0 Examples → V1 Counterexamples → V2 Project trials → V3 Cross-project validation → V4 Conformance
```

The lanes exchange evidence but do not exchange authority. A source discovered by the corpus lane does not become normative automatically. A conceptual decision does not authorize deletion of its historical sources. A successful project translation does not, by itself, establish universal semantics.

### 5.2 Decision flow

Every material decision continues to follow:

```text
Question
  → evidence and source lineage
  → alternatives
  → compatibility tests and counterexamples
  → proposed decision
  → dissent, consequences, and deferred questions
  → Stage-Acceptance
  → authorized migration
  → verification
```

### 5.3 Stage completion rule

A numbered stage is complete only when its acceptance record covers:

- scope and explicit exclusions;
- disposition of every scheduled work package;
- traceability from evidence to decisions;
- compatibility tests and counterexamples;
- preserved dissent and deferred questions;
- affected artifacts and derived projects;
- canonical consistency checks;
- a plain-language summary; and
- named authority, decision status, and date.

---

## 6. Replacement stage plan

### M0 — Migration control point

**Purpose:** Establish a trustworthy starting state before 2.1.3.

**Required work:**

1. Record DR-010 as Stage-Accepted on 18 August 2026 in every affected 2.1 status surface, without changing the substance of the approved proposal.
2. Reconcile the 2.1 README, Summary, Change Log, Decision Register, Concept Register, Tension Register, Deferred Questions, Evidence Register, and foundation-paper revision ledger.
3. Preserve an evidence snapshot of the current tree, current commit, working-tree changes, ignored ZIP checkpoints, and file hashes.
4. Create a corpus manifest whose minimum fields are path, artifact identifier, family, format, provenance, authority status, maturity status, lineage parent, duplicate group, encoding condition, and proposed disposition.
5. Mark archives explicitly as historical checkpoints or backups; do not let an archive silently outrank a live governed artifact.
6. Separate reversible quarantine/recovery work from semantic disposition.

**Approval checkpoint M0:** The project steward confirms that the status synchronization faithfully records DR-010 and that the evidence snapshot is adequate. This checkpoint does not approve the replacement plan's later semantic decisions.

**Dependency:** M0 is required before opening DR-011.

**Pause-closure state — 18 August 2026:** The DR-010 status reconciliation, Git/evidence checkpoint, explicit non-opening of 2.1.3, preserved next question, and Observed-only maturation channel are complete. The full corpus manifest and archive-classification portions of M0 remain pending and must be completed before DR-011 is opened; they do not prevent the two- or three-day pause.

**Return state — 20 August 2026:** The repository-wide corpus manifest, explicit classification of all four archives, reversible recovery/semantic-disposition boundary, and maturation routing are complete as a Proposed M0 completion under `M0_CORPUS_CONTROL_COMPLETION_2026-08-20.md`. Project-steward confirmation remains pending. No 2.1.3 analysis or DR-011 content has been opened.

**Acceptance state — 20 August 2026:** The project steward approved the M0 corpus-control completion through `M0_ACCEPTANCE_RECORD_2026-08-20.md`. M0 is closed and its dependency preceding 2.1.3 is satisfied. This checkpoint does not accept this migration plan as a whole or create DR-011 content.

---

### 2.1 — Foundational Conceptual System

**Current state:** 2.1.1 through 2.1.7 are Stage-Accepted and M0 is accepted. Revised `SYMK-2X-DR-012`, `SYMK-2X-DR-013`, `SYMK-2X-DR-014`, and `SYMK-2X-DR-015` close 2.1.4 through 2.1.7 for progression with their complete lineages preserved. Under `SYMK-2X-EV-137`–`138`, 2.1.8 is formally open. Streams A–F evidence `SYMK-2X-EV-139`–`144` establishes and consolidates the complete Question/Reasoning/Answer/quality/time/cost/Value/outcome/consequence/feedback/correction/Learning system. Stream G evidence `SYMK-2X-EV-145` creates complete Proposed DR-016: Question, Reasoning, Answer, and Value are proposed Foundational concepts; Complex Question is proposed as supporting qualification; all adjacent families are individually routed; DR-013 dispositions remain unchanged; and the DQ-014 universal conceptual answer is proposed. DR-016 awaits project-steward review and has no normative authority. No accepted new disposition or DQ answer, metric, model, threshold, weight, benchmark, objective, optimization, policy, Foundation Paper revision, implementation, project change, 2.1.9 opening, final-stage decision, Ratification, or commit is authorized.

#### 2.1.3 — Knowledge and Intelligence

Resolve the reciprocal boundary between Knowledge and Intelligence. At minimum:

- define what each term does for SymK;
- identify possible bearers and the conditions for attribution;
- distinguish capability, competence, skill, performance, and adaptation;
- determine whether Intelligence is constitutively multidimensional and distinguish capability dimension, specialization, actual configuration, attributed profile, and score or classification Projection;
- distinguish the universal concept from a particular actual Bearer and from a fallible attribution identifying a proposed Bearer;
- separate an intelligence attribution from a representation of performance;
- state the roles of substrate, organized system, Context, Scope, Domain, and Applicability;
- keep agency, autonomy, rationality, and consciousness distinct unless evidence requires a dependency; and
- determine which epistemic questions must remain open for 2.1.4.

#### 2.1.4 — Knowledge Engineering and epistemic conditions

Resolve knowledge claims, knowledge assets, epistemic status, evidence, provenance, validation, Representation, and Projection. Establish why Knowledge Engineering engineers epistemic conditions rather than merely extracting or storing information.

#### 2.1.5 — Cooperation and cooperative formation

Resolve cooperation, learning, instruction, training, education, socialization, coordination, participation, and formation. Preserve the 2.0 ruling that cooperation is a process or mode within SymK—not SymK's overriding objective. Address coercion, asymmetry, dissent, and power.

#### 2.1.6 — Responsibility, agency, and authority

Resolve bearer-specific responsibility, attribution, agency, autonomy, authorization, accountability, obligation, and distributed responsibility. Prevent capability or system participation from silently implying agency, authority, or moral responsibility.

#### 2.1.7 — Amplified Intelligence and DIA

Integrate the preceding clusters into a defensible account of Intelligence Amplification and SymK's identity as a discipline. Define what is amplified, for whom, under which Context and Scope, by which mechanisms, and with which limits.

#### 2.1.8 — Reasoning, answers, value, and feedback

Resolve reasoning, inference, answer, recommendation, decision support, value, utility, benefit, cost, feedback, correction, and learning loops. Keep epistemic success, practical usefulness, authorization, and truth from collapsing into one measure.

#### 2.1.9 — Integrated conceptual baseline

Produce one dependency graph and one boundary-controlled vocabulary. Audit all accepted clusters for circular definitions, unacknowledged bearers, implicit scope, domain leakage, mismatched human/machine semantics, and unhandled tensions.

#### 2.1.10 — Foundation-paper review, revision, and human communication

After 2.1.9, review the four preserved v0.1 publication units before preparing v0.2:

- `SymK_Foundation_Paper_Intelligence_v0.1.md` and its PDF projection;
- `SymK_Foundation_Paper_Knowledge_v0.1.md` and its PDF projection;
- `SymK_Foundation_Paper_Knowledge_Engineering_v0.1.md` and its PDF projection; and
- `SymK_Foundation_Paper_Education_for_Cooperation_v0.1.md` and its PDF projection.

The review has four distinct layers:

1. **Conceptual review:** compare every paper with the Stage-Accepted 2.0 baseline and the provisional integrated 2.1 baseline.
2. **Cross-paper review:** identify inconsistent terminology, duplicated claims, gaps, and conflicting explanations across the set.
3. **Human-communication review:** have the complete papers read as papers, not merely analyzed as extracted text; test comprehension, explanatory sequence, audience assumptions, misleading authority cues, and whether an informed newcomer can understand the SymK argument.
4. **Publication review:** verify Markdown-to-PDF correspondence, citations, typography, diagrams, page flow, legibility, accessibility, and the absence of clipping or rendering defects.

Automated comparison, extraction, and visual checks may support the work, but they cannot satisfy the human-communication review by themselves.

For each paper, record a review report and one explicit disposition: revise into v0.2, retain an identified v0.1 passage with justification, issue a governed erratum or addendum, or defer a named issue to 2.1.11. Then revise the four Markdown sources as v0.2, generate new PDF projections, and repeat the publication and human-readability checks. The Markdown sources remain governed; PDFs remain human-facing publication projections. The v0.1 pairs are preserved and never overwritten.

**Approval checkpoint 2.1.10H:** The project steward accepts the four review reports and the human-facing v0.2 publication set, or routes named unresolved issues to 2.1.11. This checkpoint does not confer constitutional authority on the papers.

#### 2.1.11 — Stage audit and acceptance

Run the full stage gate, close or explicitly route every deferred question, and Stage-Accept the integrated conceptual system.

**Approval checkpoint 2.1:** Project-steward Stage-Acceptance. No constitutional Ratification and no wholesale canonical migration occur here.

---

### 2.2 — Constitutional Axiom Set

**Purpose:** Derive a coherent constitutional candidate from the accepted 2.0 identity and 2.1 conceptual baseline.

**Required work:**

- test A0–A4, A6, J1, and any additional candidates against the 30 preserved tensions;
- correct A0's inherited claim that cooperation is SymK's objective;
- distinguish axioms, jurisdictional rules, principles, methods, definitions, and implementation policies;
- write operational implications, prohibited interpretations, counterexamples, and conflict rules for each candidate;
- identify what a derived project must inherit and what it may specialize; and
- produce a minimal candidate rather than constitutionalizing every useful design preference.

**Approval checkpoint 2.2:** The project steward may mark the set **Stage-Accepted Constitutional Candidate**. The record must say explicitly: **not Ratified and not yet the final constitutional authority**.

**Dependency:** Requires accepted 2.1. Supplies the candidate governed by 2.3.

---

### 2.3 — Constitutional Governance and Ratification

**Purpose:** Constitute durable authority and make constitutional change governable.

**Required work:**

- define the ratifier or ratifying body, quorum or decision rule, and conflicts of interest;
- define proposal, review, contest, Stage-Acceptance, Ratification, amendment, supersession, retirement, and emergency procedures;
- define standing for challenge and the preservation of dissent;
- define waivers, exceptions, experimental forks, and expiration conditions;
- define conflict precedence among constitution, principles, concepts, methods, project rules, and external obligations;
- define versioning, compatibility, and re-ratification triggers;
- adopt the transitional-authority clause described in section 3.3; and
- under the newly effective procedure, review and ratify, amend, or return the 2.2 candidate.

**Approval checkpoint 2.3A:** Project-steward Stage-Acceptance of the governance mechanism under transitional authority.
**Ratification checkpoint 2.3R:** The authority constituted by 2.3 ratifies the constitutional set and records the constitutional baseline.

**Dependency:** 2.3 uses the 2.2 candidate as a live test. Ratification is impossible before 2.3A.

---

### 2.4 — Legacy Disposition and constitutional migration

**Purpose:** Decide the fate of every inherited authority claim and migrate only what the ratified constitution authorizes.

**Required work:**

- build an exhaustive disposition matrix for registered axioms, principles, philosophies, notes, roadmaps, charters, white papers, and legacy rules;
- evaluate the fixed Human/AI cooperation roles, Meta-PLC identity, Pool Exclusivity, SymK Philosophy, and inherited principles explicitly;
- use controlled outcomes: retain, revise, supersede, reclassify, specialize to a project, archive as evidence, or retire;
- preserve source identity and decision lineage even when an artifact is superseded;
- update registries and canonical mappings only after each semantic disposition is accepted; and
- prove that no legacy document can silently override the ratified constitution.

**Approval checkpoint 2.4:** Constitutional authority accepts the disposition matrix and the migrated constitutional corpus.

**Dependency:** Requires 2.3R. Its results constrain 2.5 and the physical work completed in 2.8.

---

### 2.5 — Semantic packaging and projection architecture

**Purpose:** Rebuild the FC, FP, and SYMK-P families from accepted semantics instead of allowing inherited templates to define them.

**Required work:**

- define package types, required fields, authority semantics, lifecycle, dependency expression, and version rules;
- rebuild foundational concept and principle artifacts from the 2.1 baseline;
- decide Entity's role as an engineering or meta-model construct without restoring it as a universal foundation by convenience;
- represent typed relationships without assuming every Relationship is a universal Entity;
- define the human-semantic source, machine-semantic projection, mismatch handling, and loss declaration;
- incorporate the mature property/metadata/classification/taxonomy analysis currently stranded in Notes;
- decide whether the existing multi-layer concept specification is retained, revised, or superseded; and
- specify representation requirements without prematurely selecting one universal serialization or formal language.

**Approval checkpoint 2.5:** Constitutional authority accepts the package system and a complete, internally consistent foundational package set.

**Dependency:** Requires accepted 2.1, ratified constitution, and 2.4 dispositions.

---

### 2.6 — Derived-project governance and specialization

**Purpose:** Define how projects such as LexBrain and sshConnectivity inherit, constrain, and extend SymK.

**Required work:**

- define project charters or constitutions, version pinning, specialization, extension, and prohibited contradiction;
- define exception requests, experimental deviations, upstream proposals, and sunset conditions;
- distinguish project vocabulary, domain models, reference models, implementation rules, and evidence supplied back to SymK;
- define multi-project and possible multi-parent conflicts;
- define upgrade and compatibility obligations; and
- prevent project success from being mistaken for universal validity.

**Approval checkpoint 2.6:** Constitutional authority accepts the derived-project governance contract and at least two worked examples.

**Dependency:** Requires 2.5 packaging and the 2.3 governance baseline.

---

### 2.7 — Grounding validation

**Purpose:** Attempt to falsify or materially revise the 2.x system through contrasting real projects.

**Primary grounds:**

- **LexBrain:** knowledge-intensive, argument- and strategy-sensitive, legally constrained, evidence- and provenance-heavy.
- **sshConnectivity:** infrastructure/operations-oriented, capability- and authorization-heavy, boundary- and failure-sensitive.

An additional infrastructure-as-code case may be used if it adds evidence not already supplied by sshConnectivity.

**Required work:**

- instantiate the same accepted concepts and packages in both projects;
- collect fit failures, forced interpretations, missing concepts, domain leakage, and incompatible projections;
- test authority, responsibility, bearer, scope, context, representation, evidence, and value boundaries;
- maintain a counterexample register and distinguish project defects from SymK defects;
- revise upstream artifacts only through their governed change procedures; and
- show at least one case in which SymK correctly refuses an invalid inference or attribution.

**Approval checkpoint 2.7:** Constitutional authority accepts the validation report, residual limitations, and any governed upstream amendments.

**Dependency:** Requires 2.6. Evidence collection begins earlier through the V lane.

---

### 2.8 — Corpus consolidation and publication

**Purpose:** Complete and audit the continuous corpus-integrity work, then publish one navigable and truthful corpus.

**Required work:**

- finish lineage and disposition for all tracked and intentionally preserved untracked artifacts;
- recover useful review-queue content by manifest before removing flattened Git objects or other debris;
- normalize corrupted filenames and encoding with recorded source-to-target mappings;
- decide whether each Knowledge Family is completed, merged, redesigned, or retired;
- replace mock and placeholder canonical claims with governed content or explicit empty-state declarations;
- reconcile the document registry, source maps, status fields, versions, README files, and actual paths;
- classify ZIP files as immutable checkpoints, backups, or removable duplicates and record checksums;
- eliminate broken local links and misleading root structures;
- establish one newcomer path that accurately explains identity, authority, status, history, and next work; and
- verify that no source or dissent was lost during physical reorganization.

**Approval checkpoint 2.8:** Corpus audit passes with no unexplained authoritative duplicates, no unclassified tracked binary objects, no mock canonical assets, and complete lineage for every normative artifact.

**Dependency:** Semantic disposition relies on 2.4; package placement relies on 2.5; project material relies on 2.6–2.7. Corpus discovery and lineage work began at M0.

---

### 2.9 — Engineering readiness and formalization

**Purpose:** Make the accepted system implementable and testable without collapsing it into one implementation.

**Required work:**

- define normative human-readable sources and permitted machine-readable projections;
- select representation profiles or formal languages only against explicit requirements;
- define lowering, transformation, and declared-loss rules;
- define identifiers, references, schemas, validation, change compatibility, and conformance levels;
- provide positive fixtures, negative fixtures, boundary cases, and cross-version tests;
- separate specification, reference implementation, project implementation, and generated artifacts;
- establish release, dependency, and reproducibility requirements; and
- demonstrate an end-to-end trace from an accepted concept through a governed project projection to verifiable behavior.

**Approval checkpoint 2.9:** Engineering-readiness audit passes and a 3.0 release candidate is authorized.

**Dependency:** Requires consolidated 2.8 corpus and validated 2.7 semantics. It may prototype earlier but cannot establish semantics by implementation convenience.

---

### 3.0 — First consolidated SymK release

**Purpose:** Publish the first coherent release whose identity, constitution, concepts, project governance, evidence, corpus, and engineering projections agree.

**Release gate:**

- ratified constitutional baseline;
- accepted foundational conceptual and package baselines;
- completed legacy disposition;
- derived-project governance and two-project validation;
- complete artifact registry and lineage;
- no unexplained status or version drift;
- reproducible publication projections;
- conformance fixtures and release notes;
- preserved dissent, limitations, and deferred roadmap; and
- named release authority and immutable release identifier.

---

## 7. Continuous corpus-integrity workstream

| Phase | Begins | Work | Completion evidence |
|---|---|---|---|
| C0 — Inventory and snapshot | M0 | File manifest, hashes, Git state, archive status, format inventory | Reproducible inventory with no invisible source class |
| C1 — Recovery and quarantine | M0–2.2 | Separate recoverable documents from Git objects, IDE metadata, duplicates, and corrupt names | Manifest-level disposition; no bulk deletion |
| C2 — Lineage reconstruction | 2.1–2.4 | Connect originals, revisions, projections, imports, decisions, and supersessions | Every authority claim has traceable provenance |
| C3 — Family curation | 2.4–2.7 | Complete or retire Knowledge Families; assess canonical candidates | No mock or placeholder canonical claim |
| C4 — Controlled physical migration | 2.4–2.8 | Apply accepted dispositions, normalize names, repair links, restructure paths | Source-to-target mappings and verification report |
| C5 — Publication | 2.8–3.0 | Newcomer navigation, registry consistency, immutable release package | Audited 3.0 corpus |

### Corpus safety rules

- Never delete `REVIEW_QUEUE` wholesale.
- Never infer semantic disposition solely from filename, directory, format, or modification date.
- Never let deduplication erase distinct provenance.
- Never overwrite a historical artifact to make it appear consistent with a later decision.
- Prefer reversible quarantine until lineage and authority are known.
- Record every rename, normalization, split, merge, supersession, and retirement.
- Treat generated PDF, JSON, YAML, diagrams, and indexes as projections unless explicitly governed otherwise.

---

## 8. Dependencies and permitted overlap

| Relationship | Rule |
|---|---|
| M0 → 2.1.3 | DR-010 status must be synchronized before DR-011 opens. |
| 2.1 → 2.2 | Constitutional candidates must use accepted concepts, not define them retroactively. |
| 2.2 ↔ 2.3 | The candidate provides a governance test case; 2.3 supplies ratification authority. Candidate drafting may iterate, but Ratification waits. |
| 2.3 → 2.4 | Legacy constitutional authority cannot be conclusively disposed before enduring authority exists. |
| 2.4 → 2.5 | Packaging must not reproduce superseded legacy semantics. |
| 2.5 → 2.6 | Projects inherit governed packages, not prose by implication. |
| 2.6 → 2.7 | Validation needs an explicit project inheritance and exception model. |
| C lane ↔ all stages | Evidence discovery may inform any open decision; physical migration waits for semantic authority. |
| 2.7 → 2.8 | Project evidence and artifacts must be curated into the final corpus. |
| 2.8 → 2.9 | Engineering specifications require stable identities, paths, status, and source authority. |
| 2.9 → 3.0 | Release requires verified projection and conformance behavior. |

Permitted overlap is evidence-producing, not authority-skipping. For example, 2.7 test cases may be prepared during 2.5, and 2.9 prototypes may explore formalization during 2.6, but neither may preempt the governing stage decision.

---

## 9. Approval checkpoints

| Checkpoint | Decision | Authority |
|---|---|---|
| P0 | Approve this plan as the working 2.x migration plan | Project steward |
| M0 | Confirm DR-010 synchronization and evidence snapshot | Project steward |
| 2.1 | Stage-Accept integrated conceptual baseline | Project steward under transitional governance |
| 2.1.10H | Accept the four Foundation Paper review reports and human-facing v0.2 publication set | Project steward under transitional governance |
| 2.2 | Stage-Accept constitutional candidate, explicitly non-Ratified | Project steward under transitional governance |
| 2.3A | Stage-Accept governance and activate transition clause | Project steward under transitional governance |
| 2.3R | Ratify constitutional baseline | Authority constituted by 2.3 |
| 2.4 | Accept legacy disposition and constitutional migration | Constitutional authority |
| 2.5 | Accept semantic package system and foundational packages | Constitutional authority |
| 2.6 | Accept derived-project governance | Constitutional authority |
| 2.7 | Accept grounding validation and residual limitations | Constitutional authority |
| 2.8 | Accept corpus audit and consolidated publication structure | Designated governance/corpus authorities |
| 2.9 | Authorize 3.0 release candidate | Designated release authority |
| 3.0 | Ratify/publish consolidated release | Constitutional and release authorities |

Approval of a stage never silently approves the next stage's unresolved choices.

---

## 10. Old-to-new migration map

| Recovered plan element | Disposition in this plan |
|---|---|
| 2.0 Identity and Jurisdiction | Preserved as accepted baseline |
| 2.1.1 Method | Preserved through DR-009 |
| 2.1.2 Structural Boundaries | Preserved through approved DR-010; status synchronization added at M0 |
| 2.1.3–2.1.11 | Preserved and made explicit with boundary and acceptance criteria |
| 2.2 Constitutional Axiom Set | Preserved, but limited to a non-Ratified candidate |
| 2.3 Constitutional Governance | Expanded to include transitional authority and actual ratification |
| 2.4 Legacy Disposition | Expanded to include constitutional migration and an exhaustive disposition matrix |
| 2.5 Foundational Concepts and Principles | Reframed as semantic packaging and projection architecture |
| 2.6 Derived-Project Governance | Preserved and supplied with inheritance, exception, and version duties |
| 2.7 Grounding Validation | Preserved but made adversarial, cross-project, and counterexample-driven |
| 2.8 Corpus Consolidation | Preserved as culmination; discovery/recovery starts at M0 |
| 2.9 Engineering Readiness | Preserved and given conformance, lowering, and projection gates |
| 3.0 release | Preserved as the first consolidated release |

---

## 11. Principal risks and controls

| Risk | Severity | Control |
|---|---:|---|
| Approved DR-010 remained Proposed in the repository | Closed 18 August 2026 | M0 pause closure synchronized the decision, registers, summaries, and ledgers before DR-011 |
| `REVIEW_QUEUE` mixes valuable evidence with hundreds of Git objects | High | Manifest-based recovery; no wholesale deletion |
| Candidate or legacy files appear authoritative because of location | High | Enforce separate location, maturity, and authority fields |
| 2.2 constitution claims authority before 2.3 exists | High | Candidate-only 2.2; transition clause and ratification in 2.3 |
| Knowledge Families advertise curation that has not occurred | High | Complete, redesign, or retire each family by C3/2.8 |
| Domain artifacts dictate universal SymK concepts | High | Cross-domain counterexamples and explicit specialization rules |
| Machine schemas dictate human semantics | High | Human-semantic source plus governed projection/loss contract |
| Six local commits and working changes lack a released checkpoint | Medium–High | Evidence snapshot, reviewed commit sequence, and later immutable tag |
| Corrupted filenames and duplicate projections obscure lineage | Medium | Recorded normalization and source-to-target mapping |
| Root and nested structures imply an engineering maturity that does not exist | Medium–High | Truthful orientation, explicit implementation status, 2.9 readiness gate |
| Foundation papers diverge from accepted 2.0/2.1 decisions | High | Revise only after 2.1.9 integration; audit at 2.1.11 |

---

## 12. Actions intentionally deferred

Until their governing checkpoints, do not:

- delete or bulk-clean the review queue;
- rewrite historical documents to match current doctrine;
- ratify the Constitution vNext candidate;
- canonically migrate legacy axioms or principles;
- restore Entity to foundational status;
- require one universal JSON, YAML, OWL, database, or other representation;
- update the four foundation papers piecemeal ahead of the integrated 2.1.9 baseline;
- treat LexBrain, sshConnectivity, Meta-PLC, PostgreSQL, or any existing implementation choice as SymK's universal architecture;
- reorganize the repository merely to make it look complete; or
- declare engineering readiness without negative fixtures and end-to-end conformance evidence.

---

## 13. Immediate next work package

Work package **2.1.7 — Amplified Intelligence and Domain Intelligence Amplifiers** is complete for progression through `SYMK-2X-EV-136` and Stage-Accepted DR-015. Its acceptance record and manifest preserve the exact accepted object and full lineage.

Work package **2.1.8 — Reasoning, Answers, Value, and Feedback** is formally open through `SYMK-2X-EV-137`–`138`. Streams A–F are analytically complete through `SYMK-2X-EV-139`–`144`; their records preserve the complete value-chain and consolidated gate. Stream G is complete through `SYMK-2X-EV-145`; its 978-line Proposed DR-016 contains the proposed Question/Reasoning/Answer/Value Foundational dispositions, Complex-Question supporting route, complete individual routing, retained DR-013 dispositions, branching spine, nine planes, sixty-part envelope, 180 prohibited entailments, twenty-four mandatory cases, twenty negative controls, eighteen alternatives, three Views, proposed DQ-014 answer, jurisdiction, impacts, downstream ownership, 60 dissent questions, thirty reopening conditions, confidence, non-effects, and project-steward checkpoint.

The immediate next action is project-steward review of Proposed `SYMK-2X-DR-016`: Stage-Accept it as written, return specified clauses for revision, preserve it as contested, or reject it with reasons and reopening instructions. Proposal preparation does not accept the complete migration plan, A0–A4/A6/J1, a definition or disposition, DQ-014 answer, metric, model, threshold, weight, benchmark, objective, optimization, trade-off, final package, paper revision, formalism, implementation, or project change. It does not grant constitutional force, complete 2.1.8 for progression, open 2.1.9, or authorize a commit.

---

## Appendix A — High-value evidence requiring later disposition

- The four v0.1 foundation papers on Intelligence, Knowledge, Knowledge Engineering, and Education.
- Constitution vNext candidates A0–A4, A6, and J1.
- The legacy axioms for symbiotic cooperation roles, Meta-PLC identity, and Pool Exclusivity.
- `SYMK-NOTE-001` on multi-layer concept specifications.
- The substantial document-taxonomy analysis currently held under Notes.
- The original Architecture Roadmap and checkpoint foundation summaries.
- Historical Meta-PLC manuals, coding/design rules, and technical-install material.
- LexBrain research and argument/strategy evidence currently mixed into Standards.
- The SymK Charter and other potentially significant artifacts held in `REVIEW_QUEUE`.
- The current Knowledge Family curation scaffolds, which are process evidence but not proof of completed curation.

## Appendix B — Evidence-confidence statement

This plan distinguishes three forms of certainty:

- **Directly established:** live governed files, Git state, file contents, archive comparisons, and the project steward's explicit approval of 2.1.2.
- **Strongly inferred:** intended stage dependencies and historical roles supported by multiple roadmap, register, and migration artifacts.
- **Still requiring governed decision:** future conceptual dispositions, constitutional ratification, legacy outcomes, package design, and physical deletion or migration.

That distinction should be preserved in all future reports so that discovery is not mistaken for decision and decision is not mistaken for implementation.

## Appendix C — Primary control sources

The following live repository paths supplied the principal governance and sequence evidence for this plan:

- `SymK 2.x Evolution history/Overview.md`
- `SymK 2.x Evolution history/01_ROADMAP/SYMK_2X_ROADMAP.md`
- `SymK 2.x Evolution history/00_CONTROL/EVOLUTION_GOVERNANCE.md`
- `SymK 2.x Evolution history/00_CONTROL/STATUS_MODEL.md`
- `SymK 2.x Evolution history/00_CONTROL/VERSIONING_POLICY.md`
- `SymK 2.x Evolution history/2.0/2.0.6_Consolidated_Baseline.md`
- `SymK 2.x Evolution history/2.0/2.0.6.2_Final_Stage_Acceptance.md`
- `SymK 2.x Evolution history/2.0/DECISION_REGISTER.md`
- `SymK 2.x Evolution history/2.0/DEFERRED_QUESTIONS.md`
- `SymK 2.x Evolution history/2.1/2.1.1_Stage_Frame_and_Concept_Governance.md`
- `SymK 2.x Evolution history/2.1/2.1.2_Concept_Inventory_and_Structural_Boundaries.md`
- `SymK 2.x Evolution history/2.1/DECISION_REGISTER.md`
- `SymK 2.x Evolution history/2.1/CONCEPT_REGISTER.md`
- `SymK 2.x Evolution history/2.1/FOUNDATION_PAPER_REVISION_LEDGER.md`
- `00_GOVERNANCE/DOCUMENT_REGISTRY.md`
- `00_GOVERNANCE/CANONICAL_DOCUMENTS.md`
- `00_GOVERNANCE/99-Notes/SYMK-NOTE-001_Multi-Layer_Concept_Specification_v0.1.md`

Migration reports, Knowledge Family curation files, `REVIEW_QUEUE`, nested `SymK/` artifacts, archives, and binary documents were inspected as supporting evidence rather than presumed governing sources.
