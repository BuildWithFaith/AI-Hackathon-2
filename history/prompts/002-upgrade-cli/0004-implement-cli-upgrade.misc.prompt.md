---
id: 0004
title: Implement CLI Upgrade
stage: misc
date: 2026-03-08
surface: CLI
model: Claude Code
feature: 002-upgrade-cli
branch: 002-upgrade-cli
user: mac
command: /sp.implement
labels: [implementation, execution, cli, python]
links:
  spec: specs/002-upgrade-cli/spec.md
  ticket:
  adr:
  pr:
files:
  - path: src/cli/main.py
    action: modified
    summary: Upgraded CLI interactive mode with SafeArgumentParser and loop error handling
  - path: tests/unit/test_cli_errors.py
    action: created
    summary: Added tests for the custom argument parser
  - path: specs/002-upgrade-cli/tasks.md
    action: modified
    summary: Checked off implementation tasks as they were completed
tests:
  - name: test_cli_errors
    result: passed
    summary: Validated that argument parse errors raise custom exceptions instead of system exits
---

## Prompt

Run the `/sp.implement` flow to execute the tasks outlined in specs/002-upgrade-cli/tasks.md and write the code to upgrade the CLI interactive mode.

## Response snapshot

Implemented `SafeArgumentParser` that subclasses `argparse.ArgumentParser` to override `error` and `exit`, raising `ArgumentParseError`. Modified the `main()` interactive loop to catch these errors and print them, rather than letting the application crash. Also added functionality to display pending tasks upon starting the interactive shell.

## Outcome

- ✅ Impact: The CLI is now robust against user typos in the interactive shell.
- 🧪 Tests: 14 tests passing.
- 📁 Files: Modified `main.py`, added `test_cli_errors.py`. 
- 🔁 Next prompts: Continue to Phase 2 web application.
- 🧠 Reflection: Creating a wrapper class instead of a massive dependency like `click` met the constitutional requirement for keeping dependencies light for the CLI MVP.

## Evaluation notes (flywheel)

- Failure modes observed: Initial bugs where argparse would catch SystemExit and crash anyway. Fixed by raising an exception in `error(self, message)` method instead.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Moving onto Phase 2 API.
