from mcptune.mcptune import MCPTune


class FakeServer:
    async def list_tools(self):
        class Tool:
            name = "echo"
            description = "echo tool"
            parameters = {
                "properties": {
                    "msg": {"type": "string"}
                },
                "required": []
            }

        return [Tool()]


def test_full_pipeline_runs():
    server = FakeServer()
    m = MCPTune(model="test", mcpserver=server)

    tools = m.adapter.server.list_tools()
    assert tools is not None