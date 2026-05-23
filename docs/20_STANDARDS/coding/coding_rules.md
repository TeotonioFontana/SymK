# Coding Rules — Symbiotic AI–Human Development (Compliance Template)

> **Mission**: Be unambiguous enough that a Python checker can evaluate compliance **deterministically** — and clear enough that humans can read it without yawning.

---

## 0) Metadata

- **Document**: `coding_rules.md`
- **Version**: 1.0.0
- **Effective date**: 2025-11-12
- **Status**: Stable (audience: humans & system architects; engineer/AI-facing doc to follow)
- **Owner**: {OWNER_OR_TEAM}
- **Applies to**: All Python code in this repository

---

## 1) Purpose & Audience

This document defines **normative** rules for Symbiotic AI–Human development. It is written for **humans and system architects** first. Once mature, we will derive an engineer/AI-oriented spec and training prompts from it.

We use RFC 2119 keywords: **MUST / MUST NOT / SHOULD / SHOULD NOT / MAY**.

---

## 2) Definitions

- **Symbiotic AI–Human Development**: The human architect defines purpose and constraints; the AI writes code. Each role respects the other's lane: the **human does not hand-edit production code**, and the **AI does not unilaterally change purpose**. Collaboration happens via explicit artifacts (e.g., PRs, RFCs, prompts).  
  Canonical roles: see [`AXIOM — Symbiotic Cooperation Roles`](../../00_AXIOMS/AXIOM_Symbiotic_Cooperation_Roles.md).
- **Boundary Function**: Public entrypoint that terminates a request/command path (e.g., CLI subcommand handler, API endpoint, job runner). Validates input and returns a standardized envelope.
- **Payload Dict**: Business result produced by a function, before envelope wrapping.
- **Top-Level Package**: Directory directly under repo root that has `__init__.py`.

---

## 3) Repository Baseline (Required Files)

**RB-001** — Each project **MUST** include a root-level `purpose.md` describing objective, scope, assumptions, and out-of-scope items.
- _Automatable check_: file exists at repo root; non-empty; first heading is `# Purpose`.

**RB-002** — A root-level `.symbiotic.yaml` **MUST** exist (see config schema in §10).  
**RB-003** — Packages intended for import **MUST** contain `__init__.py`.  
**RB-004** — Pre-commit and CI examples **SHOULD** be present (`.pre-commit-config.yaml`, `.github/workflows/*.yml`).  
**RB-005** — The shim `common/result_envelope.py` **SHOULD** exist (created by `sym-init`).

---

## 4) Tooling Baseline

- Python: {PYTHON_VERSION} (e.g., 3.11+)
- Packaging: `pyproject.toml` (PEP 621)
- Formatting: Black + isort
- Linting: ruff/pylint; mypy (optional)
- Static checks: `sym-check` (this spec)
- Tests: pytest + coverage ≥ {COVERAGE_TARGET}%

---

## 5) Rule Index (with IDs & Severities)

| ID       | Title                                         | Severity | Automatable |
|----------|-----------------------------------------------|----------|-------------|
| **R-100**| Purpose doc present (`purpose.md`)            | ERROR    | Yes         |
| **R-200**| Docstrings include Args/Returns/Raises        | WARNING  | Yes         |
| **R-210**| Args document ranges/allowed sets if relevant | WARNING  | Yes (heur.) |
| **R-300**| Static per-key types for dict literal returns | ERROR    | Yes         |
| **R-400**| Cross-package imports only from `common`      | ERROR    | Yes         |
| **R-500**| No A↔B function bounce in a module            | ERROR    | Yes         |
| **R-600**| Envelope on boundary functions (Option 2)     | ERROR    | Yes         |
| **R-610**| Boundary naming matches regex                 | WARNING  | Yes         |
| **R-620**| Single envelope import per module             | WARNING  | Yes         |

> The checker **MUST** fail on any **ERROR**; it **MAY** exit with code 1 on **WARNING**-only runs.

---

## 6) Rules (Normative)

### R-100 — Purpose document present
**MUST** have `purpose.md` at repo root with an H1 `# Purpose` and a brief scope statement.  
_Compliance_: path exists, non-empty, first non-blank line starts with `# Purpose`.

### R-200 — Docstrings must include Args/Returns/Raises
Every public function/class **MUST** have a docstring with **Args**, **Returns**, and **Raises** (where applicable).  
_Compliance_: heuristic text search; warning if missing.

### R-210 — Document ranges / allowed sets
When parameters have constraints (e.g., `min/max`, `allowed=[…]`), the docstring **SHOULD** mention them.  
_Compliance_: heuristic search for numbers, `min`, `max`, `allowed`, or examples; warning if absent.

### R-300 — Static per-key types for dict literal returns
If a function returns dict **literals**, each key’s value type **MUST** be consistent across returns in the module.  
_Compliance_: AST-only; ERROR on mixed types for the same key.

### R-400 — Cross-package imports only from `common`
Absolute imports into **other** top-level packages **MUST NOT** occur. The only permitted cross-package import is from **`common`**.  
_Compliance_: AST import scan; ERROR on violations.

### R-500 — No A↔B function bounce
Two different functions that call each other in the same module **MUST NOT** exist.  
_Compliance_: call-graph from AST; ERROR on mutual calls.

### R-600 — Envelope on boundary functions (Option 2)
Public/boundary functions **MUST** return a standardized envelope via `@enveloped(...)`.  
Private helpers (`_name`) **MAY** return plain values iff:
1) they are called **only** from enveloped boundaries, and  
2) any dict literal returns still follow **R-300**.  
_Compliance_: symbol scan + decorator presence on boundary functions.

### R-610 — Boundary naming matches regex
Boundary function names **SHOULD** match `boundary_name_regex` (default: `"(run|execute|perform|backup|restore|handle|process)"`).  
_Compliance_: warning when a public function looks like a boundary (by location/role) but doesn’t match the regex.

### R-620 — Single envelope import per module
A module that uses `@enveloped` **SHOULD** contain at most **one** import of the form:
`from <pkg_top>.result_envelope import enveloped`.  
_Compliance_: CST/regex check; warning on duplicates.

---

## 7) Envelope Contract (for R-600)

**Shape**:
```json
{
  "ok": true,
  "status": "success" | "invalid" | "error",
  "code": 200 | 422 | 500,
  "msg": "optional",
  "data": { },
  "errors": [ ],
  "exception": { "type": "...", "message": "...", "trace": "..." }?,
  "meta": { "fn": "pkg.mod.fn", "ts": "UTC-ISO", "duration_ms": 0, "args": { } }
}
```

**Decorator**: `@enveloped(schema=..., require_payload_dict=True, include_trace=False)`  
**Validation**: Validate inputs at boundaries only; helpers assume validated values.

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
    """Fetch a user and (optionally) their roles.

    Returns payload dict with stable per-key types:
      found (bool)  — Whether the user exists.
      user  (dict)  — Always a dict; empty when not found.
      roles (list)  — Always a list (possibly empty).
    """
    user = db.get_user(user_id, region=region)
    if not user:
        return { "found": False, "user": {}, "roles": [] }
    roles = db.get_roles(user.id) if include_roles else []
    return { "found": True, "user": {"id": user.id, "name": user.name, "email": user.email}, "roles": roles }
```

---

## 10) Configuration (`.symbiotic.yaml`)

**Keys** (all optional unless marked **required**):
```yaml
# required
pkg_top: "common"                    # where result_envelope shim lives
# recommended defaults
boundary_name_regex: "(run|execute|perform|backup|restore|handle|process)"
schema_mode: "hints"                 # or "minimal"
write_mode: "mirror"                 # or "inplace" (used by codemod)
out_dir: ".sym-mirror"
copy_others: true
exclude_dirs: ["tests", ".venv", "venv", "__pycache__"]
cross_pkg_allow: ["common"]          # checker enforces that only 'common' is allowed (R-400)
bounce_exempt: []                    # list of module names exempted from R-500 (rare)
report_json: "reports/symbiotic_report.json"
report_md:   "reports/symbiotic_report.md"
```

**Checker contract**:  
- **Exit code 2** on any ERROR rule violation.  
- **Exit code 1** if only WARNINGs.  
- **Exit code 0** if clean.

---

## 11) CI / Pre-commit

- Pre-commit runs: formatters + `sym-check` (warnings allowed, errors fail).  
- CI runs `sym-check` and uploads `reports/*` artifacts.

---

## 12) Waivers

- Use `docs/waivers/YYMMDD-<short>.md` with: context, rule(s), duration, owner, rollback plan.  
- Waivers expire; CI must show them in the report.

---

## 13) Migration (Adopting Incrementally)

1) `sym-init` at repo root (drops `.symbiotic.yaml` and the `common/result_envelope.py` shim).  
2) `sym-decorate --write-mode mirror --out-dir .sym-mirror` and review the diff.  
3) Merge selectively; add schemas; tighten `purpose.md`.  
4) Enable pre-commit and CI workflow.

---

## 14) Non-goals

- Deep type inference or whole-program analysis.  
- Enforcing business semantics beyond the documented schema.

---

## 15) Glossary

- **Boundary**: Public entrypoint requiring validation + envelope.  
- **Envelope**: Standard wrapper with status/code/errors/exception/meta around a payload dict.  
- **Bounce**: Mutual calls between two functions in the same module.  
- **Top-level package**: Importable directory at repo root containing `__init__.py`.

