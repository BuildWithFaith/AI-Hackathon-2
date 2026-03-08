---
description: "Task list for upgrading CLI"
---

# Tasks: Upgrade CLI to be Robust and Interactive

**Input**: Design documents from `/specs/002-upgrade-cli/`
**Prerequisites**: plan.md, spec.md

## Phase 1: Setup

**Purpose**: Initializing execution environment for the feature

- [x] T001 Verify project structure and `pytest` availability

---

## Phase 2: User Story 1 & 3 - Interactive Shell & Error Handling (Priority: P1)

**Goal**: Implement a persistent shell that handles errors gracefully without exiting.

### Tests
- [x] T002 [P] [US1] Create unit tests for custom `ArgumentParser` error handling in `tests/unit/test_cli_errors.py`
- [x] T003 [P] [US1] Update `test_cli_create_task` and others in `test_cli.py` passing if needed

### Implementation
- [x] T004 [US1] Create `SafeArgumentParser` in `src/cli/main.py` that raises exception on error instead of `sys.exit`
- [x] T005 [US1] Update `main()` interactive `while` loop to catch `ArgumentParseError` and print usage
- [x] T006 [US1] Update `main()` interactive loop to handle `EOFError` and `KeyboardInterrupt`

---

## Phase 3: User Story 2 - Auto-display Pending Tasks (Priority: P2)

**Goal**: Automatically show pending tasks when launching interactive mode.

### Implementation
- [x] T007 [US2] Modify `main()` in `src/cli/main.py` to call `engine.list_tasks('pending')` before starting the `while` loop.

---

## Phase 4: Polish & Documentation

**Purpose**: Finalizing the upgrade

- [x] T008 Run `ruff` to format and check `src/cli/main.py`
- [x] T009 Ensure all tests pass
