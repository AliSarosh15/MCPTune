import pytest
from mcptune.sampling.primitive import PrimitiveSampler


@pytest.fixture
def sampler():
    return PrimitiveSampler()


def test_string_sampling_returns_str(sampler):
    value = sampler.sample({"type": "string"})
    assert isinstance(value, str)


def test_integer_sampling_returns_int(sampler):
    value = sampler.sample({"type": "integer"})
    assert isinstance(value, int)


def test_number_sampling_returns_float(sampler):
    value = sampler.sample({"type": "number"})
    assert isinstance(value, float)


def test_boolean_sampling_returns_bool(sampler):
    value = sampler.sample({"type": "boolean"})
    assert isinstance(value, bool)


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