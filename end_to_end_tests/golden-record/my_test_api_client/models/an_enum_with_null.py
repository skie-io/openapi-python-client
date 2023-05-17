from enum import Enum
from typing import List


class AnEnumWithNull(str, Enum):
    FIRST_VALUE = "FIRST_VALUE"
    SECOND_VALUE = "SECOND_VALUE"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def from_values(cls, *values: str) -> List["AnEnumWithNull"]:
        return [cls(value) for value in values]
