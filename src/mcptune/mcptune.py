
import uuid
from dataclasses import replace

from mcptune.sampling.primitive import PrimitiveSampler
from mcptune.schema.dataset import DatasetRow

from .adapters.fastmcp import FastMCPAdapter
from .schema import ToolSpec


class MCPTune:
    def __init__(self, model: str, mcpserver, adapter=None):
        self.model = model
        self.mcpserver = mcpserver
        self.adapter = adapter or FastMCPAdapter(mcpserver)
        self.sampler = PrimitiveSampler()

    async def discover(self):
        """Discover tools from the MCP server and convert them to our internal Tool representation"""
        # print("[1] Discovering tools...")
        # tools = await self.mcpserver.list_tools()

        return await self.adapter.discover_tools()

        # toolsdef = [ Tool(
        #                name=t.name,
        #                description=t.description,
        #                parameters=self.extract_parameters(t.parameters),
        #                outputSchema=self.extract_output_schema(t.output_schema)
        #                ) for t in tools
        #            ]

        # return toolsdef

    def build_dataset(self, tools: list[ToolSpec]) -> list[DatasetRow]:
        dataset = []

        for tool in tools:
            arguments = self.build_arguments(tool)

            request = self.build_mcp_request(tool, arguments)

            dataset.append(DatasetRow(tool_name=tool.name, arguments=arguments, request=request))

        return dataset

    def build_arguments(self, tool: ToolSpec) -> dict:
        args = {}

        for param in tool.parameters:
            args[param.name] = self.sampler.sample(param.schema)

        return args

    def build_mcp_request(self, tool: ToolSpec, arguments: dict) -> dict:
        return {
            "jsonrpc": "2.0",
            "id": str(uuid.uuid4()),
            "method": "tools/call",
            "params": {"name": tool.name, "arguments": arguments},
        }

    async def execute_dataset(self, rows: list[DatasetRow]) -> list[DatasetRow]:
        executed = []
        for row in rows:
            try:
                response = await self.adapter.call_tool(row.tool_name, row.arguments)
                executed.append(replace(row, response=response))
            except Exception as e:
                executed.append(replace(row, error=f"{type(e).__name__}: {e}"))
        return executed

    def train(self, dataset):
        print("[3] Training model...")
        return "trained-model"

    def evaluate(self, model):
        print("[4] Evaluating model...")
        return {"accuracy": 0.9}

    async def run(self):
        tools = await self.discover()
        dataset = self.build_dataset(tools)
        model = self.train(dataset)
        metrics = self.evaluate(model)

        print("Done:", metrics)
        return model, metrics
