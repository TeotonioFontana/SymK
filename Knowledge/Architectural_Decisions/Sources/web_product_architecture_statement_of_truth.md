# Web & Product Architecture — Statement of Truth

## 1. Purpose

This document captures the agreed **web / domain / project structure** for Teotonio Fontana’s products, aligned with the **SymK product life cycle** and the chosen **go-to-market strategy**.

It is intended as a **stable reference for SymK** and future decisions. If reality diverges from this, the document must be updated.

---

## 2. High-level goals

1. **Single main brand domain**

   - Use **`www.teotoniofontana.com.br`** as the primary corporate site.
   - Avoid registering separate domains per product unless a product becomes a clear standalone success.

2. **Multiple products, each with its own identity**

   - Each SaaS product targets a **specific customer segment** (LexBrain, IaaC, InteractSVG, etc.).
   - Software Engineering and Consulting remain **custom, high-touch services**.
   - Developer Tools are **free helpers** to promote the company and demonstrate expertise.

3. **Easy product addition / removal**

   - New products must be easy to introduce and retire without massive DNS or infrastructure changes.
   - Product presence on the website should be **driven by SymK decisions**, not by ad hoc hacks.

4. **Fast experimentation**

   - With SymK + AI support, the target is to bring a **new product from concept to early-adopter test in ~3 months**.
   - The architecture must **support this speed** instead of fighting it.

---

## 3. SymK product life cycle → Web / Infra mapping

### Stage 0 — SymK Design (Internal Only)

- **Activities**
  - Use SymK to define:
    - Problem / opportunity
    - Product vision and capabilities
    - Target segments and value proposition
  - Architectural sketches, data models, UX flows, etc.

- **Web / Infra**
  - No public site yet.
  - Internal repositories (code + docs) may exist.
  - **No DNS, no nginx changes** at this stage.

---

### Stage 1 — Public “Idea” / Concept Page

**Goal:** Validate interest before building a full app.

- **Where it lives**
  - On the **main corporate site**:
    - Example:  
      `https://www.teotoniofontana.com.br/products/lexbrain`
      `https://www.teotoniofontana.com.br/products/iaac`
      `https://www.teotoniofontana.com.br/products/interactsvg`
  - Implemented as normal pages in the **corporate (non-Node) site**.

- **Content**
  - Problem statement and proposed solution.
  - Short explanation of the product concept.
  - Optional concept screenshots or mockups.
  - **Early access / “Notify me” form** (to build a waiting list).

- **Tech**
  - Static / server-rendered HTML under the existing main site stack (Apache or similar).
  - No separate subdomain, no Node app yet.

---

### Stage 2 — Fully Functional Prototype (Early Adopters)

**Goal:** Ship a working product fast and test it with real users.

- **Where it lives**
  - Each product gets its own **subdomain**:

    - `https://lexbrain.teotoniofontana.com.br`
    - `https://iaac.teotoniofontana.com.br`
    - `https://interactsvg.teotoniofontana.com.br`
    - `https://pythontools.teotoniofontana.com.br` (for the tools suite)

  - These subdomains point to **Node.js apps** (Wappler projects) behind nginx.

- **Positioning**
  - Marked clearly as **“Beta”** or **“Early Access”**.
  - Access may be invite-only or limited to selected users.

- **Tech stack (typical)**
  - **Wappler Node.js project** per product.
  - Node app listens on an internal port (e.g. 3010, 3011, 3012…).
  - nginx has a **server block per product subdomain**:
    - terminates HTTPS
    - proxies requests to the product’s Node port
  - The main site’s Stage-1 page simply links to this subdomain.

- **SymK role**
  - SymK provides:
    - initial domain model
    - feature backlog
    - UI skeleton
    - docs and checklists for release
  - Target: **reach this stage in ~3 months** from initial concept.

---

### Stage 3 — Polished Product (Production)

**Goal:** Turn a successful prototype into a stable SaaS.

- **Where it lives**
  - **Same subdomain as Stage 2**, now considered production:
    - e.g. `https://lexbrain.teotoniofontana.com.br`
  - The product is no longer labeled “beta”.

- **Changes vs. Stage 2**
  - Harden security, logging, and monitoring.
  - Improve UX, onboarding, and documentation.
  - Introduce proper pricing, billing, and support where applicable.
  - Optionally introduce a **staging environment**:
    - `stg-lexbrain.teotoniofontana.com.br` → staging Node app
    - `lexbrain.teotoniofontana.com.br` → production Node app

- **Main site adaptation**
  - The corresponding Stage-1 product page is updated:
    - From “Join the beta” → to “Start your free trial” or equivalent.
    - Clear CTA that leads into the subdomain application.

---

### Stage 4 — Break-out Success (Optional)

**Goal:** Promote a winning product to its own independent identity.

- **When**
  - Only if a product becomes sufficiently successful and strategically important.

- **Steps**
  - Register a dedicated domain, e.g.:
    - `lexbrain.ai`
  - Point this new domain to the **same application** (or a new infrastructure tier).
  - Configure redirects:
    - `lexbrain.teotoniofontana.com.br` → 301 redirect to `lexbrain.ai`
  - Keep TeotonioFontana.com as the **“origin story” and umbrella brand**, but let the product stand alone.

---

## 4. Domain strategy summary

1. **Single master brand domain**

   - `www.teotoniofontana.com.br` remains the main entry point.
   - Holds:
     - corporate information
     - list of SaaS products
     - software engineering services
     - consulting services
     - developer tools overview

2. **Per-product subdomains**

   - **Pattern:** `<product>.teotoniofontana.com.br`
   - Used for:
     - Stage 2 prototypes
     - Stage 3 production apps
   - This avoids URL changes between beta and GA.

3. **Developer Tools**

   - All free helper tools live under **one application**:
     - `pythontools.teotoniofontana.com.br`
   - Inside that app:
     - Multiple tools (DB → SQLAlchemy, MD → PDF, MD → DOCX, code analyzer, etc.) are separate modules or pages.
   - Purpose:
     - Promote the company
     - Demonstrate technical expertise
     - Provide value to the developer community

4. **No separate domains per product by default**

   - New domains are **exceptional**, not the norm.
   - They are reserved for products that clearly justify a standalone brand and organization.

---

## 5. Project & repo structure (conceptual)

For each product that reaches Stage 2 (prototype):

- Create a **product repo** (or monorepo structure with clear packages) containing:

  - `frontend/` — Wappler Node project
  - `backend/` — (optional) dedicated API / worker services
  - `infra/` — nginx / systemd / deployment scripts
  - `docs/` — SymK PLC docs, product specification, release notes, etc.

- Also maintain a **main-site repo** where product landing pages are stored:

  - `www.teotoniofontana.com.br` content
  - `/products/<product>` pages for Stage 1 & Stage 3 marketing.

Later, this can be automated via a **SymK “new-product” template**.

---

## 6. Constraints and assumptions

1. **Adding / removing products must be low-friction**

   - Adding a new product mostly means:
     - New entry in the products list on the main site
     - New product subdomain vhost + Node app
   - Removing a product means:
     - Deprecation notice on main site page
     - Optional redirect from product subdomain to an explanation or archive page.

2. **Wappler Node projects are first-class citizens**

   - Each product app is allowed to be a full Wappler Node project, with:
     - its own `index.js`
     - its own layouts and views
     - its own assets
   - Infrastructure must not constrain legitimate Wappler patterns.

3. **Subsite path hacks (like `/pythontools` behind the main domain) are discouraged**

   - Using a **subdomain per app** is cleaner than trying to mount Wappler Node under a path like `/pythontools` on the main hostname.
   - Past debugging experience showed that path-based subsite setups can conflict with:
     - asset paths
     - routing
     - Wappler’s assumptions about “site root”

---

## 7. SymK integration

- SymK uses this document as the **canonical policy** when:
  - Proposing new products
  - Designing routes and URLs
  - Generating nginx configs and Wappler targets
  - Planning releases in PLC documents

- For any new product or major website change, SymK should:
  1. Check this document.
  2. Propose URLs and project structure consistent with it.
  3. Explicitly flag any deviation as **“requires update to Statement of Truth”**.

---

## 8. Change control

- This document is a **living artifact**.
- Changes should:
  - Be versioned (e.g. via Git).
  - Be made only when there is a conscious architectural decision.
  - Be referenced from SymK PLC docs when a product’s status changes (e.g. Stage 1 → Stage 2).

---

**Current status:**  
This reflects the agreed understanding as of the latest SymK / web architecture discussion.
