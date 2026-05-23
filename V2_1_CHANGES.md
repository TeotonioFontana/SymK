# SymK v2.1 — Placement Fixes

This is a **structure-only** refinement over SymK v2 (no content edits).

## What was fixed (and why)

1) **Human–AI roles are now canonical**
- Moved: `docs/30_GUIDES/_UNCLASSIFIED/Symbiotic_Development_Protocol_v1.0-alpha.md`
- To: `docs/00_AXIOMS/AXIOM_Symbiotic_Cooperation_Roles.md`

Reason: the Human/AI duty split is a **foundational axiom**, not a loose guide.

2) **Research references are guides (not unclassified)**
- Moved to: `docs/30_GUIDES/human_ai/`

3) **Symbiotic config belongs to templates**
- Moved: `symbiotic.yaml` → `templates/dotfiles/.symbiotic.yaml`

Reason: it is a **dotfile template** (intended to be copied to app repo roots).

4) **PLC manuals are not PLC meta**
- Moved: `plc/meta/User_Manuals/*` → `plc/manuals/`
- Moved: `plc/meta/How_to_Run_PLC_1_Discovery.md` → `plc/manuals/`

Reason: `plc/meta/` is the PLC source catalog; manuals are operational reading.

5) **Generated ZIP artifacts are not source**
- Moved: `plc/meta/1_Discovery.zip` → `artifacts/plc/1_Discovery.zip`

6) **macOS `._*` files are quarantined**
- Moved into `artifacts/_macos/` to keep the repo clean.

## Output
- `V2_1_MOVE_MAP.csv` lists all v2 → v2.1 moves.
