# Configuration Model Overview — SymK Rewrite (v5)
*sshConnectivity / audit_topology ecosystem*

---

## How to Read This Document (Mandatory)

This document is **not a configuration reference**.

- Authoritative truth lives in the YAML configuration files.
- This document exists to **expose incompleteness, ambiguity, and contradiction**.
- Redundancy is intentional.
- Any inconsistency is a **finding**, not an error.

This document models **how humans and AI reason together (SymK)**.
It is a *thinking instrument*, not a spec sheet.

---

## 1. Epistemic Structure (SymK Model)

The system is described using **independent variables** and **dependent projections**.

---

## 2. Independent Conceptual Variables

### 2.1 Applications (WHY)

Applications are products with roadmap and market intent.

**Current applications (snapshot)**

- osteolab
- teotoniofontana
- iaac
- lexbrain
- hyperadm
- pythontools
- svgtools
- pptx2web
- symk

---

### 2.2 Services / APIs (WHAT)

Backend capabilities supporting one or more applications.

**Current services (snapshot)**

- osteolabapi
- teotoniofontana-api
- hyperadm-api
- hypermediaapi
- spservicesapi
- iaac-api
- lexbrain-api
- pythontools-api
- pptx2web-api
- svgtools-api
- symk-api

---

### 2.3 Frontend Interfaces (HOW)

User-facing runtimes.

---

### 2.4 Operational Identities (WHO)

Control and accountability identities.

---

## 3. Structural Projections

- `services.topology.yaml` — architecture
- `services.yaml` — runtime realization
- `sshMenu.yaml` — access surface

---

## 4. Derived Execution Layer

- `sshConnectivity.yaml` — dependent execution mechanics

---

## 5. Exhaustive Property Cross-Reference (Exploratory)

| Property | Owner |
|--------|------|
| runtime | services.yaml |
| port | services.yaml |
| ssh_access | services.topology.yaml |
| host | sshMenu.yaml |
| keepalive | sshConnectivity.yaml |

---

## 6. Developer Tooling & Environment

Captured via:
- `dev_environment.yaml`
- Tooling appendix

---

## 7. Final SymK Principle

> **Humans define intent.  
> AI enforces structure.  
> Execution exposes contradictions.  
> Incompleteness is information.**

---

# SymK Semantic Axioms and Operating Policies (Addendum)

This section captures **non-negotiable semantics** agreed during the manual semantic audit.  
It is intentionally written for humans first (architects/operators), and then mirrored into automated semantic checks.

## Axiom A1 — `runtime` vs `stack` (no ambiguity)

- **`runtime`** = the *execution platform* (language/ecosystem).  
  Examples: `python`, `nodejs`, `php`
- **`stack`** = the *serving/framework layer* sitting on top of the runtime.  
  Examples: `fastapi`, `flask`, `express`, `node`, `apache-php`

**Source of truth:** `property-dictionary` (canonical semantics).  
Schemas must validate **syntax**; the dictionary defines **meaning**.

## Axiom A2 — Port governance is policy, not nostalgia

Historic Apache port allocations are not “implementation detail”; they are a **port-namespace policy** that prevents collisions and supports deterministic growth.

### Legacy HTTP port intervals (historical reservations)

These were historically bound by Apache virtual hosts and may be migrated to NodeJS over time, but the **interval reservation remains useful**:

- **8001–8005** (platform family)
  - 8001 `hyperadm.com.br`
  - 8002 `hyperdoc.com.br`
  - 8003 `spservices.com.br`
  - 8004 `lexbrain.com.br`
  - 8005 `hyperdocs.com.br`
- **8051–8054** (commercial apps family)
  - 8051 `osteolab.com.br`
  - 8052 `af.poa.br`
  - 8053 `advocaciafontana.adv.br`
  - 8054 `financialbrain.com.br`

### How to use this policy going forward

- **Do not** hardcode “Apache ports” into product meaning.
- **Do** use intervals as a **guideline** for “next available port” decisions.
- The enforcement point is the **semantic audit** (not the schema), because the “right port” is a governance decision.

**Source of truth:** `Port Allocation Policy` (this document section) + `services.yaml` canonical registry.

## Axiom A3 — SSH access is an IDE requirement (frontends and backends)

SSH is not “maintenance only”. In this architecture, SSH is **development infrastructure**:
- remote IDE access
- SFTP upload/download
- logs, debugging, operational fixes

Therefore:
- `ssh_access` is generally **true** for both backend and frontend hosts.
- Exceptions must be **explicitly** justified (e.g., fully managed/containerized target).

**Source of truth:** `services.topology.yaml` (`ssh_access`) and `sshMenu.yaml` (the concrete access catalog).

## Axiom A4 — Application vs Service (value flow definition)

- **Application**: a set of components that together deliver **end-user value** (customers).  
- **Service**: delivers value **to applications** (APIs, internal pages, automation endpoints, etc.).

Important consequence:
- Not every API is a “service”. Some APIs are part of an **application product boundary** (e.g., the API *is* the product).

**Source of truth:** `services.topology.yaml` (`type`) and this axiom.

## Axiom A5 — `admin` is break-glass; service users are ownership

- `admin` is a super-user for bootstrap/troubleshooting (“break-glass”).
- Each application/service must also have its **own Debian user** for routine operation and IDE workflows.

**Source of truth:** `sshMenu.yaml` (`user`) + `dev_environment.yaml` (IDE/tooling mappings).

## Axiom A6 — Target architecture is 1 service per server (sharing is temporary)

The **target** architecture is:  
> each service (and typically each application boundary) can move to its **own server**.

Current multi-service hosts exist for **economic reasons**, not as the semantic truth.

Therefore:
- configs must remain **service-scoped**, even if the current host is shared.
- moving a service to a dedicated host should be **config-only change**, not a semantic refactor.

**Source of truth:** SymK PLC (lifecycle), `services.yaml` registry, and `services.topology.yaml`.

---

*Revision note:* Addendum created on 2026-01-06 to preserve the outcomes of the manual semantic audit for later automation (`semantic_audit.py`).
