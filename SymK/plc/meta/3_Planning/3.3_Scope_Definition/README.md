# 3.3 Scope Definition

_Phase 3 — Planning_

## 1. Purpose / Objective
Clarify what is in scope and out of scope for a given delivery wave, to avoid expectation drift.

## 2. Description
Lists included epics/features, explicit exclusions and non-goals. Ties each scoped item back to the roadmap and vision. Defines boundaries so teams know what NOT to do in this wave.

## 3. Input
- **Required:**
- type=leaf, ref=3.1
- **Optional:**
- type=leaf, ref=1.2

## 4. Outcomes
- [required] type=doc, ref=PLC/3_Planning/3.3_Scope_Definition/scope_definition.md
- [optional] type=data, ref=PLC/3_Planning/3.3_Scope_Definition/scope_items.json

## 5. Tools / Methodology
- **Methods:**
  - Scope workshop
  - Story mapping
  - Impact mapping
- **Tools:**
  - Markdown editor
  - Board / Kanban tool
- **Templates:**
  - scope_definition_template.md

## 6. AI Support / Symbiotic Role
- **Roles:**
  - scope_checker
  - risk_spotter
- **Prompt contracts:**
  - `plc.3.3.highlight_scope_risks`
  - `plc.3.3.check_scope_vs_vision`
- **Input context:**
  - doc: PLC/3_Planning/3.3_Scope_Definition/scope_definition.md
  - doc: PLC/1_Discovery/1.1_Product_Vision/product_vision.md
  - data: PLC/3_Planning/3.3_Scope_Definition/scope_items.json
- **Expected outputs (AI-assisted):**
  - doc: PLC/3_Planning/3.3_Scope_Definition/scope_definition.md
