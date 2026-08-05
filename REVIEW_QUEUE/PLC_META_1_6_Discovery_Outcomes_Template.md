# PLC_META — 1.6 Discovery Outcomes (Template)

## 1. Purpose & Scope

This chapter defines **how any product instance** (IaaC, LexBrain, whatever comes next) must **close PLC_1 – Discovery**.

It has two jobs:

1. Turn all prior Discovery work (1.1–1.5) into a **clear decision** for the product instance:
   - **GO as Product**
   - **GO as Internal-Use Tool**
   - **NO-GO / Park**

2. When the decision is **GO** (in any form), force explicit answers to three **fundamental outcome questions**:
   1. For **what size of business** the idea is suitable.  
   2. Whether it is **good as a consulting asset**.  
   3. Whether it is **good to help the architect/founder find a job** (career leverage).

This chapter is **meta**: it defines the pattern.  
Each product instance (e.g., PLC_IaaC/1.6) must *instantiate* this template with concrete answers.

---

## 2. Decision Options

At the end of PLC_1 for any product instance, only three outcomes are allowed:

1. **Green Light — Product**
   - The instance will be developed as a **market-facing product** (sold, licensed, or otherwise offered to external customers).

2. **Green Light — Internal Use Only**
   - The instance will be developed as an **internal strategic tool**:
     - To support internal operations,
     - To power consulting/engagements,
     - Or to serve as a **future product candidate**, but **not** positioned as a product now.

3. **No-Go / Park**
   - The instance will **not** be developed beyond exploratory prototypes at this time.  
   - Knowledge is retained; we define **re-entry conditions** (what must change to revisit it).

Each product-specific PLC_1.6 file must **pick exactly one** of these options and justify it.

---

## 3. Baseline Discovery Outcomes (Preconditions)

Before a product instance is allowed to make a PLC_1.6 decision, the following PLC_1 artifacts must exist in a minimally solid form:

- **1.1 Product Vision**
  - Clear articulation of:
    - Target segments or personas,
    - Problem and promise,
    - North Star narrative / “why now”.

- **1.2 Market Research**
  - Defined market segments and first-pass prioritization.  
  - Overview of main competitors, alternatives, and pricing patterns.  
  - Evidence that the problem exists beyond imagination.

- **1.3 Stakeholder Map**
  - Buying center and power dynamics mapped for main segments.  
  - Key roles, goals, fears, triggers, and objections.

- **1.4 Discovery Methodologies (PLC-side)**
  - Methods used: interviews, JTBD, competitor teardown, etc.  
  - “Done criteria” for PLC_1 explicitly defined.

If any of these is missing or clearly weak, PLC_1.6 for that instance may only conclude:

> “Discovery not complete — return to strengthen 1.x before deciding GO/NO-GO.”

No pretending.

---

## 4. Fundamental Outcome Questions (Mandatory on Any Green Light)

Whenever a product instance gets a **Green** (Product or Internal), PLC_1.6 must explicitly answer three questions.

### 4.1 Business Size Fit  
**“For what size of business is this idea suitable?”**

We classify the natural fit of the product instance using simple buckets:

- **Very small / solo**  
  Freelancers, solo consultants, micro-startups (1–5 people).

- **Small**  
  Small companies (5–50 people, few systems, limited compliance).

- **Mid-market**  
  50–500 people, meaningful complexity, several systems or cloud accounts, usually some formal audits.

- **Enterprise**  
  500+, multi-team, multi-account, heavy governance.

- **Service providers**  
  MSPs, consulting firms, platform providers, partners (operate across many clients).

Each instance must:

- Name its **primary “sweet spot”**.  
- Name **secondary / future** targets.  
- State explicitly where the product is **overkill or misaligned**.

This avoids the classic “our target is everyone” delusion.

---

### 4.2 Consulting Leverage  
**“Is this product good as a consulting weapon?”**

Here we evaluate how well the product instance supports **consulting and services** even if product monetization is weak or delayed.

Each instance must answer:

- Can this product:
  - Power **higher-value assessments** (diagnostics, posture reviews, migrations, optimizations)?  
  - Structure **repeatable offerings** (fixed-scope packages, maturity journeys)?  
  - Provide reusable **IP** (frameworks, reports, methods) that differentiate the consulting brand?

- If the *product* path is slow or blocked:
  - Does this still have strong **internal value for projects**?

We tag each product instance with a simple level:

- **Consulting leverage:**
  - ☐ Weak  
  - ☐ Moderate  
  - ☐ Strong  
  - ☐ Core pillar of consulting strategy

---

### 4.3 Career Leverage  
**“Is it good to help find a job?”**

Blunt but necessary: working on this product instance must be evaluated as a **career move** for the architect/founder.

Each instance must answer:

- Does building this produce **portfolio-grade assets**?  
  - Public or partially anonymized artifacts:
    - Architectures, diagrams, docs, reference implementations, talks, whitepapers, etc.  
  - Skills aligned to target roles:
    - e.g., AWS architectures, infra tooling, AI integration, security, product leadership.

- Is the time spent on this **better or worse** for job-hunting than:
  - Random certs,  
  - Generic side projects,  
  - Short-term freelancing.

We tag:

- **Career leverage:**
  - ☐ Mostly irrelevant  
  - ☐ Helpful but indirect  
  - ☐ Strong signal for target roles

A product that is **internal-only** but has **strong career leverage** may still be the right call.

---

## 5. Outcome A — Green Light as Product (Template)

When an instance is **GO as Product**, PLC_1.6 must fix the following for that instance:

### 5.1 Target & Positioning

- **Primary beachhead segment** (one, not many).  
- **Primary scenario / JTBD for v1** (what we solve first, concretely).  
- **Short product statement** (2–3 sentences) aligned with 1.1.

### 5.2 Offering & Deployment Shape

- What exactly we intend to sell in v1:
  - Platform,  
  - Tool + services,  
  - Partner-only engine,  
  - Other (but clearly stated).

- Intended **deployment model** for v1:
  - SaaS,  
  - Self-hosted,  
  - Hybrid,  
  - Plugins/tooling.

### 5.3 Pricing Direction (Hypothesis Only)

We’re not setting final pricing in PLC_1, only the **direction**:

- Primary pricing axis:
  - Per user / per seat,  
  - Per account / workspace / environment,  
  - Per transaction / usage,  
  - Per project / license.

- Intended **tiering** (e.g., Basic / Pro / Enterprise / Partner).

If even a rough direction is impossible to state, the “GO as Product” is **not mature**.

### 5.4 Success Metrics for PLC_2/3

Each instance must define what “this seems to be working” looks like in the next phases, e.g.:

- X design partners or early adopters.  
- Y real-world uses (projects, runs, deployments) driven by the product.  
- Z paying customers/pilots or high-intent prospects.

### 5.5 Explicit Answers to Fundamental Questions

In the **product-specific 1.6 file**, the instance must record:

- **Business size fit:**  
  - [free text + ticked size buckets]

- **Consulting leverage:**  
  - [selected level + 2–3 lines of explanation]

- **Career leverage:**  
  - [selected level + 2–3 lines of explanation]

---

## 6. Outcome B — Green Light as Internal Tool Only (Template)

When an instance is **GO as Internal Only**, PLC_1.6 must clarify:

### 6.1 Internal Scope

- Where this tool will be used:
  - Internal infra,  
  - Specific consulting lines,  
  - Lab / R&D usage,  
  - Training / demos.

### 6.2 Architecture & Quality Level

We must be explicit:

- Will the core be built to **product-grade** (clean enough to productize later)?  
- Or as a **power tool** with relaxed constraints?

Recommendation: even for internal-only, core concepts that are widely reusable should be kept clean enough to reuse.

### 6.3 Re-evaluation Conditions

For each instance:

- Under which conditions might we revisit **productization**?
  - Number of internal uses?  
  - Clear external demand?  
  - Strategic shift?

- Who owns the responsibility to **trigger that review** (role, not name)?

### 6.4 Fundamental Questions Still Apply

Even if it’s internal-only, the instance must still document:

- **Business size fit** (where it applies in practice).  
- **Consulting leverage** (how it powers services).  
- **Career leverage** (how it will be presented externally, even if not sold).

---

## 7. Outcome C — No-Go / Park (Template)

If the decision is **NO-GO / Park**:

### 7.1 Knowledge Capture

The instance’s 1.6 file must capture:

- **Why** we parked it:
  - Market too early / too small / too crowded,  
  - Misaligned with strategy or bandwidth,  
  - Technically or legally too risky.

- Which assets remain useful:
  - Concepts, research, partial code, diagrams.

### 7.2 Re-entry Conditions

We must define **explicit triggers** to reconsider:

- Market changes, new regulations, new platforms.  
- A large partner or client asking specifically for this.  
- Internal capability jumps (e.g., new team, new infra).

### 7.3 Fundamental Questions (Retrospective)

Even on a NO-GO we briefly state:

- **Business size fit** (why it wasn’t attractive enough).  
- **Consulting leverage** (why it didn’t justify itself as a tool).  
- **Career leverage** (why effort is better spent elsewhere).

---

## 8. Decision Summary Template (Per Product Instance)

Each product-specific `PLC_<Product>/1.6_Discovery_Outcomes.md` should end with a one-page summary like:

- **Decision:**  
  - ☐ Product  
  - ☐ Internal Only  
  - ☐ No-Go / Park  

- **Business size fit (sweet spot):**  
  - [free text + checked buckets]

- **Consulting leverage:**  
  - [Weak / Moderate / Strong / Core pillar] + short explanation.

- **Career leverage:**  
  - [Irrelevant / Helpful / Strong] + short explanation.

- **Primary segment(s) and scenario for v1 (if Product):**  
  - [segment + core use case]

- **Top 3 reasons for this decision:**  
  - [reason 1]  
  - [reason 2]  
  - [reason 3]

- **Top 3 risks / assumptions to validate in PLC_2/3 (if Product or Internal):**  
  - [risk 1]  
  - [risk 2]  
  - [risk 3]

This is the **receipt** for the entire PLC_1 effort per product instance.
