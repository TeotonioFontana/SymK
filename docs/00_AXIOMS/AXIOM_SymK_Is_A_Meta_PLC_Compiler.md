# AXIOM — SymK Is a Meta PLC Compiler
**Type:** AXIOM  
**Scope:** SymK Foundations (applies to all SymK-driven projects)  
**Change policy:** Versioned  
**Owner:** SymK Foundations

---

## Statement

**SymK is not a project lifecycle for itself.**  
SymK is a **Meta PLC**: a **compiler template** that defines:

- the PLC steps/phases
- the expected tasks per step
- the required outcomes per step
- the transition gates between steps

A **project PLC** is the set of outcomes produced when a project executes the Meta PLC.

---

## Implications

### 1) Every project has its own PLC
Each application or product project maintains its **own PLC workspace**, composed primarily of **outcomes** produced by executing the Meta PLC.

SymK provides the **meta** specification and the **tooling**; projects hold their **instantiated results**.

### 2) Dual outcomes are mandatory
Each PLC step MUST produce **two outcome lines**:

- **Human outcome** — Markdown (readable, decision-grade)
- **Machine outcome** — JSON (structured, executable by engines)

These are two views of the same truth. Neither is optional.

### 3) Transitions are code-supported
Moving from one PLC step to another is not “manual paperwork”.

Transitions MUST be supported by code that:
- validates required fields
- enforces vocab/dictionary constraints where applicable
- generates derived artifacts deterministically
- produces a verifiable transition record

### 4) Foundations belong to projects (SymK provides templates)
**Purpose, concepts, enablers, taxonomies, and models** belong to the **project Foundations**.

SymK provides:
- a **template set** of Foundations and standards
- the **rules** that govern canonical sources, determinism, and validation
- the **tools** used to compile/validate PLC outcomes

SymK resembles a project structurally, but its output is a **template compiler**, not an application.

---

## Consequences

- If a project has PLC documents but no machine outcomes, it is incomplete.
- If a project has machine outcomes but no human outcomes, it is opaque and unsafe.
- If transitions can be performed without validation, the PLC loses authority.
