## 10. Detailed Leaf Specification: 1.1 Product Vision

This chapter instantiates the generic leaf template (Purpose, Description, Input, Outcomes, Tools, AI Support) for the specific leaf:

- **Leaf ID:** `1.1`
- **Leaf Name:** `Product Vision`
- **Phase:** `1 – Discovery`

It serves as the reference for:

- What **must** exist for Product Vision to be considered “done”.
- How artifacts are organized under `PLC/`.
- How the **machine view** (`product_vision.json`, AI contract) should look.

The same pattern will be reused for other leaves (1.2, 1.3, 2.x, etc.).

---

### 10.1 Purpose / Objective

**Goal of 1.1 Product Vision:**

- Make explicit **why** the product exists.
- Clarify **who** it serves at a high-level (segments, not personas).
- Describe **what change** it aims to produce in the organization or market.
- Establish **what “success” looks like** for the initiative.

This leaf is the narrative anchor: every later decision (architecture, planning, scope, GTM) must be traceable back to the Product Vision.

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

This is the key bridge into later GTM work (Phase 9).

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

This document is the reference later when someone says “we shipped, so it’s done” — and you need to check if success criteria were actually met.

---

#### 10.2.5 `vision_scope.md` (required, high-level)

**Type:** doc  
**Path:** `PLC/1_Discovery/1.1_Product_Vision/vision_scope.md`

**Purpose:** Provide an **early, coarse-grained scope** for the vision (NOT a backlog).

Suggested sections:

- In-scope capabilities (big rocks)
- Explicit non-goals (things we will NOT do)
- Major assumptions (tech, organization, data, integrations)

Phase **3.3 Scope Definition** will refine this later. Here, the point is to set **hard boundaries** around the vision.

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

In addition to the human-readable docs, 1.1 must produce a **structured, machine-readable view** of the Product Vision.

#### 10.4.1 `product_vision.json` (required)

**Type:** data  
**Path:** `PLC/1_Discovery/1.1_Product_Vision/product_vision.json`

**Purpose:** Summarize the Product Vision in a stable JSON format that tools and AI agents can consume.

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
  }
}
```

The exact schema will be finalized in the Meta PLC JSON, but the **intent** is:

- One canonical JSON file encapsulating Product Vision.
- Easy to diff, validate, and feed into downstream tools.

---

### 10.5 Optional Outcome (Data) — AI Contract

This outcome encodes how AI is **allowed to behave** in leaf 1.1.

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
    "consistency_checker"
  ],
  "prompts": {
    "draft_vision": "plc.1.1.draft_vision",
    "review_clarity": "plc.1.1.review_clarity",
    "check_consistency": "plc.1.1.check_consistency"
  },
  "inputs": [
    "product_vision.md",
    "problem_statement.md",
    "value_proposition.md"
  ],
  "outputs": [
    "review_notes.md",
    "improvement_suggestions.md"
  ]
}
```

This allows:

- Tools to know **which files** AI should read before acting.
- A stable mapping between leaf `1.1` and named prompt flows (`plc.1.1.*`).
- Clear boundaries on where AI assistance is expected and how its outputs should be stored.

---

### 10.6 Summary for Meta PLC `outcomes` (Leaf 1.1)

When encoding 1.1 in `meta_plc.json`, the **outcomes** for this leaf should capture at least:

**Required outcomes:**

- `doc: "PLC/1_Discovery/1.1_Product_Vision/product_vision.md"`
- `doc: "PLC/1_Discovery/1.1_Product_Vision/problem_statement.md"`
- `doc: "PLC/1_Discovery/1.1_Product_Vision/value_proposition.md"`
- `doc: "PLC/1_Discovery/1.1_Product_Vision/success_criteria.md"`
- `doc: "PLC/1_Discovery/1.1_Product_Vision/vision_scope.md"`
- `data: "PLC/1_Discovery/1.1_Product_Vision/product_vision.json"`

**Optional outcomes:**

- `doc: "PLC/1_Discovery/1.1_Product_Vision/elevator_pitch.md"`
- `doc: "PLC/1_Discovery/1.1_Product_Vision/vision_one_pager.md"`
- `doc: "PLC/1_Discovery/1.1_Product_Vision/risks_and_unknowns.md"`
- `data: "PLC/1_Discovery/1.1_Product_Vision/ai_contract_product_vision.json"`

This chapter is the normative reference for any implementation of **leaf 1.1 Product Vision** in SymK-compliant projects.
