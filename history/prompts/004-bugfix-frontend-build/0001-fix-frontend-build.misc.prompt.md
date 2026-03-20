---
id: 0001
title: fix-frontend-build
stage: misc
date: 2026-03-20
surface: claude-code
model: ai-agent
feature: 004-bugfix-frontend-build
branch: 004-bugfix-frontend-build
user: agent
command: /sp.implement
labels: [phase2, bugfix, frontend]
links:
  spec: specs/004-bugfix-frontend-build/spec.md
  plan: ""
  tasks: ""
  ticket: ""
  adr: ""
  pr: ""
files:
  - phase2/frontend/package.json
  - phase2/frontend/src/lib/api.ts
  - phase2/frontend/src/lib/auth.ts
  - phase2/frontend/src/app/api/auth/[...all]/route.ts
tests: []
---

## Prompt

"Fix Next.js build errors by migrating app/ and lib/ directories to src/ and installing missing Better Auth dependencies"

## Response snapshot

Executed `pnpm add better-auth axios lucide-react` natively within the Next.js frontend environment. Relocated `api.ts`, `auth.ts`, and core authentication UI components into the isolated `/src` directory correctly mirroring the Next.js aliased module map constraint. Stripped invalid `PUT` and `DELETE` handler exports from auth router. 

## Outcome

- ✅ Impact: `pnpm build` succeeds perfectly. Next.js router mappings are aligned.
- 🧪 Tests: 0
- 📁 Files: 4 updated/moved
- 🔁 Next prompts: None
- 🧠 Reflection: While the global `create-next-app` initialization generated a `--src-dir` skeleton, external commands creating root `/app` and `/lib` structures broke aliasing logic implicitly. We must enforce boundary validation when scaffolding alongside automated Next.js templates. BetterAuth DB syntax has been strictly enforced using `pg.Pool`.
