# SymK Product Lifecycle (PLC) — Reference Manual (Markdown Draft)

Version: v0.1.0-draft  
Status: Working draft — canonical until DOCX version is generated.

---

## 1. Introduction

The SymK Product Lifecycle (PLC) defines **how a product lives** from discovery to operation.

This manual is the **human-facing** reference. It explains:

- The phases and sub-phases (leaves) of the PLC.
- What each leaf must produce.
- How the PLC is represented as files and folders in a project.
- How tools (like scaffolding scripts and AI agents) consume that structure.

The **machine-facing** side (JSON/YAML) is defined by:

- The global **Meta PLC** JSON in SymK.
- Per-project **Meta snapshot** JSON stored alongside each PLC instance.

---

## 2. Audience & Scope

### 2.1 Audience

This manual is intended for:

- Product / Solution Architects  
- Tech Leads  
- SymK Tooling Authors  
- Anyone who has to **create, maintain, or consume** PLC data

### 2.2 Scope

This document covers:

- The **SymK PLC model** (phases and leaves).
- The difference between:
  - **Meta PLC** (method, global, in SymK)
  - **PLC instance** (per-product, inside each project)
- How the PLC is represented as:
  - Human artifacts (Markdown, diagrams, decks)
  - Machine artifacts (JSON/YAML)
- How the **scaffolding tool** generates the PLC stub folders for a project.

It does **not** prescribe UX tools, ticketing systems, or specific CI vendors. Those are project choices, as long as they respect the PLC contracts.

---

## 3. Meta PLC vs PLC Instance

### 3.1 Meta PLC (Global, in SymK)

The **Meta PLC** is the **method**. There is exactly **one** canonical Meta PLC in SymK at any given time.

- Stored as JSON, e.g.:

  ```text
  symbiotic_devkit/plc/PLC_META/meta_plc.json
  ```

- Describes:
  - Phases (1–10)
  - Leaves per phase (e.g. `1.1 Product Vision`, `1.2 Market Research`)
  - For each leaf:
    - Purpose / Description
    - Inputs / Outcomes
    - Tools / Methods / Templates
    - AI contract (roles, prompt IDs, expected inputs/outputs)

This file is **tooling input**, not marketing copy. It evolves frequently, especially early on.

### 3.2 No PLC Examples Inside SymK

There is **no** `PLC_EXAMPLE/` tree inside SymK.

- All **examples and didactic guidance** live in this manual (Markdown).
- If you want an “example PLC”, you build it as a **real PLC instance** inside a project, not as a toy tree in SymK.

SymK owns:

- The **Meta PLC** (`meta_plc.json`)
- The **tools** (e.g. `plc_scaffold_from_meta.py`)
- The **reference manual** (this MD)

Nothing else.

### 3.3 PLC Instance (Per Project)

Each product / project has its own **PLC instance**.

Rules:

1. The PLC lives **inside the project repository**, under:

   ```text
   <project_root>/PLC/
   ```

2. At project bootstrap time, we take a **snapshot** of the Meta PLC:

   ```text
   <project_root>/PLC/meta_plc.vX.Y.Z.json
   ```

   or

   ```text
   <project_root>/PLC/meta/meta_plc.json
   ```

   with a `version` field inside.

3. The **PLC stub** (folders and READMEs) is scaffolded from that snapshot.

Result:

- SymK holds the **living meta**.
- Each project holds a **frozen copy** of the meta as used at startup + its own PLC contents.

Later, we can compare:

- Project’s `meta_plc.vX.Y.Z.json`
- Current `meta_plc.json` in SymK

to see if it’s worth migrating.

---

## 4. Leaf Structure (Per Sub-Phase)

Each sub-phase (leaf) — e.g., `1.1 Product Vision`, `1.2 Market Research` — follows a **standard template**, both in the manual and in the file structure.

### 4.1 Human-Facing Leaf Template

Each leaf has a `README.md` under:

```text
<project_root>/PLC/<PhaseDir>/<LeafDir>/README.md
```

The content follows this structure:

1. **Purpose / Objective**  
   - Why this leaf exists.  
   - What decision or understanding it must produce.

2. **Description**  
   - Short narrative of the work done here.  
   - Scope, boundaries, key concerns.

3. **Input**  
   - What this leaf depends on.  
   - Upstream leaves (e.g. `1.1 Product Vision`) and external sources.  
   - Ideally separated into:
     - Required inputs
     - Optional inputs

4. **Outcomes**  
   - Artifacts that must exist when this leaf is “done”.  
   - Both human and machine artifacts:  
     - Docs: Markdown, decks, diagrams  
     - Data: JSON/YAML with structured data  
   - Each outcome is tagged as:
     - Required
     - Optional

5. **Tools / Methodology**  
   - Methods: e.g. interviews, SWOT, C4, threat modeling.  
   - Tools: e.g. draw.io, Miro, spreadsheets, code generators.  
   - Templates: pointers to specific boilerplates (e.g. `templates/stakeholder_map.md`).

6. **AI Support / Symbiotic Role**  
   - How AI participates in this leaf.  
   - Roles: e.g. summarizer, critic, risk spotter, consistency checker.  
   - Stable prompt contracts / IDs: e.g. `plc.1.2.summarize_market`.  
   - Expected AI inputs: which docs/data AI is allowed to read here.  
   - Expected AI outputs: drafts, summaries, matrices, risk lists, etc.

### 4.2 Machine-Facing Leaf Representation

In the **Meta PLC JSON**, each leaf has fields mapping to the template above:

- `purpose`
- `description`
- `inputs`: list of `{type, ref, required}`  
- `outcomes`: list of `{type, ref, required}`  
- `tools`: `{methods, tools, templates}`  
- `ai_contract`: `{enabled, roles, prompt_ids, input_spec, output_spec}`

This is how tools (Python, AI agents, CLIs) know what each leaf is supposed to be.

---

## 5. PLC Phases (1–10)

Below is the **standard PLC phase list**. Details for each leaf live in the Meta PLC JSON and are explained in this manual only where necessary.

### 5.1 Phase 1 — Discovery

**Goal:** Understand the problem space and define the product at a high level.

Leaves (typical):

- `1.1 Product Vision`
- `1.2 Market Research`
- `1.3 Stakeholder Map`

### 5.2 Phase 2 — Architecture

**Goal:** Define the technical and information architecture.

Leaves (typical):

- `2.1 System Blueprints`
- `2.2 Reference Stacks`
- `2.3 Security Model`

### 5.3 Phase 3 — Planning

**Goal:** Plan roadmap, releases and scope.

Leaves (typical):

- `3.1 Roadmap`
- `3.2 Release Trains`
- `3.3 Scope Definition`

### 5.4 Phase 4 — Design

**Goal:** Turn requirements/architecture into concrete experience and interaction designs.

Leaves (examples):

- `4.1 UX Flows`
- `4.2 IA Diagrams`
- `4.3 Design System`

### 5.5 Phase 5 — Development

**Goal:** Implement backend, frontend and infrastructure, respecting SymK coding rules (boundaries, core, adapters, models).

Leaves (examples):

- `5.1 Backend`
- `5.2 Frontend`
- `5.3 Infrastructure`

### 5.6 Phase 6 — Testing

**Goal:** Validate correctness, quality and risk coverage.

Leaves (examples):

- `6.1 Test Plans`
- `6.2 QA Suites`
- `6.3 Security Tests`

### 5.7 Phase 7 — Deployment

**Goal:** Move changes safely into runtime environments.

Leaves (examples):

- `7.1 Runtime Configs`
- `7.2 CI/CD Pipelines`
- `7.3 Observability`

### 5.8 Phase 8 — Operations

**Goal:** Keep the system healthy and performant in production.

Leaves (examples):

- `8.1 SRE Procedures`
- `8.2 Incident Response`
- `8.3 Performance Tuning`

### 5.9 Phase 9 — Go-to-Market (GTM)

**Goal:** Enable positioning, sales and commercial success.

Leaves (examples):

- `9.1 Positioning`
- `9.2 Sales Enablement`
- `9.3 Pricing`

### 5.10 Phase 10 — Documentation

**Goal:** Ensure technical and user-facing documentation stays coherent and traceable.

Leaves (examples):

- `10.1 Technical Docs`
- `10.2 User Docs`
- `10.3 Release Notes`

---

## 6. Machine Structures

### 6.1 Global Meta PLC (in SymK)

SymK holds the **one true Meta PLC**:

```text
symbiotic_devkit/plc/PLC_META/meta_plc.json
```

This file contains:

- Meta-level fields:
  - `version`
  - `name`
  - `description`
- `phases`: [ { id, name, description, leaves: [...] }, ... ]
- For each leaf:
  - `id`, `name`, `phase`
  - `purpose`, `description`
  - `inputs` / `outcomes`
  - `tools`
  - `ai_contract`

This is the **input** for scaffolding tools and documentation generators.

### 6.2 Per-Project Meta Snapshot

Each project keeps a **snapshot** of the Meta PLC as used at creation time, under its own `PLC/`:

Example patterns:

```text
<project_root>/PLC/meta_plc.v1.0.3.json
# or
<project_root>/PLC/meta/meta_plc.json
```

This snapshot must include:

- The Meta version (e.g. `"version": "v1.0.3"`)
- The full meta structure (same as SymK’s `meta_plc.json` at that time)

Projects may later compare this snapshot with newer Meta PLC versions to decide on migrations.

### 6.3 Optional plc_instance.json

In the future, a project may maintain a synthesized:

```text
<project_root>/PLC/plc_instance.json
```

This would describe:

- Current project status per leaf.
- Owners, timestamps, and key artifacts.
- AI usage per leaf.

This file is **optional**, but very useful for dashboards and agents. Its exact schema can be defined once PLC instances are more mature.

---

## 7. PLC Scaffolding Tool

### 7.1 Purpose

The script:

```text
plc_scaffold_from_meta.py
```

generates or updates a **PLC stub** (folders + READMEs + optional placeholders) from a **Meta PLC JSON**.

It is used primarily when:

- Creating a **new project PLC/ tree** from the current Meta snapshot.
- Regenerating leaf `README.md` files after Meta changes (if a project opts to sync).

### 7.2 Behaviour (High-Level)

Given:

- `--meta` → path to a `meta_plc.json`  
- `--root` → project root  
- `--plc-dir` → PLC directory name (usually `PLC`)

it creates:

```text
<root>/<plc-dir>/<PhaseId>_<PhaseNameSlug>/<LeafId>_<LeafNameSlug>/
```

and populates:

- `README.md` per leaf with the **leaf template** sections.
- Optional empty placeholder files for doc/data outcomes if `--create-outcomes` is used.

Existing files are preserved unless explicitly overwritten.

### 7.3 Flags

- `--meta PATH` (required)  
  Path to the Meta PLC JSON file (SymK’s or project’s snapshot).

- `--root PATH` (default: `.`)  
  Project root where the PLC tree is generated.

- `--plc-dir NAME` (default: `PLC`)  
  Directory under root to hold the PLC structure.

- `--create-outcomes` (flag)  
  Creates **empty files** for outcomes of type `doc` or `data`.

- `--force` (flag)  
  Overwrites existing `README.md` files for phases and leaves.  
  Outcome files are never overwritten, only created if missing.

### 7.4 Typical Usage — New Project

Inside a **new project** just created by `symk-project-init`:

1. Copy the **current meta** from SymK into the project:

   ```bash
   cp /path/to/SymK/PLC_META/meta_plc.json PLC/meta_plc.v1.0.3.json
   ```

2. Generate the PLC stub:

   ```bash
   python3 path/to/plc_scaffold_from_meta.py      --meta PLC/meta_plc.v1.0.3.json      --root .      --plc-dir PLC      --create-outcomes
   ```

Result:

```text
PLC/
  meta_plc.v1.0.3.json       # snapshot of Meta
  1_Discovery/
    1.1_Product_Vision/
      README.md
      ... (placeholders if defined as outcomes)
    1.2_Market_Research/
    1.3_Stakeholder_Map/
  2_Architecture/
  ...
```

From here, humans fill in the content; tools can read both the snapshot and the evolving PLC.

---

## 8. Governance & Versioning

- The **Meta PLC** in SymK is versioned (semantic version).  
- Each project pins to a specific Meta version via its `meta_plc.vX.Y.Z.json` snapshot.  
- Changes to the Meta PLC are treated like **API changes**:
  - New mandatory leaves or artifacts require migration guidance.
  - Renames or removals must be documented.

Recommended:

- Maintain a `PLC_META/CHANGELOG.md` in SymK for Meta PLC evolution.
- Encourage projects to record which Meta version they use in:
  - `PLC/meta_plc.vX.Y.Z.json`
  - Optionally `PLC/plc_meta_ref.yaml` or similar.

---

## 9. Summary

- SymK owns:
  - **One** evolving Meta PLC (`meta_plc.json`)
  - The **tools** (`plc_scaffold_from_meta.py`, `symk-project-init`, etc.)
  - The **reference manual** (this Markdown)

- Each project owns:
  - A **PLC/** folder with all lifecycle artifacts.
  - A **snapshot** of the Meta PLC used at startup.

- Each leaf uses the same **6-section template**:
  - Purpose / Objective  
  - Description  
  - Input  
  - Outcomes  
  - Tools / Methodology  
  - AI Support / Symbiotic Role  

- The scaffolding tool bridges the gap:
  - Reads Meta PLC → generates PLC stub in the project.

Once this MD stabilizes, we can freeze a new version and generate the DOCX version on top of it.
