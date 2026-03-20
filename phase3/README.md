# Phase 3: AI-Powered Todo Chatbot

This Phase introduces an intelligent conversational interface to the Todo Application, allowing users to interact with their tasks using natural language.

## Architecture

*   **Frontend (Next.js)**: Features a beautiful, custom-built Chat UI (`/chat`) using React, Lucide-React for iconography, and tailored CSS for a sleek glassmorphic experience.
*   **Backend (FastAPI)**: Introduces the Intelligence Layer using the **OpenAI Agents SDK**.
*   **MCP Server (FastMCP)**: Task operations (Add, List, Complete, Delete, Update) are exposed to the AI Agent via an Official Model Context Protocol (MCP) server natively integrated into the FastAPI backend.
*   **Database (Neon Serverless PostgreSQL)**: 
    *   State is managed seamlessly by tracking `Conversation` and `Message` models. 
    *   The platform utilizes `SQLModel` ORM mapping directly alongside Phase 2's `User` and `Task` schemas.

## Features

- **Natural Language Task Management**: Try saying "Add a task to buy groceries", "Mark my first task as complete", or "What tasks are pending right now?".
- **Context-Aware Memory**: The chatbot maintains conversational history stored persistently in PostgreSQL enabling follow-up questions and continued workflows across browser sessions.
- **Secure Contexts**: All MCP actions enforce `user_id` ownership validation out-of-the-box, ensuring users can only read or mutate their own tasks.

## How to Run

### Backend
1. Navigate to `phase3/backend`
2. Ensure your `.env` contains your Neon Database URL (`DATABASE_URL`) and your OpenAI API Key (`OPENAI_API_KEY`).
3. Install dependencies using `uv`: 
   ```bash
   uv sync
   ```
4. Start the FastAPI server: 
   ```bash
   uv run fastapi dev main.py
   ```

### Frontend
1. Navigate to `phase3/frontend`
2. Install dependencies:
   ```bash
   pnpm install
   ```
3. Start the Next.js development server:
   ```bash
   pnpm dev
   ```
4. Visit `http://localhost:3000/chat` to start messaging!
