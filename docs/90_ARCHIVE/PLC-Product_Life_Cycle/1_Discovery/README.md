# 1.3 Stakeholder Map — SymK

## 1. Purpose

This document answers three simple questions:

1. **Who cares about SymK?**
2. **How much power do they have over it?**
3. **What do they actually want from it?**

This is a working map to drive:
- prioritization,
- communication,
- and expectation management across the PLC phases.

---

## 2. Stakeholder groups (high level)

### 2.1 Internal / Core stakeholders

1. **Product Architect (you)**
   - Role: Vision owner and ultimate design authority for SymK.
   - Interest: High — SymK encodes your way of building systems.
   - Power: Very high — defines direction, scope, and non-negotiables.

2. **AI Engineering Partner (“Duke” / ChatGPT)**
   - Role: Main AI co-developer producing code, docs, scaffolds.
   - Interest: High — central to the “symbiotic” concept.
   - Power: Indirect — shapes implementation quality, speed, and consistency.

3. **Core Engineering Team**
   - Role: Implements and extends SymK tooling; uses it daily.
   - Interest: High — SymK will either make their life better or miserable.
   - Power: High — adoption, feedback, and resistance can make or break it.

4. **DevOps / Platform Engineering**
   - Role: Integrates SymK into CI/CD, infra, and platform workflows.
   - Interest: High — SymK changes how projects are scaffolded and governed.
   - Power: High — controls pipelines and platform standards.

5. **Tech/Product Leadership (if/when present)**
   - Role: Sponsors and prioritizes SymK relative to other work.
   - Interest: Medium–High — cares about throughput, quality, predictability.
   - Power: High — can allocate time/budget or stall the initiative.

---

### 2.2 Secondary stakeholders

6. **Consumers of SymK (Downstream Projects)**
   - Examples: IaaC Tools, Hyperdocs / LexBrain, future SaaS products.
   - Interest: Medium–High — they want consistency and acceleration.
   - Power: Medium — or high collectively: if they ignore SymK, it fails as a standard.

7. **QA / Testing Roles**
   - Role: Use SymK’s testing structure and enforcement.
   - Interest: Medium — SymK can clarify and standardize their work.
   - Power: Medium — can demand more testability and coverage patterns.

8. **Security / Compliance**
   - Role: Validate that AI-assisted processes and tooling are auditable and safe.
   - Interest: Medium — grows as the product becomes more external/regulated.
   - Power: Medium–High — can block releases or impose requirements.

9. **Future Customers / External Users**
   - Role: External companies or teams adopting SymK as a product.
   - Interest: Variable — from “curious” to “critical infra dependency”.
   - Power: Long-term High — their demands will shape SymK’s evolution.

10. **Toolchain Vendors / Ecosystem**
    - Examples: IDEs, CI systems, cloud infra, AI APIs.
    - Role: Integration points.
    - Interest: Low–Medium — mainly technical interoperability.
    - Power: Indirect — feature limits and changes constrain what SymK can do.

---

## 3. Stakeholder map (Influence vs Interest)

| Stakeholder                      | Interest | Influence/Power | Positioning / Strategy                        |
|----------------------------------|----------|-----------------|-----------------------------------------------|
| Product Architect                | High     | Very High       | Key decision-maker, maintain clarity + focus  |
| AI Partner (Duke / ChatGPT)     | High     | High (indirect) | Treat as core collaborator, define constraints|
| Core Engineering Team            | High     | High            | Co-design tools; involve early and often      |
| DevOps / Platform Engineering    | High     | High            | Strategic partner; integrate SymK deeply      |
| Tech/Product Leadership          | Medium   | High            | Keep informed; show ROI and risk reduction    |
| Downstream Projects              | High     | Medium          | Listen for friction; prioritize their pain    |
| QA / Testing                     | Medium   | Medium          | Align test structure; provide solid hooks     |
| Security / Compliance            | Medium   | Medium–High     | Engage early when externalization starts      |
| Future Customers                 | High     | High (later)    | Gather signals; design for future needs       |
| Toolchain / Ecosystem            | Low–Med  | Medium (indirect)| Track constraints; design around limitations |

Simplified grid:

- **High influence / high interest**  
  → Architect, Core Eng, DevOps  
  → Must be in the loop on design decisions and tradeoffs.

- **High influence / medium interest**  
  → Leadership, Security/Compliance  
  → Need periodic, concise updates and clear risk/benefit framing.

- **Medium influence / high interest**  
  → Downstream projects, Future customers  
  → Source of concrete requirements and feedback.

---

## 4. Stakeholder goals & pains

### 4.1 Architect

- **Goals**
  - Encode a **repeatable, opinionated way** to build products with AI.
  - Avoid one-off solutions and architecture entropy.
- **Pains**
  - Manually enforcing rules across multiple codebases.
  - Maintaining consistency over time and across projects.

### 4.2 Core Engineering Team

- **Goals**
  - Faster project setup with sane defaults.
  - Less time arguing about folder structure, doc formats, and rules.
- **Pains**
  - Boilerplate, repetitive work.
  - Being blocked by “process” that doesn’t add value.

### 4.3 DevOps / Platform

- **Goals**
  - Standard inputs into CI/CD and infra pipelines.
  - Predictable project layouts and config locations.
- **Pains**
  - Every team doing “their own thing”.
  - Fragile pipelines due to inconsistent repo conventions.

### 4.4 Downstream Projects

- **Goals**
  - Reuse SymK backbone instead of reinventing scaffolding.
  - Leverage AI safely but aggressively.
- **Pains**
  - Legacy/dev-only conventions.
  - Poor documentation and drift between projects.

### 4.5 Leadership

- **Goals**
  - Better throughput, quality, and predictability.
  - Confidence that AI use is controlled and auditable.
- **Pains**
  - Projects that depend on “heroics” and tribal knowledge.
  - Risk exposure from uncontrolled AI usage.

---

## 5. RACI-ish view for key PLC areas

High-level responsibility mapping for SymK (first iterations):

| Area / Activity                     | Architect | AI Partner | Core Eng | DevOps | Leadership |
|------------------------------------|----------|-----------|----------|--------|-----------|
| Product vision & scope             | R/A      | C         | C        | I      | C         |
| PLC folder & artifact structure    | R        | C         | C        | C      | I         |
| SymK tooling design (decorators, CLIs) | R   | C         | R        | C      | I         |
| IDE & CI integration               | C        | C         | C        | R      | I         |
| Coding standards & ruleset         | R        | C         | C        | C      | I         |
| Internal rollout (to projects)     | R        | C         | R        | R      | C         |
| Externalization (docs, packaging)  | R        | C         | C        | C      | A         |

Legend:
- **R** – Responsible
- **A** – Accountable
- **C** – Consulted
- **I** – Informed

---

## 6. Communication & engagement plan

### 6.1 Minimum cadence (internal)

- **Architect ↔ Core Engineering**
  - Frequency: continuous + weekly checkpoint.
  - Topic: design decisions, technical tradeoffs, feedback from use.

- **Architect ↔ DevOps/Platform**
  - Frequency: weekly or per major change.
  - Topic: CI/CD integration, repo structure impacts, automation hooks.

- **Architect ↔ Downstream Projects**
  - Frequency: per onboarding + milestone reviews.
  - Topic: friction, missing features, migration issues.

- **Architect ↔ Leadership**
  - Frequency: milestone-based.
  - Topic: progress vs. goals, ROI, risks, and upcoming changes.

### 6.2 Artifacts supporting communication

- PLC folder itself (`/PLC`), including:
  - **1.1 Product Vision**
  - **1.2 Market Research**
  - **1.3 Stakeholder Map** (this doc)
- Short **CHANGELOG / RELEASE_NOTES** under `10.3_Release_Notes`.
- Architecture overviews under `2_Architecture`.

---

## 7. Risks related to stakeholders

1. **Low buy-in from Core Eng / DevOps**
   - Risk: SymK seen as bureaucracy.
   - Mitigation: prioritize real productivity wins; keep v1 minimal and useful.

2. **Leadership not convinced**
   - Risk: SymK becomes a “pet framework” with partial adoption.
   - Mitigation: show clear before/after stories for real projects.

3. **Downstream projects ignore the standard**
   - Risk: fragmentation; SymK becomes optional “nice-to-have”.
   - Mitigation: make SymK the path of least resistance (best tooling, fastest start).

4. **Over-centralization on the Architect**
   - Risk: bottleneck; limited scalability.
   - Mitigation: document principles well; make tools encode decisions; enable others to extend safely.

---

## 8. Stakeholder action backlog

Concrete next steps for this phase:

1. **List specific named stakeholders** for:
   - Core Engineering,
   - DevOps,
   - QA,
   - Downstream project owners.
   (Even if some are just “future roles” for now.)

2. **Capture initial expectations**:
   - Short interviews or notes: “What would SymK need to do for you to use it daily without swearing?”

3. **Define adoption order**:
   - Decide who is **first internal adopter** (e.g., IaaC Tools).
   - Plan **one lightweight pilot** instead of trying to roll out everywhere at once.

4. **Align on non-negotiables vs. flexible parts**:
   - Mark which conventions are hard rules vs. recommended patterns.

5. **Revisit this map** after:
   - First internal pilot,
   - First external user (even if a friendly).

This document should be updated whenever a major new stakeholder appears or a current one changes influence or interest.
