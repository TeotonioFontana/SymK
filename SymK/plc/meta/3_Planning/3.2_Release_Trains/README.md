# 3.2 Release Trains

_Phase 3 — Planning_

## 1. Purpose / Objective
Define how features move from development to production through structured release cycles.

## 2. Description
Specifies release cadence, environments, branching model and eligibility criteria for features entering each train (e.g., quality gates, required checks). This prevents ad-hoc, chaotic releases.

## 3. Input
- **Required:**
- type=leaf, ref=3.1
- **Optional:**
- type=external, ref=org/release_policies

## 4. Outcomes
- [required] type=doc, ref=PLC/3_Planning/3.2_Release_Trains/release_policy.md
- [optional] type=data, ref=PLC/3_Planning/3.2_Release_Trains/release_trains.json

## 5. Tools / Methodology
- **Methods:**
  - Release planning sessions
  - Environment mapping
  - Change management review
- **Tools:**
  - Markdown editor
  - Diagram tool
- **Templates:**
  - release_policy_template.md

## 6. AI Support / Symbiotic Role
- **Roles:**
  - policy_summarizer
  - gate_checker
- **Prompt contracts:**
  - `plc.3.2.summarize_release_policy`
  - `plc.3.2.check_gates_coverage`
- **Input context:**
  - doc: PLC/3_Planning/3.2_Release_Trains/release_policy.md
  - data: PLC/3_Planning/3.2_Release_Trains/release_trains.json
- **Expected outputs (AI-assisted):**
  - doc: PLC/3_Planning/3.2_Release_Trains/release_policy.md
