# 2.1 System Blueprints

_Phase 2 — Architecture_

## 1. Purpose / Objective
Provide a shared, high-level view of the system context, main components, and core flows.

## 2. Description
Captures context diagrams, component boundaries, major flows and key integration points. Serves as the backbone for technical decisions, planning and risk analysis.

## 3. Input
- **Required:**
- type=leaf, ref=1.1
- **Optional:**
- type=leaf, ref=1.3
- type=doc, ref=PLC/1_Discovery/1.2_Market_Research/market_overview.md

## 4. Outcomes
- [required] type=doc, ref=PLC/2_Architecture/2.1_System_Blueprints/system_blueprints.md
- [optional] type=asset, ref=PLC/2_Architecture/2.1_System_Blueprints/diagrams/
- [optional] type=data, ref=PLC/2_Architecture/2.1_System_Blueprints/architecture_map.json

## 5. Tools / Methodology
- **Methods:**
  - C4 modeling
  - Architecture workshops
- **Tools:**
  - Diagram tool
  - Markdown editor
- **Templates:**
  - system_blueprints_template.md

## 6. AI Support / Symbiotic Role
- **Roles:**
  - diagram_explainer
  - map_consistency_checker
- **Prompt contracts:**
  - `plc.2.1.describe_architecture_map`
  - `plc.2.1.check_consistency_with_vision`
- **Input context:**
  - doc: PLC/2_Architecture/2.1_System_Blueprints/system_blueprints.md
  - doc: PLC/1_Discovery/1.1_Product_Vision/product_vision.md
  - data: PLC/2_Architecture/2.1_System_Blueprints/architecture_map.json
- **Expected outputs (AI-assisted):**
  - doc: PLC/2_Architecture/2.1_System_Blueprints/system_blueprints.md
