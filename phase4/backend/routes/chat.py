from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from sqlmodel import Session, select
from core.db import engine
from models import Conversation, Message

from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from agents.mcp.server import MCPServerStdio
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    print("WARNING: GOOGLE_API_KEY environment variable not set")

external_provider = AsyncOpenAI(
    api_key=GOOGLE_API_KEY or "DUMMY_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

model = OpenAIChatCompletionsModel(
    openai_client=external_provider,
    model="gemini-2.5-flash",
)

run_config = RunConfig(
    model=model,
    model_provider=external_provider,
    tracing_disabled=True
)

router = APIRouter()
class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[int] = None

class ChatResponse(BaseModel):
    conversation_id: int
    response: str

@router.post("/api/{user_id}/chat", response_model=ChatResponse)
async def chat_endpoint(user_id: str, req: ChatRequest):
    with Session(engine) as session:
        if req.conversation_id:
            convo = session.get(Conversation, req.conversation_id)
            if not convo or convo.user_id != user_id:
                raise HTTPException(status_code=404, detail="Conversation not found")
        else:
            convo = Conversation(user_id=user_id)
            session.add(convo)
            session.commit()
            session.refresh(convo)

        user_msg = Message(
            conversation_id=convo.id,
            user_id=user_id,
            role="user",
            content=req.message
        )
        session.add(user_msg)
        session.commit()
        
        history = session.exec(
            select(Message).where(Message.conversation_id == convo.id).order_by(Message.created_at)
        ).all()

    # Build prompt with exact current user ID to ensure the agent uses it for filtering/scoping
    prompt = f"System constraint: The current user's ID is '{user_id}'. You must use this user_id in all tool calls.\n"
    prompt += "Conversation Context:\n"
    for msg in history[:-1]:
        prompt += f"{msg.role}: {msg.content}\n"
    prompt += f"User: {req.message}\n"
    prompt += "Please process the user's message, use tools if needed, and respond."

    # Execute the agent
    # Agent typically needs API key. We surround with try/except in case OPENAI_API_KEY is not set.
    try:
        server = MCPServerStdio(
            name="TodoMCPServer",
            params={
                "command": "uv",
                "args": ["run", "python", "mcp_server.py"],
                "cwd": os.getcwd(),
                "env": dict(os.environ)
            }
        )
        async with server:
            agent = Agent(
                name="TodoAgent",
                instructions="You are a helpful todo assistant. Use the provided tools to manage tasks for the user. Return a concise, friendly response confirming actions. Ensure you pass the correct user_id when using tools.",
                mcp_servers=[server]
            )
            result = await Runner.run(agent, input=prompt, run_config=run_config)
            response_text = result.final_output if hasattr(result, 'final_output') else str(result)
    except Exception as e:
        response_text = f"Error communicating with AI: {str(e)}"

    # Save Assistant response
    with Session(engine) as session:
        asst_msg = Message(
            conversation_id=convo.id,
            user_id=user_id,
            role="assistant",
            content=response_text
        )
        session.add(asst_msg)
        session.commit()

    return ChatResponse(
        conversation_id=convo.id,
        response=response_text
    )
