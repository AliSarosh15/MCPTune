from mcptune.mcptune import MCPTune
from mcptune.schema.tools import ToolSpec, ToolParameter


def test_mcp_request_structure():
    m = MCPTune(model="x", mcpserver=None)

    tool = ToolSpec(
        name="weather",
        description="",
        parameters=[]
    )

    req = m.build_mcp_request(tool, {"city": "Porto"})

    assert req["jsonrpc"] == "2.0"
    assert req["method"] == "tools/call"
    assert req["params"]["name"] == "weather"
    assert req["params"]["arguments"]["city"] == "Porto"