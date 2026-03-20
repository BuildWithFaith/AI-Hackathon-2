from mcp_server import mcp
import pytest

@pytest.mark.asyncio
async def test_mcp_tools_exist():
    tools = await mcp.list_tools()
    tool_names = [t.name for t in tools]
    assert "add_task" in tool_names
    assert "list_tasks" in tool_names
    assert "complete_task" in tool_names
    assert "delete_task" in tool_names
    assert "update_task" in tool_names
