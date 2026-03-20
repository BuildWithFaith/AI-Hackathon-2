---
id: 0002
title: Plan CLI Upgrade
stage: plan
date: 2026-03-08
surface: CLI
model: Claude Code
feature: 002-upgrade-cli
branch: 002-upgrade-cli
user: mac
command: /sp.plan
labels: [planning, architecture, cli, design]
links:
  spec: specs/002-upgrade-cli/spec.md
  ticket:
  adr:
  pr:
files:
  - path: specs/002-upgrade-cli/plan.md
    action: created
    summary: Created plan.md for implementing the CLI upgrades
  - path: specs/002-upgrade-cli/research.md
    action: created
    summary: Added research on how to subclass argparse.ArgumentParser to prevent exits
  - path: specs/002-upgrade-cli/quickstart.md
    action: created
    summary: Created documentation for the new CLI interactive mode
  - path: CLAUDE.md
    action: modified
    summary: Updated agent context with the feature plan specifics
tests:
  - name: constitution_check
    result: passed
    summary: Plan aligns with the constitution limits
---

## Prompt

Run the `/sp.plan` flow for 002-upgrade-cli.

## Response snapshot

Generated the technical plan, identifying `argparse` limitations. To prevent `sys.exit()` on bad input, `SafeArgumentParser` will be created. The plan involves updating the interactive loop to persist operations and catch exceptions. Updated the agent context files manually using `.specify/scripts/bash/update-agent-context.sh`.

## Outcome

- ✅ Impact: A clear technical path was laid out without requiring bulky third-party dependencies.
- 🧪 Tests: Constitution check passed. Code modifications isolated to `src/cli/main.py`.
- 📁 Files: plan.md, research.md, quickstart.md, data-model.md
- 🔁 Next prompts: Generate development tasks (/sp.tasks).
- 🧠 Reflection: By keeping standard library components and subclassing `argparse`, we maintain exactly the minimum viable implementation requested by the constitution.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Generate task checklists.
