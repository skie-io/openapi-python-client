from enum import Enum


class AnotherAllOfSubModelType(str, Enum):
    SUBMODEL = "submodel"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def from_values(cls, *values: str) -> list["AnotherAllOfSubModelType"]:
        return [cls(value) for value in values]
