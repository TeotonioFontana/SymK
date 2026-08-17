# Knowledge as the Shared Medium

## A Foundational Paper for SymK

**Status:** Foundational working paper  
**Version:** 0.1  
**Date:** 7 August 2026  
**Scope:** Conceptual foundation and development guidance; not yet a ratified SymK specification

---

## Abstract

SymK holds that knowledge is the shared medium through which intelligences cooperate. That statement gives knowledge a constitutional role: if the concept is vague, reduced to documents, or confused with a technical representation, every later SymK structure inherits the confusion.

This paper develops a working foundation for knowledge in SymK. It begins with philosophical epistemology, where the analysis of propositional knowledge has moved from the familiar justified-true-belief account through the Gettier problem to reliabilist, anti-luck, virtue-theoretic, contextualist, and knowledge-first approaches. It then distinguishes that inquiry from the engineering tradition of knowledge representation, including epistemic logic, first-order logic, rules, frames, description logics, ontologies, knowledge graphs, probabilistic models, and neural representations.

The central conclusion is that no representation is knowledge merely because it is stored, structured, inferred, or generated. A graph contains assertions; a document expresses claims; a database preserves records; a model encodes learned regularities. Each can participate in knowledge, but none independently settles truth, warrant, meaning, scope, or responsible reliance.

The paper proposes a plural and layered working account. In SymK, **knowledge is an epistemic achievement in which an intelligence, or a cooperative system of intelligences, stands in a sufficiently truth-connected, competence-bearing, or direct relation to what is known such that it may be responsibly relied upon within a stated scope**. SymK does not claim to store that achievement directly. It engineers the conditions under which knowledge claims, capabilities, grounds, provenance, contexts, challenges, decisions, and representations can become shared, durable, governed, and evolvable.

This distinction preserves the ambition of the SymK motto while preventing the system from declaring its own contents true. It also produces concrete development constraints and a research agenda for the eventual formal SymK concept of Knowledge.

---

## 1. Why knowledge is foundational to SymK

SymK began as a protocol for symbiotic cooperation between Human Intelligence and Artificial Intelligence. It then expanded into an Engineering of Knowledge System and generalized its objective toward sustained cooperation among intelligences of any kind.

This evolution made knowledge central for a practical reason. A dialogue can produce insight, but a dialogue is temporary. Cooperation becomes cumulative only when what was learned can survive the interaction that produced it. Participants must be able to recover not only a conclusion, but also its meaning, grounds, scope, history, objections, and consequences. New participants must be able to continue the work without reconstructing it from fragments.

SymK therefore adopted a compact constitutional statement:

> **Knowledge is the shared medium. Cooperation is the objective.**

The statement is powerful, but it carries a danger. The word *knowledge* is used differently in philosophy, science, organizational practice, information systems, and artificial intelligence. It can mean a factive cognitive relation, a skill, familiarity with a person or place, a justified belief, an organizational capability, a database, an ontology, a set of rules, or patterns encoded in a neural model. These uses overlap, but they are not equivalent.

If SymK leaves the ambiguity unresolved, several errors become likely:

1. A stored statement may be treated as true merely because it is in the repository.
2. A technically valid inference may be treated as epistemically warranted outside the assumptions of its formal system.
3. A document, graph, or model may be mistaken for the knowledge it represents.
4. Consensus or governance may be mistaken for truth.
5. Propositional knowledge may be treated as the only form of knowledge, excluding skills, methods, and direct familiarity.
6. Human and machine outputs may be granted or denied epistemic standing solely because of their origin.
7. A domain-specific convention may silently enter the universal SymK Core.

The purpose of this paper is not to end the philosophical debate over knowledge. It is to determine what SymK must preserve from that debate, what it must refuse to assume, and what it must engineer so that intelligences can responsibly share what they know.

---

## 2. The first correction: there is no simple historical definition to inherit

The familiar account of propositional knowledge is:

> A subject *S* knows a proposition *P* if and only if *P* is true, *S* believes *P*, and *S* is justified in believing *P*.

This is commonly called the **justified true belief**, or **JTB**, account.

It is often introduced as a definition inherited directly from Plato. That history is too simple. Plato's *Theaetetus* examines the insufficiency of true judgment and considers the addition of an account, but it does not leave us with an unambiguous endorsement of the modern JTB formula. The contemporary Stanford Encyclopedia survey goes further: the idea that JTB was a universally accepted traditional analysis is partly a convenient reconstruction of a more complicated history [Ichikawa and Steup 2026].

This matters to SymK because a foundation should not be built on a pedagogical legend. JTB remains useful as a conceptual decomposition:

- **Truth** separates knowledge from successful error.
- **Belief or acceptance** connects a proposition to an epistemic subject.
- **Justification, warrant, or support** separates knowledge from a lucky guess.

But useful components do not establish a complete definition.

### 2.1 The Gettier rupture

In 1963, Edmund Gettier published two counterexamples in which a subject appears to have a belief that is both justified and true, yet true only through an accidental route [Gettier 1963]. The cases made vivid that justification can point toward a false basis while luck makes the final proposition true.

The important lesson for SymK is broader than the fate of JTB:

> **A claim does not become knowledge merely because its content is true and its holder can present reasons for believing it. The relation among claim, grounds, process, and truth also matters.**

This immediately affects knowledge engineering. A repository can contain a true assertion with impressive documentation and still preserve the wrong reasons. A model can return a correct answer through a brittle correlation. A rule system can infer a true conclusion from a faulty premise if another circumstance happens to make the conclusion true. Correct output alone does not reveal epistemic quality.

### 2.2 Families of post-Gettier responses

The post-Gettier literature did not converge on a single replacement. It produced families of proposals, each highlighting something that knowledge engineering must take seriously:

| Approach | Central intuition | Lesson for SymK |
|---|---|---|
| No-false-lemmas and defeasibility | Knowledge should not depend on a relevant falsehood or survive undefeated counterevidence. | Preserve inferential dependencies, defeaters, and challenges. |
| Reliabilism | A belief should arise from a process that tends to produce truth. | Record the process, method, source performance, and conditions of reliability. |
| Causal approaches | The fact known should be appropriately connected to the belief. | Provenance should include how the content was produced, not only where it was copied from. |
| Sensitivity and safety | Knowledge should track truth across relevant alternatives or avoid easy error in nearby situations. | Test robustness, boundary conditions, and counterfactual failure modes. |
| Virtue epistemology | True belief should arise through epistemic competence. | Model competencies, responsible agents, and the quality of performance. |
| Contextualism and pragmatic approaches | Standards for appropriate knowledge attribution may depend on conversational or practical context. | Make scope, stakes, purpose, and applicable standards explicit. |
| Knowledge-first | Knowledge may be conceptually primitive rather than reducible to more basic conditions. | Do not assume that an engineering schema is a successful philosophical analysis. |

Reliabilism, safety, virtue, and contextual approaches disagree about the nature of knowledge. SymK should not pretend that a database schema can settle those disagreements. It can, however, preserve the distinctions that the disagreements reveal.

### 2.3 Knowledge may be primitive without being unstructured

Timothy Williamson's knowledge-first program argues that knowledge need not be analyzable into more basic epistemic concepts. On this view, knowledge itself can help explain evidence, assertion, and action [Williamson 2000; Ichikawa and Steup 2026].

SymK should take this possibility seriously. A formal object with fields for `truth`, `belief`, and `justification` would not thereby define knowledge. Nevertheless, even if knowledge is primitive, its occurrences can still be characterized by relations, conditions, evidence, limits, and consequences.

This supports a methodological distinction:

- A **philosophical analysis** seeks the nature or necessary and sufficient conditions of knowledge.
- An **engineering characterization** identifies what must be recorded, tested, governed, and preserved when a system claims to support knowledge.

SymK can advance the second while keeping the first open.

---

## 3. Knowledge is not only “knowing that”

The JTB and Gettier debates principally concern propositional knowledge: knowing that something is the case. SymK cannot limit itself to that form.

### 3.1 Propositional knowledge: knowing that

Propositional knowledge has content capable of truth or falsity:

- knowing that a medicine has a contraindication;
- knowing that a legal deadline expires on a date;
- knowing that a specification requires a given behavior.

It is the easiest form to express in claims, rules, and graphs. It is also the form most directly addressed by epistemic logic.

### 3.2 Practical knowledge: knowing how

Gilbert Ryle made the distinction between knowledge-how and knowledge-that central in twentieth-century analytic philosophy. His challenge was that intelligent performance cannot always be reduced to prior contemplation of propositions [Ryle 1949; Pavese 2022].

For SymK, this is decisive. A procedure document is not identical to the ability to perform the procedure. A model description is not the competence to apply it. A physician's diagnostic skill, a lawyer's judgment in an interview, and an engineer's ability to recognize a failure pattern may be partly expressible in propositions but not exhausted by them.

Knowledge-how may require:

- demonstrated capability;
- situated judgment;
- feedback from performance;
- adaptation to cases not explicitly described;
- tacit discrimination learned through practice.

SymK must therefore support capabilities, methods, exemplars, simulations, and performance evidence in addition to propositions.

### 3.3 Knowledge by acquaintance or familiarity

Bertrand Russell distinguished knowledge of truths from direct acquaintance with things, experiences, or particulars [Russell 1910–11, 1912]. The precise theory is controversial, but the distinction identifies another practical boundary. Knowing a person, an organization, a city, a dataset, or a codebase is not always equivalent to knowing a finite list of propositions about it.

Familiarity develops through repeated encounter and may support recognition, expectation, and judgment before it is fully articulated. SymK should not claim to serialize acquaintance. It can preserve records of encounters, observations, exemplars, and the claims derived from them.

### 3.4 A plural foundation

The initial SymK concept should therefore recognize at least three modes:

1. **Knowing that** — propositional, truth-apt content.
2. **Knowing how** — capability or competence manifested in action.
3. **Knowing through acquaintance** — direct or accumulated familiarity with an object, situation, or field of experience.

These modes may interact. A skilled practice may depend on propositions; propositions may be discovered through practice; acquaintance may supply the discriminations required for both. Their representations and validation methods nevertheless differ.

---

## 4. Epistemology and knowledge representation ask different questions

The phrase *knowledge representation* can tempt us to assume that a representation becomes knowledge when it is sufficiently formal. That inference is invalid.

Epistemology asks questions such as:

- What is it for a subject to know?
- Must knowledge be true?
- What excludes epistemic luck?
- What forms of warrant or competence matter?
- Can a group know something that no individual fully knows?

Knowledge representation and reasoning asks questions such as:

- In what language should assertions be encoded?
- What relations and constraints can be expressed?
- What conclusions follow under a chosen semantics?
- Is inference decidable or computationally tractable?
- How can inconsistent or uncertain information be managed?

The two inquiries meet, but they do not coincide. A representation formalism specifies the meaning and manipulation of expressions inside a model. It does not, by itself, establish that the model's assertions are true, responsibly acquired, or suitable for a real decision.

This distinction can be written compactly:

```text
Reality or practice
        │
        │ epistemic relation, inquiry, competence, experience
        ▼
Knowledge and knowledge claims
        │
        │ expression, abstraction, encoding
        ▼
Representations
        │
        │ computation, inference, retrieval, generation
        ▼
Outputs for interpretation or action
```

Engineering acts on every transition. None of the arrows is automatic.

---

## 5. What the major formalisms actually provide

SymK should treat formal systems as complementary projections. Each answers a different class of questions and introduces its own assumptions.

### 5.1 Epistemic modal logic

Epistemic logic introduces operators such as `K_a φ`, read as “agent *a* knows that φ.” In Kripke-style semantics, the operator is evaluated over possible worlds connected by an accessibility relation. The familiar principles include:

- **K:** closure under known implication;
- **T:** if an agent knows φ, then φ is true;
- **4:** if an agent knows φ, the agent knows that it knows φ;
- **5:** if an agent does not know φ, the agent knows that it does not know φ.

S5 can be axiomatized in several equivalent ways, commonly using K, T, and 5, with 4 derivable in the system. S5 is mathematically elegant, but its epistemic interpretation is demanding. Negative introspection assumes a remarkably complete view of one's own epistemic state, and standard closure properties create the problem of logical omniscience: real agents do not know every logical consequence of what they know [Rendsvig, Symons, and Wang 2025].

For SymK, epistemic logic is valuable for modeling explicit commitments and multi-agent information states. It should not be used as an unqualified psychological model of Human Intelligence or Artificial Intelligence.

### 5.2 First-order logic and Horn rules

First-order logic represents objects, predicates, relations, quantification, and implication with precise model-theoretic semantics. Horn-clause subsets support efficient rule-oriented inference and underlie logic programming.

They are powerful for explicit entailment, but classical inference is usually monotonic: adding information does not retract earlier conclusions. Real knowledge processes are often non-monotonic. New evidence can defeat an assumption, narrow a context, or supersede a rule. SymK must therefore distinguish logical consequence inside a formal theory from epistemic acceptance in an evolving environment.

### 5.3 Semantic networks and frames

Early semantic networks organized concepts and associations as nodes and links. Quillian's work on semantic memory made this graph intuition influential. Minsky's frames represented stereotyped situations using structured collections of slots, defaults, and expectations [Quillian 1968; Minsky 1974/1975].

These approaches made context and structured expectation more visible than flat logical clauses, but early systems often lacked standardized formal semantics. Their lasting lesson is that knowledge is not only a list of isolated propositions: structured situations, defaults, and relations matter.

### 5.4 Description logics and OWL

Description logics formalize concepts, roles, individuals, subsumption, and classification while controlling expressiveness to retain useful computational properties. OWL 2 provides standardized ontology languages whose Direct Semantics is connected to the description logic SROIQ. Its profiles deliberately trade expressive power for reasoning performance [W3C 2012].

OWL demonstrates an important engineering principle: greater expressiveness is not free. A language must be selected according to the reasoning tasks, scale, and guarantees required. An ontology can define a domain model and support valid inferences without certifying that its assertions accurately describe the world.

### 5.5 Ontologies and knowledge graphs

Ontologies specify concepts, relations, constraints, and sometimes axioms for a domain. Knowledge graphs organize assertions around identified entities and relations using graph-oriented data models. RDF, for example, defines graphs as sets of subject-predicate-object triples; asserting a triple expresses a claim that a relation holds between denoted resources [W3C 2014]. Modern knowledge graphs may use RDF, property graphs, schemas, rules, embeddings, and deductive or inductive enrichment [Hogan et al. 2021].

The name *knowledge graph* does not remove the epistemic distinction. A graph can contain:

- true, false, outdated, disputed, or context-dependent assertions;
- observations and hypotheses at different maturity levels;
- inferred claims whose validity depends on a chosen entailment regime;
- links with uncertain identity or provenance.

A graph becomes useful for knowledge work when those differences are governed rather than hidden.

### 5.6 Probabilistic representations

Bayesian networks model dependencies among random variables and update degrees of belief under probabilistic assumptions. Markov Logic Networks attach weights to first-order formulas and combine logical structure with probabilistic graphical models [Richardson and Domingos 2006].

These approaches represent uncertainty more naturally than classical true-or-false assertion systems. Yet probability is not identical to epistemic warrant. A calibrated probability, a subjective credence, a statistical frequency, and confidence in a source are different quantities. SymK must identify which uncertainty is being represented and how it was obtained.

### 5.7 Neural representations

Neural models encode learned regularities across distributed parameters rather than explicit symbolic assertions. Research has shown that pretrained language models can recall some relational facts, motivating the question of whether such models function as knowledge bases [Petroni et al. 2019]. Their strengths include flexible generalization and natural-language interaction. Their limitations for governed knowledge include unstable retrieval, opaque provenance, sensitivity to phrasing, difficult correction of individual claims, and no automatic distinction between well-grounded knowledge and plausible completion.

SymK should treat neural models as participants and representational instruments, not as self-authenticating repositories of truth. A generated answer is a contribution to an epistemic process. It becomes a governed knowledge asset only through traceable evaluation and adoption.

### 5.8 Comparative view

| Formalism | Primary object | Strongest contribution | Typical limitation | Appropriate SymK role |
|---|---|---|---|---|
| Epistemic modal logic | Agent-relative modal propositions | Reasoning about who knows what | Idealized introspection and logical closure | Model explicit epistemic states and information change |
| First-order logic | Predicates and quantified formulas | Expressive, precise entailment | General inference is undecidable; often monotonic | Semantic and deductive projection |
| Horn rules | Rules and facts | Executable, efficient inference | Restricted expressiveness; rule conflict and revision need policy | Operational rule projection |
| Frames | Structured situations and defaults | Contextual organization and inheritance | Semantics may be informal or system-specific | Human-oriented schemas and prototypes |
| Description logics / OWL | Concepts, roles, and individuals | Classification with decidable fragments | Expressiveness-performance tradeoff; open-world assumptions | Ontology projection and validation support |
| RDF / knowledge graphs | Entity-relation assertions | Integration, identity, traversal, linked claims | A triple does not carry warrant or truth by itself | Graph projection of claims and provenance |
| Bayesian networks | Probabilistic variables | Uncertain inference under explicit dependencies | Model structure and probabilities may be disputed | Quantified uncertainty projection |
| Markov logic | Weighted logical formulas | Relational uncertainty | Computational cost and model interpretation | Probabilistic-relational experiments |
| Neural models | Distributed parameters | Pattern learning and flexible generation | Opaque grounds, unstable recall, weak claim-level governance | Discovery, synthesis, retrieval, and critique participant |

The comparison leads to a foundational conclusion:

> **SymK should not choose one representation and call it Knowledge. It should govern several projections of knowledge-related objects while preserving the conceptual source they express.**

---

## 6. The distinction SymK must preserve

The central conceptual separation is among **knowledge**, **knowledge claims**, **knowledge assets**, and **representations**.

### 6.1 Knowledge

Knowledge is the epistemic achievement. It concerns the relation between an intelligence and what is known. For propositional knowledge, truth matters. For practical knowledge, competence and successful performance matter. For acquaintance, direct or accumulated relation matters.

SymK cannot manufacture truth by declaring a status, and it cannot directly inspect every cognitive or social condition that makes knowledge obtain.

### 6.2 Knowledge claim

A knowledge claim is an assertion that some intelligence or community presents as true, warranted, reliable, or otherwise fit for reliance. It may later be accepted, restricted, defeated, or rejected.

A claim is representable and governable. It is not knowledge merely by being labeled as one.

### 6.3 Knowledge asset

A knowledge asset is a governed package that makes an epistemic contribution durable and reusable. Depending on its mode, it may connect:

- a proposition, method, capability, model, or object of familiarity;
- its meaning and identity;
- its source and provenance;
- evidence and warrant;
- counterevidence, objections, and alternatives;
- applicable context and scope;
- maturity and acceptance status;
- responsible participants and decisions;
- temporal validity and version history;
- human and machine representations;
- operational tests and observed consequences.

A knowledge asset is the primary object SymK can engineer. It is evidence of, and infrastructure for, knowledge—not a metaphysical container of knowledge.

### 6.4 Representation

A representation is a form in which a claim, capability, relation, or asset is expressed or operationalized: natural language, diagrams, demonstrations, code, logical formulas, RDF triples, database records, embeddings, model weights, or executable procedures.

Several representations may express the same governing concept. Each representation can reveal some structure and hide another. Meaning must not silently migrate to whichever representation is easiest to implement.

### 6.5 Epistemic status

Epistemic status records SymK's current governed position toward an asset. A minimal lifecycle may include:

```text
Observation
    ↓
Claim or candidate capability
    ↓
Under evaluation
    ↓
Provisionally accepted
    ↓
Accepted for a stated scope
    ↓
Challenged, restricted, superseded, or reaffirmed
```

These are governance states, not truth values. `Accepted` means that a claim has satisfied a declared process for a declared use. It never means that SymK has made the proposition true.

---

## 7. A working definition for SymK

The following definition is proposed as a foundation for continued inquiry, not as a final philosophical victory:

> **Knowledge, in SymK, is an epistemic achievement in which an intelligence, or a cooperative system of intelligences, stands in a sufficiently truth-connected, competence-bearing, or direct relation to what is known such that it may be responsibly relied upon within a stated scope.**

Each phrase performs a necessary function.

### Epistemic achievement

Knowledge is not accidental success. The term leaves room for warrant, reliability, safety, competence, and appropriate causal relations without prematurely selecting one complete theory.

### An intelligence, or a cooperative system of intelligences

The original Human-AI case remains included, while the definition allows Human-Human, AI-AI, organizational, and future forms of cooperation. Whether a collective literally knows, or only distributes the conditions of knowledge among participants, remains an open foundational question.

### Truth-connected, competence-bearing, or direct relation

The alternatives correspond to the plural modes:

- truth-connected for propositional knowledge;
- competence-bearing for knowledge-how;
- direct or accumulated relation for acquaintance and familiarity.

The definition does not claim that these modes are reducible to a single formula.

### Responsibly relied upon

Knowledge has consequences. In SymK, calling something knowledge authorizes some form of reasoning or action. Responsible reliance requires that uncertainty, limitations, and applicable standards remain visible.

### Within a stated scope

What may be relied upon in one context may be insufficient in another. Scope can include domain, time, jurisdiction, population, task, stakes, assumptions, and required confidence. Scope does not make truth relative; it makes the conditions and limits of the claim explicit.

### 7.1 The operational corollary

Because an engineered system cannot simply place an epistemic achievement inside a file, SymK requires a second statement:

> **SymK engineers governed knowledge assets that preserve the best available, challengeable evidence that knowledge has been achieved, together with the representations required to share and apply it.**

This is how the philosophical foundation becomes an engineering program.

### 7.2 Interpreting the constitutional motto

The motto can now be read precisely:

> **Knowledge is the shared medium** means that cooperation proceeds through governed epistemic achievements and knowledge assets whose meaning, grounds, scope, and history can survive changes in participant and representation.

It does **not** mean that every shared artifact is knowledge, that the repository is infallible, or that governance creates truth.

---

## 8. The proposed SymK knowledge object

The following is a conceptual inventory, not a database schema:

```text
KnowledgeObject
├── identity
├── epistemic mode
│   ├── knowing-that
│   ├── knowing-how
│   └── acquaintance/familiarity
├── content or capability
├── subject or responsible community
├── object or referent
├── scope and context
├── grounds
│   ├── evidence
│   ├── method or process
│   ├── provenance
│   └── relevant competence
├── epistemic assessment
│   ├── maturity/status
│   ├── confidence or uncertainty model
│   ├── defeaters and counterevidence
│   └── relevant alternatives
├── governance
│   ├── decisions
│   ├── responsibilities
│   ├── version and temporal validity
│   └── adoption scope
├── representations
│   ├── human
│   ├── semantic/formal
│   └── operational/machine
└── application and validation history
```

The structure encodes several principles:

1. Content is not separated from grounds.
2. Acceptance is not separated from scope.
3. Current status is not separated from history.
4. Representations are plural and subordinate to the governing object.
5. Objections and failed tests remain part of the knowledge asset.
6. The participant who proposes a claim need not be the authority who adopts it.
7. Human and artificial contributions are evaluated through traceable epistemic roles, not prestige or origin alone.

---

## 9. Candidate foundational commitments

The following commitments are candidates for the future SymK Axiomatic Constitution. This paper proposes them for examination; it does not silently ratify them as axioms.

### K-01 — Knowledge and representation are distinct

No document, graph, rule, database record, prompt, embedding, or model weight is identical to the knowledge it represents or supports.

**Engineering consequence:** Every technical object must identify its conceptual and epistemic source.

### K-02 — Truth is not created by governance

Approval, consensus, authority, repetition, or successful storage does not make a proposition true.

**Engineering consequence:** Epistemic status and truth conditions must not use the same field or identifier.

### K-03 — No knowledge claim is context-free in application

Reliance occurs within a scope of domain, assumptions, time, purpose, and stakes.

**Engineering consequence:** Scope and context are first-class, not explanatory notes added later.

### K-04 — Grounds are part of the durable asset

A conclusion without accessible provenance, evidence, method, or competence cannot support cumulative cooperation at the required level.

**Engineering consequence:** SymK preserves why and how, not only what.

### K-05 — Operational acceptance remains defeasible

SymK must be able to revise what it accepts without pretending that earlier states never existed.

**Engineering consequence:** Challenges, supersession, and lineage are normal lifecycle events.

### K-06 — Contradiction must be represented before it is resolved

Conflicting claims may expose different contexts, concepts, assumptions, or evidence. Premature merging destroys information.

**Engineering consequence:** Preserve competing positions and their scopes; do not force a single value merely for storage convenience.

### K-07 — Knowledge has plural modes

Knowing-that, knowing-how, and acquaintance cannot be assumed to share one representation or validation process.

**Engineering consequence:** Capability and experience evidence must not be forced into proposition-only structures.

### K-08 — Formal inference is conditional knowledge work

A conclusion is valid relative to a formalism, premises, semantics, and inference regime. Validity inside that system is not sufficient for real-world truth or responsible use.

**Engineering consequence:** Derived claims must retain their premises and inference context.

### K-09 — Epistemic standing is not conferred by participant type

A human assertion is not knowledge merely because a human made it. An artificial output is not knowledge merely because a model generated it, nor is it disqualified merely because it is artificial.

**Engineering consequence:** Record the epistemic role, process, evidence, and evaluation of each contribution.

### K-10 — Shared knowledge is not mere consensus

A group may agree and be wrong. It may also distribute relevant evidence, competence, and responsibility across participants without any one participant possessing the whole.

**Engineering consequence:** Model agreement separately from warrant and model collective dependencies explicitly.

### K-11 — Knowledge must remain challengeable

An asset that cannot expose its grounds, limits, alternatives, or revision path cannot participate fully in SymK's cooperative objective.

**Engineering consequence:** Challenge and review interfaces are constitutional features, not optional collaboration tools.

### K-12 — Knowledge engineering begins before implementation

Storage and inference technologies may test a concept, but they may not silently define it.

**Engineering consequence:** The Knowledge concept and its governance must be specified independently from any particular graph, database, model, or file format.

---

## 10. Implications for Human-AI and multi-intelligence cooperation

The proposed foundation changes how SymK understands participation.

### 10.1 AI output is a contribution, not a verdict

An artificial system may retrieve evidence, discover patterns, generate hypotheses, formalize relations, test consistency, simulate alternatives, or critique an argument. These are substantial epistemic contributions. They do not independently establish that an output is knowledge.

The same is true of Human Intelligence. Testimony, expertise, lived experience, and judgment can be powerful grounds, but human authorship is not a truth condition.

### 10.2 Roles may be distributed

One intelligence may observe, another may formalize, a third may challenge, and a fourth may authorize use within an organization. The resulting epistemic achievement may be cooperative even when responsibilities differ.

SymK should preserve at least the roles of:

- source or observer;
- claimant;
- interpreter;
- formalizer;
- critic;
- validator;
- decision authority;
- adopter;
- affected party;
- maintainer.

The roles should not be permanently assigned by intelligence type. A Human Intelligence can formalize; an Artificial Intelligence can critique; an organization can adopt; a machine process can validate a formal constraint; a domain expert can reject the relevance of that formal validation to practice.

### 10.3 Shared does not mean identical

Different intelligences need not possess identical internal representations. Cooperation requires sufficient semantic alignment, traceable translation, and visibility of disagreement—not cognitive uniformity.

Human-readable explanation, formal semantics, executable rules, and neural encodings may be complementary projections. SymK's task is to preserve their governed relationship.

---

## 11. Development requirements derived from the foundation

Any SymK implementation of knowledge should satisfy the following requirements.

### 11.1 Separate the layers

The implementation must distinguish:

- concept from representation;
- claim from acceptance;
- acceptance from truth;
- evidence from conclusion;
- provenance from authority;
- logical validity from empirical reliability;
- confidence from probability;
- current state from historical state.

### 11.2 Preserve epistemic lineage

For any material claim, a participant should be able to determine:

1. who or what introduced it;
2. what it originally meant;
3. which sources or experiences supported it;
4. how it changed;
5. what objections were raised;
6. why its current status was assigned;
7. where it is adopted;
8. which representations express it;
9. what would cause it to be reconsidered.

### 11.3 Support non-monotonic evolution

The system must allow new evidence to restrict, defeat, or supersede earlier conclusions. It must retain the earlier state for audit and learning without presenting it as current.

### 11.4 Allow multiple representational projections

Natural-language definitions, examples, formal axioms, graph structures, rules, tests, and machine-oriented schemas should trace to the same governed concept where appropriate. A change in one projection must not silently rewrite the others.

### 11.5 Make uncertainty typed

The system should not reduce all uncertainty to one scalar. It should distinguish, where relevant:

- confidence in a source;
- probability of an event;
- incompleteness of evidence;
- ambiguity of meaning;
- disagreement among participants;
- instability across contexts;
- model uncertainty;
- unresolved contradiction.

### 11.6 Preserve negative results

Failed hypotheses, counterexamples, rejected formulations, and boundary failures are knowledge assets when their status and rationale are explicit. Deleting them weakens future cooperation by forcing rediscovery.

### 11.7 Avoid premature universalization

A concept validated in LexBrain, SPServicesAPI, sshConnectivity, medicine, law, or infrastructure is evidence for SymK. It enters the universal Core only after its domain assumptions have been exposed and it has survived the appropriate conceptual process.

---

## 12. Open foundational questions

This paper narrows the problem but does not close it. At least the following questions require deliberate SymK work.

### 12.1 Is knowledge necessarily factive in the formal SymK vocabulary?

The dominant philosophical view holds that false propositions cannot be known. SymK should likely preserve factivity for propositional Knowledge while using `KnowledgeClaim`, `AcceptedClaim`, or `EpistemicAsset` for fallible system states. The exact terminology and migration consequences remain to be decided.

### 12.2 Can a cooperative system literally know?

Organizations and distributed teams often act on knowledge that no individual fully possesses. SymK must determine whether collective knowledge is a genuine epistemic state, a structured distribution of individual states and artifacts, or both under different conditions.

### 12.3 What qualifies an artificial system as an epistemic subject?

The answer cannot be assumed from current product labels. Candidate considerations include stable identity, capacity to form and revise commitments, sensitivity to evidence, memory, competence, self-modeling, accountability relations, and participation in challenge.

### 12.4 How should knowledge-how be governed?

Capability evidence may include demonstrations, outcomes, simulations, supervision, accreditation, repeated performance, and transfer to new cases. SymK needs maturity and validation models that do not reduce skill to a procedure document.

### 12.5 What is the relation between knowledge and understanding?

An agent may retrieve true propositions without understanding their relations or significance. Understanding may be a separate epistemic achievement required for explanation, transfer, or responsible action.

### 12.6 How should context affect knowledge attribution?

SymK must distinguish three possibilities:

- the proposition itself varies with context;
- the evidential standard varies with context;
- the proposition and evidence remain fixed while authorization for reliance varies with stakes.

These should not be collapsed into one generic `context` field.

### 12.7 How should conflicting but locally successful models coexist?

Different models may predict effectively at different scales or for different purposes while offering incompatible explanations. SymK needs a principled account of model scope, pluralism, and inter-model relations.

### 12.8 What are the smallest irreducible primitives?

The final Knowledge concept may depend on Truth, Intelligence, Claim, Evidence, Warrant, Context, Representation, Capability, Experience, and Responsibility. Primitive Minimalism requires that none be promoted merely because it is familiar or convenient.

---

## 13. A practical evaluation gate

Before a proposed object is admitted as a SymK knowledge asset, reviewers should ask:

| Gate | Question |
|---|---|
| Identity | What exactly is the claim, capability, or object of familiarity? |
| Mode | Is this knowing-that, knowing-how, acquaintance, or a combination? |
| Grounds | What evidence, process, competence, or direct relation supports it? |
| Truth connection | For a proposition, how is the claim connected to what makes it true rather than merely to a successful answer? |
| Scope | Under which domain, time, assumptions, population, task, and stakes may it be relied upon? |
| Alternatives | Which plausible counterexamples, defeaters, or competing explanations were considered? |
| Provenance | Can the contribution be traced through sources, transformations, and participants? |
| Status | What has been observed, inferred, evaluated, accepted, or merely proposed? |
| Representation | Which human, semantic, and machine projections exist, and do they remain aligned? |
| Responsibility | Who may challenge, decide, adopt, maintain, and bear consequences? |
| Revision | What evidence would restrict, defeat, or supersede the asset? |
| Cooperation | How does the asset improve cumulative cooperation among intelligences? |

Passing the gate does not prove knowledge in the philosophical sense. It establishes that SymK has preserved the conditions required for responsible shared use and future challenge.

---

## 14. Conclusion

The literature does not give SymK a single definition ready to copy. That is not a failure. It reveals the dimensions that any serious Engineering of Knowledge System must preserve.

Philosophical epistemology shows that truth, belief, warrant, reliability, competence, luck, context, and agency cannot be reduced to the fact that a statement was stored or accepted. The distinctions among knowing-that, knowing-how, and acquaintance show that knowledge is not exhausted by propositions. Knowledge-first epistemology warns that a formal decomposition may characterize knowledge without analyzing it into more basic parts.

Knowledge-representation research supplies powerful languages for expressing claims, relations, constraints, uncertainty, and agent-relative information. It also demonstrates that each formalism trades one capability for another. Epistemic logic idealizes agents. Description logics control expressiveness for decidability. Graphs integrate claims but do not certify them. Probabilistic models quantify selected uncertainties. Neural models learn and generate patterns but do not automatically expose grounds or governance.

SymK's foundational task is therefore not to declare one of these representations to be knowledge. It is to engineer a governed bridge between epistemic achievement and durable cooperative use.

The proposed working definition is:

> **Knowledge, in SymK, is an epistemic achievement in which an intelligence, or a cooperative system of intelligences, stands in a sufficiently truth-connected, competence-bearing, or direct relation to what is known such that it may be responsibly relied upon within a stated scope.**

The proposed engineering corollary is:

> **SymK engineers governed knowledge assets that preserve the best available, challengeable evidence that knowledge has been achieved, together with the representations required to share and apply it.**

Together, these statements protect the constitutional motto:

> **Knowledge is the shared medium. Cooperation is the objective.**

Knowledge remains the medium not because SymK makes every artifact true, but because it preserves the epistemic relations, grounds, meanings, capabilities, contexts, and histories that allow different intelligences to understand, challenge, apply, and improve what they share.

---

## References

Baader, F., Calvanese, D., McGuinness, D. L., Nardi, D., and Patel-Schneider, P. F., eds. (2003). *The Description Logic Handbook: Theory, Implementation and Applications*. Cambridge University Press. [Publisher record](https://books.google.com/books?id=riSeOKw5I6sC).

Brachman, R. J., and Levesque, H. J. (2004). *Knowledge Representation and Reasoning*. Morgan Kaufmann. [Publisher sample chapter](https://booksite.elsevier.com/samplechapters/9781558609327/9781558609327.PDF).

Pavese, C. (2022). “Knowledge How.” *Stanford Encyclopedia of Philosophy*, Fall 2022 edition. [Stable entry](https://plato.stanford.edu/archives/fall2022/entries/knowledge-how/).

Hasan, A., and Fumerton, R. (2024). “Knowledge by Acquaintance vs. Description.” *Stanford Encyclopedia of Philosophy*, Summer 2024 edition. [Stable entry](https://plato.stanford.edu/archives/sum2024/entries/knowledge-acquaindescrip/).

Gettier, E. L. (1963). “Is Justified True Belief Knowledge?” *Analysis*, 23(6), 121–123. [DOI and journal record](https://academic.oup.com/analysis/article-abstract/23/6/121/109949).

Rendsvig, R., Symons, J., and Wang, Y. (2025). “Epistemic Logic.” *Stanford Encyclopedia of Philosophy*, Summer 2025 edition. [Stable entry](https://plato.stanford.edu/archives/sum2025/entries/logic-epistemic/).

Hogan, A., Blomqvist, E., Cochez, M., et al. (2021). “Knowledge Graphs.” *ACM Computing Surveys*, 54(4), Article 71. [DOI](https://doi.org/10.1145/3447772); [open manuscript](https://arxiv.org/abs/2003.02320).

Ichikawa, J., and Steup, M. (2026). “The Analysis of Knowledge.” *Stanford Encyclopedia of Philosophy*, Summer 2026 edition. [Stable entry](https://plato.stanford.edu/archives/sum2026/entries/knowledge-analysis/).

Minsky, M. (1974/1975). “A Framework for Representing Knowledge.” MIT-AI Laboratory Memo 306; reprinted in *The Psychology of Computer Vision*. [MIT text](https://www.mit.edu/~dxh/marvin/web.media.mit.edu/~minsky/papers/Frames/frames.html).

Petroni, F., Rocktäschel, T., Riedel, S., Lewis, P., Bakhtin, A., Wu, Y., and Miller, A. (2019). “Language Models as Knowledge Bases?” In *Proceedings of EMNLP-IJCNLP 2019*, 2463–2473. [ACL Anthology](https://aclanthology.org/D19-1250/). DOI: [10.18653/v1/D19-1250](https://doi.org/10.18653/v1/D19-1250).

Quillian, M. R. (1968). “Semantic Networks.” In M. Minsky, ed., *Semantic Information Processing*. MIT Press. [Bibliographic record](https://philpapers.org/rec/QUISN).

Richardson, M., and Domingos, P. (2006). “Markov Logic Networks.” *Machine Learning*, 62, 107–136. [DOI](https://doi.org/10.1007/s10994-006-5833-1).

Russell, B. (1910–11). “Knowledge by Acquaintance and Knowledge by Description.” *Proceedings of the Aristotelian Society*, 11, 108–128.

Russell, B. (1912). *The Problems of Philosophy*. Williams and Norgate.

Ryle, G. (1949). *The Concept of Mind*. Hutchinson.

Williamson, T. (2000). *Knowledge and Its Limits*. Oxford University Press.

W3C (2012). *OWL 2 Web Ontology Language Document Overview, Second Edition*. W3C Recommendation. [Specification](https://www.w3.org/TR/owl2-overview/).

W3C (2014). *RDF 1.1 Concepts and Abstract Syntax*. W3C Recommendation. [Specification](https://www.w3.org/TR/rdf11-concepts/).

---

## Document governance note

This paper should evolve through explicit SymK governance. Revisions should distinguish:

- corrections to the literature survey;
- changes to the proposed working definition;
- changes to candidate foundational commitments;
- changes to implementation guidance;
- resolution of open foundational questions.

No implementation should silently promote the conceptual inventory in Section 8 into the canonical SymK schema. The inventory is evidence for specification work, not a substitute for it.
