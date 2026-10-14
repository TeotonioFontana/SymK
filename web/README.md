# SymK Web

Project-owned web application for inspecting the SymK side of the controlled
Knowledge Engineering jurisdiction migration.

## Commands

- `npm run dev` — local development server.
- `npm run build` — strict TypeScript check and production build.
- `npm run preview` — preview the production output.

The production base is `/symk/`. Migration content lives in `src/project.ts`;
rendering and interaction live in `src/main.ts`. Checklist state is local browser state
only and does not edit or approve any SymK governance artifact.

## Protocol governance modules

- `roles.html` manages candidate participant kinds and roles, compatible role
  combinations, contribution handoffs, and accountability obligations.
- `authority.html` manages candidate authority boundaries, escalation paths,
  challenges, and legitimate access restrictions.

Both modules preserve the SymK jurisdiction boundary: they do not grant substantive
authority to participants, approve Foundation commitments, configure Workbench
operations, or decide domain truth. Their current records are persisted in the local
browser so the interaction contract can be exercised without silently changing a
governed source. Each authoring flow labels candidate records explicitly and includes
AI-review prompt generation for decisions that require collaborative judgment.
