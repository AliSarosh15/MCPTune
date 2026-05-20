from dataclasses import dataclass
from typing import Any


@dataclass
class ToolParameter:
    name: str
    type: str
    required: bool
    description: str


@dataclass
class Tool:
    name: str
    description: str
    parameters: list[ToolParameter]