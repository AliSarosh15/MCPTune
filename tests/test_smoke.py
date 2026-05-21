from mcptune import MCPTune
from .servers.mock_server import MockMCPServer
from .servers.mock_fastmcp_server_01 import mcp as FastMCPServer
import asyncio

def test_tune_runs():
    m = MCPTune(model="dummy-model", mcpserver="dummy-server")
    model, metrics = asyncio.run(m.run())

    assert model is not None 
    assert "accuracy" in metrics

def test_discover_tools():
    m = MCPTune(model="model", mcpserver=FastMCPServer)

    tools = asyncio.run(m.discover())
    assert tools[0].name == "get_weather"
    assert tools[1].name == "calculator"


async def test_build_dataset():
    m = MCPTune(model="model", mcpserver=FastMCPServer)

    tools = await m.discover()
    dataset = await m.build_mcp_requests(tools)
    assert isinstance(dataset, list)
    assert len(dataset) == 3
    

async def test_mcp_pipeline_integration():
    server = MockMCPServer()

    m = MCPTune(model="model", mcpserver=server)

    tools = await m.discover()
    assert "add" in server.list_tools()

    dataset = await m.build_mcp_requests(tools)
    assert isinstance(dataset, list)

    model = m.train(dataset)
    assert model is not None