# Task Checklist: AI-Powered Todo Chatbot

## Setup & Dependencies
- [x] T001 [US1] Install `openai-agents` and `mcp` packages in the backend.
- [x] T002 [US1] Install OpenAI ChatKit in the frontend.

## Database & Models
- [x] T003 [P] [US1] Write validation tests for `Conversation` and `Message` models.
- [x] T004 [US1] Implement `Conversation` and `Message` SQLModel schemas in the backend.
- [x] T005 [US1] Generate and run Alembic migrations for the new schemas (handled by `create_db_and_tables`).

## MCP Server
- [x] T006 [P] [US1] Write unit tests for MCP tool endpoints (`add_task`, `list_tasks`, etc.).
- [x] T007 [US1] Implement `mcp_server.py` exposing the 5 required tools.
- [x] T008 [US2] Ensure `list_tasks` properly filters by `status` and `user_id`.
- [x] T009 [US3] Ensure `update_task`, `delete_task`, and `complete_task` enforce `user_id` ownership.

## Intelligence Layer (FastAPI)
- [x] T010 [P] [US1] Write API test for `POST /api/{user_id}/chat` endpoint rejecting invalid requests.
- [x] T011 [US1] Implement `routes/chat.py` utilizing the `openai-agents` SDK and the MCP server tools.
- [x] T012 [US1] Connect `chat.py` to `main.py` router.

## Frontend (Next.js)
- [x] T013 [US1] Add chat API client method in `frontend/lib/api.ts`.
- [x] T014 [US1] Build `chat/page.tsx` conversational UI using OpenAI ChatKit.
- [x] T015 [US1] Verify End-to-End flow of sending a natural language prompt and seeing the task created.
