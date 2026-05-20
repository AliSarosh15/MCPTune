from typing import Protocol


class MCPServerProtocol(Protocol):
    def list_tools(self) -> list[str]:
        return []

    def call_tool(self, name: str, args: dict):
        return -1