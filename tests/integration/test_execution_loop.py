# tests/conftest.py
import pytest
from fastmcp import FastMCP

from mcptune import MCPTune
from mcptune.adapters.fastmcp import FastMCPAdapter


@pytest.fixture
def fastmcp_server():
    mcp = FastMCP("test-server")

    @mcp.tool
    def get_weather(city: str) -> str:
        """Get weather for a city"""
        return f"Weather for {city}"

    @mcp.tool
    def add(a: int, b: int) -> int:
        """Add two integers"""
        return a + b

    return mcp


@pytest.fixture
def adapter(fastmcp_server):
    return FastMCPAdapter(fastmcp_server)


@pytest.fixture
def tuner(fastmcp_server):
    return MCPTune(model="test-model", mcpserver=fastmcp_server)
