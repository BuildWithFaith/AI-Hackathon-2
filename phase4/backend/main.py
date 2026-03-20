from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from core.db import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize DB upon startup
    create_db_and_tables()
    yield

from routes.tasks import router as tasks_router
from routes.chat import router as chat_router

app = FastAPI(title="Phase 2 Web App Todo API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://192.168.1.5:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks_router)
app.include_router(chat_router)

@app.get("/")
def read_root():
    return {"message": "API is running"}

from core.db import engine
@app.get("/api/diagnostic-db")
def get_db_url():
    return {"url": str(engine.url)}
