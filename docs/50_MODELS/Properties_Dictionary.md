# Property Dictionary — SymK Semantic + Syntax + Conventions + Enforcement + Source of Truth (Aligned to connectivityctl.vocab.json v1.5)

*SymK canonical dictionary (human form of the vocab + contract properties)*

This document defines, for **every property** and **every grouping key** (vocab sections + contract section containers), its:

* **Semantics** (meaning / purpose)
* **Syntax** (type / allowed values)
* **Operational conventions**
* **Enforcement layer** (schema vs audit vs runtime)
* **Source of Truth** (where the truth lives)

Nothing is implicit.

---

## Global Naming Rules

### Property names (contract-level keys)

* **snake_case** always (YAML keys).
* If a property is a reference key, name it `*_ref`.
* UI-only contract hints must live under a `ui:` block (preferred) or be clearly prefixed (`ui_*`).
* Reserved namespace:

  * `x_*` = legacy/compat/experimental **only** (never authoritative)

**Enforcement:** audit
**Source of Truth:** this dictionary + contract schemas

### Grouping keys (section/container keys)

If a key’s job is “grouping meaning” (example: `ui_contracts`, `types`, `metadata`), it **must declare its purpose**.
Otherwise it becomes a semantic landfill.

**Enforcement:** audit (documentation completeness)
**Source of Truth:** vocab (`x_section_contracts`) + this dictionary

### Identifiers vs references

* **id** = local stable identifier (usually kebab-case), stable inside its container.
* ***_ref** = global join key meant for cross-file linkage (patterns defined in vocab.types).

**Enforcement:** schema + audit
**Source of Truth:** declaring YAML + referenced YAML

---

## A) Vocab Structure Keys (connectivityctl.vocab.json)

These are **not runtime properties**. They are **vocab sections** (grouping keys) that govern meaning across all contracts.

### vocab (ROOT CONTAINER)

**Semantics:** top-level wrapper for the vocabulary payload.
**Syntax:** object with required keys (id/version/status/sections).
**Conventions:** do not place unrelated config here.
**Enforcement:** schema (vocab schema) + human governance
**Source of Truth:** connectivityctl.vocab.json

### id (VOCAB)

**Semantics:** stable vocab identity string used by contracts (`metadata.vocab_ref.id`).
**Syntax:** string (e.g., `connectivityctl`)
**Enforcement:** schema
**Source of Truth:** connectivityctl.vocab.json

### version (VOCAB)

**Semantics:** vocab release version pinned by contracts (`metadata.vocab_ref.version`).
**Syntax:** string (e.g., `1.5`)
**Conventions:** bump when tokens/mappings/contracts change.
**Enforcement:** schema + audit (pinning)
**Source of Truth:** connectivityctl.vocab.json

### status (VOCAB)

**Semantics:** governance flag (canonical / draft / deprecated etc.).
**Syntax:** string
**Enforcement:** governance/audit policy
**Source of Truth:** connectivityctl.vocab.json

---

## A.1) x_section_contracts (VOCAB SECTION — semantic documentation registry)

**Semantics:** **mandatory documentation layer** defining purpose/authority/enforcement for each top-level vocab section.
Prevents drift by making “what this section is for” explicit.
**Syntax:** object keyed by section name. Each entry has `purpose`, `authority`, `enforcement`.
**Conventions:** if a new top-level section is added, it must be documented here.
**Enforcement:** audit (documentation completeness)
**Source of Truth:** connectivityctl.vocab.json → `x_section_contracts`

---

## A.2) governance (VOCAB SECTION)

**Semantics:** defines authority, source-of-truth rules, and deprecation discipline for the vocab.
**Syntax:** object
**Conventions:** contracts must pin `metadata.vocab_ref` to this vocab id+version.
**Enforcement:** audit + human governance
**Source of Truth:** connectivityctl.vocab.json → `governance`

---

## A.3) enums (VOCAB SECTION)

**Semantics:** canonical enum tokens and meanings. These tokens are the **only** allowed values for enum-bound properties (except explicit deprecated aliases handled via mappings + audit).
**Syntax:** object of enum families (each has `values`, optional `axis/note/status`).
**Conventions:** never invent tokens in contracts. If you need a new token, it’s a vocab change.
**Enforcement:** schema (enum refs) + audit (deprecated usage rules)
**Source of Truth:** connectivityctl.vocab.json → `enums`

---

## A.4) mappings (VOCAB SECTION)

**Semantics:** deterministic cross-axis mappings + migration alias translations.
Mappings do **not** introduce new truths; they relate existing truths and provide controlled migration paths.
**Syntax:** object of mapping tables.
**Conventions:**

* mappings are **deterministic** (no “maybe”).
* migration aliases must be explicit (e.g., `up -> active`).
  **Enforcement:** audit + tooling (translators/generators)
  **Source of Truth:** connectivityctl.vocab.json → `mappings`

### operational_state_aliases (MAPPING TABLE — migration-only)

**Semantics:** controlled translation of historically overloaded/binary health tokens (`up/down/healthy`) into canonical `operational_state`.
**Syntax:** map(alias_token → canonical_token)
**Conventions:** aliases are **not canonical**; forbid outside `x_legacy` once policy flips.
**Enforcement:** audit (warn now / error later)
**Source of Truth:** connectivityctl.vocab.json → `mappings.operational_state_aliases`

---

## A.5) ui_contracts (VOCAB SECTION)

**Semantics:** UI-only ordering/defaults intended to be mirrored by contracts.
It is **not business logic** and must never redefine semantic axes; it standardizes presentation and default filters only.
**Syntax:** object keyed by domain (e.g., `terminals`).
**Conventions:** contracts may mirror these lists under `<contract>.ui.*` and audit enforces equality.
**Enforcement:** audit (mirror equality + misuse detection)
**Source of Truth:** connectivityctl.vocab.json → `ui_contracts`

---

## A.6) types (VOCAB SECTION)

**Semantics:** reusable type constraints (patterns/minLength/etc.) used across contracts for join keys and identifiers.
**Syntax:** object keyed by type name; each has `{ schema, description }`.
**Conventions:** contracts should reuse these shapes via schemas (or generators) to avoid drift.
**Enforcement:** schema validation (primary) + audit (secondary)
**Source of Truth:** connectivityctl.vocab.json → `types`

---

## A.7) properties (VOCAB SECTION)

**Semantics:** semantic contract for core properties (meaning, syntax binding, enforcement, source-of-truth).
Explains **why** a property exists and how it should be governed.
**Syntax:** object keyed by property name; each has `{ semantics, syntax, enforcement, source_of_truth }`.
**Enforcement:** schema + audit (as declared per property)
**Source of Truth:** connectivityctl.vocab.json → `properties`

---

## A.8) audit_rules (VOCAB SECTION)

**Semantics:** audit-only invariants and migration constraints beyond what schemas can (or should) enforce.
Prevents axis confusion and uncontrolled legacy drift.
**Syntax:** object with rule families (lists of assertions).
**Enforcement:** audit only
**Source of Truth:** connectivityctl.vocab.json → `audit_rules`

---

## A.9) metadata (VOCAB SECTION)

**Semantics:** operational info about the vocab release (timestamps, change summary).
**Not a semantic authority.**
**Syntax:** object
**Enforcement:** none
**Source of Truth:** connectivityctl.vocab.json → `metadata`

---

## B) Canonical Axes Model (the thing that stops you from inventing a fourth “lifecycle”)

### lifecycle

**Semantics:** life stage of an entity (portfolio/product lifecycle). Universal axis.
**Syntax:** enum:lifecycle
`planned | provisioning | production | deprecated | retired`
**Conventions:** required for first-class entities in scope (services, servers, pools, terminals entries).
**Enforcement:** schema + audit
**Source of Truth:** vocab.enums.lifecycle

### operational_state

**Semantics:** instantaneous health/availability of a runtime entity.
**Syntax:** enum:operational_state
`unknown | active | degraded | maintenance | draining | offline | broken`
**Conventions:**

* Don’t use `up/down/healthy` (they are migration aliases only).
* `unknown` is valid when you truly don’t observe it yet.
  **Enforcement:** schema + audit + runtime(optional)
  **Source of Truth:** runtime observation + contracts + vocab.enums.operational_state

### environment

**Semantics:** deployment lane/context (where it runs). Orthogonal to lifecycle and operational_state.
**Syntax:** enum:environment
`aws-prod | aws-pre | aws-inc`
**Conventions:** environment binding lives in topology/placement contracts (not in services.yaml catalog unless you intentionally model it there).
**Enforcement:** schema + audit
**Source of Truth:** vocab.enums.environment + environment registries in contracts

### terminal_entry_state

**Semantics:** state/readiness of the **access entry itself** (menu contract), not the server/service.
**Syntax:** enum:terminal_entry_state
`active | enabled(deprecated alias) | disabled | experimental | placeholder | deprecated | misconfigured | broken`
**Conventions:** use `active` (not `enabled`) unless you’re mid-migration.
**Enforcement:** schema + audit
**Source of Truth:** vocab.enums.terminal_entry_state + terminals.yaml

### app_stage (optional nuance)

**Semantics:** optional product maturity detail; must map consistently to lifecycle.
**Syntax:** enum:app_stage
`idea | discovery | build | beta | production | sunset`
**Conventions:** if present, audit must verify mapping: `mappings.app_stage_to_lifecycle`.
**Enforcement:** audit (mapping consistency)
**Source of Truth:** vocab.enums.app_stage + vocab.mappings.app_stage_to_lifecycle

---

## C) Common Structural Properties (All YAML Contracts)

### metadata (CONTRACT)

**Semantics:** document-level metadata container.
**Syntax:** object
**Conventions:** includes at least `version`, `owner`, `description`, `vocab_ref`.
**Enforcement:** schema
**Source of Truth:** declaring YAML file

### vocab_ref (CONTRACT)

**Semantics:** pin contracts to a specific vocab release (prevents silent drift).
**Syntax:** object `{ id, version }`
**Conventions:** must match vocab id+version exactly.
**Enforcement:** schema + audit
**Source of Truth:** contract metadata + connectivityctl.vocab.json

### version / owner / description

**Semantics:** standard doc metadata.
**Syntax:** string/number as applicable.
**Enforcement:** schema (where required)
**Source of Truth:** declaring YAML file

### id (ENTITY)

**Semantics:** stable identifier **inside its container**.
**Syntax:** string (kebab-case unless a vocab.type says otherwise).
**Enforcement:** schema
**Source of Truth:** declaring YAML file

### label

**Semantics:** human display name (UI).
**Syntax:** string
**Enforcement:** audit (quality)
**Source of Truth:** declaring YAML file

### notes

**Semantics:** exceptional/temporary human notes; never carries core semantics.
**Syntax:** string
**Enforcement:** none (audit may flag abuse)
**Source of Truth:** declaring YAML file

### x_legacy (NAMESPACE)

**Semantics:** backward compatibility container; never authoritative.
**Syntax:** object
**Enforcement:** audit (containment rules)
**Source of Truth:** legacy history only

---

## D) Services Runtime Contract (services.yaml)

### services (CONTRACT ROOT)

**Semantics:** canonical registry of WHAT services exist (identity + runtime intent), not placement.
**Syntax:** object with `metadata`, `catalog` (+ optional `ui` mirror if you decide).
**Conventions:** placement belongs to services.topology.yaml.
**Enforcement:** schema
**Source of Truth:** services.yaml

### services.catalog (CONTRACT SECTION KEY)

**Semantics:** map of service entries keyed by `service_ref`.
**Syntax:** object map(service_ref → ServiceEntry)
**Conventions:** key MUST equal entry `id` (explicit join clarity).
**Enforcement:** schema + audit
**Source of Truth:** services.yaml

### service_ref

**Semantics:** stable join key for services across contracts.
**Syntax:** vocab.types.service_ref
**Enforcement:** schema
**Source of Truth:** services.yaml keys

### uid

**Semantics:** opaque immutable identifier for the service entry.
**Syntax:** string (format policy is local; keep stable)
**Enforcement:** schema + audit (immutability rule)
**Source of Truth:** services.yaml

### runtime

**Semantics:** base execution runtime/language.
**Syntax:** enum:runtime → `python | nodejs | php`
**Enforcement:** schema + audit
**Source of Truth:** vocab.enums.runtime

### framework

**Semantics:** application framework on top of runtime.
**Syntax:** enum:framework → `fastapi | flask | express | none`
**Enforcement:** schema + audit
**Source of Truth:** vocab.enums.framework

### port / ports

**Semantics:** listening TCP port(s).
**Syntax:** integer 1–65535 / list of integers
**Conventions:** use **either** `port` or `ports` (not both) unless you intentionally support both in schema (but then you must define semantics clearly).
**Enforcement:** schema + audit (port allocation policy)
**Source of Truth:** services.yaml

### systemd_service

**Semantics:** systemd unit name managing the process.
**Syntax:** string
**Enforcement:** schema + runtime(optional)
**Source of Truth:** systemd + services.yaml

### health_endpoint

**Semantics:** HTTP readiness/liveness endpoint path.
**Syntax:** string path starting with `/`
**Enforcement:** schema + audit
**Source of Truth:** service code + services.yaml

### logs

**Semantics:** logging configuration container.
**Syntax:** object
**Conventions:** keep schema permissive; enforce deeper rules via audit if needed.
**Enforcement:** schema (container) + audit(optional)
**Source of Truth:** runtime config + services.yaml

### environment_overrides

**Semantics:** per-environment overrides for runtime intent (ports, framework, logs, etc.).
**Syntax:** map(environment_key → overrides)
**Enforcement:** schema
**Source of Truth:** services.yaml

### lifecycle

**Semantics:** universal life stage for the service entity.
**Syntax:** enum:lifecycle
**Enforcement:** schema + audit
**Source of Truth:** vocab.enums.lifecycle

### operational_state

**Semantics:** instantaneous observed/declared state of the service entity (optional until you implement observation).
**Syntax:** enum:operational_state
**Conventions:** if you don’t observe it yet, use `unknown` (not fake “healthy”).
**Enforcement:** schema + audit
**Source of Truth:** runtime observation + services.yaml (until runtime owns it)

### app_stage (optional)

**Semantics:** product maturity nuance; must map consistently to lifecycle.
**Syntax:** enum:app_stage
**Enforcement:** audit (mapping)
**Source of Truth:** services.yaml + vocab.mappings.app_stage_to_lifecycle

---

## E) Architectural Topology (services.topology.yaml)

### services.topology (CONTRACT ROOT)

**Semantics:** authoritative placement + topology for services (where they run, relationships, exposure, environments).
**Syntax:** object (domain-specific)
**Enforcement:** schema + audit
**Source of Truth:** services.topology.yaml

### topology_type

**Semantics:** architectural role of the unit.
**Syntax:** enum:topology_type
`application | service | frontend | worker | database | gateway`
**Enforcement:** schema + audit
**Source of Truth:** vocab.enums.topology_type

### exposure

**Semantics:** network exposure level.
**Syntax:** enum:exposure → `public | internal`
**Enforcement:** schema + audit
**Source of Truth:** vocab.enums.exposure

### environments

**Semantics:** allowed deployment lanes for this unit.
**Syntax:** list of enum:environment
**Enforcement:** schema + audit
**Source of Truth:** vocab.enums.environment + topology contract

### relations

**Semantics:** dependency graph container.
**Syntax:** object
**Enforcement:** schema + audit
**Source of Truth:** services.topology.yaml

> NOTE: `server_state` is deprecated in vocab. Use `lifecycle + operational_state` instead for runtime inventory.

---

## F) Terminal Catalog (terminals.yaml)

### terminals (CONTRACT ROOT)

**Semantics:** catalog of operator access entries (UX contract), not runtime bindings.
**Syntax:** object with `metadata`, `ui` (mirror), `catalog/entries` depending on your contract shape.
**Enforcement:** schema + audit
**Source of Truth:** terminals.yaml

### ui (CONTRACT SECTION KEY — mirror container)

**Semantics:** contract-local mirror of UI ordering/defaults (presentation only).
**Syntax:** object mirroring `vocab.ui_contracts.terminals`.
**Enforcement:** schema (shape) + audit (mirror equality)
**Source of Truth:** vocab.ui_contracts.terminals

### terminal_type

**Semantics:** UI bucket/type used by terminals menu.
**Syntax:** enum:terminal_type
**Enforcement:** schema + audit
**Source of Truth:** vocab.enums.terminal_type

### scope

**Semantics:** subsystem tag used for grouping/labels/filters (still semantic-light).
**Syntax:** enum:scope
**Enforcement:** schema + audit
**Source of Truth:** vocab.enums.scope

### kind

**Semantics:** connection kind from operator perspective.
**Syntax:** enum:kind → `shell | logs`
**Conventions:** if you want `console/admin`, that’s a **vocab change first**.
**Enforcement:** schema
**Source of Truth:** vocab.enums.kind

### environment

**Semantics:** lane/context for the entry.
**Syntax:** enum:environment
**Enforcement:** schema + audit
**Source of Truth:** vocab.enums.environment

### terminal_entry_state

**Semantics:** readiness/state of the **access entry itself**.
**Syntax:** enum:terminal_entry_state
**Enforcement:** schema + audit
**Source of Truth:** vocab.enums.terminal_entry_state

### lifecycle (terminal entry)

**Semantics:** universal lifecycle for the entry as a first-class citizen.
**Syntax:** enum:lifecycle
**Enforcement:** schema + audit
**Source of Truth:** vocab.enums.lifecycle

### target_ref

**Semantics:** stable join key for binding catalog ↔ runtime targets.
**Syntax:** vocab.types.target_ref
**Enforcement:** schema + audit (uniqueness)
**Source of Truth:** terminals.yaml

### required_user

**Semantics:** required Linux user after connect.
**Syntax:** string
**Enforcement:** audit + runtime
**Source of Truth:** terminals.yaml + OS users

---

## G) Terminal Runtime Contract (terminals.runtime.yaml)

### defaults (CONTRACT SECTION KEY)

**Semantics:** default runtime bindings applied unless overridden per target.
**Syntax:** object
**Enforcement:** schema
**Source of Truth:** terminals.runtime.yaml

### targets (CONTRACT SECTION KEY)

**Semantics:** map(target_ref → runtime binding object).
**Syntax:** object map
**Enforcement:** schema + audit (coverage rules)
**Source of Truth:** terminals.runtime.yaml

### backend

**Semantics:** execution backend used to open a session.
**Syntax:** enum:backend → `ssm`
**Enforcement:** schema
**Source of Truth:** vocab.enums.backend

### ssm_target

**Semantics:** AWS SSM target id (EC2 instance id today).
**Syntax:** vocab.types.ssm_target
**Enforcement:** schema + audit + runtime
**Source of Truth:** AWS + terminals.runtime.yaml

### aws.region

**Semantics:** AWS region for session execution.
**Syntax:** vocab.types.aws_region
**Enforcement:** schema + audit
**Source of Truth:** terminals.runtime.yaml

### aws.profile

**Semantics:** local AWS CLI profile name.
**Syntax:** string
**Enforcement:** audit (must exist locally)
**Source of Truth:** local ~/.aws/config + terminals.runtime.yaml

### session.user_switch.method

**Semantics:** strategy to switch into required_user.
**Syntax:** enum:user_switch_method → `sudo_login`
**Enforcement:** schema
**Source of Truth:** vocab.enums.user_switch_method

---

## H) SSH Menu Contract (sshMenu.yaml)

### sshMenu (CONTRACT ROOT)

**Semantics:** human navigation / SSH endpoints menu contract (operator UX).
**Syntax:** object
**Enforcement:** schema + audit
**Source of Truth:** sshMenu.yaml

(Keep your existing sshMenu properties here; they’re not in the provided vocab excerpt beyond enums/types you may later formalize. If you want role enums governed, that’s a vocab change.)

---

## I) Connectivity Execution Contract (sshConnectivity.yaml)

### sshConnectivity (CONTRACT ROOT)

**Semantics:** tunneling + connectivity execution policy (how tunnels/sessions are created/kept alive).
**Syntax:** object
**Enforcement:** schema + audit
**Source of Truth:** sshConnectivity.yaml

(Keep your existing sshConnectivity properties here; vocab currently governs only shared enums/types used across contracts.)

---

## J) SymK Closure Rule

If a **contract property** exists in YAML and is not defined here (or explicitly delegated to vocab.enums/types), it is undefined.

If a **token** is used and is not in `vocab.enums.*` (or not an explicitly mapped deprecated alias), it is invalid.

---

## Appendix: Deprecated / Legacy Fields (canonical stance)

### server_state (DEPRECATED)

**Semantics:** mixes lifecycle + operational_state. Replace with `lifecycle + operational_state`.
**Syntax:** deprecated enum family in vocab
**Enforcement:** audit warning (or error once you flip the switch)
**Source of Truth:** legacy only

### service_lifecycle (DEPRECATED)

**Semantics:** domain dialect; replace with lifecycle + environment.
**Enforcement:** audit warning
**Source of Truth:** legacy only

### legacy terminal lifecycle (DEPRECATED)

**Semantics:** old terminals.yaml lifecycle tokens. Replace with `terminal_entry_state` + `lifecycle`.
**Enforcement:** audit warning/error depending on migration window
**Source of Truth:** legacy only
