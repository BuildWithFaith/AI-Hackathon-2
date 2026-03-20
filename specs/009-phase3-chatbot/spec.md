# Feature Specification: AI-Powered Todo Chatbot

**Feature Branch**: `009-phase3-chatbot`  
**Created**: 2026-03-20  
**Status**: Draft  
**Input**: User description: "AI-Powered Todo Chatbot integrating OpenAI ChatKit, Agents SDK and MCP tools"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add a Task via Natural Language (Priority: P1)

As a user, I want to tell the chatbot to remember a task (e.g., "Remind me to buy groceries"), so that it automatically creates a todo item without me filling out a form.

**Why this priority**: Core functionality of an AI-powered todo app is converting intent to tasks.

**Independent Test**: Can be fully tested by sending a message to the `/api/{user_id}/chat` endpoint and verifying a new task is created using the `add_task` MCP tool.

**Acceptance Scenarios**:

1. **Given** a stateless chat session, **When** I say "Add a task to buy groceries", **Then** the AI agent calls `add_task` with title "Buy groceries" and responds confirming the action.

---

### User Story 2 - View Pending Tasks (Priority: P2)

As a user, I want to ask the chatbot what I have left to do, so I can get a summary of pending tasks.

**Why this priority**: Essential for users to retrieve their existing tasks in a conversational manner.

**Independent Test**: Can be tested by asking "What tasks are pending?" and verifying the AI calls `list_tasks` with `status: "pending"`.

**Acceptance Scenarios**:

1. **Given** pending tasks exist, **When** I ask "What is pending?", **Then** the AI calls `list_tasks` and replies with a summary of pending tasks.

---

### User Story 3 - Manage Existing Tasks (Update/Complete/Delete) (Priority: P2)

As a user, I want to tell the chatbot to mark a task as complete, rename it, or delete it, so I can manage my list conversationally.

**Why this priority**: Enables full CRUD via chat, making the UI optional.

**Independent Test**: Test by asking to complete task 3, then verifying via `complete_task` tool.

**Acceptance Scenarios**:

1. **Given** an open task, **When** I say "Mark task 3 as complete", **Then** the AI calls `complete_task` and confirms.
2. **Given** a task, **When** I say "Delete the meeting task", **Then** the AI may list tasks to find the ID, then calls `delete_task` and confirms.

### Edge Cases

- What happens when a user asks to delete a task that doesn't exist? The AI should gracefully report the error.
- How does system handle vague prompts like "Remind me"? It should ask for clarification on the task title.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST integrate OpenAI Agents SDK and Official MCP SDK in the FastAPI backend.
- **FR-002**: System MUST provide a stateless POST `/api/{user_id}/chat` endpoint that saves conversation and message history to the Neon database.
- **FR-003**: System MUST expose 5 MCP tools: `add_task`, `list_tasks`, `complete_task`, `delete_task`, `update_task`.
- **FR-004**: System MUST integrate Next.js frontend with OpenAI ChatKit.
- **FR-005**: AI Agents MUST perform operations solely via the provided MCP tools.

### Key Entities

- **Task**: Includes user_id, title, description, completed status, etc.
- **Conversation**: Represents a chat session (user_id, id, timestamps).
- **Message**: Represents a single turn in a conversation (user_id, conversation_id, role, content).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can successfully create a task via natural language in under 5 seconds response time.
- **SC-002**: AI correctly maps user intents (Add, List, Update, Complete, Delete) to the correct MCP tools 95%+ of the time.
