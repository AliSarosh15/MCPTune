from dataclasses import dataclass, field
from typing import Any


@dataclass
class ToolParameter:
    name: str
    type: str
    required: bool
    description: str


@dataclass
class ToolSpec:
    name: str
    description: str
    parameters: list[ToolParameter]
    outputSchema: ToolParameter | None = None
    raw_input_schema: dict[str, Any] = field(default_factory=dict)