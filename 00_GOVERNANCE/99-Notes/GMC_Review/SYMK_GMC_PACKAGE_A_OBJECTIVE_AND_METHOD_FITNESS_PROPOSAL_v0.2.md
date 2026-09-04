# SymK GMC Package A — Objective and Method Fitness Proposal v0.2

**Status:** Corrected proposal for project-steward review — not accepted
**Date:** 4 September 2026
**Supersedes as current proposal:**
`SYMK_GMC_PACKAGE_A_OBJECTIVE_AND_METHOD_FITNESS_PROPOSAL_v0.1.md`
**Correction authority:** Project-steward request to improve Package A after the
SPServices uncontrolled-start prevention test exposed an execution-release gap
**Members:** GMC-001 and GMC-002, with bounded interfaces to GMC-009–012 and GMC-014
**Depends on:** Stage-Accepted DR-014 and DR-016 distinctions, the GMC disposition
register, the cooperating-packages evaluation and provisional active `SYMK-GP-001`
**Normative effect:** None unless separately accepted through competent procedure

## 1. Correction result

Package A v0.1 could identify a weak objective and an unjustified method, but it did
not by itself prevent execution from beginning. It separated plan, method and
execution conceptually without requiring a distinct execution-release decision.

Version 0.2 corrects that gap through three independent gates:

1. **Objective Acceptance** — accepts the outcome-facing objective as a valid basis
   for method consideration;
2. **Method Selection** — selects a method version as a bounded, evidence-bearing
   route to that objective; and
3. **Execution Release** — authorizes specified actors or tools to perform specified
   actions within an explicit envelope.

No earlier gate entails a later gate. Approval of a plan, roadmap, proposal,
objective or method does not authorize execution.

## 2. Decision requested

Accept, correct or reject a project-method governance profile that:

- requires an externally meaningful and assessable outcome-facing objective;
- governs the selected method as a separate, challengeable method hypothesis;
- prohibits material execution before independent Objective Acceptance, Method
  Selection and Execution Release gates pass;
- scales the execution-release envelope and evidence burden to consequence,
  sensitivity, reversibility and external effect;
- permits useful autonomy inside an accepted envelope rather than requiring
  approval for every step; and
- stops or escalates only when authority is absent, expired, materially ambiguous or
  exceeded, or when a declared material stop condition occurs.

Acceptance would make this a provisional SymK project-method governance profile and
authorize later operational template work and competent 2.4 classification. It
would not select a real method, open a closed evolution stage, create constitutional
force or accept GMC-003–014.

## 3. Problem addressed

A technically controlled project may still be strategically uncontrolled when it:

- starts from an objective expressed mainly as its own stages or deliverables;
- assumes a method without comparing relevant alternatives;
- treats plan approval or a conversational continuation instruction as authority for
  every downstream action;
- accumulates implementation and assurance evidence while outcome-relevant learning
  remains weak;
- advances from proposal to construction, external access or operation without a
  separately bounded release; or
- continues after the objective, method, risk or permitted-effect boundary changes
  materially.

Conversely, preventing every action until a new micro-approval is issued creates
delay, ceremonial review and false safety. Package A must therefore prevent
unauthorized start while preserving bounded autonomy for reversible, low-consequence
work.

## 4. Compatibility boundary

This corrected proposal operationalizes, without reopening, accepted distinctions
among:

- target, objective, expectation, intended outcome and actual outcome;
- recommendation, proposal, plan, instruction, decision and Authorization;
- assessment, method selection, execution, action and consequence;
- Authority capacity, an actual authorization occurrence and implementation fact;
- output, quality, cost, Value, feedback and Learning; and
- project methods versus universal SymK concepts.

It proposes no new Foundational concept. Its objective, method-fitness and
execution-release structures are project-governance profiles subject to later
classification.

## 5. Working terms

| Term | Working meaning in v0.2 | Must remain distinct from |
| --- | --- | --- |
| outcome-facing objective | governed intended externally meaningful condition or capability with affected parties, horizon and assessment basis | plan, deliverable, method, metric, actual outcome or Value |
| internal deliverable | artifact, capability, state or checkpoint produced inside the plan | the external reason it matters |
| method | organized approach, procedure or pattern considered or selected to contribute to an objective | objective, implementation, result or universal rule |
| method hypothesis | scoped claim that a method is expected to contribute under declared conditions | guarantee, causal proof, selection or execution authority |
| method fitness | multidimensional assessment relation among method, objective, Context, alternatives, evidence and consequences | popularity, compliance, completion, score or Value |
| Objective Acceptance | authorized decision that an objective version is adequate to govern method consideration | objective truth, method selection or execution release |
| Method Selection | authorized decision selecting a method version and its conditions relative to an accepted objective | fitness assessment, implementation or execution release |
| Execution Release | time- and scope-bounded Authorization for identified actors or tools to perform identified operations and effects | plan approval, method selection, actual execution or success |
| execution envelope | complete boundary of permitted subjects, actions, resources, data, environments, effects, budgets, time and stop conditions | broad intent or unlimited discretion |
| review trigger | condition requiring reassessment or escalation | automatic pause, pivot, rejection or failure |

These are proposal-local working terms and do not amend accepted SymK vocabulary.

## 6. Outcome-facing objective rule

A material plan must answer:

> **What externally meaningful condition, capability or decision quality should be
> different for identified beneficiaries or affected subjects if this work
> succeeds?**

“External” means outside the internal anatomy of the plan. It may refer to a Domain
practice, user capability, sponsor decision, governed knowledge state,
organizational resilience or another declared beneficiary-facing boundary. It does
not require a commercial customer, immediate public effect or a single numerical
measure.

Legitimate objectives may concern long-horizon outcomes, research, infrastructure,
governance or harm prevention when their horizon, contribution claim, evidence,
uncertainty and affected boundary are explicit.

An objective fails when it can only be explained by restating internal stages,
document names, implementation components or compliance activities and cannot say
why their completion matters outside that structure.

## 7. Minimum objective envelope

A consequence-proportional objective record identifies:

1. objective Identity and version;
2. proposing subject and acceptance authority;
3. beneficiaries and materially affected subjects;
4. Domain, Scope and Context;
5. intended external condition, capability or decision-quality change;
6. baseline, reference condition or acknowledged absence;
7. intended and intermediate horizons;
8. observable outcome criteria, counterevidence and important unknowns;
9. indicators or proxies and their validity limits;
10. purpose and Value claim, separately governed;
11. constraints and non-compensable conditions;
12. assumptions, dependencies, uncertainty and alternative interpretations;
13. internal deliverables and their claimed contribution without substitution;
14. challenge, revision, expiry and reopening paths; and
15. the explicit statement that Objective Acceptance creates no Method Selection or
    Execution Release.

## 8. Black-box objective test

Before Objective Acceptance, a reviewer evaluates the plan while treating its
implementation as a black box:

| Question | Passing evidence | Failure exposed |
| --- | --- | --- |
| What is different outside the plan? | named condition, capability or decision-quality change | internal completion used as objective |
| For whom or for what affected boundary? | beneficiaries and affected subjects | provider- or artifact-only framing |
| Why does the difference matter? | scoped purpose and Value claim | deliverable assumed valuable |
| When could it be assessed? | horizon and observation conditions | timeless aspiration |
| What counts against success? | failure, uncertainty and counterevidence conditions | unfalsifiable objective |
| Can it be explained without internal component names? | sponsor-readable statement | recursive technical justification |

Passing this test does not establish that the objective is true, valuable,
authorized for all affected subjects or achievable. Detailed Engineering criteria
remain necessary at their own boundary.

## 9. Objective Acceptance gate

Objective Acceptance passes only when competent authority records:

- the exact objective version accepted;
- the declared beneficiaries and affected horizon;
- the evidence and uncertainty supporting its adequacy;
- material dissent, exclusions and unresolved questions;
- the applicable observation and challenge basis;
- acceptance conditions, expiry and reopening triggers; and
- explicit zero authority for method selection and execution.

Failure or deferral returns the plan for reframing or records a qualified no-objective
result. It does not authorize method work beyond separately permitted exploration.

## 10. Method-hypothesis rule

Every material method selection states:

> **For accepted objective version O, in Context C, method version M is expected to
> contribute through rationale R, relative to alternatives A, under assumptions S,
> with evidence E, costs and risks K, and review conditions T.**

The hypothesis may be uncertain. Sunk work, method availability, familiarity,
technical elegance, compliance or prior success may be evidence but cannot substitute
for objective-relative fitness.

A mandated method record distinguishes the mandate, issuing authority,
non-discretionary elements, purpose of the mandate, remaining choices and escalation
route when fitness evidence is adverse. Package A does not authorize deviation from
a competent mandate.

## 11. Minimum method-selection record

Method Selection preserves:

1. method Identity, version and owner;
2. exact accepted objective Identity and version;
3. proposing, assessing and selecting authorities;
4. intended contribution and causal or practical rationale;
5. Domain, Scope, Context, horizon and affected subjects;
6. prerequisites, assumptions and dependencies;
7. relevant alternatives, including continuation, combination, experiment and
   qualified no-method where material;
8. evidence and counterevidence for comparative fitness;
9. applicable fitness dimensions and non-compensable conditions;
10. direct, indirect, transition, verification, opportunity and residual costs;
11. sensitivity, reversibility, external effects and failure consequences;
12. uncertainty, dissent and missing evidence;
13. observation plan and review triggers;
14. decision conditions, expiry and reopening paths; and
15. explicit zero Execution Release.

## 12. Method-fitness profile

Method fitness is plural and objective-relative. Candidate dimensions include:

- relevance to the intended outcome;
- Domain and stakeholder adequacy;
- epistemic yield and uncertainty reduction;
- feasibility and available capability;
- time to useful or reliance-ready result;
- direct and total cost;
- safety, privacy, legality and ethical compatibility;
- reversibility, recoverability and correction cost;
- interoperability, dependency and lock-in;
- evidence quality and observability;
- adaptability and Learning capacity;
- burden distribution and affected-subject consequences; and
- compatibility with mandatory constraints.

No dimension is universally mandatory or sufficient. No aggregate score may erase a
material failed, disputed, unknown or non-compensable condition. Measures,
thresholds and weights remain within competent jurisdiction.

## 13. Method Selection gate

Method Selection passes only when competent authority records:

- the exact accepted objective and selected method versions;
- the comparative rationale and alternatives actually considered;
- the fitness profile, evidence, counterevidence, uncertainty and dissent;
- mandated and discretionary components;
- review triggers and expiry;
- the intended form of later Execution Release; and
- explicit zero execution authority at selection time.

Selection may authorize preparation of a separate execution-release proposal only
when that non-executing preparation is itself within existing authority.

## 14. Why a third gate is mandatory

Objective Acceptance answers **what result is worth pursuing**. Method Selection
answers **which route is presently preferred and why**. Neither answers:

- who may act;
- which tool may operate;
- which data or system may be accessed;
- which state changes are permitted;
- when work may begin or must end;
- how much time, money, volume or external interaction may be consumed; or
- what event must stop or escalate execution.

Those questions belong to an independent Execution Release. Without it, a sound
plan may still begin uncontrolled execution.

## 15. Execution-release rule

> **No material execution may begin solely from proposal preparation, plan approval,
> Objective Acceptance, Method Selection, conversational continuation, artifact
> placement, implementation readiness or prior related authority. Execution begins
> only under a current, attributable and sufficiently bounded Execution Release.**

A continuation phrase such as “go ahead” is interpreted against the exact current
checkpoint and immediately proposed next action. It does not silently authorize
later gates, external effects, sensitive access, irreversible change or indefinite
autonomy.

When the intended scope is materially ambiguous, the executor must narrow to the
clearly authorized reversible boundary or request clarification. Ambiguity does not
justify either unlimited action or unnecessary paralysis.

## 16. Minimum execution envelope

A material Execution Release identifies, proportionately:

1. release Identity, version, issuer and authority source;
2. exact objective and selected-method versions;
3. authorized actors, agents, tools and delegation limits;
4. permitted work and explicitly excluded work;
5. environments, systems and resources in scope;
6. permitted data classes and prohibited data/content;
7. allowed operations, state changes and external effects;
8. forbidden operations and effects;
9. sensitivity, reversibility, affected horizon and consequence classification;
10. time, cost, volume, request, access or other material budgets;
11. start condition, effective time, expiry and completion condition;
12. required validation, monitoring and evidence;
13. material stop, reassessment and escalation conditions;
14. rollback, recovery, containment or safe-stop capability where applicable;
15. expected outputs and their status limitations;
16. reporting, accountability and evidence owner; and
17. change-control rule for non-material adjustments and material envelope changes.

The envelope may refer to governed standing policies or profiles rather than repeat
them verbatim. Referenced authority must be current and applicable.

## 17. Proportional execution-release forms

Package A proposes three forms without fixing a universal risk scale:

### 17.1 Standing or sandbox release

Suitable for low-consequence, reversible work within a controlled environment, such
as read-only inspection, synthetic analysis or isolated drafting. It may authorize a
broad class of actions for a bounded period without per-step approval.

### 17.2 Task release

Suitable for reversible or moderately consequential work with a defined deliverable,
workspace, data boundary, budget and completion condition. It authorizes normal
implementation choices inside the envelope.

### 17.3 Exact or high-consequence release

Suitable when work involves sensitive data, external systems, publication,
production, irreversible effects, significant affected-subject risk or expensive
recovery. It uses narrower identities, budgets, monitoring and stop conditions.

The form follows competent assurance assessment. Labels do not establish actual
risk. Package C remains responsible for fuller proportional-assurance development.

## 18. Bounded autonomy rule

An accepted Execution Release should authorize enough discretion to complete the
declared task efficiently. The executor need not request approval for every ordinary
choice when the choice:

- remains inside the accepted objective, method and execution envelope;
- creates no materially different effect, exposure or affected horizon;
- stays within budgets and stop conditions;
- preserves required evidence and reversibility; and
- does not cross a separately governed decision or authority boundary.

Repeated micro-approval is not the default assurance mechanism. Material expansion,
not routine execution detail, requires renewed authority.

## 19. Material change and stop rule

Execution must stop safely or escalate when:

- no applicable Execution Release can be identified;
- the release is expired, consumed, revoked or superseded;
- objective or method identity no longer matches the authorized versions;
- an actor, tool, data class, environment, operation or effect exceeds the envelope;
- a material budget or stop condition is reached;
- required monitoring or safe-stop capability fails;
- new evidence materially changes the risk, legality, fitness or affected horizon;
- a review trigger is reached and the release requires suspension; or
- authority becomes materially ambiguous.

Non-material implementation adjustments may proceed when the envelope's
change-control rule permits them. Every anomaly does not require shutdown.

## 20. Definition of uncontrolled execution

For Package A, execution is uncontrolled when material action:

1. begins without an applicable Execution Release;
2. relies on plan or method approval as if it were execution authority;
3. cannot be attributed to a current authority, actor/tool and envelope;
4. exceeds permitted operations, data, systems, effects, budgets or time;
5. continues after expiry, consumption, revocation or a mandatory stop condition;
6. changes objective or method materially without renewed decisions; or
7. cannot produce the evidence required to distinguish authorized from unauthorized
   effects.

An undesired outcome does not prove uncontrolled execution, and a desired outcome
does not prove controlled execution.

## 21. Role and authority separation

| Role | Contribution | Does not establish automatically |
| --- | --- | --- |
| objective sponsor or claimant | proposes outcome and justification | Domain adequacy, Value or authority for all affected subjects |
| Objective Acceptance authority | accepts objective version for method consideration | Method Selection or Execution Release |
| Domain authority or reviewer | assesses meaning and applicability | funding, project selection or universal truth |
| method proposer or assessor | supplies hypothesis, alternatives and fitness evidence | Method Selection or execution |
| Method Selection authority | selects method and conditions | Execution Release, implementation or success |
| Execution Release authority | authorizes bounded actors/actions/effects | actual execution, semantic authorship or favorable outcome |
| executor, agent or tool | performs permitted work | authority beyond the envelope or ownership of prior decisions |
| affected subject or representative | supplies experience, standing, challenge or consent where applicable | sole control of every decision absent governing authority |

One subject may occupy several roles only when each authority and occurrence remains
separately evidenced.

## 22. SPServices-like start-control stress test

The motivating scenario has two distinct control questions:

1. **Operational control:** Were live access, protected data and technical effects
   bounded? Extensive technical gates may make the answer yes.
2. **Strategic control:** Was the plan prevented from advancing a poorly justified
   primary method merely because earlier steps were approved? The v0.1 answer was no.

Under v0.2, a plan framed mainly as a sequence from analysis through scanning to
property drafting would be evaluated as follows:

| Gate | Test result before correction | Required disposition |
| --- | --- | --- |
| Objective Acceptance | fail if success is stated mainly through internal stages rather than a defensible Domain outcome | reframe objective before material method selection |
| Method Selection | fail if deterministic scanning is assumed without relevant standards-first or AI-Human alternatives | compare alternatives and record fitness, uncertainty and dissent |
| Execution Release | fail if broad plan approval or repeated continuation instructions are the only authority for downstream material work | issue a bounded release for the exact next work class |
| Continuing execution | reassess when control readiness grows while outcome-relevant learning does not | use declared trigger; do not infer automatic pivot |

Low-risk read-only inspection or synthetic experimentation could still proceed under
a standing or sandbox release. Sensitive live access or external effects would
require an exact release. This prevents strategic drift without recreating a
micro-approval chain for every reversible step.

**Stress-test result:** v0.2 would prevent material start unless all three gates are
separately satisfied. It cannot guarantee prevention if authorities review
ceremonially, tools ignore the release, or no enforcement mechanism exists; those
remain review, implementation and Package B/C responsibilities.

## 23. Additional counterexamples

The v0.1 cases remain applicable. Version 0.2 adds:

| Case | Required result |
| --- | --- |
| plan and method are accepted but no execution actor is named | no material start |
| “go ahead” follows a proposal checkpoint | authorize only the exact immediately presented next action when sufficiently clear; no downstream inheritance |
| sandbox analysis discovers need for live data | stop at sandbox boundary and propose a new release |
| executor makes an ordinary reversible design choice inside a task release | proceed without micro-approval |
| monitoring fails during sensitive execution | safe stop or containment under the envelope |
| objective wording changes only typographically | proceed if change-control rule classifies it non-material |
| selected method changes materially during implementation | require renewed Method Selection and Execution Release |
| successful unauthorized operation produces desired outcome | record desired outcome and authorization failure independently |
| authorized operation produces adverse outcome | record adverse outcome without inventing authorization failure |
| standing authority is too broad to identify data or effects | fail the release-sufficiency test |

## 24. Acceptance tests for v0.2

Before acceptance, review must establish that v0.2:

1. preserves exact DR-014 and DR-016 authority, plan, action, outcome and Value
   boundaries;
2. introduces no new Foundational concept or universal Domain objective;
3. makes objectives sponsor-readable without hiding Engineering conditions;
4. accommodates research, infrastructure, governance, prevention and long-horizon
   objectives;
5. keeps indicators distinct from represented outcomes;
6. governs mandated methods without authorizing deviation;
7. preserves alternatives, counterevidence, dissent and uncertainty;
8. treats fitness as multidimensional without one universal scalar;
9. separates Objective Acceptance, Method Selection and Execution Release;
10. makes plan approval and conversational continuation insufficient for unlimited
    execution;
11. defines a complete but proportionate execution envelope;
12. enables bounded autonomy without per-step approval;
13. stops on absent, expired, exceeded or materially ambiguous authority;
14. distinguishes strategic control from operational control;
15. does not claim that documentation alone enforces the release;
16. interfaces with Package C assurance and Package D observation/pause without
    accepting them;
17. passes the v0.1 and v0.2 counterexamples across Human, Scientific and
    Engineering Views;
18. applies `SYMK-GP-001` without boilerplate; and
19. remains usable for low-consequence work.

## 25. Operational record shape

A later template may use:

1. outcome-facing objective;
2. Objective Acceptance decision;
3. method hypothesis and alternatives;
4. fitness profile and Method Selection decision;
5. execution envelope and Execution Release decision;
6. bounded autonomy and change-control rule;
7. observation, evidence and stop conditions;
8. actual execution and effects record;
9. outcome and method assessment; and
10. prohibited inferences, challenge and reopening.

This shape is illustrative and creates no schema or mandatory file format.

## 26. Prohibited inferences — what v0.2 does not mean

1. Objective Acceptance does not establish objective truth, Value or attainability.
2. Method Selection does not establish fitness, causal contribution or execution
   authority.
3. Execution Release does not establish that execution occurred, complied, succeeded
   or produced Value.
4. Three gates do not require three people, documents, meetings or manual clicks.
5. Separate gates do not prohibit one competent authority from issuing more than one
   decision when each effect remains explicit.
6. A bounded release is not a guarantee against misuse, error or harm.
7. “Go ahead” is not always invalid authority; its scope depends on the exact current
   checkpoint and presented action.
8. Ambiguity does not authorize unlimited execution or require paralysis beyond the
   materially uncertain boundary.
9. Low-consequence standing authority does not make low-consequence work risk-free.
10. Exact release does not make maximal governance universally appropriate.
11. A stop condition does not establish project failure or require abandonment.
12. Documentation compliance does not prove substantive control or non-ceremonial
    review.
13. Acceptance of v0.2 would not accept Packages B–D or GMC-003–014.
14. Package A is not the only or necessarily highest-priority SymK improvement.

## 27. Dissent and open questions

1. Which minimum artifact identity is needed when all three decisions occur in one
   compact low-risk record?
2. When is a conversational instruction sufficiently exact to constitute an
   Execution Release?
3. Which subjects may issue standing or sandbox authority, and for how long?
4. How should distributed or institutional authority be represented without forcing
   one approver?
5. Which materiality test distinguishes ordinary implementation choice from method
   change?
6. How should emergency authority shorten the gates while preserving retrospective
   evidence and challenge?
7. When should a review trigger require automatic stop rather than reassessment while
   continuing?
8. How should tools enforce envelope limits without mistaking machine checks for
   complete governance?
9. How are overlapping releases composed, prioritized, revoked or consumed?
10. How should a release handle probabilistic or emergent effects that cannot be
    enumerated exactly?
11. What evidence demonstrates that review was substantive rather than ceremonial?
12. Which execution-envelope fields belong in universal policy, project profiles or
    Domain standards?

## 28. Reopening conditions

Reassess v0.2 if:

- the three gates become ceremonial duplicate approvals;
- the execution envelope forces maximal documentation on low-consequence work;
- standing releases become broad substitutes for accountable authority;
- shorthand-instruction interpretation repeatedly over- or under-authorizes work;
- executors evade material-change review by decomposing changes;
- stop requirements create greater material harm than controlled continuation;
- enforcement mechanisms cannot represent the envelope faithfully;
- Package C or D establishes incompatible assurance or lifecycle semantics;
- multi-Domain tests expose authority or affected-subject failures; or
- accepted SymK conceptual or constitutional changes alter the dependencies.

## 29. Authorities and non-effects

This corrected proposal does not:

- accept GMC-001 or GMC-002;
- issue an Objective Acceptance, Method Selection or Execution Release for real work;
- create a metric, threshold, schema, runtime guard or enforcement mechanism;
- open or bypass SymK 2.4 or another evolution stage;
- amend Stage-Accepted DR-009–018 or `SYMK-GP-001`;
- revise a Product Vision, Foundation Paper, Constitution, axiom or standard;
- accept or reject GMC-003–014; or
- establish that the GMC set exhausts SymK improvement.

## 30. Corrected proposal result

**PACKAGE A V0.2 CORRECTS THE V0.1 EXECUTION-RELEASE GAP. MATERIAL EXECUTION REQUIRES
SEPARATE OBJECTIVE ACCEPTANCE, METHOD SELECTION AND EXECUTION RELEASE; EACH LATER
GATE HAS ZERO IMPLIED AUTHORITY FROM THE EARLIER GATE. A PROPORTIONAL EXECUTION
ENVELOPE DEFINES ACTORS, TOOLS, DATA, SYSTEMS, ACTIONS, EFFECTS, BUDGETS, TIME,
EVIDENCE, AUTONOMY, CHANGE CONTROL AND STOP CONDITIONS. THE SPSERVICES-LIKE TEST NOW
STOPS STRATEGICALLY UNCONTROLLED START WHILE ALLOWING BOUNDED LOW-CONSEQUENCE WORK.
THIS IS A CORRECTED PROPOSAL, NOT ACCEPTANCE, ENFORCEMENT, STAGE OPENING OR
IMPLEMENTATION AUTHORITY.**
