from enum import Enum
from typing import List


class GetLocationHeaderTypesStringEnumHeader(str, Enum):
    ONE = "one"
    THREE = "three"
    TWO = "two"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def from_values(cls, *values: str) -> List["GetLocationHeaderTypesStringEnumHeader"]:
        return [cls(value) for value in values]
