# SymK v2 Migration Report

This migration **reorganizes files by placement only** (no content edits).

## Outputs
- `MIGRATION_MAP.csv` — old path → new path (one row per file)
- `UNCLASSIFIED_TODO.md` — items that were hard to classify confidently

## Summary
- Source ZIP: `SymK.zip`
- Files moved: **413**
- Files ignored: **54** (venv/IDE caches, node_modules, pycache, etc.)
- Unclassified docs: **92**

## Destination breakdown (files)
- `docs/`: 203
- `misc/`: 96
- `packages/`: 55
- `plc/`: 53
- `contracts/`: 6

## Key placement rules (high level)
- `Foundations/`, `Guidelines/`, `Marketing Strategies/` → `docs/` (typed buckets)
- `Contracts/` → `contracts/`
- `PLC_META/` → `plc/meta/`
- Root/embedded `*.zip` → `artifacts/`
- `auxiliary_tools/md2pdf/` → `packages/md2pdf/`
- `symbiotic_devkit/` → `packages/symbiotic_devkit/` (docs pulled into `docs/` where detected)

## Notes / caveats
- This is a **structure-only** reorg. Code imports/paths may require adjustments in a later step.
- Documents were classified via deterministic filename/folder heuristics into AXIOMS/POLICIES/STANDARDS/GUIDES/PLAYBOOKS/MODELS.
- Anything ambiguous was placed under `docs/30_GUIDES/_UNCLASSIFIED/` and listed in `UNCLASSIFIED_TODO.md`.
