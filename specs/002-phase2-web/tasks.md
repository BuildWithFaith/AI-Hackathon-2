# Implementation Tasks: Phase 2 Web App

## Phase: Setup and Infrastructure
- [x] T001 [P] [US1] Create unit tests for DB connection logic
- [x] T002 [US1] Initialize FastAPI backend and SQLModel DB connection (`phase2/backend`)
- [/] T003 [P] [US1] Write test for verifying frontend Next.js routing and NextAuth/Better Auth API route
- [/] T004 [US1] Initialize Next.js 14 frontend project (`phase2/frontend`) and install `better-auth`

## Phase: Backend Database & Models
- [x] T005 [P] [US2] Write tests for User and Task model schema validation using SQLModel
- [x] T006 [US2] Define `User` and `Task` SQLModel models in `backend/models.py`
- [x] T007 [P] [US1] Create tests for JWT Decoding middleware in FastAPI
- [x] T008 [US1] Implement JWT Authentication middleware and inject into FastAPI router

## Phase: Backend API CRUD Routes
- [x] T009 [P] [US2] Create API tests for GET, POST, PUT, DELETE, and PATCH endpoints for Tasks
- [x] T010 [US2] Implement CRUD endpoints in FastAPI `backend/routes/tasks.py` ensuring `user_id` filtering
- [x] T011 [P] [US3] Create API tests validating that GET `/api/tasks?status=pending` filters properly
- [x] T012 [US3] Add `status` filtering support to GET `/api/tasks`

## Phase: Frontend Auth & Integration
- [x] T013 [P] [US1] E2E or Component test for SignIn and SignUp pages
- [x] T014 [US1] Build Next.js Auth pages (`/sign-in`, `/sign-up`) using Better Auth React hooks
- [x] T015 [P] [US2] Component tests for task creation form and task list
- [x] T016 [US2] Build Dashboard page (`/app/dashboard`) to list, create, and delete tasks
- [x] T017 [US2] Configure Axios/Fetch interceptor in `frontend/lib/api.ts` to attach Better Auth JWT Token
- [x] T018 [US3] Add Filter UI (All/Pending/Completed) to the dashboard connecting to the API filter logic
