# 1.2 Market Research — SymK

## 1. Purpose of this document

This document defines **what market SymK is actually playing in**, who else is there, and why anyone should care.

Goal: give Architecture (2.x) and Planning (3.x) a **clear, evidence-based context** so we don’t design a cathedral for a village.

---

## 2. Market definition

### 2.1 Category

SymK sits at the intersection of:

- **AI-assisted software development**
- **Developer productivity / DevEx**
- **Platform engineering & internal developer platforms**
- **Software governance (quality, compliance, auditability)**

Positioning statement:

> SymK is an **AI-governed product lifecycle backbone** for teams that want
> aggressive AI usage in development **without losing control, traceability, or architecture discipline**.

### 2.2 Key problem we solve (market-facing)

Most teams using AI for development today have:

- Lots of **ad-hoc AI usage** (chat windows, copy-paste, fragments of prompts),
- Little to no **governance** (no enforced rules, no traceability),
- **Inconsistent structures** between repos and projects,
- No **single “way we do AI dev here”** that scales organization-wide.

SymK addresses this by:

- Standardizing **folder structures, lifecycles, and artifacts** across projects,
- Encoding **rules and constraints in tools** (decorators, checkers, scaffolds),
- Acting as a **meta-layer** over multiple products and repos.

---

## 3. Target segments

### 3.1 Primary segment — “Deep-tech builder orgs”

Characteristics:

- Have **multiple internal products** (APIs, services, platforms),
- Already using AI tools heavily (GPT, Copilot, etc.),
- Feel the pain of:
  - architecture drift,
  - inconsistent documentation,
  - unpredictable AI output,
  - and onboarding overhead.

Sub-segments:

1. **Platform / DevOps heavy orgs**
   - Already think in terms of **platform engineering**.
   - SymK integrates nicely as the **“AI-aware product backbone”**.

2. **Consultancies / boutiques**
   - Build solutions for multiple clients.
   - Need **repeatable patterns** and a way to re-use structure and tooling.

3. **Regulated / compliance-sensitive teams**
   - Need **traceability** for changes and AI decisions.
   - SymK provides conventions + enforcement for that.

### 3.2 Secondary segment — “Advanced indie / small teams”

- High-skill teams with limited headcount.
- Want to **scale with AI instead of headcount**, but not at the cost of chaos.
- SymK gives them:
  - structure,
  - automation,
  - and a way to keep the codebase sane while moving fast.

---

## 4. Internal vs external adoption path

### 4.1 Internal “dogfooding” market

First stage: SymK is used internally by **our own projects**, e.g.:

- IaaC Tools,
- Hyperdocs / LexBrain,
- Any new backend or infra-oriented project.

This gives us:

- Real-world proof SymK **reduces friction and increases consistency**,
- A **portfolio of live examples**,
- Better insight into:
  - what is a must-have,
  - what is over-engineering.

### 4.2 External productization

Only after SymK is stable internally do we **formalize**:

- Install / upgrade story,
- Versioning,
- Backward compatibility,
- Documentation for external teams.

Until then, all “market” for SymK is **internal + close partners**.

---

## 5. Competitive landscape (conceptual)

SymK will overlap with:

1. **AI coding assistants**
   - e.g., tools that generate code but **don’t define the product lifecycle**.
   - They help write code; they don’t define how your projects are structured or governed.

2. **Internal developer platforms / portals**
   - Solve “how devs consume infra and services”.
   - SymK is **lower level**: it defines the **project structure, lifecycle, and AI usage rules**.

3. **CI/CD and quality gates**
   - Enforce testing, linting, etc.
   - SymK **feeds these pipelines** with the right structure, configs, and checks.

4. **Project templates / boilerplates**
   - Often one-shot scaffolds.
   - SymK is **living scaffolding + ongoing rules**, not just a starter repo.

SymK’s differentiation:

- Strong focus on **AI governance + lifecycle structure**, not just “developer experience” in the generic sense.
- Encodes **opinionated rules** instead of being yet another neutral toolkit.

---

## 6. User needs & pains (hypotheses)

### 6.1 Core pains

- “We’re using AI heavily, but our architecture is drifting.”
- “Every new repo looks different.”
- “We can’t easily audit what AI did or why.”
- “New devs struggle to understand **how we work here**.”
- “We know we need rules, but nobody has the time to enforce them.”

### 6.2 Desired outcomes

- **Consistency**: new project feels familiar from day one.
- **Trust in AI output**: bounded by rules, patterns, and checks.
- **Lower onboarding time**: conventions + docs + structure.
- **Better alignment** across architects, devs, DevOps, and product.

SymK will be validated by measuring:

- Time to scaffold a new project.
- Time for a new dev to become productive.
- Rate of architectural / structural “surprises” in reviews.

---

## 7. Market trends that favor SymK

- Explosion of **AI coding assistants** → code velocity up, coherence down.
- **Platform engineering** becoming mainstream → organizations ready to adopt opinionated workflows.
- Growing pressure for **auditability and compliance** in software changes.
- Shift from “AI as a toy” → “AI as part of core workflows”.

SymK rides these waves by offering the **“AI-aware lifecycle discipline”** that many teams are missing.

---

## 8. Risks and constraints

### 8.1 Key risks

- Teams might:
  - perceive SymK as **too opinionated**,
  - or feel it adds “process overhead” without obvious short-term payoff.
- Competes with the inertia of:
  - “We already have our own templates/scripts,”
  - “We’ll just standardize manually (and never do).”

### 8.2 Mitigation ideas

- Start with **internal successes and case studies**.
- Keep the **first version minimal**:
  - PLC structure,
  - basic scaffolding,
  - a small set of high-value enforcers.
- Provide **opt-in tiers of strictness**:
  - baseline rules (always on),
  - advanced rules (can be progressively adopted).

---

## 9. Research backlog

Tasks to be completed in this phase (can be tracked as issues):

1. **User interviews / notes**
   - Architects, senior devs, DevOps:
     - “How are you using AI in dev today?”
     - “What scares you about it?”
     - “What would a ‘governed AI dev workflow’ need to do for you to trust it?”

2. **Tool ecosystem mapping**
   - Catalog what is already used:
     - IDEs, CI/CD, infra tools, AI tools.
   - Identify **integration points** and **low-friction entry points** for SymK.

3. **Internal benchmarking**
   - Compare:
     - one project with SymK structure,
     - one project without,
   - Measure:
     - onboarding friction,
     - code review friction,
     - time to scaffold.

4. **Prioritization of first external persona**
   - Decide: who is the **first “ideal external user”**?
     - Platform team?
     - Small consulting shop?
   - Use this to guide the first externally-facing docs and features.

---

## 10. How this feeds later phases

- **2_Architecture**
  - Defines how SymK manifests technically:
    - packages, CLIs, schemas, integration points.

- **3_Planning**
  - Turns market & user needs into:
    - roadmap,
    - MVP definition,
    - release waves.

- **4_Design**
  - UI/UX (if/when needed),
  - developer experience flows,
  - CLI ergonomics.

If future work contradicts the assumptions above, this document must be updated — or we acknowledge we’re building for a different market than SymK was originally aimed at.

