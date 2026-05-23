# 2.2 Reference Stacks

_Phase 2 — Architecture_

## 1. Purpose / Objective
Define allowed technology stacks and constraints so teams don’t reinvent the wheel or create unmaintainable setups.

## 2. Description
Documents languages, frameworks, databases, hosting models and supporting services that are approved for this product. Captures constraints (versions, SLAs, support status) and references any organization-wide standards.

## 3. Input
- **Required:** none explicitly defined.
- **Optional:**
- type=leaf, ref=2.1
- type=external, ref=org/tech_standards

## 4. Outcomes
- [required] type=doc, ref=PLC/2_Architecture/2.2_Reference_Stacks/reference_stack.md
- [optional] type=data, ref=PLC/2_Architecture/2.2_Reference_Stacks/tech_stack.json

## 5. Tools / Methodology
- **Methods:**
  - Tech radar review
  - Architecture Decision Records (ADR)
- **Tools:**
  - Markdown editor
  - Spreadsheet
- **Templates:**
  - reference_stack_template.md
  - adr_template.md

## 6. AI Support / Symbiotic Role
- **Roles:**
  - summarizer
  - gap_checker
- **Prompt contracts:**
  - `plc.2.2.summarize_tech_stack`
  - `plc.2.2.check_stack_against_requirements`
- **Input context:**
  - doc: PLC/2_Architecture/2.2_Reference_Stacks/reference_stack.md
  - data: PLC/2_Architecture/2.2_Reference_Stacks/tech_stack.json
- **Expected outputs (AI-assisted):**
  - doc: PLC/2_Architecture/2.2_Reference_Stacks/reference_stack.md
