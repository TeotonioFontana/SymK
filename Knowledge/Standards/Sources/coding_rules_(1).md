# Coding Rules — Symbiotic AI–Human Development (Compliance Template, v1.1.0)

> **Mission**: Specify rules that a Python checker can evaluate **deterministically**, while staying readable for humans and system architects. This document is **normative**; CI must enforce **ERROR** rules.

---

## 0) Metadata

- **Document**: `coding_rules.md`
- **Version**: 1.1.0
- **Effective date**: 2025-11-12
- **Status**: Stable for 1.x.x
- **Owner**: {OWNER_OR_TEAM}
- **Applies to**: All Python code in this repository

We use RFC 2119 keywords: **MUST / MUST NOT / SHOULD / SHOULD NOT / MAY**.

---

## 1) Purpose & Audience

Define guardrails for Symbiotic AI–Human development. Written for **humans and system architects**. Once mature, an engineer/AI-facing spec and prompts will be derived from this.

---

## 2) Definitions

- **Symbiotic AI–Human Development**: Human architect defines purpose/constraints; AI writes code. Human does not hand‑edit production code; AI does not unilaterally change purpose. Collaboration uses explicit artifacts (PRs, RFCs, prompts).
- **Boundary Function**: Public entrypoint that terminates a request/command path (CLI handler, API endpoint, job runner). Validates input and returns a standardized envelope.
- **Payload Dict**: Business result produced by a function, before envelope wrapping.
- **Top‑Level Package**: Directory at repo root with `__init__.py` used as import root.

---

## 3) Repository Baseline (Required Files)

**RB-001** — Root `purpose.md` describing objective, scope, assumptions, out‑of‑scope.  
_Compliance_: `/purpose.md` exists; first heading is `# Purpose`; non‑empty.

**RB-002** — Root **`.symbiotic.yaml`** exists (see §12).  
**RB-003** — Importable packages contain `__init__.py`.  
**RB-004** — `pyproject.toml` present (PEP 621).  
**RB-005** — `.pre-commit-config.yaml` and `.github/workflows/*.yml` **SHOULD** exist.  
**RB-006** — `common/result_envelope.py` shim **SHOULD** exist (via `sym-init`).  
**RB-007** — `.gitignore` and (optional) `.editorconfig` **SHOULD** exist.  
**RB-008** — `LICENSE` and `CODEOWNERS` **SHOULD** exist.

---

## 4) Python Standards & “Pythonic” Practices

- **Style**: Follow **PEP 8** (naming, whitespace, line length ~88–100), and **PEP 257** for docstrings (module/class/function).  
- **Typing**: Prefer precise type hints on public APIs: `dict[str, Any]` over bare `dict`. Use `typing` and `collections.abc` for protocols/iterables.  
- **Imports**: No wildcard imports; order = stdlib / third‑party / local; absolute imports preferred across packages; relative allowed within a package.  
- **Immutability**: No mutable default args. Avoid hidden mutation; return new values.  
- **Exceptions**: EAFP over LBYL for I/O; raise narrow exceptions; don’t swallow; map to envelope at boundaries.  
- **Logging**: Structured and contextual; log **once** per boundary; no `print()` in production paths.  
- **I/O & Paths**: Use `pathlib`; open files with explicit encodings (`utf-8`).  
- **Time & TZ**: Use UTC; store times as aware timestamps (ISO 8601).  
- **Concurrency**: Prefer `concurrent.futures`/`asyncio` when needed; guard shared state.  
- **Resources**: Use context managers (`with`) for files/locks/clients.  
- **Security**: Don’t log secrets/PII; fetch secrets from env/secret manager; validate inputs.  
- **Packaging**: Declare deps in `pyproject.toml`; prefer pinned or constrained versions; avoid unused deps.

> These are **recommended defaults**. Enforceable subsets appear in the Rule Index.

---

## 5) Rule Index (with IDs, Severities, Automatable)

| ID       | Title                                                | Severity | Automatable |
|----------|------------------------------------------------------|----------|-------------|
| **R-100**| Purpose doc present (`purpose.md`)                   | ERROR    | Yes         |
| **R-110**| `.symbiotic.yaml` present                            | ERROR    | Yes         |
| **R-120**| `pyproject.toml` present                             | ERROR    | Yes         |
| **R-130**| `__init__.py` in importable packages                 | ERROR    | Yes         |
| **R-140**| `.gitignore` present                                 | WARN     | Yes         |
| **R-150**| `.editorconfig` present                              | WARN     | Yes         |
| **R-200**| Docstrings include Args/Returns/Raises               | WARN     | Heuristic   |
| **R-210**| Args document ranges/allowed sets (when relevant)    | WARN     | Heuristic   |
| **R-220**| Module docstring present                             | WARN     | Heuristic   |
| **R-230**| No `TODO`/`FIXME` in production code                 | WARN     | Yes         |
| **R-240**| No mutable default arguments                         | ERROR    | Yes         |
| **R-250**| No wildcard imports                                  | ERROR    | Yes         |
| **R-260**| Import order: stdlib / third‑party / local           | WARN     | Heuristic   |
| **R-270**| Explicit file encodings (utf‑8)                      | WARN     | Heuristic   |
| **R-280**| UTC timestamps (ISO 8601) in meta                    | ERROR    | Yes         |
| **R-290**| No `print()` in non‑test modules                     | WARN     | Yes         |
| **R-300**| Static per‑key types for dict literal returns        | ERROR    | Yes         |
| **R-310**| No wildcard `from x import *`                        | ERROR    | Yes         |
| **R-320**| No `eval`/`exec` in production                       | ERROR    | Yes         |
| **R-330**| Secrets not logged (basic grep)                      | WARN     | Heuristic   |
| **R-340**| Dependency drift (unused deps)                       | WARN     | Heuristic   |
| **R-400**| Cross‑package imports only from `common`             | ERROR    | Yes         |
| **R-410**| Relative imports only within the same package        | WARN     | Yes         |
| **R-500**| No A↔B function bounce                               | ERROR    | Yes         |
| **R-550**| Exceptions mapped to triad at boundaries             | ERROR    | Yes         |
| **R-560**| Single logging at boundary (no duplicate step logs)  | WARN     | Heuristic   |
| **R-600**| Envelope on boundary functions (Option 2)            | ERROR    | Yes         |
| **R-610**| Boundary naming matches regex                        | WARN     | Yes         |
| **R-620**| Single envelope import per module                    | WARN     | Yes         |
| **R-630**| Envelope validates against schema (if configured)    | WARN     | Yes         |
| **R-700**| Tests present for boundaries                         | WARN     | Yes         |
| **R-710**| Coverage ≥ {COVERAGE_TARGET}%                      | WARN     | Yes         |
| **R-720**| Deterministic tests (seeded randomness)              | WARN     | Heuristic   |
| **R-800**| CI fails on ERROR, warns on WARN                     | ERROR    | Yes         |
| **R-810**| Pre‑commit configured and active                     | WARN     | Yes         |
| **R-900**| Waivers documented and time‑boxed                    | WARN     | Yes         |
| **R-910**| Deprecations documented (SemVer)                     | WARN     | Heuristic   |
| **R-920**| CHANGELOG updated                                    | WARN     | Heuristic   |
| **R-930**| Codegen headers on generated files                   | WARN     | Heuristic   |
| **R-940**| License headers where required                       | WARN     | Heuristic   |
| **R-950**| Security scanning run (SAST/Lint)                    | WARN     | Yes         |

> **Exit codes**: 2 on any **ERROR** rule; 1 if only **WARN**; 0 clean.

---

## 6) Rules (Normative Details)

### R-100 — Purpose document present
`/purpose.md` **MUST** exist with H1 `# Purpose` and scope summary.

### R-110 — `.symbiotic.yaml` present
Root file **MUST** exist; see §12 for keys.

### R-120 — `pyproject.toml` present
PEP 621 metadata and dependencies declared.

### R-130 — `__init__.py` in importable packages
Any importable directory **MUST** include `__init__.py`.

### R-140 — `.gitignore` present
Repo **SHOULD** include `.gitignore` with Python and tool patterns.

### R-150 — `.editorconfig` present
Editor defaults **SHOULD** be provided (utf-8, LF, 2/4 spaces).

### R-200 — Docstrings include Args/Returns/Raises
Public functions/classes **MUST** have docstrings with Args/Returns/Raises.

### R-210 — Document ranges/allowed sets
When constraints exist (`min/max`, `allowed=[…]`), docstrings **SHOULD** mention them.

### R-220 — Module docstring present
Each module **SHOULD** state purpose and key contracts.

### R-230 — No `TODO`/`FIXME` in production
Warnings emitted for markers outside tests/examples.

### R-240 — No mutable default arguments
Errors on `def f(x=[])`/`{}`. Use `None` sentinel.

### R-250 — No wildcard imports
Prohibit `import *` and `from x import *` (see R‑310 for clarity).

### R-260 — Import order
Recommended order: stdlib / third‑party / local. Heuristic warning only.

### R-270 — Explicit encodings
File i/o **SHOULD** specify `encoding="utf-8"`.

### R-280 — UTC timestamps
`meta.ts` **MUST** be ISO‑8601 UTC.

### R-290 — No `print()` in non‑test modules
Use logging. Tests/examples are exempt.

### R-300 — Static per‑key types for dict literal returns
Dict literal returns **MUST** keep per‑key types stable within a module.

### R-310 — No wildcard `from x import *`
(clarifies R‑250) Enforced explicitly.

### R-320 — No `eval`/`exec` in production
Prohibited unless a security waiver is granted.

### R-330 — Secrets not logged
Heuristic grep for common secret key names; warning if matched.

### R-340 — Dependency drift
Heuristic: warn on imports not present in `pyproject.toml` and vice‑versa.

### R-400 — Cross‑package imports only from `common`
Absolute imports into other top‑level packages **MUST NOT** occur unless `common`.

### R-410 — Relative imports only within the same package
Warn if relative import crosses package boundaries.

### R-500 — No A↔B function bounce
Mutual calls indicate tangled responsibilities.

### R-550 — Exceptions mapped to triad at boundaries
Boundary layers **MUST** translate exceptions into `invalid` (422) or `error` (500).

### R-560 — Single logging at boundary
Avoid duplicate step logs for the same event.

### R-600 — Envelope on boundary functions (Option 2)
Boundary functions **MUST** return the standardized envelope via `@enveloped(...)`.  
Private helpers (`_name`) **MAY** return plain values iff:
1) Called **only** from boundaries; and  
2) Dict‑literal returns still obey **R‑300**.

### R-610 — Boundary naming matches regex
Names **SHOULD** match `"(run|execute|perform|backup|restore|handle|process)"`.

### R-620 — Single envelope import per module
At most one: `from <pkg_top>.result_envelope import enveloped`.

### R-630 — Envelope validates against schema
If `envelope.schema.json` is present, checker **SHOULD** validate envelopes for boundary tests.

### R-700 — Tests present for boundaries
Boundary happy/invalid/error paths covered.

### R-710 — Coverage ≥ {COVERAGE_TARGET}%
Warn when below target.

### R-720 — Deterministic tests
Seed randomness where relevant; avoid time flakiness.

### R-800 — CI fails on ERROR, warns on WARN
Mandatory gating.

### R-810 — Pre‑commit configured and active
Formatters + `sym-check` included.

### R-900 — Waivers documented and time‑boxed
Waivers live in `docs/waivers/YYMMDD-<short>.md`.

### R-910 — Deprecations documented (SemVer)
Mark deprecated APIs; include migration and removal version.

### R-920 — CHANGELOG updated
Keep a human‑readable change log per release.

### R-930 — Codegen headers on generated files
Generated files **SHOULD** include a header identifying generator, version, and “do not edit”.

### R-940 — License headers where required
Apply per‑project policy.

### R-950 — Security scanning
Run SAST/linters; capture in CI logs.

---

## 7) Envelope Contract (for R‑600)

**Status triad**: `success | invalid | error`  
**Codes**: `200 | 422 | 500`

**Shape**:
```json
{
  "ok": true,
  "status": "success",
  "code": 200,
  "msg": "optional",
  "data": {},
  "errors": [],
  "exception": { "type": "...", "message": "...", "trace": "..." },
  "meta": { "fn": "pkg.mod.fn", "ts": "UTC-ISO", "duration_ms": 0, "args": {} },
  "version": "optional",
  "run_id": "optional",
  "partial": false
}
```

**Notes**
- Optional fields (`version`, `run_id`, `partial`) **MAY** appear; omit if unused.
- Canonical key: `exception.trace` (not `traceback`).
- `meta.ts` **MUST** be ISO‑8601 UTC.

---

## 8) Docstring Template (Recommended)

```python
def fn(arg1: str, limit: int = 100) -> dict:
    """Short, imperative summary.

    Args:
      arg1: What it is. Allowed: non-empty.
      limit: Max items. Range: 1..1000 (default 100).

    Returns:
      Dict payload with stable per-key types.

    Raises:
      ValueError: If inputs violate constraints.
    """
```

---

## 9) Boundary Example (Recommended)

```python
from common.result_envelope import enveloped

@enveloped(schema={
    "user_id":       {"type": int,  "min": 1},
    "include_roles": {"type": bool, "required": False, "default": False},
    "region":        {"type": str,  "required": False, "default": "us-east-1",
                      "allowed": ["us-east-1", "us-east-2", "eu-west-1"]},
})
def run_get_user(user_id: int, include_roles: bool = False, region: str = "us-east-1") -> dict:
    """Fetch a user and (optionally) roles with stable payload types.

    Returns payload dict:
      found (bool)  — Whether the user exists.
      user  (dict)  — Always a dict; empty when not found.
      roles (list)  — Always a list (possibly empty).
    """
    user = db.get_user(user_id, region=region)
    if not user:
        return { "found": False, "user": {}, "roles": [] }
    roles = db.get_roles(user.id) if include_roles else []
    return { "found": True, "user": { "id": user.id, "name": user.name, "email": user.email }, "roles": roles }
```

---

## 10) Return Dict Scaffold (Copy‑paste)

**Mandatory keys**:
```json
{
  "ok": true,
  "status": "success | invalid | error",
  "code": 200,
  "data": {},
  "errors": [],
  "meta": { "fn": "pkg.mod.fn", "ts": "UTC-ISO", "duration_ms": 0, "args": {} }
}
```

**Optional keys (examples)**:
```json
{
  "msg": "optional human message",
  "exception": { "type": "...", "message": "...", "trace": "..." },
  "version": "1.0.0",
  "run_id": "2025-11-12T18:00:00Z-abc123",
  "partial": false
}
```

---

## 11) Logging & Error Mapping (Patterns)

- **Map** exceptions at boundaries to the triad:
  - `invalid` (422): input/schema/config violations
  - `error`   (500): unexpected failures (IO/DB/Network/etc.)
- **Log** once per boundary with: `fn`, key params, correlation id, and summary outcome.
- **Never log secrets/PII**. Mask or drop.

---

## 12) Configuration (`.symbiotic.yaml`)

```yaml
spec_version: "1.0.0"              # checker can warn on mismatches
pkg_top: "common"                  # REQUIRED (envelope shim)
boundary_name_regex: "(run|execute|perform|backup|restore|handle|process)"
schema_mode: "hints"               # or "minimal"
write_mode: "mirror"               # or "inplace" (for codemod)
out_dir: ".sym-mirror"
copy_others: true
exclude_dirs: ["tests", ".venv", "venv", "__pycache__"]
cross_pkg_allow: ["common"]        # R-400 only 'common'
bounce_exempt: []                  # rare exemptions to R-500
report_json: "reports/symbiotic_report.json"
report_md:   "reports/symbiotic_report.md"
```

---

## 13) CI & Pre‑commit

- **Pre‑commit**: formatters + `sym-check` locally.  
- **CI**: install deps; run `sym-check`; upload `reports/*` artifacts; fail on **ERROR** rules.

---

## 14) Waivers & Deprecations

- Waivers: time‑boxed notes in `docs/waivers/YYMMDD-<short>.md` with context, owner, rollback.  
- Deprecations: mark API, provide migration, set removal version (SemVer).

---

## 15) Non‑Goals

- Deep whole‑program type inference.  
- Enforcing business semantics beyond declared schemas.

---

## 16) Glossary

- **Boundary** — Public entrypoint requiring validation + envelope.  
- **Envelope** — Standard wrapper with status/code/errors/exception/meta around a payload dict.  
- **Bounce** — Mutual calls between two functions in a module.  
- **Top‑level package** — Importable directory at repo root containing `__init__.py`.

