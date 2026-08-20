Stream D is complete as an analytical working result. No project files were changed.

## 2.1.4D — Representation, Projection, Ontology, Logic, and two-lane alignment

### Central result

> Representation makes selected aspects of a subject available. Projection is the governed relationship by which those aspects are selected, transformed, supplemented, constrained, or omitted in a target Representation.

Neither completeness nor equivalence should be presumed. A Representation can be precise, valid, useful, and well-formed while remaining epistemically inadequate or materially lossy.

## 1. Representation

The Stage-Accepted definition remains sufficient:

> A Representation is a situated form through which selected aspects of a subject are made available for interpretation, communication, reasoning, storage, or action.

A material Representation should identify:

- represented subject;
- Representation identity and version;
- purpose and intended audience or consumer;
- form or medium;
- originating source;
- relevant Context, Scope, Domain, Applicability, and time;
- responsible participant or process;
- represented claims, roles, and relationships;
- governing semantics or interpretation rules;
- epistemic and governance status;
- uncertainty and disagreement;
- limitations and known unrepresented dimensions;
- and lineage to other Representations.

A Representation can be false, misleading, obsolete, misapplied, or internally inconsistent while still being a Representation.

## 2. Projection

Projection must be modeled as a typed relationship, not merely as a generated file.

A projection relates:

`source subject or Representation → target Representation`

and records its epistemically material effects.

### Projection effects

At minimum, distinguish:

| Effect | Meaning |
|---|---|
| Preservation | A source distinction is retained within the target’s declared semantics |
| Translation | Meaning is expressed through a different vocabulary or form |
| Selection | Only dimensions relevant to a purpose are included |
| Abstraction | Detail is intentionally reduced while a broader structure is retained |
| Aggregation | Several source elements are combined |
| Decomposition | One source element is represented through several target elements |
| Transformation | Source structure is materially reorganized |
| Enrichment | New annotations, classifications, or relationships are added |
| Inference | Target content is derived rather than directly reproduced |
| Strengthening | The target imposes a stricter constraint than the source |
| Weakening | The target permits more than the source |
| Omission | A source dimension is absent |
| Distortion | The target produces a materially misleading interpretation |
| Loss | Material source meaning cannot be recovered from the target alone |

These effects may coexist. A projection can preserve identity while losing uncertainty, or preserve claim content while strengthening cardinality.

## 3. Epistemic preservation obligations

For epistemic use, a Representation or Projection must preserve—or explicitly declare its treatment of—the following when material:

1. subject identity;
2. concept and predicate identity;
3. claim content and epistemic stance;
4. proposed Bearer;
5. source and contributing roles;
6. Domain, Context, Scope, Applicability, and time;
7. grounds and evidence relationships;
8. provenance and derivation;
9. assessment method and result;
10. uncertainty and disagreement;
11. governance status;
12. reliance authorization;
13. authority and responsibility;
14. inferential premises, rules, assumptions, and method;
15. lifecycle state and version;
16. challenge, supersession, and retirement history;
17. intended use and observed consequences;
18. semantic-package or governing-definition version;
19. material additions, omissions, transformations, and strengthening;
20. route back to the governed source.

Not every projection must carry all this information inline. A reduced operational projection may retain references to a fuller governed record. What is prohibited is presenting the reduction as complete without declaring the loss.

## 4. Declared-loss record

Every materially lossy projection should eventually have an alignment record containing:

- source and target identities and versions;
- governing concept or package version;
- projection purpose;
- owning layer and responsible authority;
- source statements or dimensions considered;
- preserved content;
- translated or transformed content;
- additions and inferred content;
- strengthened or weakened constraints;
- omitted or inexpressible content;
- known semantic loss;
- affected reasoning or reliance;
- uncertainty about the mapping;
- verification evidence;
- applicable Context and Scope;
- reversibility or route to the fuller source;
- and alignment status.

A silent omission is a defect. A declared omission may be a legitimate design decision.

## 5. Validity and adequacy must remain separate

“Valid” cannot be used as a single universal status.

| Evaluation | Question |
|---|---|
| Syntactic validity | Does the artifact conform to its grammar or encoding rules? |
| Schema conformance | Does it satisfy the declared structural constraints? |
| Logical validity | Does the conclusion follow from the premises under the chosen semantics? |
| Semantic fidelity | Does the Representation preserve the source meaning it claims to express? |
| Epistemic sufficiency | Are the grounds adequate for the relevant claim or attribution? |
| Empirical adequacy | Does it fit the relevant observations or performance evidence? |
| Applicability | Is it suitable in this Context under the declared Scope? |
| Governance validity | Was it produced or approved through the applicable governed process? |
| Normative/legal validity | Does it possess force under the relevant authority? |
| Reliance authorization | May it be used for this purpose and consequence profile? |
| Operational usefulness | Does it help accomplish the intended task? |
| Consequential acceptability | Are its observed or expected effects tolerable and responsible? |

Passing one evaluation does not imply passing the others.

## 6. Minimum Ontology boundary

SymK does not need a single universal upper ontology. It needs the capacity to preserve certain distinctions across representations.

A future semantic expression must be able to distinguish:

- concept, term, definition, instance, and Representation;
- subject identity, identifier, state, and version;
- actual bearing, attribution claim, assessment, and record;
- Knowledge, claim, ground, evidence, asset, and Representation;
- source, derivation, Projection, and target Representation;
- Context, Scope, Domain, and Applicability;
- generic Relationship and specific typed relationships;
- process, role, state, event, artifact, and decision;
- universal SymK meaning and Domain specialization;
- governance authority, epistemic authority, and reliance authority;
- current effective view and preserved historical assertions;
- absence, unknown, inapplicable, rejected, false, and prohibited;
- active, superseded, withdrawn, and retired;
- and human-semantic meaning versus machine-semantic expression.

These are semantic obligations. They do not require every distinction to become a class, table, JSON object, RDF node, or independent package.

Derived projects own their Domain ontologies while preserving the SymK minimum.

## 7. Minimum Logic boundary

SymK does not need to select one Logic in 2.1. It must require future logical expressions to declare their assumptions and limits.

The machine-semantic lane must eventually support or responsibly address:

### Typed relations

`supports`, `contradicts`, `cites`, `derives_from`, `attributes_to`, `assesses`, `authorizes`, `applies`, and `supersedes` cannot collapse into `relatedTo`.

### Qualification

Material claims and relations must be qualifiable by Context, Scope, Domain, time, authority, method, and uncertainty.

### Explicit non-entailments

SymK must express or test prohibitions such as:

- representation does not entail Knowledge;
- acceptance does not entail truth;
- provenance does not entail warrant;
- authority does not entail epistemic sufficiency;
- absence does not entail falsity;
- Intelligence attribution does not entail Knowledge attribution;
- operational usefulness does not entail responsible applicability.

### Negation and absence

A future formal profile must declare whether it uses:

- open-world or closed-world assumptions;
- explicit negation;
- default negation;
- incomplete information;
- local closure;
- or Domain-specific completeness claims.

A missing assertion cannot receive one universal meaning.

### Contradiction

The system must be able to preserve conflicting claims without either:

- deriving everything from inconsistency;
- silently selecting one claim;
- or deleting dissent for storage convenience.

Different profiles may use paraconsistent, defeasible, contextual, provenance-partitioned, or other mechanisms. Selection is deferred.

### Time and version

Claims, rules, applicability, assessments, and authorizations can change. The formal expression must not treat the newest record as if earlier records never existed.

### Defeasibility and revision

Epistemic reasoning is frequently non-monotonic. New evidence can defeat an assumption, narrow applicability, or supersede an earlier rule.

Classical monotonic entailment may remain appropriate for bounded formal subproblems, but it cannot stand in for the entire epistemic lifecycle.

### Modality and authority

The machine lane must not confuse:

- what is asserted;
- what is believed or assessed;
- what is permitted;
- what is required;
- what is legally authoritative;
- what may be relied upon;
- and what is claimed to be true.

### Inferential lineage

Derived claims must retain premises, source versions, rules or models, inference regime, assumptions, and relevant uncertainty.

## 8. Two-lane semantic alignment

Semantic authority belongs to the governed concept record and decision lineage—not inherently to prose, logic, YAML, JSON, OWL, code, or another notation.

### Human-semantic lane

Must preserve:

- purpose and meaning;
- distinctions and exclusions;
- rationale;
- examples and counterexamples;
- interpretation;
- uncertainty and dissent;
- known limits;
- and implications for people, systems, and practice.

### Machine-semantic lane

Must make selected elements inspectable or computable:

- identities and versions;
- types and typed relationships;
- Context, Scope, Domain, and Applicability;
- constraints and non-entailments;
- dependencies;
- provenance and lineage;
- authority and lifecycle state;
- alignment;
- and declared loss.

A machine expression may be authoritative for an explicitly governed formal claim within its declared scope. It does not thereby control broader meaning or omitted dimensions.

## 9. Alignment states

A future alignment contract should distinguish:

- **verified within scope** — tested correspondence for declared claims;
- **partially aligned** — only identified source dimensions are expressed;
- **lossy but acceptable** — loss is explicit and appropriate for purpose;
- **strengthened** — target adds restrictions;
- **weakened** — target permits additional interpretations or states;
- **unverified** — correspondence has not been adequately tested;
- **version-divergent** — lanes refer to different source versions;
- **materially conflicting** — the target contradicts or distorts the source;
- **not representable in this profile** — a dimension is intentionally outside the formalism.

“Aligned” without scope or verification evidence is insufficient.

## 10. Mismatch governance

When the lanes disagree:

1. neither silently overwrites the other;
2. the compatibility or completeness claim becomes qualified;
3. the mismatch is classified;
4. affected use may be restricted;
5. the nearest adequate owner reviews the artifact it controls;
6. implementation evidence may challenge the source concept;
7. the projection cannot amend the source automatically;
8. the decision and correction retain lineage.

Mismatch classes include:

- source ambiguity;
- omission;
- strengthening;
- weakening;
- distortion;
- translation divergence;
- version conflict;
- formalism limitation;
- implementation defect;
- or source-concept defect.

## 11. Counterexample results

- **Exactly one responsible party in a schema:** if the source permits distributed responsibility, this is declared strengthening or conflict.
- **One generic relationship edge:** connectivity survives while epistemic meaning is destroyed.
- **Missing database row:** it cannot silently mean false, unknown, rejected, or inapplicable.
- **Formally valid inference from false premises:** logical validity passes; epistemic sufficiency fails.
- **Knowledge graph with provenance:** graph structure and lineage do not establish Knowledge.
- **SharePoint projection without uncertainty:** it is a lossy operational projection and must link back to the full record.
- **Generated summary omitting dissent:** fluent compression is semantically incomplete and may be unsuitable for decision use.
- **Domain ontology copied into SymK:** specialization has been mistaken for universal ownership.
- **Code base class becomes universal Entity:** implementation reuse has acquired unauthorized semantic force.
- **Retired rule replaced in place:** the current view is simplified by destroying epistemically material history.
- **High-performing model with opaque grounds:** operational usefulness may be established without establishing adequate claim-level provenance or epistemic sufficiency.
- **Procedure document for practical Knowledge:** formal completeness does not establish competence.

## Provisional dispositions

| Candidate | Stream D disposition |
|---|---|
| Representation | Retain Stage-Accepted foundational status |
| Projection | Retain Stage-Accepted governed supporting relationship |
| Alignment | Governed relationship and verification record |
| Semantic loss | Required declared projection condition |
| Formal validity | Governed supporting distinction |
| Semantic fidelity | Required projection assessment |
| Ontology | Engineering/formal discipline expressing selected conceptual commitments; not universal semantic owner |
| Logic | Formal reasoning apparatus with declared scope and assumptions |
| Human-semantic lane | Necessary interpretive expression |
| Machine-semantic lane | Necessary formal projection for selected claims |
| One universally authoritative notation | Reject |
| One universal `valid` status | Reject |
| One universal closed-world assumption | Reject |

## DQ-018 and DQ-022 result

Stream D completes the conceptual portion of both deferred questions:

- **DQ-018:** SymK needs minimum Ontology and Logic capabilities sufficient to preserve identity, qualification, typed relations, non-entailments, contradiction, absence, time, authority, revision, and lineage. It does not need to select a universal Ontology or Logic in 2.1.
- **DQ-022:** A dual-lane package requires a governed concept record, human-semantic nucleus, scoped machine-semantic claims, an alignment record, declared loss, mismatch governance, and decision lineage. Final package anatomy and contract syntax remain deferred to 2.5.

## Stream D gate

Stream D passes for continuation. It preserves DR-009’s two-lane authority, DR-010’s Representation and Projection definitions, DR-011’s non-substitution rules, and Streams B–C’s lifecycle and status separation.

It selects no formal language, schema, package structure, storage model, API, or lowering architecture and therefore does not authorize DR-012.

The next step is **Stream E: consolidated stress testing, compatibility analysis, affected-artifact consequences, dissent, confidence, and reopening conditions**.
