from enum import Enum
from typing import List


class DifferentEnum(str, Enum):
    DIFFERENT = "DIFFERENT"
    OTHER = "OTHER"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def from_values(cls, *values: str) -> List["DifferentEnum"]:
        return [cls(value) for value in values]
