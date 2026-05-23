# SymK User’s Manual  
_Version: draft_

---

## 0. About This Manual

### 0.1 What SymK Is

SymK is a **meta-project**.

It doesn’t ship a single product. It defines:

- A **Project Life Cycle (PLC)** framework.
- A **Symbiotic Cooperation Protocol** between a human architect and AI.
- A set of **templates, tools, and guidelines** that other projects (IaaC, LexBrain, etc.) plug into.

Think of SymK as the **operating system** for how you and AI think together about products, from idea to architecture to build.

### 0.2 Who This Manual Is For

This manual is aimed at:

- Architects and senior engineers.
- Product owners who actually sign off risk.
- People who like building things more than telling pretty stories about them.

It is **not** aimed at:

- Committee-style “process owners”.
- People who believe more templates automatically mean more intelligence.

If you want checklists without thinking, this is the wrong manual.

### 0.3 What This Manual Covers (and What It Doesn’t)

This manual explains:

- The **philosophy** behind SymK (why it exists).
- The **structure** of the PLC framework (phases and their roles).
- How to **run PLC_1 — Discovery** in practice.
- How to use AI as a **thinking partner**, not a slide factory.

It does **not**:

- Teach basic product management.
- Replace technical design docs or implementation manuals.
- Guarantee that every idea becomes a good business. (Most shouldn’t.)

### 0.4 How to Read This Manual

Recommended usage:

1. **Read Chapter 1 once** to understand the mindset.
2. **Skim the PLC overview** when you start a new project.
3. **Use the Discovery chapters (PLC_1)** when you’re evaluating a specific idea.
4. Treat everything as **tools** and **lenses**, not dogma.

If you catch yourself “filling templates for compliance,” you’ve gone off script.

---

## 1. SymK in a Nutshell

### 1.1 What SymK Is (and Is Not)

SymK exists to answer a specific question:

> How can a human architect and AI think together  
> in a way that surfaces more truth, earlier, with fewer blind spots —  
> without drowning in bureaucracy?

From that, a few consequences:

- SymK is:
  - A **framework** for structuring product work (PLC).
  - A **philosophy** for human–AI cooperation.
  - A **tooling ecosystem** (templates, prompts, catalogs) that can be reused across different products.

- SymK is **not**:
  - A “use AI to code faster” cookbook.
  - A cargo cult of canvases, matrices, and buzzwords.
  - A promise that “if you follow the steps, the product will succeed.”

SymK’s job is to:

- Make it **harder to lie to yourself** about an idea.
- Make it **cheaper to kill bad paths early**.
- Make it **easier to go deep** on the ideas that actually survive.

Everything else is negotiable.

### 1.2 Symbiotic Cooperation: Human and AI Roles

This manual does not restate role definitions.

**Canonical reference:** [`AXIOM — Symbiotic Cooperation Roles`](../../docs/00_AXIOMS/AXIOM_Symbiotic_Cooperation_Roles.md)

What this manual assumes, at a glance:
- The **human** owns purpose, constraints, decisions, and consequences.
- The **AI** provides breadth, iteration, and critique — and is expected to challenge assumptions.

### 1.3 Core Mantras

SymK is built around a few blunt principles.

#### 1.3.1 Issues Are Fine. Unknown Gaps Are Not.

Problems, trade-offs, and risks are normal.  
What kills products is **what nobody saw coming**.

So SymK cares about:

- Explicitly listing **unknowns** and **assumptions**.
- Probing them with AI and methods in PLC_1.
- Using that to decide whether an idea deserves further investment.

“Everything looks clean” is suspicious. Reality isn’t clean.

#### 1.3.2 No-Go Is a Valid and Often Excellent Outcome

Most ideas in the world:

- Don’t have a real segment.
- Don’t have a realistic GTM path.
- Don’t justify the engineering needed to make them robust.

SymK treats **No-Go** as success when:

- The decision is explicit.
- The reasons are documented.
- The time and attention saved are real.

Other valid outcomes include:

- **Internal-only** — good for your own stack, not for sale.
- **Consulting-first** — better as a service offering than as a product (for now).
- **Career-only** — ideal as a portfolio / authority piece, not a standalone business.

Not everything worth building is worth productizing.

#### 1.3.3 Documentation Is a Side Effect, Not the Goal

SymK is allergic to:

- Decks created to impress instead of to decide.
- 40-page “studies” that could be replaced by 4 honest pages.
- Templates treated as a religion.

In SymK:

- **Size is a cost.**  
  Every page must earn its existence by changing or clarifying a decision.
- **Templates are scaffolding, not cages.**  
  If a section doesn’t influence the Go / No-Go logic, keep it minimal or skip it.

Any time you feel proud of how thick the document is, stop and ask:  
“Did this thickness improve the decision, or just my ego?”

#### 1.3.4 AI Is an Attack Dog and Compressor, Not Just a Writer

Using AI to generate more words is trivial and mostly useless.

SymK prefers to use AI for three things:

1. **Drafting**  
   - Turn raw notes into structured drafts when you don’t want to wrestle with blank pages.

2. **Attacking**  
   - Ask AI to find contradictions, hand-waving, and missing cases between:
     - Vision (1.1),
     - Market (1.2),
     - Stakeholders (1.3),
     - Methods used (1.4).

3. **Compressing**  
   - Summarize everything into short, sharp decision packs before you decide in 1.6.

The order matters: draft → attack → compress.  
Skipping “attack” and going straight from “draft” to “pretty PDF” is exactly what SymK is designed to avoid.

### 1.4 Where the PLC Fits

The SymK PLC (Project Life Cycle) is how this philosophy becomes **repeatable practice**.

At a high level:

- PLC_1 — **Discovery**  
  - Take an idea and test whether it deserves architecture and engineering.
- PLC_2 — **Architecture & Design**  
  - Shape the system and its constraints (technical + human).
- PLC_3 — **Build & Integration**  
  - Implement, integrate, and automate.
- PLC_4 — **Validation & Observability**  
  - Check if reality agrees with the theory.
- PLC_5+ — (Reserved for evolution, scaling, and portfolio-level decisions.)

This manual focuses first on PLC_1 because:

- That’s where the **biggest waste** tends to happen (over-investing in the wrong ideas).
- That’s where SymK’s human–AI symbiosis gives the most leverage.

Later chapters will map this philosophy into concrete steps, starting with:

- **How to actually run PLC_1 — Discovery**  
  using the 3-pass pipeline and the 1.1–1.6 structure.

---

## 2. The SymK PLC Framework

### 2.1 What a PLC Is in SymK

In SymK, a **PLC (Project Life Cycle)** is a structured map of how an idea moves from:

- vague concept →
- evaluated opportunity →
- designed system →
- built and integrated solution →
- validated and observed reality.

Each PLC phase is broken into **nodes** (like 1.1, 1.2, 1.3…) and each node answers three core questions:

1. **Purpose** – What decision does this node help us make?
2. **Inputs** – What does it need to work (docs, data, interviews, prior phases)?
3. **Outcomes** – What does it produce (docs, models, decisions, signals)?

On top of that, each node also defines:

- Recommended **methods** (how to do the thinking).
- Recommended **tools** (templates, scripts, AI prompts).
- Recommended **AI roles** (draft, attack, compress, compare, etc.).

The PLC is not a waterfall: it’s a **navigation map**.  
You move around it in **passes** and **loops**, not in a straight line.

### 2.2 META PLC vs Product PLCs

SymK distinguishes between:

- **PLC_META** — the **reference life cycle** that lives in the SymK project.
  - Defines **what phases exist** (1_Discovery, 2_Architecture, …).
  - Defines **what each node means** (1.1, 1.2, 1.3…).
  - Provides **templates** and **guidelines** for how to execute them.
- **Product PLCs** — specific instantiations for concrete products, like:
  - `PLC_IaaC` for IaaC Recovery Suite.
  - `PLC_LexBrain` for LexBrain.
  - Future projects (Hyperdocs, InteractSVG, etc.).

The relationship is simple:

- PLC_META defines the **shape and semantics** of the life cycle.
- Each Product PLC:
  - **reuses** the phase structure,
  - **fills in** the product-specific content,
  - optionally **extends** nodes with extra details if needed.

Practically:

- PLC_META lives in the SymK repo and is treated as **ground truth**.
- Product PLCs reference the META structure but are free to choose:
  - which phases to run,
  - how deep to go in each,
  - and what to skip.

### 2.3 High-Level PLC Phases

The PLC in SymK is intentionally compact. It’s designed to cover the whole product story without turning into a bureaucracy.

The current high-level phase map is:

1. **PLC_1 — Discovery**  
   Mission: **decide if the idea deserves architecture and engineering**.

   - Clarify vision (1.1).
   - Understand market & alternatives enough to see if there’s a **real segment** and **real gap** (1.2).
   - Map stakeholders and politics (1.3).
   - Decide which methods and tools to actually use (1.4, 1.5).
   - Reach a clear **Go / No-Go / Internal / Consulting / Career** decision (1.6).

2. **PLC_2 — Architecture & Design** (META outline)  
   Mission: **shape the system** so that it can be built and operated safely.

   Typical nodes (names may evolve):

   - 2.1 System context and boundaries  
   - 2.2 Domain model and core flows  
   - 2.3 Non-functional constraints (scalability, security, compliance)  
   - 2.4 Architecture options and trade-offs  
   - 2.5 Chosen architecture & rationale (decision record)  

   In SymK style, PLC_2 should also:
   - Expose **risks and unknowns** early.
   - Use AI to explore **alternative architectures** and attack the chosen one before committing.

3. **PLC_3 — Build & Integration** (META outline)  
   Mission: **implement and integrate** the system according to PLC_2.

   Typical concerns:

   - Repositories, branching strategies, environments.
   - Automation (CI/CD, testing, static analysis).
   - Interfaces between components and between teams.
   - AI-assisted coding standards and refactoring patterns.

4. **PLC_4 — Validation & Observability** (META outline)  
   Mission: **check if reality matches the story**.

   Typical nodes:

   - Validation strategy (tests, drills, simulations).
   - Metrics and telemetry design.
   - Operational runbooks (normal operations and failure modes).
   - Feedback loops into PLC_2 and PLC_3 (design and implementation corrections).

5. **PLC_5+ — Evolution / Portfolio (reserved)**  
   Mission: **manage the long-term evolution and portfolio**.

   This includes:

   - When to extend vs retire products.
   - How to use learnings from one PLC to influence others.
   - How to allocate limited attention across multiple bets.

For now, this manual will go deep into **PLC_1**, and outline PLC_2+ at **META level**, so they’re ready when you expand SymK further.

### 2.4 Folders, Numbering, and On-Disk Conventions

SymK uses a strict but simple filesystem convention so that humans and tools can work together.

At META level (SymK repo), PLC_1 looks like:

- `PLC/`
  - `1_Discovery/`
    - `1.1_Product_Vision_Template/`
      - `1.1_Product_Vision.md` (phase spec)
      - `1.1_Product_Vision_Template.md` (content template)
    - `1.2_Market_Research_Template/`
      - `1.2_Market_Research.md`
      - `1.2_Market_Research_Template.md`
    - `1.3_Stakeholder_Map_Template/`
      - `1.3_Stakeholder_Map.md`
      - `1.3_Stakeholder_Map_Template.md`
    - `1.4_Discovery_Methodologies_Template/`
      - `1.4_Discovery_Methodologies.md`
      - `1.4_Discovery_Methodologies_Template.md`
    - `1.5_Discovery_Tools_Template/`
      - `1.5_Discovery_Tools.md`
      - `1.5_Discovery_Tools_Catalog.md`
    - `1.6_Discovery_Outcomes/`
      - `1.6_Discovery_Outcomes.md`
      - `1.6.1_Decision_Framework_Template/…`
      - `1.6.2_Business_Size_Fit_Template/…`
      - `1.6.3_Consulting_Leverage_Template/…`
      - `1.6.4_Career_Leverage_Template/…`
      - `1.6.5_Success_Metrics_and_Risks_Template/…`

Principles behind this structure:

- **Numbers first**:  
  - `1.2_…` sorts correctly and signals its place in the PLC.
- **Spec vs Template**:
  - `1.2_Market_Research.md` describes what the node is and how it behaves.
  - `1.2_Market_Research_Template.md` is what you copy/fill for a specific project.
- **Granularity**:
  - Large, conceptually complex nodes (like 1.6) are split into subtemplates (1.6.1–1.6.5) to keep each decision sharp.

Product PLCs (like `PLC_IaaC`) can mirror this structure, but typically only store **filled templates and decisions**, not the META specs.

### 2.5 How PLCs Enable Comparability and Reuse

Because PLC_META defines a common structure:

- Different products can be **compared** at similar points:
  - 1.1 visions side by side,
  - 1.2 market researches across projects,
  - 1.6 decision rationales for a portfolio view.
- Tools (scripts, AI agents) can operate over multiple PLCs because they know:
  - where to find inputs and outputs,
  - what each node is supposed to contain.

This enables things like:

- A “portfolio view” tool that reads all `1.6_Discovery_Outcomes` across products and shows:
  - which ideas were killed and why,
  - which ones are internal tools,
  - which ones are live product bets.
- AI agents that can:
  - learn from previous PLC runs,
  - suggest reusable patterns,
  - flag when a new idea resembles a previously killed one (and why).

In other words, the PLC is not just a process. It’s a **data model** for how you think about product work across time and across ideas.

---
