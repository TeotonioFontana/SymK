# 3. Planning — Meta Phase Definition

This is the **meta definition** of the Planning phase. It is project-agnostic and
defines how any product should turn vision and architecture into a realistic plan.

## 1. Purpose

Decide **what will be built when** and **to what depth**. Planning connects:

- product vision and market needs,
- architecture constraints,
- team capacity and priorities.

## 2. Required Inputs

From Discovery:

- Product Vision
- Market Research
- Stakeholder Map
- Project Model Canvas (if available)

From Architecture:

- System Blueprints
- Reference Stacks
- Security Model

Tools track these via references to other phases, not hardcoded paths.

## 3. Recommended Tooling & Models

- Roadmaps (time-based, outcome-based, or both).
- Release train planning.
- Estimation techniques (t-shirt sizing, story points, etc.).
- Prioritization frameworks (e.g., MoSCoW, RICE).
- Lightweight backlog tools or spreadsheets, mirrored into Markdown when possible.

## 4. Required Human-Facing Outcomes

Every project should produce at least:

- Roadmap — high-level view of major capabilities and milestones.
- Release Trains — grouping of features into releases or iterations.
- Scope Definition — clear MVP, subsequent phases, and out-of-scope items.

## 5. Machine-Facing Template

`phase_template.json` specifies:

- which upstream phase outputs Planning depends on,
- which Planning outputs must be present in a valid PLC instance,
- default locations (paths) for those outputs in the project folder.

The project's concrete state is tracked in `PLC/3_Planning/phase_state.json`.
