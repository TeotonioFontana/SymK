# SymK Review Queue

**Status:** Reversible recovery quarantine and future disposition input
**Owning stage:** SymK 2.8 — Corpus Consolidation
**Authority:** Evidence only; no file becomes canonical or executable by placement

This directory mixes potentially valuable historical artifacts, recovered source
trees, archives and hundreds of flattened Git objects. It must be processed through
manifest-based recovery and individual disposition. Never delete, promote, execute
or bulk-classify the queue as one object.

## Current handling rules

1. Preserve filenames and bytes until an item has a recorded identity and lineage.
2. Treat source-internal authority labels under `SYMK-KB-001`; they do not
   self-activate.
3. Inspect archives and Git objects through read-only recovery procedures.
4. Route code, documentation, governance and binary artifacts separately.
5. Move or promote an item only through a governed disposition with a reversible
   source-to-destination record.
6. Do not treat successful execution as semantic or governance authority.

The complete recovery and disposition work remains assigned to
[`2.8B — Review Queue Recovery, Quarantine and Disposition`](../SymK%202.x%20Evolution%20history/2.8/2.8B_Review_Queue_Recovery_Quarantine_and_Disposition.md).

## Known readable entry points

- `SYMK-CHARTER-001_The_SymK_Charter_v0.1.md` — historical charter evidence, not
  canonical authority.
- `1_Discovery.zip` and `project_init.zip` — classified recovery bundles; retain in
  reversible quarantine.
- `Discovery_Meta_Phase_Definition.md` — the Discovery template formerly misplaced
  as this directory's README.

The presence of `.symbiotic.yaml`, `pyproject.toml`, code, manuals or templates does
not make this directory a buildable or active project.
