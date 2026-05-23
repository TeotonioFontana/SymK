# PLC_IaaC — 1.6 Discovery Outcomes

## 1. Status of PLC_1 for IaaC

Preconditions check:

- **1.1 Product Vision**  
  - Exists and is coherent: IaaC as a **Recovery & Deployment Engine** for AWS environments, using **environment images / run-ids**, with DR + migration + evidence.

- **1.2 Market Research**  
  - Drafted: segments (MSPs, SaaS, Enterprise, Legal, Consulting, AWS partners, SaaS devs), competitors (AWS-native and vendors), gaps, differentiation, pricing patterns.

- **1.3 Stakeholder Map**  
  - Drafted: Strategic, Technical, Risk/Compliance, Finance, Ops, plus AWS and key customers.

- **1.4 PLC Discovery Methodologies**  
  - Defined at META level; IaaC is already using that toolkit (vision doc, MR, stakeholder map, etc.).

Conclusion: **Discovery is “good enough” to make a 1.6 decision**, with the understanding that details will be refined in PLC_2/3.

---

## 2. Decision

**Decision for IaaC:**

- ☑ **Green Light — Product**  
- ☐ Green Light — Internal Only  
- ☐ No-Go / Park  

Interpretation:

- IaaC will move forward as a **market-facing product**,  
- With the understanding that **consulting usage and internal deployments** are the **first go-to-market vehicles** (consulting-led product).

---

## 3. Business Size Fit — IaaC Scoring

### 3.1 Buckets and Scores (0–3)

0 = irrelevant / bad fit  
1 = edge / exception  
2 = workable but not ideal  
3 = natural home

| Segment type        | Description (for IaaC)                                                                 | Score |
|---------------------|----------------------------------------------------------------------------------------|:-----:|
| **Very small / solo** | 1 account, no formal DR drills, no audits, minimal infra                              | 0–1   |
| **Small**           | 1–3 accounts, some backups, occasional questionnaires                                  | 1–2   |
| **Mid-market**      | 3–20 accounts, SOC2/ISO pressure, DR “sort of happens”                                 | 3     |
| **Enterprise**      | 20+ accounts, AWS Org, DR/BC is a formal topic                                         | 2–3   |
| **Service providers** (MSPs, consulting, AWS partners, SaaS dev shops) | Many client accounts, DR/migration as services                       | 3     |

### 3.2 Rationale

- **Very small / solo (0–1)**  
  - Overkill. They don’t have multi-account complexity, formal DR drills, or real audits.  
  - If they ever use it, it will be via a **managed service provider**, not as direct customers.

- **Small (1–2)**  
  - Occasionally relevant **if** they are **compliance-heavy** (FinTech, HealthTech, Legal, etc.).  
  - Adoption friction is high: limited budget, usually “backup = enough” mindset.

- **Mid-market (3)**  
  - Sweet spot: complexity appears (multi-account, multi-region, real customers and SLAs), but teams are thin.  
  - They need DR/migration **without** building an internal DR platform team.

- **Enterprise (2–3)**  
  - Strong fit technically and in governance terms, but:  
    - Longer cycles, heavier security/procurement.  
    - Likely to start through **consulting-led projects** or via **MSPs/AWS partners**.

- **Service providers / MSPs / consulting / AWS partners / SaaS dev shops (3)**  
  - Perfect match: one engine, many client accounts.  
  - Can bundle IaaC into **DRaaS, migration services, resilience assessments**, etc.

### 3.3 Sentence-level Answer (for 1.6)

> **Business size fit (IaaC):**  
> IaaC is primarily suited for **service providers (MSPs, consulting firms, AWS partners, SaaS platform teams)** and **mid-market to lower-enterprise AWS customers** with multi-account complexity and compliance pressure. It is **overkill for very small setups** and only selectively relevant for small companies with strong regulatory or contractual DR requirements.

---

## 4. Consulting Leverage — IaaC

### 4.1 Axes and Scores (0–3 each)

1. **Sales hook** – Can IaaC help win consulting deals?
   - Score: **2/3**  
     - “We have our own environment imaging + DR/migration engine” is a credible hook.  
     - But you still need proof (demos, pilots) — not magic by itself.

2. **Delivery accelerator** – Does it make consulting execution faster/safer?
   - Score: **3/3**  
     - Centralizes DR/migration logic; replaces per-project scripts and ad-hoc runbooks.  
     - Produces repeatable artifacts (manifests, run-ids, evidence) across clients.

3. **Differentiation / margin** – Does it make your consulting obviously better?
   - Score: **3/3**  
     - Most consultants talk about DR; few can show **account-level images, simulated recoveries, and evidence packs**.  
     - Strong story for “we don’t just promise DR; we can demonstrate it.”

**Total: 8/9 ⇒ Strong**

### 4.2 Sentence-level Answer

> **Consulting leverage (IaaC): Strong (8/9).**  
> IaaC can sit at the center of DR, migration, and AWS resilience consulting: it gives a tangible **engine** and **reports** that differentiate your work, reduces per-project scripting, and supports standardized offers (DR drills, migration programs, environment health checks). It is not a pure “sales magic bullet,” but as soon as you have a few case studies, it becomes a very strong consulting weapon.

---

## 5. Career Leverage — IaaC

### 5.1 Target roles

For you, the main target roles are:

- AWS / Cloud Architect (multi-account, DR, governance).  
- Backend / Infra Architect with strong automation bias.  
- AI-assisted development / tooling roles (where “I built the tools that build systems” matters).

### 5.2 Axes and Scores

1. **Relevance to job requirements (0–3)**  
   - Multi-account AWS, DR, snapshots, migrations, IaC, automation — all are common in senior cloud/infra roles.  
   - Score: **3/3**.

2. **Signal strength (0–3)**  
   - If IaaC achieves even a solid MVP (orchestration + manifests + a few real runs), it shows **system-level thinking**, not just scripts.  
   - Score: **3/3**.

3. **Story quality (0–3)**  
   - “I designed and built an environment imaging and DR/migration engine for multi-account AWS organizations, with run-ids, manifests, and audit evidence” is an excellent story, and you can tailor it per role.  
   - Score: **3/3**.

**Total: 9/9 ⇒ Strong**

### 5.3 Sentence-level Answer

> **Career leverage (IaaC): Strong (9/9).**  
> IaaC is almost a perfect portfolio project for senior cloud/infra and AI-assisted engineering roles: it demonstrates deep understanding of AWS primitives (snapshots, multi-region, IAM, Org), system design (orchestration, manifests, DR workflows), and automation, and can be presented as a coherent, high-impact product/engine rather than a scattered collection of scripts.

---

## 6. Target & Positioning for IaaC (Given the Green Light)

### 6.1 Primary Beachhead

- **Primary segment:**  
  - **Service providers (MSPs, AWS partners, consulting firms)** that manage **multiple AWS accounts** for clients and already sell (or want to sell) **DR/migration/resilience services**.

- **Primary scenario / JTBD for v1:**  
  - “When we need to **prepare and run DR drills or migrations across multiple AWS accounts**, we want a way to **image environments into run-ids, simulate recovery/deployment in a safe account/region, and generate evidence** so that we can **sell DR/migration services with confidence and repeatability**.”

### 6.2 Secondary Segments (Explicit)

- Mid-market SaaS / FinTech / HealthTech that:  
  - Have **multi-account AWS**,  
  - Face **SOC2/ISO/PCI** pressure,  
  - Run periodic **DR drills / migrations**.

- Lower-enterprise cloud teams that need **account/region-level DR and migration** but don’t have a dedicated internal tool.

---

## 7. Offering & Deployment Shape (Hypothesis for PLC_2/3)

### 7.1 v1 Offering

- **Core concept:**  
  - **IaaC Engine**: environment imaging + DR/migration orchestration + evidence artifacts.

- **Initial packaging (hypothesis):**
  - **Tool + consulting bundle** for early design partners:
    - “We bring IaaC + an engagement to run DR drills / migrations and leave you with the engine + runbooks.”

- Later: evolve to a more **productized SKU** once engine and UX stabilize.

### 7.2 Deployment Model (v1 Hypothesis)

- **Primary:**  
  - **Self-hosted inside the customer’s AWS account(s)**:  
    - All sensitive data and control remain in the customer org.  
    - IaaC runs as a set of orchestrator scripts/services + config inside their environment.

- **Optional (later):**  
  - A **light external orchestrator** or “Control Plane” that keeps only metadata and config, not full environment secrets.

Rationale: for DR/migration, customers and auditors are suspicious of pure-SaaS control planes having deep access to everything. Self-hosted by default keeps friction lower.

---

## 8. Pricing Direction (Hypothesis, Not a Decision)

Not binding, just a bias for PLC_2/3 work.

- **Primary pricing axis (hypothesis):**
  - **Per AWS account or per “protected environment”**, combined with a **run-id / drill quota**.

- **Example shape:**
  - Core: includes X accounts, Y run-ids per month/year.  
  - Add-ons:
    - Extra accounts,  
    - Extra run-ids / drills,  
    - Advanced reporting / evidence features,  
    - “Partner/MSP edition” with multi-tenant management.

- **Consulting overlay:**
  - Packaged offerings: “DR Readiness Program”, “Migration Readiness + Execution”, priced as projects but powered by IaaC.

---

## 9. Success Metrics for PLC_2/3 (Short-term)

For IaaC to be considered **on-track** after PLC_2/3:

- **Design partners:**
  - At least **3–5** serious design partners:
    - 1–2 MSPs / AWS partners,  
    - 1–2 mid-market SaaS / regulated mid-market,  
    - 1 enterprise or enterprise-like org (could be via consulting).

- **Real-world usage:**
  - At least **5–10 DR drills or migration projects** where IaaC is used meaningfully (not just demo mode).

- **Evidence of willingness to pay:**
  - At least **one paying customer** (tool + consulting bundle is fine), or  
  - Strong pipeline with concrete budget discussions.

- **Portfolio / career:**
  - Public or anonymized **architecture + case-study material** you can confidently use in job applications and sales decks.

---

## 10. Top 3 Reasons for the Decision

1. **Pain and complexity are clearly real** in the target segments (multi-account AWS, DR, migrations, audits).  
2. **Differentiation exists** vs AWS-native tools and backup vendors: **full environment imaging + redeploy + evidence**, plus DR/migration dual use.  
3. **High leverage**: IaaC strengthens consulting offerings **and** is extremely strong as a portfolio asset for your career.

---

## 11. Top 3 Risks / Assumptions to Validate Next

1. **Adoption friction**  
   - Will MSPs and mid-market SaaS teams accept the operational complexity of an environment-imaging engine, or will they retreat to “we’ll keep using snapshots + scripts”?

2. **AWS-native evolution**  
   - If AWS makes Resilience Hub + Backup + DR services significantly more “environment aware”, the differentiation window may narrow.

3. **Execution bandwidth**  
   - You need to split time between:  
     - Building the engine,  
     - Running real projects,  
     - Using this as a career asset.  
   - If execution is too thin, the product may stagnate in “eternal MVP”.
