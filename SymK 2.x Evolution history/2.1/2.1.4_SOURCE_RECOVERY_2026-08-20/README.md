# SymK 2.1.4 Source-Recovery Bundle

**Status:** Preserved source evidence — immutable recovery set  
**Recovery date:** 20 August 2026  
**Source task:** `01a020b0-246a-7f83-bbaf-3b74fadf4a01`  
**Scope:** Selected 2.1.4 analytical, review, proposal, challenge, reconciliation, and acceptance messages only  
**Decision authority:** None by this bundle alone

## 1. Purpose

This bundle removes a material dependency on recoverable conversation history. It preserves the exact project reconstruction and 2.1.4 resumption account, followed by the substantive messages that led from Streams B–E through the first DR-012 proposal, the project-steward lane challenge, the Human–Scientific–Engineering reconciliation, the revised proposal, and the project-steward acceptance.

The prior repository registration compressed much of this material into 2.1.4B–G. Those files remain useful analytical summaries, but they are not substitutes for the source responses preserved here.

## 2. Source index

| File | Timestamp (UTC) | Message ID | Role | Source characters | Lineage meaning |
|---|---|---|---|---:|---|
| `00_PROJECT_RECONSTRUCTION_AND_2.1.4_RESUMPTION_RESPONSE.md` | 2026-08-20 19:41:32.054 | `msg_0088a89015520412016a875852dff087d1bcab207415b5e8b0` | Assistant | 8,609 | Exact project structure, roadmap, Stage 2.1 sequence, 2.1.4 status, Stream A findings, and resumption account |
| `01_STREAM_B_ORIGINAL_RESPONSE.md` | 2026-08-20 19:45:11.429 | `msg_0088a89015520412016a87591ef65c87d1a27e758fd6752ab3` | Assistant | 13,281 | Complete original Stream B response |
| `02_STREAM_C_ORIGINAL_RESPONSE.md` | 2026-08-20 19:48:08.682 | `msg_0088a89015520412016a8759cd1f1887d1a41cec07190c1ca4` | Assistant | 14,137 | Complete original Stream C response |
| `03_STREAM_D_ORIGINAL_TWO_LANE_RESPONSE.md` | 2026-08-20 19:50:20.639 | `msg_0088a89015520412016a875a4f7d4487d1834ac5f5951c5424` | Assistant | 15,956 | Original unreconciled two-lane Stream D response |
| `04_STREAM_E_ORIGINAL_RESPONSE.md` | 2026-08-20 19:51:39.363 | `msg_0088a89015520412016a875a9e869887d1b1c451661b9e6a7c` | Assistant | 16,455 | Complete original Stream E response |
| `05_FIRST_PROPOSED_DR-012_ORIGINAL_RESPONSE.md` | 2026-08-20 19:53:28.652 | `msg_0088a89015520412016a875af451f887d1997d6a17bc2bf03b` | Assistant | 28,316 | Complete first proposal; superseded before acceptance |
| `06_PROJECT_STEWARD_LANE_CHALLENGE.md` | 2026-08-20 19:58:23.711 | `msg_01a020c0-d5df-7d73-93c8-dbada2d996bd` | Project steward | 142 | Exact challenge that more than two lanes/views had been required |
| `07_LANE_CHALLENGE_ACKNOWLEDGMENT.md` | 2026-08-20 19:59:36.753 | `msg_0088a89015520412016a875c9ece2087d19f0420e7b8f4ac45` | Assistant | 3,301 | Immediate recognition of the defect and correction direction |
| `08_THREE_VIEW_RECONCILIATION_ORIGINAL_RESPONSE.md` | 2026-08-20 20:05:17.740 | `msg_0088a89015520412016a875dd609b087d19df1178f4a4078b7` | Assistant | 13,736 | Complete Human–Scientific–Engineering reconciliation |
| `09_REVISED_PROPOSED_DR-012_ORIGINAL_RESPONSE.md` | 2026-08-20 20:13:52.827 | `msg_0088a89015520412016a875faa1de087d1bb525dbea34da55b` | Assistant | 39,110 | Complete response containing the revised proposal |
| `10_PROJECT_STEWARD_ACCEPTANCE.md` | 2026-08-20 21:31:12.512 | `msg_01a02115-ceff-7062-8406-00e138188a66` | Project steward | 22 | Exact acceptance: `Accept SYMK-2X-DR-012` |

## 3. Recovery method and fidelity

The files were extracted from the local task event record by exact message identifier. The substantive message text is preserved without rewriting. A terminal line feed was normalized when each Markdown file was materialized. Character counts above describe the original message text before that file-level normalization.

Only the eleven governed 2.1.4 messages listed above were copied. System instructions, developer instructions, tool exchanges, hidden reasoning, unrelated conversation, and environment state were not imported into the SymK project.

The clean decision artifact `../2.1.4H_RECOVERED_FULL_REVISED_PROPOSED_DR-012_KNOWLEDGE_ENGINEERING_EPISTEMIC_CONDITIONS_AND_THREE_VIEW_REPRESENTATION.md` contains the proposal body that appears inside the writing block in source file 09. The independently retained project-steward attachment supplied the same body; only a terminal line feed was added on registration.

## 4. Authority and lineage rules

1. Files 00–09 are source and analytical evidence; they do not acquire decision authority merely by preservation.
2. File 03 and the first proposal in file 05 remain superseded proposal history.
3. File 06 is the authoritative project-steward challenge that caused the view-model correction.
4. File 09 supplies the exact revised proposal presented before acceptance.
5. File 10 supplies the project-steward acceptance evidence.
6. The separate corrective acceptance record identifies the clean recovered proposal body as the accepted object.
7. Existing 2.1.4B–G files and the original acceptance record remain preserved as the earlier compressed registration, not rewritten as though they had been exact transcripts.

## 5. Preservation rule

Treat this directory as immutable evidence. Any later annotation, interpretation, or correction must be written in a separate governed artifact and must not edit these recovered source files. Integrity is recorded in `SOURCE_MANIFEST_2026-08-20.sha256`.
