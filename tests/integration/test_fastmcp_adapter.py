import pytest

from fastmcp import FastMCP

from mcptune.adapters.fastmcp import FastMCPAdapter
from mcptune.schema.tools import ToolSpec, ToolParameter


@pytest.fixture
def mock_server():
    mcp = FastMCP("mock-server")

    @mcp.tool
    def get_weather(city: str) -> str:
        """Get weather for a city"""
        return f"Weather for {city}"

    @mcp.tool
    def add(a: int, b: int) -> int:
        """Add two integers"""
        return a + b

    return mcp


@pytest.mark.asyncio
async def test_discover_tools_returns_toolspecs(mock_server):

    adapter = FastMCPAdapter(mock_server)

    tools = await adapter.discover_tools()

    assert isinstance(tools, list)
    assert len(tools) == 2

    for tool in tools:
        assert isinstance(tool, ToolSpec)


@pytest.mark.asyncio
async def test_tool_metadata_is_extracted(mock_server):

    adapter = FastMCPAdapter(mock_server)

    tools = await adapter.discover_tools()

    weather_tool = next(
        tool for tool in tools
        if tool.name == "get_weather"
    )

    assert weather_tool.name == "get_weather"
    assert weather_tool.description != ""

    assert len(weather_tool.parameters) == 1

    parameter = weather_tool.parameters[0]

    assert isinstance(parameter, ToolParameter)

    assert parameter.name == "city"
    assert parameter.schema["type"] == "string"
    assert parameter.required is True


@pytest.mark.asyncio
async def test_raw_schema_is_preserved(mock_server):

    adapter = FastMCPAdapter(mock_server)

    tools = await adapter.discover_tools()

    weather_tool = next(
        tool for tool in tools
        if tool.name == "get_weather"
    )

    assert weather_tool.raw_input_schema is not None

    assert "properties" in weather_tool.raw_input_schema


@pytest.mark.asyncio
async def test_call_tool(mock_server):

    adapter = FastMCPAdapter(mock_server)

    result = await adapter.call_tool(
        "add",
        {
            "a": 2,
            "b": 3
        }
    )

    assert result.structured_content["result"] == 5