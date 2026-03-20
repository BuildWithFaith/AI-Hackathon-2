# Implementation Plan: Phase 2 Full-Stack Web App

## Goal Description
Convert the CLI system from Phase 1 into a full-stack web application with persistent storage and secure authentication. The application will consist of a Next.js (App Router) frontend, a FastAPI backend, and a Neon Serverless PostgreSQL database. It will replace in-memory storage with SQLModel-driven DB persistence, and implement Better Auth with JWT for security.

## Proposed Changes

### Project Structure Setup
All work will be contained within the `phase2` directory to maintain hackathon organization requirements.
- **phase2/frontend/**: Next.js application root.
- **phase2/backend/**: FastAPI application root.
- **CLAUDE.md guidelines**: Add contextual instructions in both frontend and backend for Claude Code as outlined by the hackathon master sheet.

### Backend Data Layer (Neon Postgres & SQLModel)
- **`phase2/backend/db.py`**: Configure database connection using the Neon connection string from Phase 2's `.env`.
- **`phase2/backend/models.py`**: Define `Task` model inheriting from SQLModel. The model will require fields mapping identical schema definitions (id, user_id, title, description, completed, created_at, updated_at).
- **Database Migrations**: We will initialize the DB schema upon FastAPI startup or via an initialization script.

### Backend Authentication Middleware & API (FastAPI)
- **`phase2/backend/main.py`**: Entry point for FastAPI app. Add CORS middleware and JWT token verification middleware.
- **`phase2/backend/routes/tasks.py`**: Implement the following REST endpoints:
  - `GET /api/tasks`
  - `POST /api/tasks`
  - `PUT /api/tasks/{task_id}`
  - `DELETE /api/tasks/{task_id}`
  - `PATCH /api/tasks/{task_id}/complete`
- Each endpoint will extract `user_id` from the decoded Better Auth JWT and apply filters so users only interact with their own tasks.

### Frontend Application (Next.js & Better Auth)
- **`phase2/frontend/lib/auth.ts`**: Configure Better Auth with JWT token strategy. 
- **`phase2/frontend/lib/api.ts`**: Axios/Fetch client wrapper that automatically attaches the `Authorization: Bearer <token>` header, fetched from the Better Auth session, to all requests routed to the FastAPI backend.
- **Authentication Pages**: `sign-in`, `sign-up` UI using generic Tailwind components.
- **App Dashboard (`/app/dashboard`)**: The main interface listing tasks and allowing creation/editing of tasks. Built with Server/Client components optimally.

## Verification Plan

### Automated/Unit Tests
- **Backend Tests**: Create Pytest tests in `phase2/backend/tests` to validate the JWT decoding logic and the database CRUD operations against a test Neon branch or SQLite mock.
- **Linting & Formatting**: Ensure `ruff format` and `ruff check` pass cleanly over the backend codebase. Ensure ESLint passes on the Next.js frontend.

### Manual Verification
- Manually test user registration and login in the browser to ensure Better Auth is correctly signing JWTs.
- Create a task via the UI, verify it persists in the Neon database by selecting directly or via the API.
- Create two different users and verify User A cannot see User B's tasks in the dashboard.
