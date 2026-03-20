---
id: 0001
title: betterauth-schema
stage: misc
date: 2026-03-20
surface: claude-code
model: ai-agent
feature: 006-bugfix-better-auth-schema
branch: 006-bugfix-better-auth-schema
user: agent
command: /sp.implement
labels: [phase2, bugfix, database, schema]
links:
  spec: specs/006-bugfix-better-auth-schema/spec.md
  plan: ""
  tasks: ""
  ticket: ""
  adr: ""
  pr: ""
files: []
tests: []
---

## Prompt

"Fix BetterAuth relation account does not exist error by pushing the auth schema directly to Postgres"

## Response snapshot

Executed `npx @better-auth/cli migrate` targeting the Neon Postgres DB. This resolved the missing `account`, `user`, `session`, and `verification` table issues that surface when querying Better Auth via the API without prior migration logic.

## Outcome

- ✅ Impact: Better Auth's Kysely adapter generated and pushed the foundational authentication schema straight to the Neon Serverless DB seamlessly.
- 🧪 Tests: 0
- 📁 Files: 0 modified (db schema updated)
- 🔁 Next prompts: None
- 🧠 Reflection: Next.js + Better Auth uses a robust table architecture separated from the custom SQLModel tables (`Tasks`). While SQLModel automatically initiates its metadata schemas on FastAPI boot (`core/db.py`), Better Auth requires a distinct, one-time manual push (via the CLI or integration config) for its core schema.
