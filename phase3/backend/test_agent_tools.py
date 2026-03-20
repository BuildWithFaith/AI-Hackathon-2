import asyncio
from mcp_server import add_task, list_tasks, complete_task, delete_task, update_task
from agents import Agent, Runner

agent = Agent(name="test", tools=[add_task, list_tasks, complete_task, delete_task, update_task])
print("Agent tools loaded successfully:", len(agent.tools))
