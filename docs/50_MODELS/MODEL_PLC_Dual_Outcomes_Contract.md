# MODEL — PLC Dual Outcomes Contract
**Type:** MODEL  
**Scope:** SymK Meta PLC + all SymK projects  
**Change policy:** Versioned  
**Owner:** SymK Foundations

---

## Purpose

Define a minimal, stable contract so every PLC step produces:
1) a **Human outcome** (Markdown), and  
2) a **Machine outcome** (JSON),

that represent the same underlying truth.

This model is not a “how-to”. It defines **what must exist**.

---

## Required artifacts per PLC step

For each PLC step instance `STEP_ID`:

- Human outcome: `STEP_ID.human.md`
- Machine outcome: `STEP_ID.machine.json`

(Projects may keep folders per step/phase; the contract is about existence and structure.)

---

## Minimal JSON structure (required fields)

The machine outcome MUST contain at least:

- `meta`
  - `schema_version`
  - `project_id`
  - `plc_step_id`
  - `plc_step_version` (of the meta PLC step definition)
  - `generated_at` (ISO timestamp)
- `intent`
  - `summary` (one paragraph)
  - `hypotheses` (list; may be empty early)
- `inputs` (list of references; may be empty)
- `decisions` (list; may be empty)
- `outputs` (list of produced artifacts/claims; may be empty)
- `risks` (list; may be empty)
- `gates`
  - `entry` (what must be true to start)
  - `exit` (what must be true to advance)
- `trace`
  - `sources` (links/paths; may be empty)
  - `tools` (tools used; may be empty)

**Rule:** empty lists are allowed early; missing required fields are not.

---

## Consistency rule

The human outcome MUST be consistent with the machine outcome:
- the same intent
- the same decisions (at least summarized)
- the same exit gate claims

Human doc may add narrative and explanations; it may not contradict the JSON.

---

## Determinism rule

Generated artifacts derived from the machine outcome MUST be reproducible:
- same machine JSON + same tool version ⇒ identical outputs

---

## Versioning

Both outcomes must reference:
- the Meta PLC step version
- the schema version for the machine JSON

Breaking changes require explicit version increments.

---

## Status

This is a **minimal baseline**. Projects may extend fields, but must not remove or weaken the required ones.
