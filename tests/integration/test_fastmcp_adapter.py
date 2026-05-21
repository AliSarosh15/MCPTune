import pytest

from mcptune.schema.tools import ToolParameter, ToolSpec


@pytest.mark.integration
async def test_discover_tools_returns_toolspecs(adapter):
    tools = await adapter.discover_tools()

    assert isinstance(tools, list)
    assert len(tools) == 2
    assert all(isinstance(tool, ToolSpec) for tool in tools)


@pytest.mark.integration
async def test_tool_metadata_is_extracted(adapter):
    tools = await adapter.discover_tools()

    weather = next(t for t in tools if t.name == "get_weather")

    assert weather.description != ""
    assert len(weather.parameters) == 1

    param = weather.parameters[0]
    assert isinstance(param, ToolParameter)
    assert param.name == "city"
    assert param.schema["type"] == "string"
    assert param.required is True


@pytest.mark.integration
async def test_raw_schema_is_preserved(adapter):
    tools = await adapter.discover_tools()
    weather = next(t for t in tools if t.name == "get_weather")

    assert weather.raw_input_schema is not None
    assert "properties" in weather.raw_input_schema


@pytest.mark.integration
async def test_call_tool_executes_and_returns_result(adapter):
    result = await adapter.call_tool("add", {"a": "2", "b": 3})

    assert result["structured_content"]["result"] == 5
    assert result["is_error"] is False
