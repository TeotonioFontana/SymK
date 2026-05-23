# Property Dictionary — Semantic + Syntax + Conventions + Source of Truth (Complete)
*SymK canonical dictionary*

This document defines, for **every property**, its:
- Semantics (meaning)
- Syntax (type / allowed values)
- Operational conventions
- Enforcement layer (schema vs audit)
- Source of Truth (where to look for the correct or next available value)

Nothing is implicit.

---

## === Common Structural Properties ===

### id
**Semantics:** Stable unique identifier of an entity.  
**Syntax:** string (`[a-z0-9-]+`)  
**Source of Truth:** Declaring YAML file  
**Enforcement:** schema

---

### label
**Semantics:** Human-readable display name.  
**Syntax:** string  
**Source of Truth:** Declaring YAML file  
**Enforcement:** none

---

### description
**Semantics:** Narrative explanation for humans.  
**Syntax:** string (multiline allowed)  
**Source of Truth:** Declaring YAML file  
**Enforcement:** none

---

### lifecycle
**Semantics:** Maturity stage of the entity.  
**Syntax:** enum (`incubation`, `pre-production`, `production`, `deprecated`)  
**Source of Truth:** `services.yaml`  
**Enforcement:** schema + audit

---

## === Runtime & Execution (services.yaml) ===

### runtime
**Semantics:** Base execution environment or language.  
**Syntax:** enum (`python`, `nodejs`, `php`)  
**Source of Truth:** `services.yaml`  
**Enforcement:** schema + audit

---

### stack
**Semantics:** Framework layered on top of runtime.  
**Syntax:** enum (`fastapi`, `flask`, `express`, `node`, `apache-php`)  
**Source of Truth:** `services.yaml`  
**Enforcement:** schema + audit

---

### port
**Semantics:** Primary listening TCP port.  
**Syntax:** integer `1–65535`  
**Conventions:** infra APIs `8100–8199`, app APIs `8200–8299`, node `3000–3099`  
**Source of Truth:** `services.yaml` (scan for next free)  
**Enforcement:** audit

---

### ports
**Semantics:** Multiple exposed TCP ports.  
**Syntax:** list of integers  
**Source of Truth:** `services.yaml`  
**Enforcement:** audit

---

### systemd_service
**Semantics:** systemd unit managing the process.  
**Syntax:** string  
**Source of Truth:** systemd unit + `services.yaml`  
**Enforcement:** schema

---

### health_endpoint
**Semantics:** HTTP liveness/readiness endpoint.  
**Syntax:** string (path)  
**Source of Truth:** service code + `services.yaml`  
**Enforcement:** audit

---

### logs
**Semantics:** Logging configuration container.  
**Syntax:** object  
**Source of Truth:** runtime config + `services.yaml`  
**Enforcement:** schema

---

### environment_overrides
**Semantics:** Per-environment runtime overrides.  
**Syntax:** map  
**Source of Truth:** `services.yaml`  
**Enforcement:** schema

---

## === Architectural Topology (services.topology.yaml) ===

### type
**Semantics:** Architectural role.  
**Syntax:** enum (`application`, `service`, `frontend`, `worker`)  
**Source of Truth:** `services.topology.yaml`  
**Enforcement:** schema + audit

---

### exposure
**Semantics:** Network exposure level.  
**Syntax:** enum (`public`, `internal`)  
**Source of Truth:** `services.topology.yaml`  
**Enforcement:** schema + audit

---

### internal_use
**Semantics:** Internal-only entity flag.  
**Syntax:** boolean  
**Source of Truth:** `services.topology.yaml`  
**Enforcement:** audit

---

### environments
**Semantics:** Execution environments.  
**Syntax:** list of strings  
**Source of Truth:** `services.topology.yaml`  
**Enforcement:** schema

---

### ssh_access
**Semantics:** Requires SSH/SFTP access.  
**Syntax:** boolean  
**Source of Truth:** `services.topology.yaml`  
**Enforcement:** audit error

---

### relations
**Semantics:** Logical dependency container.  
**Syntax:** object  
**Source of Truth:** `services.topology.yaml`  
**Enforcement:** schema

---

## === Access Surface (sshMenu.yaml) ===

### environment
**Semantics:** Target environment context.  
**Syntax:** string  
**Source of Truth:** `services.topology.yaml`  
**Enforcement:** audit

---

### host
**Semantics:** Hostname or IP.  
**Syntax:** string  
**Source of Truth:** DNS / infra + `sshMenu.yaml`  
**Enforcement:** schema

---

### role
**Semantics:** Operational role.  
**Syntax:** enum (`api`, `frontend`, `database`, `worker`)  
**Source of Truth:** `sshMenu.yaml`  
**Enforcement:** audit

---

### user
**Semantics:** Debian/Linux user identity.  
**Syntax:** string  
**Source of Truth:** OS users + `sshMenu.yaml`  
**Enforcement:** audit error

---

### jump
**Semantics:** Logical jump host reference.  
**Syntax:** string | null  
**Source of Truth:** `sshMenu.yaml`  
**Enforcement:** audit

---

### connection_group
**Semantics:** UI grouping only.  
**Syntax:** string  
**Source of Truth:** `sshMenu.yaml`  
**Enforcement:** none

---

### order
**Semantics:** Menu ordering hint.  
**Syntax:** integer  
**Source of Truth:** `sshMenu.yaml`  
**Enforcement:** none

---

## === Connectivity Execution (sshConnectivity.yaml) ===

### identity_strategy
**Semantics:** Authentication mechanism.  
**Syntax:** enum (`agent_or_key`, `key_only`, `ssm_only`)  
**Source of Truth:** `sshConnectivity.yaml`  
**Enforcement:** audit

---

### keepalive
**Semantics:** SSH keepalive policy.  
**Syntax:** object  
**Source of Truth:** `sshConnectivity.yaml`  
**Enforcement:** schema

---

### timeout
**Semantics:** Connection timeouts.  
**Syntax:** object  
**Source of Truth:** `sshConnectivity.yaml`  
**Enforcement:** schema

---

### retry_policy
**Semantics:** Reconnection behavior.  
**Syntax:** object  
**Source of Truth:** `sshConnectivity.yaml`  
**Enforcement:** schema

---

### tunnels
**Semantics:** First-class secure channels.  
**Syntax:** list of objects  
**Source of Truth:** `sshConnectivity.yaml`  
**Enforcement:** audit

---

## === Developer Tooling (dev_environment.yaml) ===

### ide / ide_version / language / language_version / debugger / formatter / linter / type_checker / test_runner / build_tools / container_tools
**Semantics:** Developer tooling context.  
**Syntax:** string or list of strings  
**Source of Truth:** `dev_environment.yaml`  
**Enforcement:** none

---

## === SymK Closure Rule ===

If a property exists in YAML and is not defined here, it is undefined.
