from dataclasses import dataclass
from typing import Any


@dataclass
class DatasetRow:
    tool_name: str
    arguments: dict
    request: dict