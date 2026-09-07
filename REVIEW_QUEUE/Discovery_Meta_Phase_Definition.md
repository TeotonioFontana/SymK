# 1. Discovery — Meta Phase Definition

This is the **meta definition** of the Discovery phase. It is **project-agnostic** and
acts as a template for any product created with the SymK devkit.

## 1. Purpose

Clarify **why** the product exists, **for whom**, and **in which context** before
any detailed architecture or planning work begins.

## 2. Recommended Inputs

These are informal; they usually come from outside the PLC:

- Initial idea or problem statement.
- Any strategic context (business goals, constraints).
- Notes from early conversations or experiments.

They are *not* enforced by tooling, but should be captured in some form (notes, docs).

## 3. Recommended Tooling & Models

- Project Model Canvas (PMC) to consolidate intent on a single page.
- AI-assisted ideation (e.g., ChatGPT) for framing vision and options.
- Stakeholder interviews or discovery calls.
- Simple documentation in Markdown (no heavy tooling required).

## 4. Required Human-Facing Outcomes

Every project should produce **at least** the following artifacts in its PLC instance:

- Product Vision — clear statement of what the product is, for whom, and why now.
- Market Research — market definition, target segments, competitors, main hypotheses.
- Stakeholder Map — main stakeholders, their interest and influence, goals and pains.

Optional but strongly recommended:

- Project Model Canvas — one-page synthesis connecting value, objectives,
  stakeholders, risks, and assumptions.

The exact filenames and folders are suggested by the meta JSON template for consistency,
but can be adapted as needed if the project PLC state is kept in sync.

## 5. Machine-Facing Template

The companion `phase_template.json` in this folder defines the **schema** of Discovery
outputs for tools. It does **not** contain project data, only the definition of what a
valid Discovery phase must expose.

Tools will:

- Read the meta template to know expected outputs.
- Read each project's `phase_state.json` to see the actual state.
- Validate that required outputs exist and are wired into downstream phases.
