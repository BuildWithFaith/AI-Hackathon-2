# Implementation Plan: Phase I — CLI Todo App

**Branch**: `[001-cli-todo]` | **Date**: 2026-02-12 | **Spec**: [spec.md](spec.md#L1)

**Input**: `/specs/001-todo-management/spec.md`

## Summary

Phase I delivers a small, well-tested, in-memory CLI Todo application written in Python. This iteration focuses on a minimal, stable core: a task model, an in-memory engine, a concise CLI UX, and automated tests. The output must be runnable locally with zero external services and act as a solid foundation for Phase II.

## Goals (Phase I)
- Deliver a working CLI todo app with create, list, update, delete, and complete operations.
- Produce a small, explicit data model and contracts for task manipulation.
- Provide automated unit and integration tests covering main flows.
- Add a reproducible quickstart so reviewers can run the CLI in under two minutes.

## Out of Scope
- Persistence to an external database (Phase II)
- Web UI, authentication, and AI features (Phase II+)

## Success Criteria / Acceptance Tests
- `todo create "Buy milk"` creates a task that appears in `todo list`.
- `todo complete <id>` marks a task complete and `todo list --all` shows status.
- Unit tests for engine functions pass and coverage is present for core operations.
- Quickstart steps in `quickstart.md` run locally using Python 3.11 and create sample tasks.

## Deliverables
- `src/cli/main.py` — CLI entrypoint
- `src/core/engine.py` — in-memory task engine (CRUD + complete)
- `src/core/models.py` — Task dataclass and serializers
- `tests/unit/*` — unit tests for engine and model
- `specs/001-todo-management/data-model.md` — canonical data model
- `specs/001-todo-management/contracts/` — function contracts (JSON/Markdown)
- `specs/001-todo-management/quickstart.md` — run instructions

## Data Model (canonical)
- `Task` fields:
  - `id: str` — UUID v4 string
  - `title: str` — short description
  - `notes: Optional[str]` — longer notes
  - `completed: bool` — completion flag
  - `created_at: str` — ISO-8601 timestamp
  - `updated_at: Optional[str]`

## CLI UX / Commands
- `todo list [--all|--completed|--pending]` — list tasks (default pending)
- `todo create "title" [--notes "..."]` — create task
- `todo get <id>` — show task details
- `todo update <id> [--title] [--notes]` — edit task
- `todo delete <id>` — remove task
- `todo complete <id>` — mark as completed

Example: `todo create "Buy milk" --notes "2%"`

## Contracts (function signatures)
- `create_task(title: str, notes: Optional[str]) -> Task`
- `list_tasks(status: Optional[str] = None) -> List[Task]`
- `get_task(id: str) -> Optional[Task]`
- `update_task(id: str, title: Optional[str], notes: Optional[str]) -> Task`
- `delete_task(id: str) -> bool`
- `complete_task(id: str) -> Task`

Implementations must raise well-defined exceptions (`NotFoundError`, `ValidationError`) documented in `contracts/`.

## Tests
- Unit tests for every engine function (happy path + key error cases).
- Integration test that runs the CLI via subprocess against a temp in-memory instance and asserts outputs.
- Use `pytest` and a simple `tox` or `python -m venv` in quickstart for reproducible runs.

## Quickstart (local)
1. Create venv: `python -m venv .venv && source .venv/bin/activate`
2. Install dev deps: `pip install -r requirements-dev.txt`
3. Run CLI: `python -m src.cli.main create "example task"`
4. List tasks: `python -m src.cli.main list`

## Milestones / Tasks (Phase I)
1. Define `Task` dataclass and serializers — specs/data-model.md
2. Implement `engine.py` (in-memory store; UUIDs + timestamps)
3. Implement `cli/main.py` command handlers using `argparse` or `click`
4. Add unit tests for engine and model
5. Add CLI integration test and quickstart documentation
6. Review and finalize contracts and `plan.md`

## Estimated Effort
- 1 developer, 1–3 days (small, iterative PRs):
  - data model + engine: 4–6 hours
  - CLI wiring: 2–4 hours
  - tests + docs: 4–6 hours

## Notes & Next Steps
- This plan intentionally keeps Phase I minimal and implementation-ready. Phase II will introduce persistent storage, web API, and auth, so design `engine` with a simple persistence adapter interface to ease transition.

---

See `specs/001-todo-management/spec.md` for the feature-level acceptance criteria
