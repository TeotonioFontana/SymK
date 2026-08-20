The reconciliation confirms the defect and supplies the correction. The first DR-012 draft should be treated as superseded before review. No project files were changed.

## Reconciliation result

SymK needs three governed semantic views:

1. **Human View**
2. **Scientific View**
3. **Engineering View**

“Human-readable” and “machine-inspectable” are representational capabilities that can occur within all three views. They are not an exhaustive pair of semantic lanes.

Separately, the migration program retains three operating lanes:

- semantic and constitutional;
- corpus integrity;
- grounding and verification.

These structures are orthogonal.

## Corrected architecture

```text
                         Governed subject
                    and decision lineage
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
     Human View         Scientific View      Engineering View
 meaning and             inquiry and          specification and
 interpretation          evidential models    realization
          │                   │                   │
          └───────────────────┼───────────────────┘
                              ▼
                   governed alignments,
                  projections, and loss
```

Each view can contain:

- human-readable representations;
- formal or structured representations;
- machine-inspectable representations;
- and purpose-specific projections.

A scientific model may be expressed in prose, mathematics, code, or data. An engineering specification may be natural-language, diagrammatic, formal, or executable. The representation format does not determine the view.

## 1. Human View

The Human View carries what participants need to understand, interpret, question, and communicate:

- purpose;
- meaning;
- definitions and distinctions;
- narrative explanation;
- examples and counterexamples;
- Context and Scope;
- uncertainty and dissent;
- affected parties and consequences;
- interpretive alternatives;
- and known limits.

It is not merely an informal precursor to formalization. It carries meaning that may not be exhausted by a formal model.

It does not acquire authority through rhetorical clarity, publication quality, or institutional familiarity.

## 2. Scientific View

The Scientific View carries systematic inquiry into whether and under which conditions claims, models, attributions, or interventions are epistemically adequate.

It includes:

- research questions and hypotheses;
- observations and measurements;
- study or inquiry design;
- methods and instruments;
- data and sampling conditions;
- evidence and counterevidence;
- causal or explanatory models;
- statistical and logical models;
- uncertainty;
- reproducibility and robustness;
- competing explanations;
- empirical adequacy;
- limitations;
- and conditions of defeat.

The Scientific View is not limited to laboratory science. It covers systematic evidential inquiry appropriate to the Domain. Legal, historical, clinical, social, and engineering inquiries may use different methods and authorities.

It does not own:

- the complete meaning of a concept;
- normative or constitutional authority;
- authorization for operational use;
- or the engineering realization of its models.

A measurement model or benchmark is a scientific Representation or Projection. It does not become the measured subject.

## 3. Engineering View

The Engineering View carries the specifications and realizations through which selected governed meaning becomes operational:

- semantic and reference models;
- constraints and invariants;
- interfaces and contracts;
- schemas and formal profiles;
- algorithms and inference mechanisms;
- architecture;
- validation rules and test fixtures;
- runtime records;
- storage and retrieval structures;
- deployment conditions;
- observability;
- failure handling;
- migration;
- and operational projections.

Engineering correctness does not establish scientific adequacy, truth, responsible applicability, or constitutional legitimacy.

A schema can faithfully implement a defective scientific model. A technically correct system can operationalize a misunderstood human concept.

## Cross-view relationships

The views must exchange evidence without exchanging authority automatically.

### Human → Scientific

Human experience, interpretation, professional judgment, testimony, and observed problems may generate hypotheses and inquiry questions.

This transformation must not turn testimony into established evidence without an appropriate method.

### Scientific → Human

Scientific findings must be interpretable in relation to their methods, uncertainty, limitations, and intended claims.

A simplified explanation is a Projection and may introduce loss.

### Scientific → Engineering

Scientific models and empirical results may inform engineering requirements, thresholds, evaluation regimes, and constraints.

This movement does not authorize engineering use automatically.

### Engineering → Scientific

Tests, runtime observations, failures, performance, non-use, and consequences return evidence about models and assumptions.

Operational success does not prove universal validity.

### Human → Engineering

Human meaning, professional practice, values, usability needs, and responsibility boundaries inform specifications.

Natural-language ambiguity must be exposed rather than silently “resolved” by implementation.

### Engineering → Human

Engineering limitations, trade-offs, transformations, and consequences must return to human interpretation and governance.

The implementation cannot conceal material restrictions behind technical detail.

## Triangular consistency rule

Pairwise alignment is insufficient. A package may have:

- human and scientific agreement but an incorrect implementation;
- human and engineering agreement built on invalid evidence;
- scientific and engineering agreement that operationalizes the wrong human meaning.

Therefore, every material governed package must eventually demonstrate triangular coherence:

| Alignment | Principal question |
|---|---|
| Human ↔ Scientific | Does the inquiry investigate the intended meaning and problem? |
| Scientific ↔ Engineering | Does the realization preserve the tested model and its limitations? |
| Human ↔ Engineering | Does the operational system preserve the intended meaning and responsibility boundaries? |
| All three | Are meaning, evidence, and realization jointly coherent within the declared Scope? |

An artifact must not claim complete alignment merely because one pair agrees.

## Machine inspectability

Machine inspectability is now classified as a cross-view representational capability.

Examples:

- a structured concept record can project the Human View;
- a dataset or formal model can project the Scientific View;
- a schema, test suite, or API contract can project the Engineering View.

Consequently:

> A machine-semantic representation must identify which view’s claims it expresses, rather than being treated as one undifferentiated “machine lane.”

The term **machine-semantic lane** should be retired or used only as shorthand for machine-inspectable projections whose source view is explicit.

## Compatibility with DR-009

The three-view model preserves DR-009’s central commitments:

- the governed concept and decision lineage retain semantic authority;
- natural language does not own meaning by format;
- formal expressions may govern explicit formal claims within Scope;
- machine representations cannot redefine omitted meaning;
- mismatch and loss remain visible.

However, it materially clarifies DR-009’s description of exactly two lanes.

The proper lineage statement is:

> DR-009 established the minimum distinction between human-semantic interpretation and machine-inspectable expression. DR-012 refines that representation model by distinguishing Human, Scientific, and Engineering Views and treating human readability and machine inspectability as cross-view capabilities.

This clarification must be explicit in DR-012. It must not be presented as though DR-009 had already decided the three-view architecture.

## Compatibility with the three program lanes

The semantic views and operating lanes address different questions:

| Program lane | Uses the views how? |
|---|---|
| Semantic and constitutional | Governs meanings, decisions, authority, and view relationships |
| Corpus integrity | Preserves the artifacts, versions, provenance, and alignments of every view |
| Grounding and verification | Produces scientific and operational evidence that may challenge semantic and engineering artifacts |

A corpus artifact can represent any view. Grounding may generate Human, Scientific, or Engineering evidence. The semantic lane decides governing meaning but cannot fabricate evidential support.

## Additional stress tests

| Case | Result |
|---|---|
| Human definition is clear, but its scientific operationalization measures something else | Human–Scientific mismatch; construct validity remains unestablished |
| Scientific model is adequate, but the implementation changes a threshold | Scientific–Engineering strengthening or distortion |
| Engineering schema matches the prose but rests on unsupported claims | Human–Engineering alignment does not compensate for Scientific failure |
| Benchmark score is treated as the capability itself | Scientific Projection incorrectly acquires ontological identity |
| Runtime performance is treated as universal validation | Engineering evidence exceeds its tested Scope |
| Legal authority is rejected because it is not empirical science | Scientific View improperly claims authority over normative/legal standing |
| A scientific paper’s ontology becomes the production schema unchanged | Scientific Representation silently becomes Engineering authority |
| A generated explanation faithfully describes code but omits scientific uncertainty | Human–Engineering agreement conceals Scientific loss |
| A formal semantic model lacks implementation detail | Not a defect if its view and purpose are correctly bounded |
| An operational field has no human or scientific alignment | It is an engineering-local element, not automatically a governed semantic concept |

The three-view model passes these cases.

## Required DR-012 amendments

The first proposal’s references to “two semantic lanes” must be replaced with:

> **SymK shall govern three coordinated semantic views: Human, Scientific, and Engineering. These views express, investigate, and realize selected aspects of the same governed subject without becoming independent semantic authorities. Human readability, formal expression, and machine inspectability are representational capabilities that may occur within more than one view and shall not be used as the identities of the views themselves.**

The proposal must also add:

> **Every material scientific or engineering Representation shall identify the view whose claims it expresses, its governing source, purpose, method or transformation, Scope, authority, uncertainty, and known loss. Evidence discovered in one view may challenge another view or the governed concept, but it does not amend that concept automatically.**

And:

> **Material alignment requires examination of Human–Scientific, Scientific–Engineering, and Human–Engineering correspondence. Pairwise agreement does not establish complete alignment when the third view materially diverges.**

## Revised dispositions

| Candidate | Revised disposition |
|---|---|
| Human View | Governed semantic and interpretive view |
| Scientific View | Governed epistemic-inquiry and evidence view |
| Engineering View | Governed specification and realization view |
| Human readability | Cross-view representational capability |
| Machine inspectability | Cross-view representational capability |
| Formal expression | Cross-view representational capability with declared semantics |
| View alignment | Typed relationship with evidence, Scope, and loss |
| Triangular coherence | Required consolidated alignment test |
| Two-lane architecture as exhaustive model | Superseded by the three-view clarification |
| Three program lanes | Retained as an independent operating model |
| Runtime/implementation | Engineering realization or Projection, not a fourth semantic authority |

## Remaining dissent

The reconciliation preserves several open questions:

1. “Scientific” may be too narrow a label for philosophical, historical, legal, or qualitative epistemic inquiry.
2. The second view may ultimately need the name **Scientific/Evidential View** or **Epistemic Inquiry View**.
3. Some formal semantic models may bridge Scientific and Engineering Views rather than belong exclusively to either.
4. Machine-generated scientific and engineering artifacts require role-based attribution rather than classification by origin.
5. Some low-consequence packages may not require a complete Scientific View, but any omission must be explicit.
6. The final package anatomy and alignment-contract format remain assigned to 2.5.
7. Operational validation and conformance remain assigned to 2.7 and 2.9.

## Revised gate conclusion

The reconciliation passes.

The first DR-012 draft is superseded as an unreconciled proposal. A revised DR-012 may now proceed using:

- three semantic views;
- cross-view human readability and machine inspectability;
- triangular alignment;
- the independent three-lane program model;
- and explicit DR-009 lineage clarification.

The next step is to issue the complete **Revised Proposed DR-012** with these corrections incorporated throughout, rather than patching only its two-lane paragraph.
