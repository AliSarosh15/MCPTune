
import json


def build_http_requests(tools):
    """
    Build example MCP HTTP requests from ToolSpec objects.
    """

    requests = []

    for tool in tools:
        request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {
                "name": tool.name,
                "arguments": {
                    param.name: f"<{param.type}>"
                    for param in tool.parameters
                }
            }
        }

        requests.append(json.dumps(request, indent=2))

    return requests


def build_stdio_dataset(tools):
    """Build a dataset for training the model using stdio interactions with the MCP server"""
    return build_http_requests(tools)