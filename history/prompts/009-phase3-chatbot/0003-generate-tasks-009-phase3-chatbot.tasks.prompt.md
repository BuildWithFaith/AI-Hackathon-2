---
id: {{ID}}
title: {{TITLE}}
stage: {{STAGE}}
date: {{DATE_ISO}}
surface: {{SURFACE}}
model: {{MODEL}}
feature: {{FEATURE}}
branch: {{BRANCH}}
user: {{USER}}
command: {{COMMAND}}
labels: [{{LABELS}}]
links:
  spec: {{LINKS_SPEC}}
  ticket: {{LINKS_TICKET}}
  adr: {{LINKS_ADR}}
  pr: {{LINKS_PR}}
files:
{{FILES_YAML}}
tests:
{{TESTS_YAML}}
---

## Prompt

Generated tasks.md based on the plan.md and spec.md for Phase 3. Included TDD (Test-Driven Development) steps as [P] tasks.

## Response snapshot

Checklist created separating tasks into logic phases: Database & Models, MCP Server, Intelligence Layer, Frontend. Added tests before code actions. 

## Outcome

- ✅ Impact: Drafted complete tasks.md.
- 🧪 Tests: Will be written for each logic layer in execution.
- 📁 Files: specs/009-phase3-chatbot/tasks.md
- 🔁 Next prompts: Implement models and validations.
- 🧠 Reflection: Ensure `openai-agents` is correctly used as confirmed by the user.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Execute implement stage.
