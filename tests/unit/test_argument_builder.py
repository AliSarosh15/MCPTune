from mcptune.schema.tools import ToolSpec, ToolParameter
from mcptune.mcptune import MCPTune


class DummySampler:
    def sample(self, schema):
        return "x"


def test_build_arguments_basic():
    tool = ToolSpec(
        name="test",
        description="",
        parameters=[
            ToolParameter(name="city", schema={"type": "string"}, required=True, description="")
        ]
    )

    m = MCPTune(model="x", mcpserver=None)
    m.sampler = DummySampler()

    args = m.build_arguments(tool)

    assert "city" in args
    assert args["city"] == "x"