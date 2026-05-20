from typing import Protocol
from discovery import Tool


class MCPServerProtocol(Protocol):
    def list_tools(self) -> list[Tool]:
        return []

    def call_tool(self, name: str, args: dict):
        return -1