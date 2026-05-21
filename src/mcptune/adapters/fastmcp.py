from mcptune.adapters.base import MCPAdapter
from mcptune.schema.tools import ToolSpec, ToolParameter

import inspect

class FastMCPAdapter(MCPAdapter):

    def __init__(self, server):
        self.server = server

    async def discover_tools(self) -> list[ToolSpec]:
        if not hasattr(self.server, "list_tools"):
            return []

        result = self.server.list_tools()

        if inspect.isawaitable(result):
            tools = await result
        else:
            tools = result

        normalized = []

        for tool in tools:
            schema = getattr(tool, "parameters", {})

            props = schema.get("properties", {})
            required = schema.get("required", [])

            parameters = [
                ToolParameter(
                    name=name,
                    type=props[name].get("type", "unknown"),
                    required=name in required,
                    description=props[name].get("description", "")
                )
                for name in props
            ]

            normalized.append(
                ToolSpec(
                    name=tool.name,
                    description=tool.description,
                    parameters=parameters,
                    raw_input_schema=schema
                )
            )

        return normalized

    async def call_tool(
        self,
        tool_name: str,
        arguments: dict
    ) -> dict:

        result = self.server.call_tool(tool_name, arguments)

        if inspect.isawaitable(result):
            return await result
        return result

