# SymK – API Online Documentation Guidelines

## Purpose

This document defines **mandatory rules** for online documentation of APIs developed under the **SymK methodology**.

Documentation is not optional, decorative, or external.  
It is a **runtime contract** between the API and its consumers (humans and machines).

Any API that does not comply with these rules is considered **non‑production‑ready**.

---

## Core Principles

1. **Self‑describing APIs**
2. **Runtime documentation (always in sync with code)**
3. **Discoverability first**
4. **Zero hidden endpoints**
5. **Versioned, explicit, and verifiable**

---

## 1. Mandatory Endpoint Discovery

### Rule

Every API **MUST expose an endpoint that lists all available endpoints**.

This endpoint is the authoritative entry point for API discovery.

### Required Endpoint

```
GET /endpoints
```

### Minimum Response Payload

Each listed endpoint MUST include:

- HTTP method
- Path
- Short description
- Version
- Status (`stable | deprecated | experimental`)

### Example Response

```json
{
  "api": "osteolabapi",
  "version": "v1",
  "endpoints": [
    {
      "method": "GET",
      "path": "/health",
      "description": "Service health check",
      "status": "stable"
    },
    {
      "method": "GET",
      "path": "/laudo",
      "description": "Generate laudo document",
      "status": "stable"
    }
  ]
}
```

No endpoint may exist outside this list.

---

## 2. Mandatory Help per Endpoint

### Rule

Every endpoint **MUST provide a human‑readable help description** explaining:

- Purpose
- Parameters
- Expected responses
- Error conditions

### Accepted Patterns

Either:

```
GET /<endpoint>/help
```

Or fully described via **OpenAPI metadata** (preferred).

### Minimum Information Required

- Endpoint purpose
- Parameters:
  - name
  - type
  - required / optional
  - description
- Example request
- Example response
- Possible error codes

An undocumented parameter is considered **invalid**.

---

## 3. OpenAPI / Swagger Is Mandatory

### Rule

All APIs **MUST expose an OpenAPI (Swagger) specification**.

This specification is the **canonical documentation source**.

### Requirements

- `summary` and `description` are mandatory
- Parameters must define:
  - type
  - required flag
  - description
- Responses must include:
  - status codes
  - schemas
  - examples

FastAPI default docs are acceptable **only if fully populated**.

Empty or auto‑generated docs without descriptions are **not compliant**.

---

## 4. Versioning Rules

### Rule

Every API **MUST be versioned explicitly**.

### Accepted Patterns

```
/v1/...
/v2/...
```

### Mandatory Version Endpoint

```
GET /version
```

### Example Response

```json
{
  "api": "osteolabapi",
  "version": "v1.2.0",
  "build": "2025-12-30",
  "status": "stable"
}
```

Deprecated endpoints MUST remain documented and marked accordingly.

---

## 5. Runtime Documentation Principle

### Rule

Documentation must reflect **the running code**, not an external artifact.

### Implications

- No PDF‑only or wiki‑only documentation
- No manually maintained endpoint lists
- No divergence between code and docs

If documentation and runtime behavior differ, **the documentation is wrong**.

---

## 6. Error Documentation

Every endpoint MUST document:

- Expected error codes
- Meaning of each error
- Recovery hints (when applicable)

Example:

| Code | Meaning |
|-----:|--------|
| 400 | Invalid parameters |
| 401 | Authentication failed |
| 403 | Authorization denied |
| 404 | Resource not found |
| 500 | Internal server error |

---

## 7. Documentation Quality Rules

- Clear, technical language
- No marketing text
- No ambiguous wording
- No undocumented magic behavior

Documentation must be usable by:

- Developers
- QA
- Automation tools
- AI agents

---

## 8. Compliance Checklist

An API is SymK‑compliant only if **ALL** items below are satisfied:

- [ ] `/endpoints` exists and is accurate
- [ ] `/version` exists
- [ ] All endpoints are listed
- [ ] All endpoints are documented
- [ ] Parameters are fully described
- [ ] OpenAPI spec is complete
- [ ] Examples are provided
- [ ] Errors are documented
- [ ] Versioning is explicit

Failure on any item blocks production deployment.

---

## Final Statement

> **In SymK, undocumented APIs do not exist.**

Documentation is not an accessory.  
It is part of the executable system.

