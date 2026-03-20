To test and run both the frontend and backend for Phase 2 locally, you will need to start two separate terminal sessions. Since you just ran pnpm i, your frontend development environment is fully prepared!

1. Start the FastAPI Backend (Terminal 1)
Open a new terminal and run the following commands to start the backend server on port 8000. Passing the --env-file flag ensures uvicorn picks up your Neon database connection string from the root .env:

bash
cd phase2/backend
uv run uvicorn main:app --reload --port 8000 --env-file ../.env
(Note: Our system automatically initializes the SQLModel tables in Neon DB the moment the FastAPI app starts! Ensure your 

phase2/.env
 file has the actual working CONNECTION_STRING or DATABASE_URL)

2. Start the Next.js Frontend (Terminal 2)
In your current terminal (or a second terminal window), start the Next.js development server:

bash
cd phase2/frontend
pnpm dev
3. Verify the Integration
Once both servers are running:

Open your browser and navigate to http://localhost:3000.
The app will automatically redirect you to the secure authentication flow (/sign-in or /sign-up).
Create a new account to test the Better Auth signing and JWT generation.
You will be redirected to your minimal Task Dashboard. From here, test creating, completing, deleting, and filtering tasks!
