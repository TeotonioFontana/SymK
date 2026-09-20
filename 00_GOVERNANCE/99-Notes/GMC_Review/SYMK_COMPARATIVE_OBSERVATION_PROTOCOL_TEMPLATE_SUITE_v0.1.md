# SymK Comparative Observation Protocol — Minimum Template Suite v0.1

**Status:** Proposed inert templates; no execution or decision authority  
**Companion:** `SYMK_COMPARATIVE_OBSERVATION_AND_VOCABULARY_ADJUDICATION_PROTOCOL_v0.1.md`

## Template A — Baseline Freeze Record

```yaml
record_type: baseline_freeze
record_id:
created_at:
authority_ref:
purpose:
prior_observation_refs: []
prior_sample:
  population_claim:
  sample_method:
  subject_count:
  strata: []
  exclusions: []
prior_instrument:
  id:
  version:
  checksum:
  configuration_ref:
prior_vocabulary:
  id:
  version:
  checksum:
supported_claims: []
unsupported_claims: []
known_contradictions: []
unsupported_formats: []
privacy_losses: []
operational_dependencies: []
frozen_artifact_checksums: []
```

## Template B — Comparative Observation Plan

```yaml
record_type: comparative_observation_plan
plan_id:
status: proposed
question:
decision_purpose:
target_population:
sampling_frame:
sampling_method:
stratification_variables: []
inclusion_rules: []
exclusion_rules: []
hypotheses: []
credible_alternatives: []
falsifying_or_restricting_results: []
primary_comparisons: []
secondary_comparisons: []
missingness_policy:
unsupported_format_policy:
materiality_criteria: []
stopping_conditions: []
privacy_policy_refs: []
retention_policy_refs: []
permitted_uses: []
prohibited_uses: []
accepted_before_result_access_by:
accepted_at:
```

## Template C — Sample and Instrument Manifest

```yaml
record_type: sample_instrument_manifest
manifest_id:
sample_id:
sample_selection_checksum:
opaque_subject_count:
stratum_counts: {}
instrument_id:
instrument_version:
instrument_checksum:
rule_set_version:
vocabulary_version:
environment_ref:
known_failure_modes: []
validation_evidence_refs: []
operator_ref:
authorization_ref:
```

## Template D — Per-Observation Record

```yaml
record_type: property_observation
observation_id:
subject_ref:
observation_target:
source_layer:
source_property_or_region:
value_state: literal | protected_ref | not_retained | none
value_or_ref:
outcome:
acquisition_method:
instrument_version:
observed_at:
scope_ref:
evidence_refs: []
sensitivity:
value_handling:
observation_reliability:
candidate_interpretations: []
semantic_confidence:
epistemic_state: observed
limitations: []
contradiction_refs: []
```

## Template E — Divergence Entry

```yaml
record_type: divergence_entry
divergence_id:
affected_object_ref:
prior_result_ref:
new_result_ref:
primary_class:
secondary_qualifiers: []
stratum_distribution: {}
instrument_contribution:
source_population_contribution:
temporal_context_contribution:
missingness_effect:
credible_alternatives: []
consequence_if_accepted:
consequence_if_ignored:
confidence:
residual_uncertainty: []
proposed_disposition:
assessor_ref:
```

## Template F — Domain Adjudication Record

```yaml
record_type: domain_adjudication
adjudication_id:
divergence_refs: []
evidence_package_ref:
decision: accept | correct | more_evidence | competing | contextualize | suspend | unresolved | reject
rationale:
scope:
dissent: []
conflicts_of_interest: []
review_conditions: []
expires_at:
domain_reviewer_refs: []
authority_ref:
decided_at:
```

## Template G — Vocabulary Change Decision

```yaml
record_type: vocabulary_change_decision
decision_id:
prior_vocabulary_ref:
candidate_vocabulary_ref:
adjudication_refs: []
outcome: no_change | strengthen | weaken | alias_change | clarify | restrict | specialize | generalize | add | deprecate | mapping_change | suspend | unresolved | reject
affected_term_refs: []
identity_effect:
definition_effect:
hierarchy_effect:
mapping_effect:
compatibility_effect:
effective_scope:
effective_time:
rollback_conditions: []
decision_authority_ref:
decided_at:
migration_authorized: false
publication_authorized: false
```

## Template H — Protocol Deviation Record

```yaml
record_type: protocol_deviation
deviation_id:
plan_ref:
detected_at:
deviation:
reason:
result_visibility_at_time: none | partial | full
affected_observations: []
bias_risk:
containment:
permitted_continuation:
reviewer_ref:
authority_ref:
```

