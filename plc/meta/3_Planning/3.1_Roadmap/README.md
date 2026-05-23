# 3.1 Roadmap

_Phase 3 — Planning_

## 1. Purpose / Objective
Define major value increments, their sequencing and indicative timelines.

## 2. Description
Captures product milestones, themes and high-level sequencing. The roadmap connects vision, market realities and architecture constraints into a time-based story that stakeholders can understand.

## 3. Input
- **Required:**
- type=leaf, ref=1.1
- type=leaf, ref=1.2
- type=leaf, ref=2.1

## 4. Outcomes
- [required] type=doc, ref=PLC/3_Planning/3.1_Roadmap/roadmap.md
- [optional] type=data, ref=PLC/3_Planning/3.1_Roadmap/roadmap.json

## 5. Tools / Methodology
- **Methods:**
  - Roadmap workshop
  - Prioritization (MoSCoW, Kano)
  - Theme-based planning
- **Tools:**
  - Spreadsheet
  - Roadmap tool
  - Markdown editor
- **Templates:**
  - roadmap_template.xlsx
  - roadmap_template.md

## 6. AI Support / Symbiotic Role
- **Roles:**
  - prioritization_assistant
  - dependency_checker
  - narrative_summarizer
- **Prompt contracts:**
  - `plc.3.1.summarize_roadmap`
  - `plc.3.1.check_roadmap_consistency`
  - `plc.3.1.highlight_timeline_risks`
- **Input context:**
  - doc: PLC/3_Planning/3.1_Roadmap/roadmap.md
  - doc: PLC/1_Discovery/1.1_Product_Vision/product_vision.md
  - data: PLC/3_Planning/3.1_Roadmap/roadmap.json
- **Expected outputs (AI-assisted):**
  - doc: PLC/3_Planning/3.1_Roadmap/roadmap.md
