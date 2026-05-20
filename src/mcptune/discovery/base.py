from typing import Protocol
from discovery import Tool
from core import ToolSpec


class MCPServerProtocol(Protocol):
    def list_tools(self) -> list[ToolSpec]:
        return []

    def call_tool(self, name: str, args: dict) -> any:
        return -1