# SymK Guideline — FastAPI Endpoint Architecture

## Status
**Mandatory standard** for all FastAPI-based applications under the SymK ecosystem.

This guideline is not stylistic. It is architectural.

---

## 1. Core Principle

> **No endpoint code is allowed inside `main.py`.**

Every HTTP endpoint **must live in its own dedicated router file**, registered explicitly via `app.include_router()`.

`main.py` must remain **boring, predictable, and stable**.

---

## 2. Why This Rule Exists

This rule exists to:

- Preserve architectural clarity
- Prevent uncontrolled growth of `main.py`
- Enable parallel development
- Reduce deployment and restart risk
- Allow clean reuse of features across applications
- Align with FastAPI’s intended design model

Violating this rule leads to:

- Tangled imports
- Hidden side effects
- Painful refactors
- Fragile deployments

---

## 3. Mandatory Responsibilities of `main.py`

`main.py` is allowed to do **only** the following:

1. Instantiate the FastAPI application
2. Load configuration and logging
3. Register routers
4. Register startup/shutdown lifecycle hooks

### Example (`main.py`)

```python
from fastapi import FastAPI
from app.routers import health, laudo

app = FastAPI(
    title="Osteolab API",
    version="2.0"
)

app.include_router(health.router)
app.include_router(laudo.router)
```

Nothing else belongs here.

---

## 4. Router-Based Endpoint Standard

### Directory Structure (Mandatory)

```text
app/
├── main.py
├── routers/
│   ├── __init__.py
│   ├── health.py
│   ├── laudo.py
│   └── image_ocr.py
├── services/
│   ├── laudo_service.py
│   └── ocr_service.py
├── core/
│   ├── config.py
│   └── logging.py
```

Each router file represents **one coherent feature**.

---

## 5. Router File Template (Canonical)

### Example: `routers/laudo.py`

```python
from fastapi import APIRouter, Request, HTTPException
from app.services.laudo_service import laudo_generate_docx
from osteolabapi import check_api_params

router = APIRouter(
    prefix="",
    tags=["laudo"]
)

@router.post("/laudo")
def laudo_generate(request: Request):
    (
        application,
        tenant_id,
        user_id,
        session_key,
        transaction_key,
        laudo_id,
        msg,
        status,
    ) = check_api_params.check_api_params("laudo", request.query_params)

    if status != 200:
        raise HTTPException(status_code=status, detail=msg)

    return laudo_generate_docx(laudo_id)
```

---

## 6. Separation of Concerns (Strict)

### Routers
- Handle HTTP
- Validate request context
- Convert errors to HTTP responses
- Call services

### Services
- Contain business logic
- Perform database access
- Generate documents
- Execute workflows

**Business logic must never live inside routers.**

---

## 7. Explicit Prohibitions

The following are **not allowed**:

- ❌ Defining endpoints inside `main.py`
- ❌ Mixing unrelated endpoints in the same router file
- ❌ Performing heavy logic inside route handlers
- ❌ Implicit router registration
- ❌ Circular imports caused by shortcuts

Violations are considered **architectural defects**, not refactoring issues.

---

## 8. Strategic Impact

Adhering to this rule enables:

- Multi-app reuse (osteolabapi, pythontools, future APIs)
- Safer PyCharm deployments
- Predictable systemd restarts
- Easier onboarding of new developers
- Long-term maintainability

This standard directly supports SymK’s goals of **repeatability, clarity, and controlled evolution**.

---

## 9. Enforcement

This guideline is **non-optional**.

Any new FastAPI endpoint that does not comply must be refactored **before** integration or deployment.

---

## 10. Summary

- `main.py` stays boring
- Each feature gets its own router file
- Routers call services
- Services hold logic
- Architecture stays clean

This is how FastAPI remains scalable instead of becoming another legacy stack.
