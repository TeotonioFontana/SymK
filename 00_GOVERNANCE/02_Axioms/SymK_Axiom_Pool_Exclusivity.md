# SymK Axiom — Pool Exclusivity

**A server must belong to exactly one pool.**  
Server sharing across pools (clusters, farms, or any equivalent grouping) is **forbidden** and must be **platform-enforced**.

## Intent

Pools are **mutually exclusive ownership boundaries**. This axiom prevents split ownership, ambiguous operations, and accidental cross-environment coupling.

## Operational meaning

- A server **MUST NOT** appear in the membership list of more than one pool.
- Any configuration attempting to assign a server to multiple pools is **invalid** and must be rejected by the platform (schema, audit, or runtime enforcement).

## Notes

- “Sharing” includes any form of dual membership, even if the intention is “just reuse capacity.”
- If multiple workloads need a shared capability, **share a service** (e.g., reverse proxy, monitoring), **not the host**.
