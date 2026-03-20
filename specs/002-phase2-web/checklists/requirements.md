# Requirements Checklist: Phase 2 Web App

**Purpose**: Validation checklist for Phase 2 web app requirements.
**Created**: 2026-03-20

## Functional Requirements

- [x] FR-001: System MUST authenticate users using Better Auth with JWT tokens on the Next.js frontend.
- [x] FR-002: System MUST validate JWT tokens on all FastAPI backend `api/tasks` routes using Next.js Better Auth secret.
- [x] FR-003: System MUST store users and tasks in Neon Serverless PostgreSQL.
- [x] FR-004: System MUST use SQLModel for ORM operations in the FastAPI backend.
- [x] FR-005: System MUST enforce that users can only view, update, or delete tasks assigned to their specific User ID.
