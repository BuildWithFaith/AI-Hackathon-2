# Phase 3 Frontend - AI Hub 💬

This is the frontend for Phase 3 of the AI Todo App setup, built with Next.js and Tailwind CSS. It introduces an interactive Chat UI to communicate with our FastAPI agent.

## Setup & Requirements

1. Ensure you have Node.js and `pnpm` installed.
2. Install the dependencies:
   ```bash
   pnpm install
   ```

## Running the Frontend

To start the Next.js development server:
```bash
pnpm dev
```

The application will be accessible at `http://localhost:3000`. Navigate to the AI Chat page via the dashboard to try communicating with the Todo AI Assistant!

## Details
- Integrates `better-auth` for identifying the current user inside the chat pane.
- Connects to the backend via standard REST endpoint at `POST /api/{user_id}/chat`.
