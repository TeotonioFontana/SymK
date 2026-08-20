# SymK M0 Corpus-Control Completion Proposal

**Status:** Proposed completion — awaiting project-steward review  
**Date:** 20 August 2026  
**Working baseline:** `2.1-dev.6`  
**Authority to perform work:** Project-steward instruction recorded as `SYMK-2X-EV-083`  
**Normative effect:** None beyond corpus inventory, preservation, classification, and status recording  
**Decision boundary:** Does not open 2.1.3 or create content for `SYMK-2X-DR-011`

## 1. Purpose

This record completes the M0 controls left pending at the 18 August pause checkpoint:

1. a repository-wide corpus manifest with every required field;
2. explicit classification of every archive;
3. separation of reversible recovery or quarantine from semantic disposition;
4. routing of every pause maturation observation; and
5. reproducible integrity evidence for project-steward review.

## 2. Deliverables

- `M0_CORPUS_MANIFEST_2026-08-20.csv` — one row per in-scope filesystem artifact.
- `M0_CORPUS_MANIFEST_SUMMARY_2026-08-20.json` — counts, controlled classifications, limitations, and archive inspection results.
- `M0_ARCHIVE_CLASSIFICATION_2026-08-20.md` — human-readable archive precedence and preservation record.
- `M0_CORPUS_CONTROL_MANIFEST_2026-08-20.sha256` — hashes of the completion package and synchronized control surfaces.

The CSV contains:

- path;
- artifact identifier or explicit `PATH:` inventory locator;
- identifier basis;
- family;
- format;
- provenance;
- Git state;
- authority status;
- maturity status;
- lineage parent;
- exact-duplicate group;
- encoding condition;
- proposed disposition;
- SHA-256; and
- size.

## 3. Corpus result

The deterministic inventory contains **992 files** below the repository root, excluding `.git` internals and self-referential M0 completion outputs.

| Git/filesystem state | Count |
|---|---:|
| Tracked | 938 |
| Untracked | 27 |
| Ignored | 25 |
| Filesystem-only path-encoding cases | 2 |

The two filesystem-only cases are the already-known filename-corrupted `SYMK-P-003` and `SYMK-P-007` source files. They are preserved without rename or inferred semantic disposition.

Other material results:

- 20 exact-byte duplicate groups covering 113 files;
- 449 recovered Git-object files retained in reversible quarantine;
- 106 other review-queue artifacts retained pending lineage and semantic review;
- 27 untracked Property/Document scaffold files retained as Proposed, noncanonical pause evidence;
- 17 local tool, operating-system, or temporary metadata artifacts marked only as reversible cleanup candidates;
- four classified archives;
- no archive containing another archive;
- no unsafe archive path.

## 4. Classification discipline

M0 uses conservative control vocabulary:

- `PATH:` identifiers are inventory locators, not governed identities.
- A declared status is reported but not validated merely by extraction.
- A `Canonical/` path is recorded as a canonical claim requiring registry verification.
- Exact duplication establishes byte identity only; it authorizes no deletion, merge, or lineage conclusion.
- `unresolved` lineage is an explicit C1–C3 assignment, not missing data hidden by the manifest.
- Proposed dispositions are preservation and routing actions, not semantic decisions.

## 5. Recovery versus semantic disposition

M0 authorizes only reversible control actions:

| Control action | M0 treatment | Later authority |
|---|---|---|
| Preserve recovered object | Recorded and retained | C1 lineage review |
| Mark technical noise | Reversible cleanup candidate only | Repository-maintenance approval |
| Detect exact duplicate | Duplicate group recorded | C2–C4 lineage and disposition |
| Classify archive | Historical/recovery role recorded | C1–C3 content review |
| Detect filename corruption | Preserve and route for recovery | C1 recovery with lineage |
| Accept, supersede, specialize, retire, or delete meaning | Prohibited at M0 | Applicable 2.x semantic/governance stage |

No artifact was moved, renamed, deleted, deduplicated, normalized, promoted, or demoted.

## 6. Maturation routing

Every observation in `MATURATION_NOTES_2.1.2_PAUSE.md` now has an explicit routing outcome:

- the Document/property observations are evidence for 2.1.4 and later package, specialization, grounding, and lowering work;
- their only 2.1.3 effect is the negative boundary that a Document, representation, asset, field, or stored assertion does not establish Knowledge merely by existing;
- the sshConnectivity observation supplies the same negative Knowledge/Representation boundary and concrete Projection evidence;
- none currently supplies sufficient cause to reopen DR-009 or DR-010; and
- no observation has been promoted beyond Observed status.

## 7. Integrity and limitations

The original `M0_EVIDENCE_MANIFEST_2026-08-18.sha256` remains an immutable closure record. Its expected mismatch for `MATURATION_NOTES_2.1.2_PAUSE.md` demonstrates the recorded post-pause additions; it is not repaired or overwritten.

The new completion checksum covers the generated manifest, archive classification, this completion proposal, maturation routing, and synchronized status surfaces.

This inventory does not claim that 992 semantic artifacts exist. The count includes review material, recovered Git objects, archives, projections, code, metadata, and control files so that no source class remains invisible.

## 8. M0 gate assessment

| M0 requirement | Result |
|---|---|
| DR-010 status synchronized | Complete at the 18 August checkpoint |
| Governed evidence snapshot | Complete at the 18 August checkpoint |
| Corpus manifest with required fields | Complete |
| Every archive explicitly classified | Complete |
| Recovery/quarantine separated from semantic disposition | Complete |
| Pause observations explicitly routed | Complete |
| Project-steward confirmation | Pending |

## 9. Approval proposition

The project steward is asked to confirm that:

1. the M0 corpus inventory is adequate as a control baseline;
2. archive classifications and authority precedence are correct;
3. reversible preservation remains separate from later semantic disposition; and
4. M0 may close, allowing 2.1.3 and analysis toward Proposed `SYMK-2X-DR-011` to open.

Approval would close M0 only. It would not accept `SYMK-2X-PLAN-002` as a whole, decide any Knowledge or Intelligence concept, revise a Foundation Paper, migrate the canonical corpus, or grant constitutional Ratification.
