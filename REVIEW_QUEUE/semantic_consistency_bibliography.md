# Semantic Consistency in Software Systems  
## Curated bibliography for vocabularies, conceptual-model quality, ontology quality, and semantic drift

## Why this reading pack exists

This bibliography is organized around one engineering claim:

> A system can be syntactically correct and still be semantically inconsistent.

That inconsistency usually begins upstream, in weak vocabularies, under-specified conceptual models, overloaded fields, ambiguous terminology, and unmanaged evolution.

The works below are selected to help answer four questions:

1. Why does a shared formal vocabulary matter?
2. How do we judge whether a conceptual model is semantically good enough?
3. How do we detect category mistakes and semantic drift?
4. How does this connect to real software and SaaS engineering practice?

---

## Recommended reading order

### 1) Start here: why a shared vocabulary matters
1. **Thomas R. Gruber (1993)** — *A Translation Approach to Portable Ontology Specifications*  
2. **Martin Fowler (2006)** — *Ubiquitous Language*

### 2) Then: how to think about semantic quality
3. **Odd Ivar Lindland, Guttorm Sindre, Arne Sølvberg (1994)** — *Understanding Quality in Conceptual Modeling*  
4. **H. James Nelson, Geert Poels, Marcela Genero, Mario Piattini (2005)** — *Quality in Conceptual Modeling: Five Examples of the State of the Art*

### 3) Then: how to judge whether the ontology/vocab is well formed
5. **Asunción Gómez-Pérez (2001/2004)** — *Evaluation of Ontologies* / *Ontology Evaluation*
6. **Nicola Guarino, Christopher Welty (2002)** — *Evaluating Ontological Decisions with OntoClean*

### 4) Then: how meaning drifts and how repairs happen
7. **S. Senatore et al. (2020)** — *OntoDrift: a Semantic Drift Gauge for Ontology Evolution Monitoring*  
8. **Nicolas Troquard et al. (2018)** — *Repairing Ontologies via Axiom Weakening*

---

## Annotated bibliography

### 1) Thomas R. Gruber (1993)
**Title:** *A Translation Approach to Portable Ontology Specifications*  
**Why it matters:** Foundational text for the idea that systems need a **shared, explicit, formal vocabulary** for a domain of discourse.  
**What to look for:** The paper frames an ontology as a specification of a representational vocabulary for a shared domain.  
**Why it matters for software:** This is the deepest academic ancestor of the engineering principle that “the vocab must be the source of truth.”  
**Relevance to your problem:** If the governing vocabulary is incomplete or ambiguous, the system stops sharing meaning consistently across tools, contracts, code, and UI.

---

### 2) Martin Fowler (2006)
**Title:** *Ubiquitous Language*  
**Why it matters:** A practical software architecture complement to ontology work.  
**What to look for:** The core idea is that developers and domain experts need a **common, rigorous language** embedded in the model and reflected in the software.  
**Why it matters for software:** Ambiguity is not just a communication problem; it becomes executable inconsistency.  
**Relevance to your problem:** This is the software-engineering version of the same disease: if teams do not share exact meanings, the codebase becomes a federation of interpretations.

---

### 3) Odd Ivar Lindland, Guttorm Sindre, Arne Sølvberg (1994)
**Title:** *Understanding Quality in Conceptual Modeling*  
**Why it matters:** Classic work on conceptual model quality.  
**What to look for:** The distinction between **syntactic**, **semantic**, and **pragmatic** quality.  
**Why it matters for software:** A model can be syntactically valid yet semantically wrong with respect to the real-world domain.  
**Relevance to your problem:** This maps directly to situations where contracts pass validation but still carry wrong or mixed meanings.

---

### 4) H. James Nelson, Geert Poels, Marcela Genero, Mario Piattini (2005)
**Title:** *Quality in Conceptual Modeling: Five Examples of the State of the Art*  
**Why it matters:** Helps connect conceptual-model quality to the downstream success or failure of the system built on top of it.  
**What to look for:** The argument that accurate, complete, reusable, maintainable, and evolvable conceptual models are critical because all downstream activities inherit their quality.  
**Why it matters for software:** If the model is semantically off, the whole system becomes increasingly off as implementation grows.  
**Relevance to your problem:** This supports the idea that weak semantics are a root cause of long-term SaaS fragility, not just a documentation annoyance.

---

### 5) Asunción Gómez-Pérez (2001/2004)
**Titles:** *Evaluation of Ontologies* / *Ontology Evaluation*  
**Why it matters:** Directly addresses how to judge whether an ontology is good enough.  
**What to look for:** Criteria such as consistency, completeness, conciseness, and other dimensions of ontology quality.  
**Why it matters for software:** This is the closest literature to a **vocab sufficiency audit** mindset.  
**Relevance to your problem:** Very useful when you need to test whether a governing vocabulary is merely official or actually sufficient to define system meaning without tribal knowledge.

---

### 6) Nicola Guarino, Christopher Welty (2002)
**Title:** *Evaluating Ontological Decisions with OntoClean*  
**Why it matters:** One of the best-known approaches for catching ontological category mistakes.  
**What to look for:** Identity, rigidity, unity, and misuse of subsumption/classification.  
**Why it matters for software:** Helps expose when people are mixing fundamentally different kinds of things under one field or hierarchy.  
**Relevance to your problem:** This is the kind of lens that catches a field intended to be semantic but polluted with UI/profile or operational residue.

---

### 7) S. Senatore et al. (2020)
**Title:** *OntoDrift: a Semantic Drift Gauge for Ontology Evolution Monitoring*  
**Why it matters:** Once a vocabulary exists, the next problem is drift.  
**What to look for:** How ontology versions can change meaning over time at concept and structure levels.  
**Why it matters for software:** Even a good initial vocabulary can decay unless change is monitored.  
**Relevance to your problem:** Useful for thinking about how to detect when contracts, code, and vocab slowly stop meaning the same thing.

---

### 8) Nicolas Troquard, Roberto Confalonieri, Pietro Galliani, Rafael Peñaloza, Daniele Porello, Oliver Kutz (2018)
**Title:** *Repairing Ontologies via Axiom Weakening*  
**Why it matters:** Focuses on inconsistency repair once the ontology has grown enough to become fragile.  
**What to look for:** Repair strategies that preserve more knowledge than simply deleting problematic axioms.  
**Why it matters for software:** Useful when your vocabulary is already in use and you need controlled correction rather than destructive cleanup.  
**Relevance to your problem:** Important for migration thinking: how to repair semantic structure without breaking everything that depends on it.

---

## Practical translation to software and SaaS systems

These works suggest a practical chain:

- **Weak vocabulary** leads to
- **weak conceptual model**, which leads to
- **ambiguous contracts and APIs**, which leads to
- **inconsistent implementation and UI**, which leads to
- **operator confusion, migration pain, and semantic drift**.

In SaaS systems, this often shows up as:

- the same term meaning different things in different modules,
- different terms being used for the same concept,
- UI labels leaking into business semantics,
- tests validating one interpretation while runtime uses another,
- migrations preserving tokens but not preserving meaning.

---

## A lens for reviewing your own system

When reviewing a governing vocabulary, ask:

1. **Is every semantic field explicitly defined, or are some only implied by enum values?**
2. **Can a future engineer recover the intended meaning from the vocab alone?**
3. **Are semantic axes cleanly separated from UI/presentation concepts?**
4. **Are deprecated aliases clearly marked and mapped?**
5. **Is there a process to detect semantic drift as the model evolves?**

If the answer to any of these is “not really,” then the vocabulary may be official, but not yet sufficient.

---

## Source list

1. Gruber, T. R. (1993). *A Translation Approach to Portable Ontology Specifications.* Knowledge Acquisition.
2. Fowler, M. (2006). *Ubiquitous Language.*
3. Lindland, O. I., Sindre, G., & Sølvberg, A. (1994). *Understanding Quality in Conceptual Modeling.* IEEE Software.
4. Nelson, H. J., Poels, G., Genero, M., & Piattini, M. (2005). *Quality in Conceptual Modeling: Five Examples of the State of the Art.* Data & Knowledge Engineering.
5. Gómez-Pérez, A. (2001/2004). *Evaluation of Ontologies* / *Ontology Evaluation.*
6. Guarino, N., & Welty, C. (2002). *Evaluating Ontological Decisions with OntoClean.* Communications of the ACM.
7. Senatore, S., et al. (2020). *OntoDrift: a Semantic Drift Gauge for Ontology Evolution Monitoring.*
8. Troquard, N., Confalonieri, R., Galliani, P., Peñaloza, R., Porello, D., & Kutz, O. (2018). *Repairing Ontologies via Axiom Weakening.*

