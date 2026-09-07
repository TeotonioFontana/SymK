# SymK

SymK is a general framework and engineering discipline for responsible Knowledge
Engineering through governed cooperation among heterogeneous Intelligence Bearers.
Its principal operational realization is the creation of Domain Intelligence
Amplifiers: governed, domain-centred, knowledge-intensive systems that help produce
better answers to complex questions with controlled quality, time and total cost.

## Current governed state

- SymK 2.0 is the Stage-Accepted predecessor through DR-008.
- SymK 2.1 is active at `2.1-rc.1`; DR-009–DR-018 are Stage-Accepted.
- 2.1.10 Stream H is open through `SYMK-2X-EV-177`.
- Five coordinated v0.3 Markdown/PDF pairs are the active Foundation Paper Human-
  review objects after eight material Human findings were dispositioned.
- Complete Human reread, newcomer testing, publication acceptance and the separate
  2.1.10H decision remain pending.
- Later evolution stages remain closed.

Start with the [canonical governance entry point](00_GOVERNANCE/README.md) and the
[active 2.1 summary](SymK%202.x%20Evolution%20history/2.1/Summary.md).

## Repository map

| Path | Role | Authority boundary |
|---|---|---|
| `00_GOVERNANCE/` | Canonical orientation, constitutional work, registries, policies and accepted governance profiles | Each artifact declares its own status; placement alone does not create authority |
| `SymK 2.x Evolution history/` | Recoverable reasoning, evidence, decisions, dissent and stage controls | Explains authority and lineage; not the canonical corpus by itself |
| `02_CORE_MODEL/` | Proposed semantic-package scaffolding | No normative effect; owned by later 2.5 decisions |
| `Knowledge/` | Imported sources, curation, candidate canonical assets and supporting resources | Governed by `SYMK-KB-001`; source labels do not self-activate |
| `04_STANDARDS/` | Legacy standards-location lineage | No normative effect by placement |
| `07_EXPERIMENTS/` | Experimental material | Evidence only unless separately governed |
| `REVIEW_QUEUE/` | Reversible recovery quarantine and later 2.8 disposition input | Never treat the directory as one disposable or authoritative object |
| `SymK/` | Nested legacy PLC/devkit/archive material | Supporting or historical evidence, not the active repository root |
| `deployment/` | Release contract and deployment-control documentation | Controls artifact publication; does not confer semantic authority |

## Authority rules

Canonical location, constitutional force, semantic authority, external authority and
implementation fact are distinct. An imported file does not govern SymK because it
calls itself canonical, normative, mandatory, Stable or production-blocking. See
[`SYMK-KB-001`](00_GOVERNANCE/SYMK-KB-001_IMPORTED_SOURCE_AUTHORITY_BOUNDARY_v0.1.md).

Accepted objects remain immutable. Current status and decision-time wording for the
accepted governance profiles are explained in the
[current-status and lineage note](00_GOVERNANCE/99-Notes/GMC_Review/SYMK_ACCEPTED_GOVERNANCE_PROFILES_CURRENT_STATUS_AND_LINEAGE_2026-09-06.md).

## Repository hygiene

The ignored `SymK/.git/` directory is incomplete legacy repository metadata: it has
an object store and historical log but no `HEAD` or `config`. The outer repository is
the only working Git repository. Do not use, repair or delete the nested residue
without an explicit recovery or removal decision.

The release contract requires a clean governed worktree for publication. Untracked
research or supporting material must be deliberately admitted, ignored or moved
outside the repository before a release build.

## Validation

Before committing governed changes:

1. verify that no accepted-object hash changed;
2. check structured files and Markdown references;
3. inspect current-state labels against the 2.1 Summary and Evidence Register;
4. validate the release contract and produce a read-only release plan; and
5. keep unrelated or unclassified files out of the commit.

Historical evidence manifests may reference earlier bytes of mutable control files.
Acceptance manifests and accepted-object hashes are the integrity boundary for
accepted decisions. Future manifests follow
[`SYMK-MAN-001`](00_GOVERNANCE/SYMK-MAN-001_FUTURE_INTEGRITY_MANIFEST_CONVENTION_v0.1.md).
