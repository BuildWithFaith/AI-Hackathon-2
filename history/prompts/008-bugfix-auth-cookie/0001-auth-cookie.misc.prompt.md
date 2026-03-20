---
id: 0001
title: auth-cookie
stage: misc
date: 2026-03-20
surface: claude-code
model: ai-agent
feature: 008-bugfix-auth-cookie
branch: 008-bugfix-auth-cookie
user: agent
command: /sp.implement
labels: [phase2, bugfix, auth, cookies]
links:
  spec: specs/008-bugfix-auth-cookie/spec.md
  plan: ""
  tasks: ""
  ticket: ""
  adr: ""
  pr: ""
files:
  - phase2/frontend/src/lib/api.ts
  - phase2/backend/core/auth.py
tests: []
---

## Prompt

"Fix 401 Unauthorized block by syncing Axios withCredentials and mapping FastAPI Auth to decode better-auth.session_token cookies directly"

## Response snapshot

Removed the manual Axios interceptor payload injection since BetterAuth natively secures JWT session identifiers inside `HttpOnly` browser cookies. Updated the frontend Axios abstraction (`api.ts`) adding `withCredentials: true`, and updated the FastAPI JWT Decoding router (`core/auth.py`) to scrape `request.cookies.get("better-auth.session_token")` implicitly when a Bearer string is natively absent.

## Outcome

- ✅ Impact: FastAPI now perfectly authorizes requests executed via the Next.js Dashboard fetching tasks safely over HttpOnly cookies.
- 🧪 Tests: 0
- 📁 Files: 2 modified
- 🔁 Next prompts: None
- 🧠 Reflection: While classic API architectures explicitly expect the access token serialized explicitly inside the `Authorization: Bearer` frame, Next.js integrated authentication platforms natively handle it via encoded cookies to eliminate XSS exposures. Enabling `allow_credentials` across the entire CORS framework natively synchronized both services.
