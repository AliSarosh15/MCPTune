# tests/mcp/mock_server.py


class MockMCPServer:
    def __init__(self):
        self.tools = {
            "add": self.add,
            "echo": self.echo,
        }

    def list_tools(self):
        return list(self.tools.keys())

    def call_tool(self, name, args):
        return self.tools[name](**args)

    def add(self, a, b):
        return a + b

    def echo(self, text):
        return text
