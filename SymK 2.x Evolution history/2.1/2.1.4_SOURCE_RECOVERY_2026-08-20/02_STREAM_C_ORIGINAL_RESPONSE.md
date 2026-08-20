Stream C is complete as an analytical working result. No project files were changed.

## 2.1.4C — Grounds, evidence, provenance, uncertainty, disagreement, status, and reliance

### Central result

> SymK must represent epistemic support as a qualified relationship among a claim or epistemic attribution, its grounds, evidence used in assessment, provenance, method, Context, Scope, assessor, criteria, uncertainty, defeaters, alternatives, and time.

No isolated object called “evidence,” no provenance chain, confidence score, approval, or authoritative source is sufficient by itself.

## 1. Ground and evidence

These concepts are related but not interchangeable.

### Ground

A **Ground** is a reason, process, competence, experience, encounter, or relation that may materially support—or partly constitute—the relevant epistemic achievement or claim.

Possible grounds include:

- observation;
- testimony;
- a reliable method;
- a valid inference from adequately supported premises;
- practical competence;
- repeated successful performance;
- direct or accumulated encounter;
- measurement;
- domain expertise;
- or a combination of distributed contributions.

Ground is not limited to a stored artifact. Practical competence and familiarity may provide grounds without being fully representable.

### Evidence

**Evidence** is a contextual role something plays in an inquiry, assessment, attribution, or challenge.

Something is evidence only relative to:

- a question or assessed object;
- a support or challenge relationship;
- an assessment method;
- an assessor or responsible process;
- Context, Scope, and time;
- relevant alternatives;
- and applicable standards.

The same item may be:

- evidence supporting one claim;
- counterevidence against another;
- irrelevant under a different Scope;
- or insufficient under higher-stakes reliance conditions.

Therefore, “evidence” should not be an intrinsic permanent label on a Document or record.

### Resulting distinction

`Ground` concerns why an epistemic achievement or claim may be appropriately connected to truth, competence, or encounter.

`Evidence` concerns how something is used to assess, support, challenge, or attribute that connection.

A Ground may be incompletely evidenced. Evidence may be genuine without being sufficient. Evidence may also be misleading, defeated, fabricated, misinterpreted, or inapplicable.

## 2. Provenance

> **Provenance is the traceable history of origin, participation, custody, derivation, transformation, and responsibility associated with an artifact, contribution, or process.**

A minimum provenance account should be capable of preserving:

- source identity;
- originating participant or system;
- production activity;
- time and relevant environment;
- custody or transfer;
- transformations and derivations;
- tools, models, prompts, or procedures materially involved;
- responsible roles;
- source versions;
- and declared gaps or uncertainty in the lineage.

Provenance can establish that an artifact came from an identified authoritative source. It does not establish that the source was correct, that the content remains applicable, or that reliance is justified.

Accordingly:

> **Provenance supports accountability and assessment; it is neither truth nor warrant.**

## 3. Epistemic support and warrant

SymK should not treat warrant as a Boolean field.

The minimum useful abstraction is a qualified **epistemic-support relationship**:

`supporting material/process → supports or challenges → assessed object`

qualified by:

- support type;
- method;
- criteria;
- Scope and Context;
- assessor;
- relevant alternatives;
- uncertainty;
- defeaters;
- temporal conditions;
- and strength or sufficiency only under an identified scheme.

“Warrant” may remain a human-semantic conclusion that the available grounds are sufficient for responsible epistemic attribution or reliance within a Scope. It should not become a metaphysical property assigned by storage.

A claim may have:

- some support but insufficient warrant;
- strong warrant under one Scope but not another;
- strong provenance but weak grounds;
- or high practical reliability without an accepted explanation of the mechanism.

## 4. Uncertainty

A single confidence number is insufficient because materially different uncertainties require different responses.

SymK’s universal minimum should distinguish at least:

| Uncertainty family | Meaning |
|---|---|
| Missing-information uncertainty | Relevant information is absent or inaccessible |
| Measurement uncertainty | Observations have error, resolution, or instrument limitations |
| Sampling uncertainty | Available cases may not represent the relevant population |
| Model uncertainty | Competing models or structural assumptions remain possible |
| Inferential uncertainty | The premises or reasoning do not determine one secure conclusion |
| Semantic uncertainty | Terms, identities, classifications, or meanings are ambiguous or vague |
| Applicability uncertainty | It is unclear whether a claim or model applies in this Context |
| Source/provenance uncertainty | Origin, custody, transformation, or authenticity is incomplete |
| Competence uncertainty | The relevant capability or performance range is incompletely established |
| Disagreement uncertainty | Qualified participants or processes reach incompatible assessments |
| Future contingency | The relevant state depends on events that have not occurred |
| Projection-loss uncertainty | A reduced Representation may omit material dimensions |

Domains may specialize these families and introduce probabilities, intervals, confidence levels, evidence grades, or other measures. SymK should govern what each measure means, not impose one universal scale.

Uncertainty must preserve:

- its type;
- object;
- source;
- method of estimation;
- Scope;
- time;
- dependencies;
- material consequences;
- and whether it can be reduced, monitored, or only acknowledged.

## 5. Disagreement

Disagreement must be represented before resolution.

At minimum, distinguish:

- **propositional disagreement:** incompatible truth-apt claims;
- **scope disagreement:** claims differ because populations, times, jurisdictions, or tasks differ;
- **conceptual disagreement:** terms or categories are understood differently;
- **methodological disagreement:** participants dispute how something should be investigated or assessed;
- **evidentiary disagreement:** they disagree about relevance, credibility, or sufficiency;
- **model disagreement:** different explanatory or predictive structures remain viable;
- **normative disagreement:** values, duties, priorities, or acceptable consequences differ;
- **authority disagreement:** participants dispute who may decide;
- **reliance disagreement:** they accept similar evidence but recommend different action under risk;
- **representational disagreement:** the apparent conflict results from different projections or abstraction levels.

Disagreement may reveal error, plural valid perspectives, different scopes, unresolved uncertainty, or power asymmetry.

Consensus is evidence about participant alignment. It is not truth. Persistent disagreement is not proof that all positions are equally adequate.

## 6. Epistemic assessment

An **Epistemic Assessment** is a governed evaluation of a specified claim, attribution, capability, asset, ground, evidence relation, or method under declared criteria.

A material assessment must preserve:

- assessed object and version;
- question being answered;
- assessor and relevant competence;
- assessment authority;
- method and criteria;
- evidence and counterevidence considered;
- excluded or unavailable evidence;
- relevant alternatives and defeaters;
- Domain, Scope, Context, and time;
- result;
- uncertainty;
- dissent;
- permitted interpretation;
- challenge path;
- and lineage to prior or later assessments.

Assessment results may include concepts such as:

- unevaluated;
- insufficiently supported;
- supported;
- contested;
- provisionally supported;
- defeated;
- reaffirmed;
- or indeterminate.

These are scheme-qualified results—not truth values or actual Knowledge.

## 7. The status-plane separation

A single `status` field would collapse distinct kinds of authority. SymK requires separate status planes:

| Status plane | Question answered |
|---|---|
| Epistemic assessment | What does a qualified assessment currently conclude? |
| Governance/workflow | How is the artifact treated by the governing process? |
| Reliance authorization | May it be used, by whom, for what, and under which conditions? |
| Applicability | Where and when is it relevant? |
| Lifecycle/availability | Is it active, superseded, withdrawn, archived, or retired? |
| Challenge/disagreement | Is it disputed, under review, answered, or unresolved? |
| Representation integrity | Is this Representation complete, verified, transformed, or loss-bearing? |
| Normative/legal authority | What binding force does it possess under the relevant authority? |

A court judgment can be legally authoritative while its factual reasoning remains contested. A scientific hypothesis can be epistemically promising while not approved for clinical reliance. A retired guideline may remain historically authoritative for an earlier decision.

Truth should not be modeled as another workflow status. If a system records that a proposition is true or false, that record remains a claim or assessment subject to its own grounds and authority.

## 8. Authority separation

Stream C requires at least these authority roles to remain distinct:

- source authority;
- domain-semantic authority;
- epistemic assessor;
- governance authority;
- normative or legal authority;
- reliance authority;
- operational decision-maker;
- and responsibility for consequences.

One participant may occupy several roles, but holding one does not automatically confer the others.

Detailed authority and responsibility rules remain assigned to 2.1.6.

## 9. Reliance authorization

> A **Reliance Authorization** is a scoped decision permitting, requiring, restricting, or prohibiting use of a claim, asset, assessment, or Representation for an identified purpose.

It must preserve:

- object and version;
- authorized users or roles;
- purpose and intended action;
- Domain, Scope, Context, and time;
- applicable assessment;
- known uncertainty and disagreement;
- consequence and reversibility profile;
- required safeguards or supervision;
- alternatives;
- authorizing authority;
- responsibility allocation;
- review and expiry conditions;
- and conditions for suspension or withdrawal.

Reliance can be rationally authorized under uncertainty—for example, during an emergency—without claiming that the relied-upon proposition is known or certainly true.

Conversely, a well-supported claim may be unsuitable for a particular use because the stakes, population, authorization, privacy conditions, or operational environment differ.

## 10. Counterexample results

- **True claim accepted for the wrong reason:** truth and governance acceptance coexist, but defective grounds prevent the acceptance from establishing Knowledge.
- **False claim with impeccable provenance:** provenance establishes lineage, not truth.
- **Authoritative source later defeated:** prior authority and reliance remain historical; epistemic assessment and current authorization may change.
- **Valid inference from false premises:** logical validity survives while epistemic sufficiency fails.
- **Emergency reliance:** authorization may be granted with explicit uncertainty, safeguards, and expiry.
- **Two incompatible claims in one asset:** both remain recoverable with separate grounds, assessments, scopes, and authorities.
- **High-confidence model output:** numeric confidence is interpreted under its model and calibration conditions; it does not become universal epistemic confidence.
- **Practical competence:** performance evidence can support a competence attribution without reducing the competence to test records.
- **Familiarity:** encounter history may support attribution without claiming that a profile recreates familiarity.
- **Missing database value:** absence does not universally mean false, unknown, rejected, or inapplicable.
- **Institutional consensus:** alignment is preserved as evidence while truth and warrant remain independently assessed.
- **Projection dropping dissent:** the projection must declare the loss and retain a route to the governed record.

## Provisional dispositions

| Candidate | Stream C disposition |
|---|---|
| Ground | Governed supporting role or relationship |
| Evidence | Contextual role in assessment, inquiry, or challenge |
| Provenance | Governed lineage/history relationship |
| Epistemic support | Qualified relationship family |
| Epistemic Assessment | Governed process and result; not truth |
| Uncertainty | Typed governed condition; Domain-specialized measures |
| Disagreement | Typed governed relationship/state that must remain visible |
| Governance status | Process-specific designation |
| Reliance Authorization | Scoped decision relationship distinct from assessment |
| Generic confidence | Insufficient without an identified object, meaning, method, and Scope |
| Generic status | Reject as semantically destructive |
| Warrant | Human-semantic assessment conclusion; exact formal treatment deferred |

## Stream C gate

Stream C passes for continuation because it preserves:

- DR-009’s purpose-led admission and two-lane rules;
- DR-010’s Context, Scope, Domain, Relationship, Applicability, Bearer, Representation, and Projection distinctions;
- DR-011’s separation of actual bearing, attribution, assessment, authority, and record;
- the Stream B lifecycle;
- plural Knowledge modes;
- explicit disagreement and uncertainty;
- and Domain ownership of specialized criteria and thresholds.

It does not authorize DR-012 or settle detailed authority rules assigned to 2.1.6.

The next step is **Stream D: Representation, Projection, Ontology, Logic, formal validity, two-lane alignment, and declared semantic loss**.
