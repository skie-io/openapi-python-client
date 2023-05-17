from enum import Enum
from typing import List


class AnotherAllOfSubModelType(str, Enum):
    SUBMODEL = "submodel"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def from_values(cls, *values: str) -> List["AnotherAllOfSubModelType"]:
        return [cls(value) for value in values]
