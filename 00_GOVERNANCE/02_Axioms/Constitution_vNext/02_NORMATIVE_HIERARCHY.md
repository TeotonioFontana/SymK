# SymK Jurisdiction-Qualified Normative Layer Model

**Status:** Proposed constitutional governance model
**Version:** 0.2
**Ratified:** No
**Authority:** `SYMK-2X-DR-005`, Stage-Accepted for SymK 2.0 migration

## 1. Purpose

SymK governance is not a single hierarchy in which every broader or more abstract document automatically defeats every narrower or more concrete one. It operates across two axes:

1. **jurisdictional reach** — where and for whom a commitment applies;
2. **realization depth** — whether the artifact governs identity, meaning, engineering, design, implementation, or operation.

Authority is also qualified by kind: constitutional, semantic, methodological, design, technical, organizational, legal, professional, or evidentiary authority are not interchangeable.

## 2. Axis A — Jurisdictional reach

| Reach | Governing question | Examples |
|---|---|---|
| Universal SymK | What must hold across every SymK-compatible project? | Constitutional commitments; universal concept invariants |
| Derived domain | What must hold for a particular domain project? | LexBrain legal concepts; sshConnectivity connectivity concepts |
| Product or system | What must hold for a particular engineered system? | Composer obligations; LibScan contracts |
| Organization | What must hold for an adopting institution? | Approval policy; access authority; risk acceptance; professional roles |
| Deployment | What must hold in this concrete operating context? | Applicable law; configuration; retained data; current operators |

Movement down this axis narrows scope. Narrower authorities may add, specialize, or strengthen commitments within their jurisdiction. They do not thereby acquire authority to redefine broader commitments silently.

## 3. Axis B — Realization depth

| Depth | Governing question | Characteristic artifacts |
|---|---|---|
| Constitutional | What must remain true for identity and compatibility? | Constitution; jurisdiction articles; Ratified axioms |
| Conceptual and semantic | What does a governed concept mean, and which distinctions must be preserved? | Concept specifications; principles; vocabularies; semantic models |
| Engineering governance | Which durable design obligations translate governing commitments? | Engineering Charters; binding standards; assurance obligations |
| Specification and architecture | Which structures and behaviors are selected, and why? | Requirements; capability specifications; protocols; ADRs; reference architectures |
| Implementation | How is the selected design concretely realized? | Code; schemas; prompts; rules; models; pipelines; infrastructure |
| Operation | How is the realization authorized, configured, used, monitored, and changed here? | Deployment configuration; operating procedures; access decisions; local records |

Movement down this axis increases concreteness. A concrete realization may preserve, specialize, strengthen, project, or operationalize a governing commitment. It may not silently supply missing philosophical or domain meaning.

## 4. Principal layers

| ID | Layer | Primary authority | Typical reach | Must not silently do |
|---|---|---|---|---|
| S0 | Epistemic sources and inquiry | Evidence, criticism, alternatives, and candidate conclusions | Any | Acquire normative force through publication, prestige, or the label “foundational” |
| S1 | SymK Constitution | Universal constitutional compatibility commitments | Universal SymK | Dictate complete domain Ontology, product design, or implementation |
| S2 | SymK governed conceptual and engineering corpus | Universal semantic and methodological authority according to declared status | Universal or cross-project | Claim constitutional force without selection and Ratification; import domain contingencies as universals |
| P1 | Derived-project Constitution | Domain constitutional identity and commitments | Derived domain | Contradict or redefine inherited SymK commitments silently |
| P2 | Derived-project governed conceptual corpus | Domain Ontology, Logic, concepts, and methods | Derived domain or declared product scope | Allow product schemas or local practice to define domain meaning accidentally |
| E1 | Engineering Charter and binding project standards | Durable engineering obligations | Project or system | Create philosophical or domain commitments merely as design preferences |
| E2 | Specification and architecture | Contextual design, contracts, projections, and decisions | Product or system | Treat a selected structure as the only legitimate realization of governing meaning |
| I1 | Implementation | Concrete technical realization | Concrete system | Acquire semantic, constitutional, or operational authority because it runs |
| O1 | Organization and deployment | Local authorization, policy, configuration, and operation | Organization or deployment | Universalize local law, policy, risk tolerance, or practice |

S0 is shown but is not a superior normative rank. Evidence can support or defeat decisions at any layer, but changes the governed artifact only through the governance process of its owner.

## 5. Why the distinctions matter

### 5.1 S1 and S2

The Constitution cannot contain every mature concept, principle, method, and semantic distinction without becoming unstable and unreadable. Conversely, a concept or principle does not acquire constitutional status merely by being called foundational.

### 5.2 P1 and P2

A project Constitution protects domain identity and durable commitments. The project conceptual corpus develops its domain Ontology, Logic, concepts, and methods. Neither a product schema nor an implementation may define those commitments accidentally.

### 5.3 E1 and E2

An Engineering Charter governs durable design obligations. Architecture and specifications select contextual solutions under those obligations. A current architectural choice is not automatically a project-wide standard.

### 5.4 I1 and O1

The same implementation can operate under different laws, institutions, authorizations, populations, configurations, and stakes. Successful execution does not establish legitimate use; project compatibility does not grant deployment authorization.

## 6. Primary ownership

Every governed artifact must declare one primary owning layer, its jurisdictional reach, its authority kind, and any dependent projections.

The owner is accountable for:

- purpose, scope, and status;
- content selection within its jurisdiction;
- versioning, change, and supersession;
- lineage, evidence, dissent, and known limitations;
- challenges addressed within its authority;
- and effects on dependent layers.

Ownership means governance accountability. It does not mean intellectual property, exclusive authorship, infallibility, or immunity from evidence and challenge.

An artifact is placed by the decision it governs and the authority it exercises—not by filename, format, repository location, technology, authorship, or current implementation.

## 7. Core placement rules

| Artifact or commitment | Primary layer |
|---|---|
| Foundation paper, research survey, operational observation, or challenge evidence | S0 |
| SymK constitutional axiom or jurisdiction article | S1 |
| Universal SymK concept, principle, method, or governed cross-project standard | S2 |
| Derived-project identity, purpose, domain boundary, or domain axiom | P1 |
| Domain Ontology, Logic, governed domain concept, or product-level concept | P2 at its declared reach |
| Project Engineering Charter or binding engineering standard | E1 |
| Capability specification, protocol, interface contract, formal projection, architecture, or ADR | E2 by default |
| Code, prompt, model, database, executable rule, pipeline, or infrastructure | I1 |
| Organizational policy, authorization, risk acceptance, deployment configuration, or operating procedure | O1 |
| Law, regulation, professional rule, or external standard | External owner; imported laterally where applicable |

A formal ontology, Markdown document, JSON schema, diagram, or other representation has no intrinsic layer. For example, OWL may express an S2 governed projection, a P2 domain Ontology, or an E2 application model. Format never determines jurisdiction.

## 8. Mixed artifacts

If one package contains material from several layers, it must expose:

- its primary layer;
- the layer and status of each governed section or child artifact;
- which content is normative, explanatory, evidentiary, illustrative, generated, or operational;
- precedence inside the package;
- and separate change authorities where necessary.

If these boundaries cannot be made clear, the package must be split.

## 9. Interlayer movement

The following relationships are distinct and must not be collapsed into generic “inheritance”:

| Relationship | Governing effect |
|---|---|
| Inheritance | Carries applicable governing commitments, lineage, precedence, and challenge duties into a declared child |
| Specialization | Preserves applicable parent meaning while adding narrower domain or contextual determination |
| Instantiation | Applies a concept or specification to a particular case with evidence and context |
| Composition | Combines governed elements while preserving their distinct contributions and authority |
| Role adoption | Assigns contextual duties and permissions without creating permanent identity or general authority |
| Projection | Expresses selected dimensions in another representation without exhaustive equivalence or ownership transfer |
| Implementation | Concretely realizes a selected specification or architecture |
| Local adoption | Selects a version for organizational or deployment use and adds local controls or restrictions |
| Challenge | Returns evidence and reasons to the owner of a contested artifact without silently amending it |

Detailed protocols for these relationships belong to later governance and project-inheritance stages.

## 10. Four directions of movement

### Downward constraint

Broader or more abstract commitments constrain narrower and more concrete realizations within their jurisdiction.

### Downward enrichment

Narrower layers add domain, product, organizational, and deployment meaning that broader layers neither contain nor pretend to contain.

### Upward evidence

Research, project work, implementation, and operation return evidence that may confirm, qualify, or challenge any governing layer.

### Lateral import

Law, professional standards, scientific knowledge, organizational policy, and technical standards enter at the layer and scope where their authority applies. Their source and jurisdiction remain traceable.

## 11. Jurisdiction-qualified precedence

> **A governing commitment has precedence over a realization only within its declared jurisdiction. A narrower authority may impose stronger local constraints without redefining broader meaning. Applicable conflicts must be classified by jurisdiction, authority kind, scope, and ownership before precedence is decided.**

Therefore:

- SymK does not dictate complete domain Ontologies or Logic;
- project constitutions do not silently redefine universal SymK concepts;
- Engineering Charters do not promote design preferences into philosophy or domain meaning;
- architectures do not become mandatory solely because they are referenced;
- implementations do not create concepts merely because a schema, model, or API requires them;
- and local or external authority may prohibit use without acquiring universal semantic authority.

The detailed conflict-routing and compatibility rules remain governed by the separate conflict-and-challenge protocol.

## 12. Cross-cutting authorities

| Authority or constraint | Effect within jurisdiction | Does not automatically do |
|---|---|---|
| Reality and observed consequence | Challenge any claim, commitment, or design through evidence | Ratify a replacement without governance |
| Law and regulation | Prohibit, require, or condition action | Define universal SymK concepts |
| Professional institutions and standards | Establish scoped competence, reliance, and responsibility requirements | Become universal across unrelated domains |
| Ethical and social constraints | Constrain purpose, design, and use | Supply one complete universal moral theory |
| Technology and physical possibility | Limit feasible realization | Determine what ought to be built or what a concept means |

An external authority may have decisive practical precedence within its jurisdiction. This is not semantic precedence over SymK.

## 13. Placement test

For every artifact or commitment, ask:

1. What decision does it govern: identity, meaning, engineering obligation, design, realization, or operation?
2. Who must comply: every SymK project, one domain, one product, one organization, or one deployment?
3. What gives it authority: Ratification, governed concept status, adoption, design decision, implementation fact, external law, or local authorization?
4. What may it change, and which meanings or authorities remain outside its jurisdiction?
5. Who owns revision and supersession?
6. What evidence may challenge it, and where must that challenge be routed?

Undefined ownership or authority means governance is incomplete.

## 14. Compatibility tests

The model is adequate only if it can explain without contradiction that:

- SymK defines universal epistemic commitments without defining Brazilian legal Ontology;
- LexBrain defines legal concepts without redefining SymK Knowledge;
- Composer and LibScan share LexBrain concepts without requiring identical architectures;
- an organization imposes stricter privacy or authorization without changing a project Constitution;
- different implementations preserve the same conceptual identity;
- operational failure challenges architecture or a governing commitment through evidence;
- and an external legal command controls deployment without becoming a SymK axiom.

## 15. Version history

- **0.2 — 2026-08-18:** Replaced the one-dimensional hierarchy with the Stage-Accepted two-axis, jurisdiction-qualified layer model; added primary ownership, placement, movement, external authority, and operation under `SYMK-2X-DR-005`; no constitutional Ratification.
- **0.1 — 2026-08-16:** Initial Proposed single normative ladder.
