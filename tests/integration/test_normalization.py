import pytest

from mcptune.adapters.fastmcp import FastMCPAdapter


class FakeContentBlock:
    """Stand-in for a FastMCP pydantic content block."""

    def __init__(self, payload: dict):
        self._payload = payload

    def model_dump(self) -> dict:
        return self._payload


class FakeCallToolResult:
    """Stand-in for fastmcp.CallToolResult, no FastMCP dependency."""

    def __init__(self, content, structured_content, is_error):
        self.content = content
        self.structured_content = structured_content
        self.is_error = is_error


@pytest.mark.unit
def test_normalize_packs_three_contract_fields():
    adapter = FastMCPAdapter(server=None)
    fake = FakeCallToolResult(
        content=[FakeContentBlock({"type": "text", "text": "hi"})],
        structured_content={"result": 5},
        is_error=False,
    )

    out = adapter._normalize_response(fake)

    assert set(out.keys()) == {"content", "structured_content", "is_error"}
    assert out["content"] == [{"type": "text", "text": "hi"}]
    assert out["structured_content"] == {"result": 5}
    assert out["is_error"] is False


@pytest.mark.unit
def test_normalize_preserves_tool_level_error():
    adapter = FastMCPAdapter(server=None)
    fake = FakeCallToolResult(
        content=[FakeContentBlock({"type": "text", "text": "boom"})],
        structured_content=None,
        is_error=True,
    )

    out = adapter._normalize_response(fake)

    assert out["is_error"] is True
    assert out["structured_content"] is None
