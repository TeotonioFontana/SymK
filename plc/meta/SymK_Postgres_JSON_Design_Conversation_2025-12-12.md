# SymK — Postgres + JSON Structures (Conversation Record)

**Date:** 2025-12-12  
**Topic:** Choosing a DBMS for SymK’s JSON-based PLC artifacts, and drafting the initial Phase 1.1 intake pipeline (HTML form → JSON → Postgres).

---

## 1) Decision Summary

- **Keep MySQL** for conventional relational-oriented applications (existing systems, traditional OLTP, familiar workflows).
- **Use PostgreSQL** for **SymK**, because SymK is **deeply grounded in JSON semantics** and needs:
  - JSON-first storage (canonical technical interface between PLC phases)
  - strong transactional reliability
  - queryability + indexing inside JSON
  - governance fields (tenant, phase, type, status, audit metadata)

**Position:** This split is sound **if** SymK is treated as a bounded context (separate data ownership), with explicit integration seams (API/events) and no casual “cross-DB joins.”

---

## 2) Why PostgreSQL for SymK (Key Points)

### What Postgres solves well
- **Native JSONB** storage as a first-class type (not “JSON as text”).
- **Efficient querying and indexing** for JSON structures (e.g., GIN indexes) to support fast filtering/search of artifacts.
- **SaaS fundamentals**: ACID transactions, concurrency control, mature ecosystem.

### What Postgres does *not* solve (the real dragons)
- **Semantics alignment** across phases and across the “two parallel lines”:
  - human-friendly documents (Markdown/PDF/etc.)
  - technical JSON artifacts (phase interfaces)
- Semantic drift is mitigated by:
  - strict schemas + versioning
  - controlled vocabulary (where needed)
  - disciplined boundaries

---

## 3) Guardrails for a Two-DB World (MySQL + Postgres)

To keep this strategy clean, enforce:

1. **Hard data boundaries** (bounded contexts):  
   - SymK writes to **Postgres only**.  
   - Conventional apps write to **MySQL only**.

2. **Avoid dual writes** (MySQL + Postgres in the same request) whenever possible.  
   Prefer outbox/event-based sync if data must cross boundaries.

3. **One “system of record” per shared concept** (e.g., tenants/users):  
   Pick the authoritative DB/service, and reference by ID elsewhere.

4. **Consistent multi-tenant keys** (`tenant_id`) and consistent ID strategy (UUID/ULID).

5. **Cross-domain reporting** should be handled via read models/analytics, not runtime cross-DB joins.

---

## 4) SymK PLC Intake Need (Phase 1.1 Application Request)

At the earliest PLC stage, architects submit an **Application Request**:
- An **HTML form** is filled by architects.
- The result is produced as a **canonical JSON structure**.
- The JSON is **validated** (strict schema).
- The JSON is **stored** in Postgres as a SymK artifact.

This supports SymK’s two parallel lines:
- **Human line:** human-readable documents (Markdown → PDF/Docx, etc.)
- **Technical line:** JSON artifacts connecting PLC phases

The integration seam (future step): link JSON ↔ document by a shared `artifact_id`.

---

# 5) Deliverables Drafted in the Conversation

## 5.1 JSON Schema — PLC 1.1 Application Request (minimal but strict)

**File suggestion:** `schemas/symk_app_request_1_1.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://symk.local/schemas/app_request/1.1.0",
  "title": "SymK PLC 1.1 — Application Request",
  "type": "object",
  "additionalProperties": false,
  "required": ["artifact_type", "phase", "schema_version", "meta", "request"],
  "properties": {
    "artifact_type": { "const": "app_request" },
    "phase": { "const": "1.1" },
    "schema_version": { "const": "1.1.0" },

    "meta": {
      "type": "object",
      "additionalProperties": false,
      "required": ["tenant_id", "created_by", "created_at", "title"],
      "properties": {
        "tenant_id": { "type": "string", "minLength": 1, "maxLength": 64 },
        "created_by": { "type": "string", "minLength": 1, "maxLength": 128 },
        "created_at": { "type": "string", "format": "date-time" },
        "title": { "type": "string", "minLength": 3, "maxLength": 140 },
        "tags": {
          "type": "array",
          "items": { "type": "string", "minLength": 1, "maxLength": 32 },
          "uniqueItems": true,
          "maxItems": 30
        },
        "source": {
          "type": "string",
          "enum": ["manual_form", "import", "api", "automation"],
          "default": "manual_form"
        }
      }
    },

    "request": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "app_name",
        "domain",
        "problem",
        "target_users",
        "goals",
        "success_metrics",
        "constraints",
        "non_goals"
      ],
      "properties": {
        "app_name": { "type": "string", "minLength": 2, "maxLength": 80 },
        "domain": {
          "type": "string",
          "minLength": 2,
          "maxLength": 80,
          "description": "Business/functional domain (e.g., legal, finance, ops)"
        },
        "problem": {
          "type": "string",
          "minLength": 20,
          "maxLength": 2000,
          "description": "What pain exists today, for whom, and why it matters"
        },
        "target_users": {
          "type": "array",
          "minItems": 1,
          "maxItems": 20,
          "uniqueItems": true,
          "items": {
            "type": "string",
            "minLength": 2,
            "maxLength": 80
          }
        },
        "goals": {
          "type": "array",
          "minItems": 1,
          "maxItems": 20,
          "items": { "$ref": "#/$defs/goal" }
        },
        "success_metrics": {
          "type": "array",
          "minItems": 1,
          "maxItems": 20,
          "items": { "$ref": "#/$defs/metric" }
        },
        "constraints": {
          "type": "object",
          "additionalProperties": false,
          "required": ["time_horizon", "security", "compliance", "technical"],
          "properties": {
            "time_horizon": {
              "type": "object",
              "additionalProperties": false,
              "required": ["start_date", "target_date", "urgency"],
              "properties": {
                "start_date": { "type": "string", "format": "date" },
                "target_date": { "type": "string", "format": "date" },
                "urgency": { "type": "string", "enum": ["low", "medium", "high", "critical"] }
              }
            },
            "security": {
              "type": "array",
              "maxItems": 20,
              "items": { "type": "string", "minLength": 2, "maxLength": 120 }
            },
            "compliance": {
              "type": "array",
              "maxItems": 20,
              "items": { "type": "string", "minLength": 2, "maxLength": 80 }
            },
            "technical": {
              "type": "array",
              "maxItems": 30,
              "items": { "type": "string", "minLength": 2, "maxLength": 140 }
            }
          }
        },
        "assumptions": {
          "type": "array",
          "maxItems": 30,
          "items": { "type": "string", "minLength": 5, "maxLength": 200 }
        },
        "non_goals": {
          "type": "array",
          "minItems": 1,
          "maxItems": 30,
          "items": { "type": "string", "minLength": 2, "maxLength": 140 }
        },
        "references": {
          "type": "array",
          "maxItems": 30,
          "items": { "$ref": "#/$defs/reference" }
        }
      }
    }
  },

  "$defs": {
    "goal": {
      "type": "object",
      "additionalProperties": false,
      "required": ["statement", "priority"],
      "properties": {
        "statement": { "type": "string", "minLength": 5, "maxLength": 200 },
        "priority": { "type": "string", "enum": ["must", "should", "could"] }
      }
    },
    "metric": {
      "type": "object",
      "additionalProperties": false,
      "required": ["name", "target", "unit"],
      "properties": {
        "name": { "type": "string", "minLength": 2, "maxLength": 80 },
        "target": { "type": "number" },
        "unit": { "type": "string", "minLength": 1, "maxLength": 24 },
        "measurement_method": { "type": "string", "minLength": 0, "maxLength": 200 }
      }
    },
    "reference": {
      "type": "object",
      "additionalProperties": false,
      "required": ["type", "value"],
      "properties": {
        "type": { "type": "string", "enum": ["url", "doc_id", "ticket", "note"] },
        "value": { "type": "string", "minLength": 1, "maxLength": 500 }
      }
    }
  }
}
```

---

## 5.2 Postgres DDL — SymK Artifact Ledger (JSONB + governance columns + indexes)

```sql
CREATE EXTENSION IF NOT EXISTS pgcrypto;  -- gen_random_uuid()

CREATE SCHEMA IF NOT EXISTS symk;

CREATE TABLE IF NOT EXISTS symk.symk_artifact (
  artifact_id     uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id       text NOT NULL,
  artifact_type   text NOT NULL,
  phase           text NOT NULL,
  schema_version  text NOT NULL,
  status          text NOT NULL DEFAULT 'draft',
  title           text NOT NULL,
  tags            text[] NULL,

  created_by      text NOT NULL,
  created_at      timestamptz NOT NULL DEFAULT now(),
  updated_at      timestamptz NOT NULL DEFAULT now(),

  payload         jsonb NOT NULL,

  CONSTRAINT chk_payload_object CHECK (jsonb_typeof(payload) = 'object'),
  CONSTRAINT chk_status CHECK (status IN ('draft','submitted','approved','archived'))
);

CREATE INDEX IF NOT EXISTS idx_symk_artifact_tenant_phase_type_time
  ON symk.symk_artifact (tenant_id, phase, artifact_type, created_at DESC);

CREATE INDEX IF NOT EXISTS idx_symk_artifact_type_version
  ON symk.symk_artifact (artifact_type, schema_version);

CREATE INDEX IF NOT EXISTS idx_symk_artifact_payload_gin
  ON symk.symk_artifact USING gin (payload);

CREATE INDEX IF NOT EXISTS idx_symk_artifact_tags_gin
  ON symk.symk_artifact USING gin (tags);

CREATE OR REPLACE FUNCTION symk.set_updated_at()
RETURNS trigger AS $$
BEGIN
  NEW.updated_at = now();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_symk_artifact_updated_at ON symk.symk_artifact;
CREATE TRIGGER trg_symk_artifact_updated_at
BEFORE UPDATE ON symk.symk_artifact
FOR EACH ROW EXECUTE FUNCTION symk.set_updated_at();
```

---

## 5.3 Node.js API — Validate (AJV + JSON Schema) → Store (Postgres JSONB)

### Dependencies
```bash
npm i express pg ajv ajv-formats
```

### `server.js` (excerpt)
```js
import express from "express";
import pg from "pg";
import Ajv from "ajv";
import addFormats from "ajv-formats";
import fs from "node:fs";

const { Pool } = pg;
const app = express();
app.use(express.json({ limit: "1mb" }));

const pool = new Pool({
  connectionString: process.env.SYMK_PG_URL
});

const ajv = new Ajv({ allErrors: true, strict: true });
addFormats(ajv);

const schema = JSON.parse(
  fs.readFileSync("./schemas/symk_app_request_1_1.schema.json", "utf-8")
);
const validate = ajv.compile(schema);

function formatAjvErrors(errors = []) {
  return errors.map(e => ({
    path: e.instancePath || "/",
    keyword: e.keyword,
    message: e.message
  }));
}

function normalizeAppRequestPayload(body) {
  const safeTrim = v => (typeof v === "string" ? v.trim() : v);
  const b = structuredClone(body);

  if (b?.meta) {
    for (const k of ["tenant_id", "created_by", "title", "source"]) {
      if (k in b.meta) b.meta[k] = safeTrim(b.meta[k]);
    }
    if (Array.isArray(b.meta.tags)) b.meta.tags = b.meta.tags.map(safeTrim).filter(Boolean);
  }

  if (b?.request) {
    for (const k of ["app_name", "domain", "problem"]) {
      if (k in b.request) b.request[k] = safeTrim(b.request[k]);
    }
    const arrKeys = ["target_users", "assumptions", "non_goals"];
    for (const k of arrKeys) {
      if (Array.isArray(b.request[k])) b.request[k] = b.request[k].map(safeTrim).filter(Boolean);
    }
  }

  return b;
}

app.post("/symk/artifacts/app-request", async (req, res) => {
  const payload = normalizeAppRequestPayload(req.body);

  if (!validate(payload)) {
    return res.status(400).json({
      ok: false,
      msg: "Schema validation failed",
      errors: formatAjvErrors(validate.errors)
    });
  }

  const { artifact_type, phase, schema_version, meta } = payload;

  const q = `
    INSERT INTO symk.symk_artifact
      (tenant_id, artifact_type, phase, schema_version, title, tags, created_by, payload, status)
    VALUES
      ($1, $2, $3, $4, $5, $6, $7, $8::jsonb, 'submitted')
    RETURNING artifact_id, created_at
  `;

  try {
    const { rows } = await pool.query(q, [
      meta.tenant_id,
      artifact_type,
      phase,
      schema_version,
      meta.title,
      meta.tags ?? null,
      meta.created_by,
      JSON.stringify(payload)
    ]);

    return res.status(201).json({
      ok: true,
      msg: "Application request stored",
      artifact_id: rows[0].artifact_id,
      created_at: rows[0].created_at
    });
  } catch (err) {
    console.error(err);
    return res.status(500).json({
      ok: false,
      msg: "Database insert failed"
    });
  }
});

app.listen(process.env.PORT || 3000);
```

---

## 5.4 HTML Form — Architect Intake (build JSON + POST)

**File suggestion:** `public/app_request_1_1.html`

- Captures metadata + request details
- Produces canonical JSON (phase/type/version)
- Sends it to `/symk/artifacts/app-request`

*(Full HTML was drafted in the conversation; keep it as the canonical starter form.)*

---

# 6) Next Steps (when resuming)

### Immediate next improvement (recommended)
Add the integration seam between lines:
1. After insert, use `artifact_id` to:
   - auto-generate a Markdown doc stub (human line)
   - store `doc_path` / `doc_url` back in Postgres
2. Enforce that “document artifact” and “JSON artifact” share the same `artifact_id`.

### Semantic containment strategy
- Maintain a small controlled vocabulary (phase keys, core terms).
- Version schemas (already started with `schema_version: 1.1.0`).
- Add migration tooling later (don’t over-engineer day 1).

---

## 7) Notes

- This record captures the **design decision** and the **initial implementation artifacts** required to start SymK PLC intake with strong schema discipline.
- The approach is intentionally “minimal but strict” to prevent early semantic drift.
