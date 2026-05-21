import asyncio

import uuid

from .schema import ToolSpec, ToolParameter
from .adapters.fastmcp import FastMCPAdapter
from .utils import build_http_requests, build_stdio_dataset
from mcptune.sampling.primitive import PrimitiveSampler
from mcptune.schema.dataset import DatasetRow

class MCPTune:
    def __init__(self, model: str, mcpserver, adapter=None):
        self.model = model
        self.mcpserver = mcpserver
        self.adapter = adapter or FastMCPAdapter(mcpserver)
        self.sampler = PrimitiveSampler()

    async def discover(self):
        """Discover tools from the MCP server and convert them to our internal Tool representation"""
        #print("[1] Discovering tools...")
        #tools = await self.mcpserver.list_tools()

        return await self.adapter.discover_tools()

        #toolsdef = [ Tool(
        #                name=t.name, 
        #                description=t.description, 
        #                parameters=self.extract_parameters(t.parameters), 
        #                outputSchema=self.extract_output_schema(t.output_schema)
        #                ) for t in tools
        #            ]

        #return toolsdef

    def build_dataset(self, tools: list[ToolSpec]) -> list[DatasetRow]:
        dataset = []

        for tool in tools:
            arguments = self.build_arguments(tool)

            request = self.build_mcp_request(tool, arguments)

            dataset.append(
                DatasetRow(
                    tool_name=tool.name,
                    arguments=arguments,
                    request=request
                )
            )

        return dataset
    
    def extract_parameters(self, parameters):
        """Convert MCP server tool parameters to our internal ToolParameter representation"""
        params = []
        for param in parameters["properties"]:
            params.append(ToolParameter(name=param, schema=parameters, required = param in parameters['required'], description=""))

        return params

    def build_arguments(self, tool: ToolSpec) -> dict:
        args = {}

        for param in tool.parameters:
            args[param.name] = self.sampler.sample(param.schema)

        return args

    def extract_output_schema(self, output_schema):
        """Convert MCP server tool output schema to our internal ToolParameter representation"""
        returnables = []
        for param in output_schema["properties"]:
            returnables.append(ToolParameter(name=param, schema=output_schema, required=param in output_schema['required'], description=""))
        return returnables[0] if returnables else None

   
    def build_mcp_request(self, tool: ToolSpec, arguments: dict) -> dict:
        return {
            "jsonrpc": "2.0",
            "id": str(uuid.uuid4()),
            "method": "tools/call",
            "params": {
                "name": tool.name,
                "arguments": arguments
            }
        }

    def train(self, dataset):
        print("[3] Training model...")
        return "trained-model"

    def evaluate(self, model):
        print("[4] Evaluating model...")
        return {"accuracy": 0.9}

    async def run(self):
        tools = await self.discover()
        dataset = await self.build_mcp_requests(tools)
        model = self.train(dataset)
        metrics = self.evaluate(model)

        print("Done:", metrics)
        return model, metrics
    

