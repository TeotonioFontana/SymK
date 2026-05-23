# How to Actually Run PLC_1 — Discovery  
_SymK META Guide_

## 0. Scope & Audience

This guide explains **how to *run*** PLC_1 (Discovery) in practice.

- It is **META**: applies to any product PLC (IaaC, LexBrain, etc.).
- It assumes the SymK artifacts under:  
  `PLC/1_Discovery/1.1 … 1.6` already exist (templates + specs).
- It is **not** a detailed user manual, but the **operating doctrine**:
  - what order to follow,
  - how deep to go,
  - when to stop,
  - how to use AI without drowning in noise.

If you just “fill every template to 100%,” you’re doing it wrong.  
This document explains how to avoid that.

---

## 1. Core Mindset

Three principles rule PLC_1:

1. **Discovery is a gate, not a launch pad.**  
   Its job is to decide if the idea deserves:
   - Go (into architecture & engineering),
   - No-Go,
   - Internal-only,
   - Consulting-first,
   - Career-only.

2. **No-Go is a success.**  
   Killing weak or misaligned ideas early saves time, money, and morale.

3. **Documentation is a side effect, not the goal.**  
   Every page must earn its keep:
   - If it doesn’t change the 1.6 decision, keep it short or skip it.

---

## 2. The 3-Pass Pipeline

You don’t run 1.1 → 1.6 once in a straight line.  
You run **three passes**, increasing depth only where needed.

### Pass 1 — Coarse Scan

Goal: **“Is there an obvious killer?”**

- Rough-fill 1.1, 1.2, 1.3, and a very light 1.4.
- Ignore elegance. Focus on:
  - Who it’s for,
  - What pain it hits,
  - Why now,
  - Whether anyone sane would care.

Typical outcomes:

- “Clearly dead” → **Stop here. No-Go / Internal idea.**
- “Promising but fuzzy” → Move to Pass 2.

---

### Pass 2 — Targeted Deepening

Goal: **Clarify only what could change the decision.**

- Use 1.4 (Methodologies) and 1.5 (Tools) intentionally.
- Deepen:
  - Market research (1.2) where GTM / segments are unclear.
  - Stakeholder map (1.3) where politics and veto power are unclear.
  - Vision (1.1) where mission vs market doesn’t align.

You are **not** trying to create a McKinsey report.  
You’re trying to answer:

> “Given the risk and potential payoff, do we know enough to judge this idea?”

---

### Pass 3 — Compression & Decision Pack

Goal: **Produce a small, sharp bundle that 1.6 can decide on.**

- Compress all the noise into a **decision pack**:
  - 1–2 pages of:
    - Why this might work,
    - Why this might fail,
    - What you’d need to believe to proceed.
- Then run 1.6.1–1.6.5:
  - Decision Framework,
  - Business Size Fit,
  - Consulting Leverage,
  - Career Leverage,
  - Success Metrics & Risks.

Outcome: **one of the canonical decisions**:

- Go → allowed into architecture lab (PLC_2+).
- No-Go → parked, with a clear rationale.
- Internal-only → useful for your own stack, not a product.
- Consulting-first → good as a service offering, product maybe later.
- Career-only → ideal as a portfolio / positioning piece, not a commercial bet.

---

## 3. Recommended Order in PLC_1

You don’t need to treat numbering as execution order, but a practical flow is:

### Step 1: 1.1 Product Vision (rough)

- Write the **first dirty version** of:
  - one-line positioning,
  - problem / context,
  - target segments (high level),
  - core promise,
  - short “why now” story.
- No more than 1–2 pages, even in draft.

**Use AI** to turn your raw brain dump into a coherent narrative,  
then let it attack inconsistencies (“this segment vs this problem doesn’t match”).

---

### Step 2: 1.2 Market Research (coarse, then deeper)

- For Pass 1:
  - Identify **macro segments**,
  - List **obvious alternatives** (AWS-native, vendors, manual workarounds),
  - Draft the **GTM Angle**:
    - vanguardists / early adopters / mainstream,
    - first 10–20 real users,
    - high-level “how we’d reach them”.

- In Pass 2:
  - Deepen only where it affects:
    - feasibility of early adopters,
    - realistic GTM for your context,
    - whether there is any segment you can credibly win.

**If 1.2 shows no segment + no realistic GTM → No-Go or Internal/Consulting-only.**

---

### Step 3: 1.3 Stakeholder Map

- Map **roles**, not people:
  - Strategic buyer(s),
  - Technical influencers,
  - Risk / compliance / finance,
  - End users, blockers.
- For each:
  - What they want,
  - What they fear,
  - How this product can make them look good (or bad).

Use AI as a **conflict detector**:

- “Buyer wants cost-cutting; users want more power and flexibility; risk wants auditability.”  
  Great. That’s the *real* battlefield.

If the stakeholder map is fantasy (“CTO just decides and that’s it”),  
1.6 should be suspicious.

---

### Step 4: 1.4 Methodologies

Here you decide:

- Which **methods** you actually used (interviews, desk research, experiments),
- Which you **deliberately skipped** (and why).

Key point:

> 1.4 is **not** “use all methods”.  
> It’s “be honest about which ones you used and which gaps remain.”

This becomes important input for 1.6.5 (risks & success metrics).

---

### Step 5: 1.5 Tools

- At META level:
  - 1.5 defines which **templates / matrices / prompt packs** exist.
- At project level:
  - You choose **only the tools that matter** for this idea.
  - Using *all* tools is a smell.

Think of 1.5 as your **tool menu**, not a checklist.  
If a tool doesn’t change the decision path, don’t use it.

---

### Step 6: 1.6 Discovery Outcomes

Only after Pass 2 and compression:

- Use 1.6.1–1.6.5 to evaluate:
  - Does this idea deserve architecture and engineering effort?
  - If yes, for **which class of business**?
  - Is the main payoff:
    - product revenue,
    - consulting revenue,
    - career positioning,
    - internal capability?

No drama. “No-Go with clear rationale” is a **strong** outcome.

---

## 4. How to Use AI in PLC_1 (Symbiotic Pattern)

Treat AI as three things, in this order:

1. **Drafting engine**  
   - Turn messy notes into structured drafts:
     - `product_vision.md`, `market_research.md`, `stakeholder_map.md`.
   - But never accept the first draft as “truth”.

2. **Attack dog**  
   - Ask it explicitly to:
     - find contradictions between 1.1, 1.2, 1.3;
     - list missing questions;
     - challenge GTM feasibility for *your* context;
     - point out hand-waving.
   - If AI never pushes back, you’re asking it the wrong questions.

3. **Compressor**  
   - Before 1.6, ask it to:
     - condense long docs into short, decision-grade summaries,
     - present “best case vs worst case vs most likely” in plain language.

Don’t use AI to:
- fluff up documents,
- create slideware,
- justify an idea you already emotionally chose.

Use it to **make it harder to lie to yourself**.

---

## 5. When to Stop (and Not Overcook Discovery)

You stop Discovery when:

1. There is a **clear No-Go reason**  
   - No reachable early adopters,
   - No credible differentiation,
   - GTM depends on capabilities you don’t have and don’t want to build.

2. Or there is a **clear bounded Go reason**  
   - A narrow but solid early segment,
   - GTM motion that matches your skills/network,
   - Known risks and unknowns that can be handled in PLC_2.

Any of these is a valid stopping point:

- “This is an internal tool only.”
- “This is a consulting accelerator, not a product (yet).”
- “This is mainly a career play (talks, portfolio, authority).”
- “This is a product worth architecting now.”

If you feel the urge to add more pages “because it looks thin,”  
check whether you’re compensating for uncertainty with volume. That’s exactly what SymK is designed to avoid.

---

## 6. Common Failure Modes This Guide Is Meant to Prevent

1. **Waterfall Discovery**  
   - Filling every template in order, to 100%, before making any call.  
   → Fix: use the **3-pass pipeline** and stop early when you have enough signal.

2. **PowerPoint Discovery**  
   - Beautiful narratives that never face GTM feasibility or stakeholder politics.  
   → Fix: force 1.2 GTM Angle + 1.3 Stakeholder Map + 1.6 decision.

3. **AGI as PowerPoint generator**  
   - Letting AI produce long, confident documents that nobody can act on.  
   → Fix: use AI as **attacker and compressor**, not just a writer.

4. **Checklists as religion**  
   - Assuming every section must be fully populated for the process to be “valid.”  
   → Fix: treat templates as **scaffolding**. Anything that doesn’t influence 1.6 can stay light.

---

If you remember only one sentence from this guide, make it this:

> **Run Discovery as a series of sharp passes that try to kill bad ideas early,  
> not as a ceremony to prove every idea deserves to live.**
