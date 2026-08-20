# PropertyApplicabilityProfile

**Definition identifier:** `symk.property_applicability_profile`
**Status:** Proposed
**Normative effect:** None
**Candidate owner/layer:** The layer governing the declared bearer scope

## Human-semantic nucleus

### PAP-001 — Working definition

A **PropertyApplicabilityProfile** is a governed declaration relating a class of
eligible Bearers to referenced PropertyDefinitions under stated conditions and
profile-level constraints.

### PAP-002 — Reference, not duplication

A profile references PropertyDefinitions by stable identity and compatible
version. It does not redefine their meanings and does not contain the values of
runtime assertions.

### PAP-003 — Applicability and presence

Membership in a profile establishes eligibility or requirement according to
the declared applicability mode. It does not by itself assert that any
particular Bearer has a value. Permitted, required, conditional, prohibited, and
not-applicable states must remain distinguishable where used.

### PAP-004 — Bearer integrity

A profile must not collect properties merely because one application view
displays them together. Each member must have the profile's declared Bearer.
Properties of a file occurrence, repository binding, claim, person, or
organization belong to the profile of that bearer.

### PAP-005 — Extension

A narrower profile may adopt a parent profile, add properties, or strengthen
constraints within declared Domain and Scope. It must preserve parent meaning,
pin the adopted version, and declare additions, strengthenings, omissions, and
conflicts. Incompatible redefinition is a deviation or challenge, not silent
specialization.

### PAP-006 — Evolution

Changing membership or applicability is a governed profile revision whose
effects on derived profiles, existing assertions, validation, search, and
repository projections must be stated.

## Prohibited interpretations

- A profile is a class definition containing runtime fields.
- Profile membership means every instance has an assertion.
- A profile can redefine a referenced PropertyDefinition.
- Display colocation establishes a common Bearer.
