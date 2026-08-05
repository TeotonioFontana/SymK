# 2.3 Security Model

_Phase 2 — Architecture_

## 1. Purpose / Objective
Make security requirements, trust boundaries and compliance constraints explicit before building.

## 2. Description
Defines security controls, trust boundaries, data classification, and key threats. Links business risk, architecture decisions and security mechanisms, avoiding “security as an afterthought”.

## 3. Input
- **Required:**
- type=leaf, ref=2.1
- **Optional:**
- type=leaf, ref=1.3
- type=external, ref=org/security_policies

## 4. Outcomes
- [required] type=doc, ref=PLC/2_Architecture/2.3_Security_Model/security_model.md
- [optional] type=data, ref=PLC/2_Architecture/2.3_Security_Model/security_policies.json

## 5. Tools / Methodology
- **Methods:**
  - Threat modeling
  - STRIDE
  - Data classification
- **Tools:**
  - Diagram tool
  - Markdown editor
- **Templates:**
  - threat_model_template.md
  - data_classification_template.md

## 6. AI Support / Symbiotic Role
- **Roles:**
  - threat_model_summarizer
  - control_mapper
- **Prompt contracts:**
  - `plc.2.3.summarize_threat_model`
  - `plc.2.3.map_controls_to_risks`
- **Input context:**
  - doc: PLC/2_Architecture/2.3_Security_Model/security_model.md
  - data: PLC/2_Architecture/2.3_Security_Model/security_policies.json
- **Expected outputs (AI-assisted):**
  - doc: PLC/2_Architecture/2.3_Security_Model/security_model.md
