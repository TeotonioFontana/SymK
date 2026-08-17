# Definitions of Knowledge and Its Formal Representations: A Literature Survey

---

## 1. Introduction

"Knowledge" is one of the most contested concepts across intellectual disciplines. It sits at the intersection of philosophy, cognitive science, computer science, and information theory, with each field generating its own vocabulary and formalisms. This survey maps the landscape from classical philosophical accounts to the symbolic and graph-theoretic formalisms used in modern artificial intelligence.

---

## 2. Philosophical Definitions of Knowledge

### 2.1 The Classical Analysis: Justified True Belief (JTB)

The dominant twentieth-century account holds that an agent *S* **knows** that *p* if and only if:

1. *p* is **true**,
2. *S* **believes** *p*, and
3. *S* is **justified** in believing *p*.

This tripartite definition descends from Plato's *Meno* and *Theaetetus*, where knowledge is distinguished from mere true opinion by the addition of a "reason" or "account." It became the working framework of analytic epistemology and is still the standard starting point.

### 2.2 The Gettier Problem (1963)

Edmund Gettier's landmark three-page paper ("Is Justified True Belief Knowledge?", 1963) showed that JTB is not *sufficient*. He constructed cases—now called **Gettier cases**—where an agent holds a justified true belief that intuitively does not count as knowledge, because the truth of the belief is a matter of luck rather than epistemic reliability. A classic example: Smith justifiably infers from a false but justified belief that "Jones will get the job" the disjunction "Jones will get the job *or* Smith will get the job"; the disjunction is true (because Smith gets the job), the belief is justified, yet Smith does not *know* it in the intended sense.

### 2.3 Post-Gettier Theories

Gettier's paper triggered a half-century of responses, each adding a fourth condition or reconceiving the analysis:

**Reliabilism** (Goldman, 1976): Knowledge is true belief produced by a *reliable* cognitive process—one that tracks truth across a wide range of cases. Justification is reconceived in causal-process terms rather than as an internalist logical relation.

**Causal Theory** (Goldman, 1967): The fact that *p* must be appropriately causally connected to the belief that *p*. This handles standard Gettier cases but struggles with knowledge of mathematical or future facts.

**Defeasibility Theory** (Lehrer & Paxson, 1969): Knowledge requires that no true defeater—a true proposition that, if known, would undercut the justification—exists. S knows that *p* if S has justified true belief and there is no true proposition *d* such that, if S came to know *d*, S would no longer be justified in believing *p*.

**Sensitivity** (Nozick, 1981): *S* knows that *p* only if: were *p* false, *S* would not believe *p* (a subjunctive conditional / counterfactual condition, sometimes called "truth-tracking").

**Safety** (Sosa, 1999; Pritchard, 2005): *S* knows that *p* only if: *S* would believe *p* only if *p* were true—i.e., in close possible worlds where *S* forms the same belief, *p* holds. Safety avoids some counterexamples to sensitivity.

**Virtue Epistemology** (Sosa, Greco, Zagzebski): Knowledge is **apt** belief—a belief that is accurate (true), adroit (the product of the agent's intellectual competence), and *apt because adroit* (its truth manifests the exercise of a reliable intellectual virtue). Zagzebski's version requires that the truth be due to an act of intellectual virtue.

**Relevant Alternatives Theory**: *S* knows that *p* only if *S* can rule out all relevant alternatives to *p*. "Relevance" is context-sensitive, which explains why everyday knowledge claims survive without requiring the elimination of far-fetched skeptical scenarios.

**Contextualism** (DeRose, Cohen, Lewis): The word "knows" is context-sensitive; the standards for knowledge attribution shift with the conversational context. In high-stakes contexts the bar rises; in ordinary contexts it lowers. This is a semantic, rather than metaphysical, response to Gettier-type puzzles and to skepticism.

**Pragmatic Encroachment / Interest-Relative Invariantism** (Stanley, Hawthorne): The practical stakes for an agent affect whether that agent genuinely knows—not just whether knowledge is attributed to them. The concept itself is interest-relative.

**Knowledge-First Epistemology** (Williamson, 2000): Knowledge is *primitive* and *unanalyzable*. Rather than analyzing knowledge in terms of belief + conditions, Williamson argues that "knows" cannot be reduced to any non-factive mental state plus further conditions. Knowledge is the most general factive mental state; belief is understood in terms of knowledge (to believe is to take something to be known).

### 2.4 Non-Propositional Knowledge

The analyses above concern **knowledge-that** (*propositional* knowledge). Two further varieties are important:

- **Knowledge-how** (procedural / competence knowledge): Gilbert Ryle (*The Concept of Mind*, 1949) distinguished "knowing that" from "knowing how." The latter is manifested in skillful performance and cannot be fully reduced to a set of propositional beliefs (the "intellectualist" reduction is contested by neo-Ryleans and defended by "intellectualists" such as Stanley & Williamson, 2001).

- **Knowledge by acquaintance**: Bertrand Russell distinguished knowledge by description (mediated by concepts) from knowledge by acquaintance (direct, unmediated familiarity with particulars—sense data, one's own mental states). This distinction has influenced debates in philosophy of mind and phenomenology.

### 2.5 Broader and Interdisciplinary Definitions

- **Pragmatist / Austinian**: J. L. Austin defines knowledge operationally as the *ability to make correct and confident assertions* about a domain. Knowledge is demonstrated by successful performance, not by internal epistemic states.
- **Anthropological / sociological**: Knowledge is understood as *culturally transmitted understanding*—a body of beliefs, practices, and skills that a community reproduces across time (cf. knowledge anthropology and Science and Technology Studies).
- **Information-theoretic**: Sometimes equated with "true information possessed by an agent," distinguishing knowledge from data (raw signals) and information (organized, meaningful data).

---

## 3. Formal Representations of Knowledge

### 3.1 Epistemic Logic (Modal Logic for Knowledge)

Epistemic logic formalizes knowledge as a **modal operator** over propositional or first-order logic. The standard language introduces, for each agent *a*, a unary operator **K_a**, where *K_a φ* reads "agent *a* knows that *φ*."

**Kripke Semantics**: A model *M = (W, R, V)* consists of:
- *W*: a non-empty set of **possible worlds**,
- *R*: an **accessibility relation** on *W* (for each agent *a*, a relation *R_a ⊆ W × W*; *w R_a v* means "world *v* is epistemically possible for *a* in world *w*"),
- *V*: a **valuation function** assigning truth values to atomic propositions at worlds.

The truth condition: *M, w ⊨ K_a φ* iff *M, v ⊨ φ* for all *v* such that *w R_a v*. That is, *a* knows *φ* in *w* precisely when *φ* holds in every world *a* cannot rule out from *w*.

**Key Axiom Schemas** (each corresponds to a property of *R_a*):

| Axiom | Formula | Property of *R_a* | Epistemic reading |
|-------|---------|-------------------|-------------------|
| **K** | K_a(φ → ψ) → (K_a φ → K_a ψ) | — (normality) | Knowledge distributes over implication |
| **T** | K_a φ → φ | Reflexivity | Knowledge is factive (truth condition) |
| **4** | K_a φ → K_a K_a φ | Transitivity | Positive introspection: knowing implies knowing that one knows |
| **5** | ¬K_a φ → K_a ¬K_a φ | Euclidean | Negative introspection: not knowing implies knowing that one doesn't know |
| **B** | φ → K_a ¬K_a ¬φ | Symmetry | — |

The system **S5** (K + T + 4 + 5) characterizes equivalence relations (*R_a* is reflexive, transitive, symmetric). S5 is the canonical logic of **ideal knowledge**, often used in theoretical computer science and game theory. Weaker systems (e.g., **KT4 = S4**) are used when negative introspection is doubted.

**Belief vs. Knowledge**: The **B_a** (belief) operator replaces T with the **D** axiom (K_a φ → ¬K_a ¬φ; consistency), yielding the system **KD45** as the canonical logic of *rational* (consistent, positively and negatively introspective) belief—weaker than S5 because belief need not be factive.

**Multi-Agent Extensions**: In systems with *n* agents, *n* accessibility relations are introduced. Group epistemic operators include:
- **E_G φ** ("everyone in group *G* knows *φ*"): conjunction of individual knowledge,
- **C_G φ** ("it is common knowledge in *G* that *φ*"): K_G φ ∧ K_G K_G φ ∧ … (infinite conjunction, formalized via the reflexive transitive closure of the union of agents' relations),
- **D_G φ** ("it is distributed knowledge in *G* that *φ*"): what would be known if agents pooled all their information.

Common knowledge (Aumann, 1976; Lewis, 1969) plays a foundational role in game theory and the analysis of social conventions.

### 3.2 Logical Knowledge Representation

**Propositional Logic**: Facts are represented as Boolean propositions; a knowledge base is a set of sentences closed under logical consequence. Truth-functional and computationally tractable (SAT-solving), but limited in expressiveness.

**First-Order Logic (FOL)**: The standard language of classical AI knowledge representation. Objects are denoted by constants and variables; predicates express properties and relations; quantifiers (∀, ∃) allow general statements. FOL is complete (Gödel) and semi-decidable, but full first-order inference is undecidable. *Knowledge bases* in FOL are sets of sentences; an agent "knows *p*" is modelled as *p* being entailed by the KB.

**Horn Clauses and Logic Programming (Prolog)**: A decidable fragment of FOL used in logic programming. A Horn clause has at most one positive literal. Datalog (Horn clauses without function symbols) is decidable and widely used in deductive databases and ontology reasoning.

**Default Logic / Non-Monotonic Reasoning** (Reiter, 1980): Classical logic is monotonic—adding facts never retracts conclusions. Default logic introduces *default rules* of the form "In the absence of information to the contrary, assume *C*." Closely related systems include autoepistemic logic (Moore, 1985)—where an agent reasons about its *own* knowledge state—and circumscription (McCarthy, 1980).

### 3.3 Semantic Networks

Introduced by Quillian (1968) as a psychological model of memory, semantic networks represent knowledge as **labeled directed graphs** where:
- **Nodes** represent concepts or entities,
- **Labeled edges** represent semantic relations (IS-A, PART-OF, HAS-PROPERTY, etc.).

Semantic networks support *inheritance reasoning*: properties attached to a concept node are inherited by all nodes connected to it via IS-A links. They formed the conceptual basis for later frame systems and ontologies.

### 3.4 Frame Systems

Minsky's **frames** (1975) organize knowledge about stereotypical situations (objects, events, processes) into record-like structures:
- A **frame** is a named data structure with **slots** (attributes) and **fillers** (values or defaults).
- Slots can have procedural attachments (if-needed, if-changed demons) for active inference.
- Frame inheritance allows sub-frames to inherit and override slot values from parent frames.

Frame systems influenced object-oriented programming and are the conceptual ancestor of class-based ontology languages (RDF Schema, OWL).

### 3.5 Production Rules

**Production systems** (Newell & Simon, 1972; used in MYCIN, OPS5, CLIPS, Drools) encode knowledge as a collection of **if-then rules**:

*IF* (condition pattern matches working memory) *THEN* (action or new assertion)

A **conflict resolution** strategy (recency, specificity, etc.) selects which rule to fire when multiple rules match. Production systems model expert knowledge explicitly, support explanation, and are easy to update—but can suffer from combinatorial explosion and frame problems at scale.

### 3.6 Description Logics (DLs)

Description logics are a family of formal, decidable fragments of FOL designed specifically for **terminological knowledge**. They underpin modern ontology languages.

**Syntactic elements**:
- **Concepts** (unary predicates): *Person*, *Employee*,
- **Roles** (binary predicates): *hasParent*, *worksFor*,
- **Individuals** (constants): *alice*, *bob*.

**TBox** (terminological box): axioms defining concept hierarchies and equivalences, e.g.,
  *Employee ⊑ Person* (every employee is a person),
  *HappyStudent ≡ Student ⊓ ∃hasHobby.⊤*.

**ABox** (assertional box): ground facts about individuals, e.g.,
  *Employee(alice)*, *worksFor(alice, ACME)*.

**ALC** (1991) is the foundational DL, supporting concept conjunction (⊓), disjunction (⊔), complement (¬), existential restriction (∃R.C), and universal restriction (∀R.C).

More expressive DLs add: role hierarchies (**H**), transitivity (**S** in place of ALC), inverse roles (**I**), nominals (**O**), unqualified number restrictions (**N**), qualified cardinality restrictions (**Q**), yielding the family **SROIQ** on which **OWL 2** is based. OWL (Web Ontology Language) is the W3C standard for the Semantic Web, with profiles OWL-Lite, OWL-DL (SHOIN semantics), and OWL 2 Full.

Key reasoning services: *satisfiability* (is a concept coherent?), *subsumption* (is C a subclass of D?), *instance checking* (does individual *a* belong to concept *C*?), *query answering*.

### 3.7 Ontologies

An **ontology** (in the computational sense, Gruber 1993) is "a formal, explicit specification of a shared conceptualization." It consists of:
- **Classes** (concepts, categories),
- **Properties** (relations between classes or between classes and data values),
- **Instances** (individuals),
- **Axioms** (logical constraints and definitions).

Prominent ontologies include: WordNet (lexical), Cyc (common sense), Gene Ontology (biology), SNOMED CT (medicine), schema.org (web data), DOLCE and BFO (upper/foundational ontologies). Ontologies differ from databases in that the formal axioms enable *deductive inference*—deriving knowledge not explicitly stored.

### 3.8 Knowledge Graphs

A **knowledge graph** (Hogan et al., 2021, *ACM Computing Surveys*) is defined as "a graph of data intended to accumulate and convey knowledge of the real world, whose nodes represent entities of interest and whose edges represent relations between these entities."

**Core models**:

1. **Directed Edge-Labelled Graph (DELG)**: A set of triples (*subject*, *predicate*, *object*) — the model of **RDF** (Resource Description Framework). Subjects and objects are nodes; predicates are labeled directed edges. IRIs provide global identifiers; literals carry data values. An RDF knowledge graph is formally a set *G ⊆ (I ∪ B) × I × (I ∪ B ∪ L)* where *I* = IRIs, *B* = blank nodes, *L* = literals.

2. **Property Graph**: Nodes and edges both carry property-value pairs and type labels. Used by graph databases such as Neo4j. More expressive for annotation but without a standard formal semantics comparable to RDF.

**Schema layers**:
- *Semantic schema* (ontology/OWL): defines the meaning of vocabulary, enables reasoning,
- *Validating schema* (SHACL, ShEx): enforces structural constraints on instances,
- *Emergent schema*: summary structures discovered from the data (e.g., graph summaries).

**Deductive knowledge**: By coupling a knowledge graph with an ontology under OWL semantics or rule languages (SPARQL, SWRL, Datalog), systems can derive implicit triples from explicit ones.

**Major real-world knowledge graphs**: Freebase, Wikidata, DBpedia, YAGO, Google Knowledge Graph, Amazon Product Graph.

### 3.9 Probabilistic and Uncertain Knowledge Representation

Classical logical formalisms assume binariness; probabilistic approaches model epistemic uncertainty:

- **Bayesian Networks** (Pearl, 1988): A directed acyclic graph (DAG) where nodes are random variables and edges encode conditional independence. The joint distribution factorizes as a product of conditional distributions. They represent *uncertain* knowledge and support inference by belief propagation.
- **Markov Logic Networks** (Richardson & Domingos, 2006): Each FOL formula is given a weight; the resulting distribution over possible worlds favors those satisfying more high-weight formulas. Integrates logical structure with probabilistic inference.
- **Probabilistic Ontologies / Ontologies with Uncertainty** (e.g., PR-OWL, BEL with uncertainty): Extend DL-based ontologies to handle degrees of belief.

### 3.10 Hybrid and Intensional Approaches

Recent work (e.g., Ngo et al., 2023, MDPI *AI*) proposes a formal two-level framework:
- **Intensional level (Θ)**: General concepts and meanings defined across all possible worlds, corresponding to the epistemological dimension (what concepts *mean*),
- **Extensional level (Φ)**: Instantiation of concepts within specific possible worlds, corresponding to the ontological dimension (what *exists*).

Epistemic logic operators bridge these levels, enabling agents with different interpretations to communicate coherently—addressing limitations of purely extensional logics such as FOL and DL in decentralized, multi-perspective systems.

---

## 4. Comparative Overview

| Framework | Expressiveness | Decidability | Handles uncertainty | Main use case |
|-----------|---------------|-------------|-------------------|---------------|
| Propositional Logic | Low | Yes (NP-complete SAT) | No | Simple rule systems |
| First-Order Logic | High | No (semi-decidable) | No | Mathematical reasoning |
| Description Logics (DL) | Medium–high | Yes (varies by DL) | No | Ontologies, Semantic Web |
| Epistemic Logic (S5) | Medium | Yes | No | Multi-agent systems, game theory |
| Semantic Networks | Low–medium | Informal | No | Legacy AI, NLP |
| Frames | Medium | Informal | Partial (defaults) | Expert systems, OOP |
| Production Rules | Medium | Yes (with restrictions) | No | Expert systems |
| Bayesian Networks | High (probabilistic) | Yes (inference NP-hard) | Yes | Decision support, diagnosis |
| Markov Logic | Very high | No (approximate) | Yes | Statistical relational AI |
| Knowledge Graphs (RDF+OWL) | High | Varies by profile | Partial | Web data integration |

---

## 5. Key Tensions and Open Questions

**Luck and reliability**: Most post-Gettier proposals try to exclude "lucky" true beliefs, but defining epistemic luck without circularity remains hard.

**Closure and skepticism**: The principle that if *S* knows *p*, and *S* knows *p → q*, then *S* knows *q* (closure) is plausible but has skeptical consequences. Contextualists and relevant-alternatives theorists deny closure in some forms.

**Implicit vs. explicit knowledge**: A knowledge base may *entail* many propositions the agent has never derived—is that "known"? Epistemic logic's S5 treats the closure of knowledge under logical consequence as trivial, which is computationally unrealistic.

**Granularity and non-monotonicity**: Real-world knowledge systems must handle defaults, exceptions, and revision. Classical logic and DLs are monotonic; production rules and default logic provide partial answers.

**Neural knowledge representation**: Large language models and neural networks encode knowledge *implicitly* in distributed parameter weights, bypassing symbolic formalisms. How to align this with explicit, inspectable representations remains an open research frontier.

---

## 6. Summary

Knowledge has been defined classically as *justified true belief*, a formulation refined by Gettier into a rich family of post-Gettier theories—reliabilism, virtue epistemology, sensitivity, safety, contextualism, and knowledge-first approaches. On the formal side, epistemic modal logic provides the most direct symbolic counterpart, treating knowledge as a modal operator over possible worlds. AI and knowledge representation research has produced a spectrum of complementary formalisms—semantic networks, frames, production rules, description logics, OWL ontologies, knowledge graphs, and probabilistic models—each trading off expressiveness, decidability, and handling of uncertainty. Bridging philosophical rigor and computational tractability remains the central open challenge.

---

## References

- Plato. *Meno*; *Theaetetus*.
- Gettier, E. L. (1963). Is Justified True Belief Knowledge? *Analysis*, 23(6), 121–123.
- Goldman, A. I. (1967). A Causal Theory of Knowing. *Journal of Philosophy*, 64(12), 357–372.
- Goldman, A. I. (1976). Discrimination and Perceptual Knowledge. *Journal of Philosophy*, 73(20), 771–791.
- Lehrer, K., & Paxson, T. (1969). Knowledge: Undefeated Justified True Belief. *Journal of Philosophy*, 66(8), 225–237.
- Nozick, R. (1981). *Philosophical Explanations*. Harvard University Press.
- Sosa, E. (1999). How to Defeat Opposition to Moore. *Philosophical Perspectives*, 13, 141–153.
- Williamson, T. (2000). *Knowledge and Its Limits*. Oxford University Press.
- Ryle, G. (1949). *The Concept of Mind*. Hutchinson.
- Aumann, R. J. (1976). Agreeing to Disagree. *Annals of Statistics*, 4(6), 1236–1239.
- Minsky, M. (1975). A Framework for Representing Knowledge. In P. H. Winston (Ed.), *The Psychology of Computer Vision*. McGraw-Hill.
- Reiter, R. (1980). A Logic for Default Reasoning. *Artificial Intelligence*, 13(1–2), 81–132.
- Gruber, T. R. (1993). A Translation Approach to Portable Ontology Specifications. *Knowledge Acquisition*, 5(2), 199–220.
- Baader, F., Calvanese, D., McGuinness, D. L., Nardi, D., & Patel-Schneider, P. F. (Eds.). (2003). *The Description Logic Handbook*. Cambridge University Press.
- Hogan, A., et al. (2021). Knowledge Graphs. *ACM Computing Surveys*, 54(4), Article 71.
- Pearl, J. (1988). *Probabilistic Reasoning in Intelligent Systems*. Morgan Kaufmann.
- Richardson, M., & Domingos, P. (2006). Markov Logic Networks. *Machine Learning*, 62(1–2), 107–136.
- Fagin, R., Halpern, J. Y., Moses, Y., & Vardi, M. Y. (1995). *Reasoning About Knowledge*. MIT Press.
- Brachman, R., & Levesque, H. (2004). *Knowledge Representation and Reasoning*. Morgan Kaufmann.
