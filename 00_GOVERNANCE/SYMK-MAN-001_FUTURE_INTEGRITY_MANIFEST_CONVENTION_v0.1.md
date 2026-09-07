# SYMK-MAN-001 — Future Integrity Manifest Convention

**Status:** Canonical repository-integrity convention
**Version:** 0.1
**Effective date:** 2026-09-06
**Scope:** Integrity manifests created after this convention takes effect
**Authority:** Project-steward authorization to repair the 2026-09-06 full
consistency inspection findings step by step
**Constitutional and semantic effect:** None

## 1. Purpose

This convention makes future integrity manifests independently interpretable and
repeatably verifiable. Historical manifests remain immutable evidence of their own
checkpoints and are not rewritten to comply retroactively.

## 2. Required manifest metadata

Every future manifest must declare, in comments within the manifest or in an exact
companion metadata file:

1. manifest identifier and version;
2. creation timestamp and responsible process or authority;
3. path base, normally `repository-root`;
4. source Git commit or tree when one exists;
5. included artifact class and explicit exclusions;
6. whether each target is immutable, checkpoint-frozen or expected to remain
   mutable;
7. hash algorithm and text/binary byte rule;
8. verification command and expected working directory; and
9. relationship to any acceptance, evidence, release or publication decision.

Metadata must not claim that a successful hash check establishes semantic validity,
acceptance, publication quality or execution authority.

## 3. Path and format rules

- Use repository-relative POSIX paths unless an external artifact requires an
  explicit immutable locator.
- Do not mix repository-root, manifest-directory and parent-directory bases in one
  manifest.
- Encode one digest and one exact path per data line.
- Preserve filename case, spaces and Unicode as stored.
- Reject missing targets during generation.
- Sort entries deterministically by exact path.
- Record the generator/tool version when a script creates the manifest.

The preferred digest is SHA-256 unless a stronger project or external requirement
applies.

## 4. Mutability classes

### Immutable accepted object

An acceptance manifest binds the exact bytes accepted. Later correction requires a
new version, digest and acceptance record. The accepted object is never silently
edited.

### Checkpoint snapshot

An evidence or stage manifest may bind mutable control paths at a named checkpoint.
Later current-byte mismatch is expected when those paths evolve, but the generating
commit or preserved object must make the checkpoint bytes recoverable.

### Release input

A release manifest binds the exact governed inputs to one build or publication. It
does not make those inputs accepted unless a separate decision says so.

## 5. Verification

Verification must distinguish at least:

- `MATCH` — current or recovered bytes equal the recorded digest;
- `MISMATCH_CURRENT` — the path exists but current bytes differ from the checkpoint;
- `MATCH_AT_COMMIT` — the recorded bytes verify at the declared Git commit;
- `MISSING` — neither the current path nor declared historical object can be found;
- `UNRESOLVED_BASE` — the path base cannot be determined; and
- `INVALID_ENTRY` — the manifest line cannot be interpreted.

For acceptance manifests, any state other than the required exact match is a release
and governance blocker until resolved. For historical mutable snapshots,
`MISMATCH_CURRENT` is not corruption when `MATCH_AT_COMMIT` succeeds.

## 6. Historical manifests

Historical manifests retain their original path conventions and bytes. A separate
index or verifier may document inferred bases, generating commits and current drift,
but it must not rewrite the historical manifest or imply corruption solely because a
mutable path later changed.

## 7. Non-effects

This convention does not:

- alter any existing digest or accepted object;
- retroactively invalidate a historical checkpoint;
- select a semantic or publication authority;
- replace the deployment release contract;
- authorize a build, release or stage transition; or
- prove content correctness from byte identity.
