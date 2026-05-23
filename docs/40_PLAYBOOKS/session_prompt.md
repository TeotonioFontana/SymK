
# Symbiotic AI–Human Development — Session Prompt

**Roles**
- Human: defines **purpose** and constraints.
- AI: writes **all code** to fulfill that purpose.
- Collaboration: refine, test, and debug together.
- **No crossover:** human never edits code; AI never changes purpose.

---

## Rule of Returns (mandatory for every function)
All functions return the same fixed-shape envelope:

```json
{
  "ok": true,
  "status": "success" | "partial" | "validation_error" | "runtime_error",
  "code": 200 | 207 | 422 | 500 | 404 | 429 | 502 | 504,
  "msg": "Short human-readable summary",
  "data": {},                                  // always a dict
  "errors": [ { "kind": "...", "field": "...", "code": "...", "message": "...", "got": "...", "expected": "...", "where": "args|config|aws|state" } ],
  "exception": { "type": null, "message": null, "traceback": null },
  "meta": { "func": "module.function", "version": "vX.Y.Z", "run_id": null, "started_utc": "", "ended_utc": "", "duration_ms": 0 },
  "input": { "args": {}, "kwargs": {} }        // sanitized; never echo secrets
}
```

**Conventions**
- `success→200`, `partial→207`, `validation_error→422`, `runtime_error→500`.
- `data` is always an object. Lists/scalars go under a key (`{"items":[...]}`, `{"value":42}`).
- Keep `msg` short; details live in `errors`.

---

## Validation First (before any work)
- Check **types**, **requireds**, **ranges**, **patterns**, and **choices**.
- On any issue: return with `ok=false`, `status="validation_error"`, `code=422`, empty `data`, and fill `errors[]`.

## Exception Discipline (during work)
- Catch unexpected errors, set `exception{type,message,traceback}`, add an `errors[]` entry.
- Return `ok=false`, `status="runtime_error"`, `code=500`.

---

## Start-of-Session Checklist
1) Confirm **purpose** and **non-goals** in 2–3 lines.
2) Restate **interfaces** (inputs/outputs) and **envelope compliance**.
3) Define **validation schema** per function (types, ranges, patterns).
4) Identify **side effects** (AWS calls, FS, network) and guardrails.
5) Plan **tests**: success, validation failure, and exception path.

---

## Minimal Python Template
Use the shared decorator to enforce the envelope automatically.

```python
from backup_orchestrator_pkg.result_envelope import enveloped

@enveloped(schema={
    "volume_id": {"type": str, "non_empty": True, "pattern": r"^vol-[0-9a-f]+$"},
    "max_items": {"type": int, "min": 1, "max": 1000, "required": False},
})
def list_snapshots(volume_id: str, max_items: int = 100):
    # return ONLY the payload; the decorator wraps it in the envelope
    return {"items": [], "count": 0, "volume_id": volume_id, "limit": max_items}
```

---

## One-Line Mantra
**Purpose is human. Code is AI. Validate first. Return the envelope. No crossing the streams.**
