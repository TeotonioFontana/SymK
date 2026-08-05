# STANDARD — SymK vs Project Content Placement
**Type:** STANDARD  
**Scope:** SymK repo structure and all SymK-driven projects  
**Change policy:** Versioned  
**Owner:** SymK Foundations

---

## Goal

Prevent structural drift by keeping **meta** assets in SymK and **instantiated outcomes** in projects.

---

## SymK repository contains (meta)

SymK MUST contain:
- Meta PLC definitions (templates for steps, tasks, expected outcomes, gates)
- Foundations templates (axioms, policies, standards, models)
- Build/validation tools for compiling PLC outcomes
- Contracts and schemas that are shared across projects
- Reusable templates for docs/configs (dotfiles, skeletons)

SymK MUST NOT contain:
- project-specific PLC outcomes (unless used as examples under archive)
- customer or tenant data
- generated project artifacts presented as canonical source

---

## Project repositories contain (instantiated outcomes)

A project MUST contain:
- its own PLC workspace (human + machine outcomes per step)
- its own project Foundations (purpose, concepts, enablers, domain vocab)
- its own runtime configs and deployment artifacts (as applicable)
- generated artifacts that are explicitly marked as derived (not canonical)

---

## Canonical vs derived

- Canonical sources: vocab/dictionaries, step machine outcomes, and authored human docs.
- Derived artifacts: generated schemas, generated MD, generated reports, exported ZIPs/PDFs.

Derived artifacts MUST NOT be edited manually.
(If you need different output, change the canonical input and rebuild.)

---

## Archive rule

Examples, experiments, and legacy material may exist under:
- `docs/90_ARCHIVE/`
- `artifacts/`

They must not be treated as canonical by tools.
