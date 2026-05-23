## 10. Detailed Leaf Specification: 1.1 Product Vision

This chapter instantiates the generic leaf template (Purpose, Description, Input, Outcomes, Tools, AI Support) for the specific leaf:

- **Leaf ID:** `1.1`
- **Leaf Name:** `Product Vision`
- **Phase:** `1 – Discovery`

It serves as the reference for:

- What **must** exist for Product Vision to be considered “done”.
- How artifacts are organized under `PLC/`.
- How the **machine view** (`product_vision.json`, AI contract) should look.
- How **product features** are anchored early via **Jobs to Be Done (JTBD)** and **feature themes**, without becoming a backlog (that’s 3.x).

The same pattern will be reused for other leaves (1.2, 1.3, 2.x, etc.).

---

### 10.1 Purpose / Objective

**Goal of 1.1 Product Vision:**

- Make explicit **why** the product exists.
- Clarify **who** it serves at a high-level (segments, not personas).
- Describe **what change** it aims to produce in the organization or market.
- Establish **what “success” looks like** for the initiative.
- Define the **core jobs to be done** and the **early feature themes** that will later be refined, scored and sliced in Planning (3.x).

This leaf is the narrative anchor: every later decision (architecture, planning, features, GTM) must be traceable back to the Product Vision.

All artifacts for this leaf live under:

```text
PLC/1_Discovery/1.1_Product_Vision/
```

---

### 10.2 Required Outcomes (Docs)

These are **mandatory human-facing documents** for 1.1.

#### 10.2.1 `product_vision.md` (required)

**Type:** doc  
**Path:** `PLC/1_Discovery/1.1_Product_Vision/product_vision.md`

**Purpose:** The **master narrative** of the product.

Suggested sections:

- Problem / Opportunity
- Who we serve (segments)
- Desired change / future state
- Why now (triggers, timing)
- What “winning” looks like qualitatively
- High-level **feature themes** (not a list of tickets; see 10.7)

All other Product Vision artifacts should be consistent with this document.

---

#### 10.2.2 `problem_statement.md` (required)

**Type:** doc  
**Path:** `PLC/1_Discovery/1.1_Product_Vision/problem_statement.md`

**Purpose:** Separate the **problem** from the solution.

Suggested sections:

- Current situation
- Pain / friction
- Constraints (regulation, legacy, culture)
- What happens if we do nothing

This protects against “solution in search of a problem”.

---

#### 10.2.3 `value_proposition.md` (required)

**Type:** doc  
**Path:** `PLC/1_Discovery/1.1_Product_Vision/value_proposition.md`

**Purpose:** Explain **why this product is worth existing**.

Suggested structure (inspired by classic value prop formulas):

- For **[segment]** that **[need / situation]**
- Our product helps **[outcome]**
- Unlike **[alternatives]**
- It does this by **[key differentiators]**

This is the key bridge into later GTM work (Phase 9) and into **feature-level value arguments** in Planning.

---

#### 10.2.4 `success_criteria.md` (required)

**Type:** doc  
**Path:** `PLC/1_Discovery/1.1_Product_Vision/success_criteria.md`

**Purpose:** Define **what success means** in measurable terms.

Suggested sections:

- Business outcomes (KPIs, ranges, timeframes)
- User outcomes (behavior changes, satisfaction, adoption)
- Technical outcomes (stability, latency, cost ceilings)
- Constraints not to violate (compliance, security, legal, brand)

Later, when features are prioritized and sliced (3.x), each major feature or epic should **map back** to one or more of these criteria.

---

#### 10.2.5 `vision_scope.md` (required, high-level)

**Type:** doc  
**Path:** `PLC/1_Discovery/1.1_Product_Vision/vision_scope.md`

**Purpose:** Provide an **early, coarse-grained scope** for the vision (NOT a backlog).

Suggested sections:

- In-scope capabilities (big rocks)
- Explicit non-goals (things we will NOT do)
- Major assumptions (tech, organization, data, integrations)

This document sets the **boundaries** within which feature work will later evolve. Phase **3.3 Scope Definition** will refine this into more concrete feature and release decisions.

---

### 10.3 Optional Outcomes (Docs)

These outputs are recommended but not strictly mandatory in the Meta PLC.

#### 10.3.1 `elevator_pitch.md` (optional)

**Type:** doc  
**Path:** `PLC/1_Discovery/1.1_Product_Vision/elevator_pitch.md`

**Purpose:** Compress the vision into a shareable 1–2 line pitch.

Example format:

> For [who] that [need], [Product] is a [category] that [key benefit].  
> Unlike [alternative], it [main differentiator].

Useful in slides, emails, and onboarding.

---

#### 10.3.2 `vision_one_pager.md` (optional)

**Type:** doc  
**Path:** `PLC/1_Discovery/1.1_Product_Vision/vision_one_pager.md`

**Purpose:** A single-page summary (often exported as PDF) for stakeholders.

Typical content:

- Short problem / solution summary
- Target users
- Value proposition
- 3–5 success metrics
- Link back to the full `product_vision.md`

---

#### 10.3.3 `risks_and_unknowns.md` (optional)

**Type:** doc  
**Path:** `PLC/1_Discovery/1.1_Product_Vision/risks_and_unknowns.md`

**Purpose:** Capture early **risks and uncertainties** specifically tied to the vision.

Basic sections:

- Strategic risks
- Market / adoption risks
- Technical / feasibility risks
- Unknowns and open questions

This connects Discovery to later risk management in Planning and Operations.

---

### 10.4 Required Outcome (Data) — `product_vision.json`

In addition to the human-readable docs, 1.1 must produce a **structured, machine-readable view** of the Product Vision, including **Jobs to Be Done** and **early feature themes**.

#### 10.4.1 `product_vision.json` (required)

**Type:** data  
**Path:** `PLC/1_Discovery/1.1_Product_Vision/product_vision.json`

**Purpose:** Summarize the Product Vision in a stable JSON format that tools and AI agents can consume, and that will later be cross-referenced by Planning (3.x) when features are prioritized (RICE, etc).

**Conceptual schema (illustrative):**

```jsonc
{
  "leaf_id": "1.1",
  "leaf_name": "Product Vision",
  "version": "v0.1.0",
  "problem": {
    "context": "",
    "pain_points": [],
    "do_nothing_risks": []
  },
  "target_users": [
    {
      "segment": "",
      "key_needs": []
    }
  ],
  "jobs_to_be_done": [
    {
      "id": "job-001",
      "statement": "When I ..., I want to ..., so I can ...",
      "segment": "primary or secondary segment",
      "importance": "high | medium | low",
      "current_satisfaction": "high | medium | low"
    }
  ],
  "value_proposition": {
    "statement": "",
    "differentiators": []
  },
  "success_criteria": {
    "business": [],
    "user": [],
    "technical": [],
    "constraints": []
  },
  "scope": {
    "in": [],
    "out": [],
    "assumptions": []
  },
  "feature_themes": [
    {
      "id": "theme-001",
      "name": "Onboarding simplification",
      "linked_jobs": ["job-001", "job-003"],
      "description": "Short description of the theme and why it matters.",
      "risk_level": "low | medium | high"
    }
  ]
}
```

The exact schema will be finalized in the Meta PLC JSON, but the **intent** is:

- Capture **jobs_to_be_done** early (JTBD lens).
- Capture **feature_themes** as conceptual clusters of future features/epics — not yet sliced, scored or scheduled.
- Provide clear references (`id`s) that Planning (3.x) can later attach to feature candidates, RICE scores, and roadmap entries.

---

### 10.5 Optional Outcome (Data) — AI Contract

This outcome encodes how AI is **allowed to behave** in leaf 1.1, including how it may assist feature-related thinking without inventing backlog on its own.

#### 10.5.1 `ai_contract_product_vision.json` (optional, recommended)

**Type:** data  
**Path:** `PLC/1_Discovery/1.1_Product_Vision/ai_contract_product_vision.json`

**Purpose:** Define a **stable AI contract** for this leaf: roles, prompt identifiers, allowed inputs, and expected outputs.

**Conceptual schema (illustrative):**

```jsonc
{
  "leaf_id": "1.1_Product_Vision",
  "enabled": true,
  "roles": [
    "summarizer",
    "challenger",
    "consistency_checker",
    "feature_theme_clarifier"
  ],
  "prompts": {
    "draft_vision": "plc.1.1.draft_vision",
    "review_clarity": "plc.1.1.review_clarity",
    "check_consistency": "plc.1.1.check_consistency",
    "suggest_feature_themes_from_jobs": "plc.1.1.suggest_feature_themes"
  },
  "inputs": [
    "product_vision.md",
    "problem_statement.md",
    "value_proposition.md",
    "product_vision.json"
  ],
  "outputs": [
    "review_notes.md",
    "improvement_suggestions.md",
    "feature_theme_suggestions.md"
  ],
  "constraints": {
    "must_not": [
      "introduce detailed backlog items or tickets",
      "assign priorities or dates (handled in 3.x)",
      "contradict defined success_criteria.md"
    ]
  }
}
```

This allows:

- Tools to know **which files** AI should read before acting.
- A stable mapping between leaf `1.1` and named prompt flows (`plc.1.1.*`).
- Clear boundaries: AI helps clarify **jobs and feature themes**, but **does not own prioritization or scheduling** — that’s Planning (3.x).

---

### 10.6 Feature Foundations in Product Vision (1.1 vs 3.x)

1.1 **does**:

- Define **Jobs to Be Done** (JTBD).
- Identify **early feature themes** linked to those jobs.
- Anchor feature thinking in **value, outcomes, and scope**.
- Produce a **structured product_vision.json** with `jobs_to_be_done` and `feature_themes`.

1.1 **does NOT**:

- Define a detailed feature backlog.
- Score or prioritize features (RICE, Kano, MoSCoW).
- Commit to releases or timelines.

All of that belongs to:

- **3.1 Roadmap** → outcome targets + high-level sequencing.  
- **3.3 Scope Definition** → translating themes/jobs into concrete feature sets, prioritized with RICE/etc.

So the dependency chain is:

```text
1.1 Product Vision (jobs, themes, success)
   ↓
1.2 / 1.3 Discovery depth
   ↓
3.x Planning (features, prioritization, releases)
```

Tools and AI agents should treat 1.1 as the **source of truth** for:

- Jobs to be done
- Early feature themes
- The “why” behind any future feature

---

### 10.7 Summary for Meta PLC `outcomes` (Leaf 1.1)

When encoding 1.1 in `meta_plc.json`, the **outcomes** for this leaf should capture at least:

**Required outcomes (docs):**

- `doc: "PLC/1_Discovery/1.1_Product_Vision/product_vision.md"`
- `doc: "PLC/1_Discovery/1.1_Product_Vision/problem_statement.md"`
- `doc: "PLC/1_Discovery/1.1_Product_Vision/value_proposition.md"`
- `doc: "PLC/1_Discovery/1.1_Product_Vision/success_criteria.md"`
- `doc: "PLC/1_Discovery/1.1_Product_Vision/vision_scope.md"`

**Required outcomes (data):**

- `data: "PLC/1_Discovery/1.1_Product_Vision/product_vision.json"`

**Optional outcomes (docs):**

- `doc: "PLC/1_Discovery/1.1_Product_Vision/elevator_pitch.md"`
- `doc: "PLC/1_Discovery/1.1_Product_Vision/vision_one_pager.md"`
- `doc: "PLC/1_Discovery/1.1_Product_Vision/risks_and_unknowns.md"`

**Optional outcomes (data):**

- `data: "PLC/1_Discovery/1.1_Product_Vision/ai_contract_product_vision.json"`

This chapter is the normative reference for any implementation of **leaf 1.1 Product Vision** in SymK-compliant projects, including how it seeds future **feature work** without turning into an uncontrolled backlog.
