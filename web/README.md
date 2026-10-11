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
