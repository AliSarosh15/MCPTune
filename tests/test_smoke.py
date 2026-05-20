from mcptune import MCPTune

def test_tune_runs():
    m = MCPTune(model="dummy-model", mcpserver="dummy-server")
    result = m.generate_dataset(tools=["tool_a"])

    assert result == [{"input": "hi", "output": "call tool_a"}]