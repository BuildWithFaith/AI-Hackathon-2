---
description: "Task list template for feature implementation"
---

# Tasks: Core Todo Management System (Phase I)

**Input**: Design documents from `/specs/001-todo-management/`
**Prerequisites**: plan.md, spec.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Python project initialization and basic structure

- [x] T001 Initialize Python virtual environment and `requirements-dev.txt`
- [x] T002 Create initial project structure (`src/cli`, `src/core`, `tests/unit`)
- [x] T003 [P] Configure `pytest` and linting tools

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [x] T004 Create `Task` model in `src/core/models.py`
- [x] T005 Implement base in-memory store in `src/core/engine.py`
- [x] T006 [P] Setup basic CLI arg parsing shell in `src/cli/main.py`
- [x] T007 [P] Create custom exception classes in `src/core/exceptions.py`

---

## Phase 3: User Story 1 - Create New Todo (Priority: P1)

**Goal**: As a user, I want to create new todo items so that I can track tasks I need to complete.

**Independent Test**: Can be tested by running `todo create "xyz"`.

### Tests for User Story 1
- [x] T008 [P] [US1] Unit test for `create_task` in `tests/unit/test_engine.py`

### Implementation for User Story 1
- [x] T009 [US1] Implement `create_task` method in `src/core/engine.py`
- [x] T010 [P] [US1] Implement `create` command in `src/cli/main.py`
- [x] T011 [US1] Add integration test for create command in `tests/integration/test_cli.py`

---

## Phase 4: User Story 2 - List All Todos (Priority: P1)

**Goal**: As a user, I want to view all my current todo items so that I can see what tasks I need to complete.

**Independent Test**: Can be tested by running `todo list`.

### Tests for User Story 2
- [x] T012 [P] [US2] Unit test for `list_tasks` in `tests/unit/test_engine.py`

### Implementation for User Story 2
- [x] T013 [US2] Implement `list_tasks` method in `src/core/engine.py`
- [x] T014 [US2] Implement `list` command in `src/cli/main.py`
- [x] T015 [US2] Add integration test for list command in `tests/integration/test_cli.py`

---

## Phase 5: User Story 3 - Update Todo Status (Priority: P2)

**Goal**: As a user, I want to mark todo items as completed.

**Independent Test**: Can be tested by running `todo complete <id>`.

### Tests for User Story 3
- [x] T016 [P] [US3] Unit tests for `get_task` and `complete_task` in `tests/unit/test_engine.py`

### Implementation for User Story 3
- [x] T017 [US3] Implement `get_task` and `complete_task` methods in `src/core/engine.py`
- [x] T018 [US3] Implement `complete` and `get` commands in `src/cli/main.py`
- [x] T019 [US3] Add integration test for complete/get commands in `tests/integration/test_cli.py`

---

## Phase 6: User Story 4 - Delete Todo (Priority: P2)

**Goal**: As a user, I want to remove todo items.

**Independent Test**: Can be tested by running `todo delete <id>`.

### Tests for User Story 4
- [x] T020 [P] [US4] Unit test for `delete_task` in `tests/unit/test_engine.py`

### Implementation for User Story 4
- [x] T021 [US4] Implement `delete_task` method in `src/core/engine.py`
- [x] T022 [US4] Implement `delete` command in `src/cli/main.py`
- [x] T023 [US4] Add integration test for delete command in `tests/integration/test_cli.py`

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T024 [P] Implement `update_task` (title/notes editing) in engine and CLI
- [x] T025 Code cleanup and formatting
- [x] T026 Write `quickstart.md`
