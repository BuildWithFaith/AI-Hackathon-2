---
name: Spec-Driven Development (SDD) Workflow
description: Step-by-step guide for using the Spec-Kit Plus workflow to specify, plan, task, and implement new features.
---

# Spec-Driven Development Workflow

This skill outlines the strict step-by-step procedure required when developing features using the Spec-Kit Plus package. It ensures consistency, prevents skipped documentation (like unfilled Prompt History Records), and maintains the required feature branch structure.

## Command Reference
The workflow revolves around four primary commands (or their underlying bash scripts):
1. **`/sp.specify`** - Create specifications
2. **`/sp.plan`** - Create implementation plans
3. **`/sp.tasks`** - Create detailed task checklists
4. **`/sp.implement`** - Execute code changes

## Step 1: Specify Feature (`/sp.specify`)
**Goal**: Define the exact user scenarios, requirements, and acceptance criteria.
1. Run `.specify/scripts/bash/create-new-feature.sh --json "FEATURE_DESCRIPTION" --number NUMBER --short-name "SHORT_NAME"`
   *(Example: `--number 002 --short-name upgrade-cli`)*
2. Read the generated `.specify/templates/spec-template.md`.
3. Open `specs/###-feature-name/spec.md` and complete all mandatory sections: User Scenarios, Priority, Requirements, and Measurable Outcomes.
4. Create `specs/###-feature-name/checklists/requirements.md` and check off the completed validation checklist items.
5. **Prompt History Record (PHR)**: Run `.specify/scripts/bash/create-phr.sh --title "specify-feature-name" --stage spec --feature "###-feature-name" --json`.
6. **CRITICAL**: Open the resulting `history/prompts/###-feature-name/...spec.prompt.md` and manually replace the `{{VARIABLES}}` with the actual details of your work.

## Step 2: Plan Implementation (`/sp.plan`)
**Goal**: Design the technical approach while adhering to the user specification and project constitution constraints.
1. Run `.specify/scripts/bash/setup-plan.sh --json`.
2. Review `.specify/memory/constitution.md` to ensure planned changes adhere to core constraints (e.g. no heavy libraries, test-driven).
3. Open `specs/###-feature-name/plan.md` and document the project structure and context.
4. If needed, create `research.md` or `quickstart.md` artifacts under `specs/###-feature-name/`.
5. Run `.specify/scripts/bash/update-agent-context.sh claude` (or the respective agent) to update central context limits.
6. **Prompt History Record (PHR)**: Run `.specify/scripts/bash/create-phr.sh --title "plan-feature-name" --stage plan --feature "###-feature-name" --json`.
7. **CRITICAL**: Open the newly generated `...plan.prompt.md` file and fill out the `{{VARIABLES}}` representing the planning actions and rationale.

## Step 3: Generate Tasks (`/sp.tasks`)
**Goal**: Break the implementation plan down into an actionable, testable checklist.
1. Read the finalized `spec.md` and `plan.md`.
2. Create `specs/###-feature-name/tasks.md`.
3. Separate the list into logical phases, ensuring to write test tasks (`[P]`) strictly *before* implementation tasks to enforce TDD. Example:
   ```markdown
   - [ ] T001 [P] [US1] Create unit tests for...
   - [ ] T002 [US1] Implement functionality in...
   ```
4. **Prompt History Record (PHR)**: Run `.specify/scripts/bash/create-phr.sh --title "generate-tasks-name" --stage tasks --feature "###-feature-name" --json`.
5. **CRITICAL**: Fill out the `...tasks.prompt.md` template with the details of the checklist created.

## Step 4: Implement Code (`/sp.implement`)
**Goal**: Write the actual code logic according strictly to the task checklist.
1. Iteratively write the code for the tasks defined in `tasks.md`. Mark them off (`[x]`) as they are completed.
2. Ensure you are running tests via `pytest` and meeting all linting requirements via `ruff format` and `ruff check`. The pipeline must pass perfectly.
3. Finish the final formatting and clean-up tasks.
4. **Prompt History Record (PHR)**: Run `.specify/scripts/bash/create-phr.sh --title "implement-feature-name" --stage misc --feature "###-feature-name" --json`.
5. **CRITICAL**: Open the resulting `...misc.prompt.md` file and explain exactly which files were modified and the outcome of the implementation phase in place of the `{{VARIABLES}}`.

---

**Summary Checklist for Workflow Discipline**:
- [ ] Did I create the correct specification documentation?
- [ ] Did I enforce Test-Driven Development (TDD) via my task checklists?
- [ ] Did I check the constitution?
- [ ] *Crucially, did I fill out the `{{VARIABLES}}` in the `.prompt.md` Prompt History Records for EVERY stage?* All templates MUST be written to before moving on!
