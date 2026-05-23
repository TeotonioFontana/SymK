# 2. Architecture — Meta Phase Definition

This is the **meta definition** of the Architecture phase. It is **project-agnostic**
and specifies what a valid architecture phase should deliver for any product.

## 1. Purpose

Translate Discovery (vision, market, stakeholders) into a **coherent technical shape**:

- systems and boundaries,
- technology stacks,
- security posture and constraints.

## 2. Required Inputs (from Discovery)

Architecture is expected to consume, at minimum:

- Product Vision
- Market Research
- Stakeholder Map

Optionally:

- Project Model Canvas (if present for the project).

Tools enforce these via references to the Discovery phase outputs, not by filenames.

## 3. Recommended Tooling & Models

- System diagrams (e.g., C4 model: Context, Container, Component diagrams).
- Architecture Decision Records (ADRs) in Markdown.
- Reference stack catalogs (languages, frameworks, infra patterns).
- Security and compliance guidelines (encryption, IAM, data flows).

## 4. Required Human-Facing Outcomes

Every project should produce at least:

- System Blueprints — high-level diagrams and descriptions of major components,
  data flows, and integration points.
- Reference Stacks — explicit choices of tech stacks, patterns, and their rationale.
- Security Model — how authentication, authorization, data classification,
  encryption, and auditability are addressed.

## 5. Machine-Facing Template

`phase_template.json` defines, for tools:

- which outputs **must** exist (IDs and types),
- the recommended default locations where those outputs should live in the project PLC.

Instance-specific data (actual files, status) belongs to the project's `PLC/2_Architecture`
tree and its `phase_state.json`.
