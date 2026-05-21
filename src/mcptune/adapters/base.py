from abc import ABC, abstractmethod

from mcptune.schema.tools import ToolSpec


class MCPAdapter(ABC):
    @abstractmethod
    async def discover_tools(self) -> list[ToolSpec]:
        pass

    @abstractmethod
    async def call_tool(self, tool_name: str, arguments: dict) -> dict:
        pass


#        request = {
#            "jsonrpc": "2.0",
#            "id": 1,
#            "method": "tools/call",
#            "params": {
#                "name": tool_name,
#                "arguments": {
#                    param.name: f"<{param.type}>"
#                    for param in arguments
#                }
#            }
#        }
