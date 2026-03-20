# Phase 3 Backend - AI Agent & MCP 🤖

This is the backend for Phase 3, featuring an AI Todo Assistant integrated natively via the Model Context Protocol (MCP).

## Setup & Requirements

1. Make sure you have python and `uv` installed.
2. Inside `phase3/backend`, copy the `.env.example` to `.env` or configure your own `.env` file containing your `GOOGLE_API_KEY` for the AI model:
   ```bash
   cp .env.example .env
   # Add your key to .env
   ```
3. A Neon PostgreSQL database is used for persistence. The connection string `CONNECTION_STRING` should be included in your `.env`.

## Running the Backend

To start the backend server, run:
```bash
uv run fastapi dev main.py
```

The FastAPI application will start at `http://127.0.0.1:8000`. 
The AI Chat endpoint `/api/{user_id}/chat` will have access to all MCP tools locally over stdio integration.

## Available MCP Tools
- `add_task`
- `list_tasks`
- `complete_task`
- `delete_task`
- `update_task`
