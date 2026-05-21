from .discovery import Tool, ToolParameter
from .utils import build_http_requests, build_stdio_dataset

class MCPTune:
    def __init__(self, model: str, mcpserver):
        self.model = model
        self.mcpserver = mcpserver

    async def discover(self):
        """Discover tools from the MCP server and convert them to our internal Tool representation"""
        print("[1] Discovering tools...")
        tools = await self.mcpserver.list_tools()

        toolsdef = [ Tool(
                        name=t.name, 
                        description=t.description, 
                        parameters=self.extract_parameters(t.parameters), 
                        outputSchema=self.extract_output_schema(t.output_schema)
                        ) for t in tools
                    ]

        return toolsdef

    def extract_parameters(self, parameters):
        """Convert MCP server tool parameters to our internal ToolParameter representation"""
        params = []
        for param in parameters["properties"]:
            params.append(ToolParameter(name=param, type=parameters['properties'][param]['type'], required = param in parameters['required'], description=""))

        return params

    def extract_output_schema(self, output_schema):
        """Convert MCP server tool output schema to our internal ToolParameter representation"""
        returnables = []
        for param in output_schema["properties"]:
            returnables.append(ToolParameter(name=param, type=output_schema['properties'][param]['type'], required=param in output_schema['required'], description=""))
        return returnables[0] if returnables else None


    def build_mcp_request(self, tools, method="HTTP"):
        print("[2] Building MCP request...")
        if method == "HTTP":
            return build_http_requests(tools)
        elif method == "stdio":
            return build_stdio_dataset(tools)
        else:
            raise ValueError(f"Unknown dataset building method: {method}")
        

    def train(self, dataset):
        print("[3] Training model...")
        return "trained-model"

    def evaluate(self, model):
        print("[4] Evaluating model...")
        return {"accuracy": 0.9}

    def run(self):
        tools = self.discover()
        dataset = self.build_dataset(tools)
        model = self.train(dataset)
        metrics = self.evaluate(model)

        print("Done:", metrics)
        return model, metrics
    

