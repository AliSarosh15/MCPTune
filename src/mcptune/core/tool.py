from dataclasses import dataclass
@dataclass


@dataclass
class ToolSpec:
    name: str
    description: str
    parameters: dict[str, str]

