# SymK M0 Archive Classification

**Status:** Recorded corpus-control evidence — awaiting project-steward confirmation of M0 completion  
**Date:** 20 August 2026  
**Scope:** Every archive present below the SymK repository root  
**Normative effect:** None  
**Governing rule:** An archive is evidence or a transport container; it does not outrank a live governed artifact by age, filename, completeness, or compression

## 1. Inspection result

Four archives are present. Every archive is a valid ZIP, was inspected recursively, contains no nested archive, contains no unsafe absolute or parent-traversal path, and remains preserved in place.

| Archive | SHA-256 | Entries | macOS metadata entries | Classification | Authoritative successor or comparison surface | Proposed disposition |
|---|---|---:|---:|---|---|---|
| `00_GOVERNANCE.zip` | `26d0dc6c6ffc729049067c6d4fb7571ecc1f374a91672f4152c049f73d4cd50b` | 100 | 48 | Historical governance checkpoint | Live `00_GOVERNANCE/` tree and its governed registries | Retain as ignored historical evidence; never use as current governance authority |
| `REVIEW_QUEUE/1_Discovery.zip` | `d6532bc951a246a44ec1fd524e878d60af1902503e64f760675dd28bfa9d63f9` | 59 | 31 | Recovery source bundle | Extracted and recovered material under `REVIEW_QUEUE/` | Retain in reversible quarantine pending lineage review |
| `REVIEW_QUEUE/project_init.zip` | `5b15a9c55583ca7622da47c7bcc593a689eded024fae4fe66ed8560460fb43a9` | 25 | 3 | Recovery source-code bundle | Recovered `project_init` and package-metadata material under `REVIEW_QUEUE/` | Retain in reversible quarantine pending lineage and code-family review |
| `SymK 2.x Evolution history/2.1.zip` | `e8ac2cc410af4a122b6099e46a5883a34de16d2387d3e4e07d91b2024d371799` | 46 | 23 | Historical pre-acceptance `2.1-dev.4` checkpoint | Live `SymK 2.x Evolution history/2.1/` package at `2.1-dev.5+` | Retain as ignored historical evidence; never use as current 2.1 authority |

Entry counts include directories. The detailed machine-readable evidence is preserved in `M0_CORPUS_MANIFEST_SUMMARY_2026-08-20.json`.

## 2. Authority boundary

Archive classification establishes provenance and precedence only. It does not:

- accept the semantics of any archived member;
- declare extracted files canonical;
- authorize deletion of an archive or duplicate;
- treat a recovered Git object as a governed document;
- replace lineage reconstruction; or
- permit a checkpoint to amend a later live decision.

If an archive contains material absent from the live tree, that material remains recoverable evidence. Its semantic disposition belongs to C1–C3 and the governing 2.x stage, not to M0.

## 3. Reversible handling

- No archive was deleted, moved, renamed, recompressed, or extracted into the live corpus.
- Existing ignored status is preserved.
- macOS metadata inside archives is recorded as container noise but is not removed.
- Exact archive hashes are preserved in the corpus manifest and M0 control checksum.

## 4. Result

The M0 archive-classification requirement is complete as an evidence and control activity. Project-steward confirmation is still required before the M0 gate is considered accepted and DR-011 may open.
