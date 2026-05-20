from mcptune import MCPTune
from tests.servers.mock_server import MockMCPServer

def test_tune_runs():
    m = MCPTune(model="dummy-model", mcpserver="dummy-server")
    model, metrics = m.run(m)

    assert model is not None 
    assert "accuracy" in metrics


def test_mcp_pipeline_integration():
    server = MockMCPServer()

    m = MCPTune(model="model", mcpserver=server)

    tools = m.discover()
    assert "add" in server.list_tools()

    dataset = m.build_dataset(tools)
    assert isinstance(dataset, list)

    model = m.train(dataset)
    assert model is not None