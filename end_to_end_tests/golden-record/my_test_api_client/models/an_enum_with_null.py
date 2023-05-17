from enum import Enum


class AnEnumWithNull(str, Enum):
    FIRST_VALUE = "FIRST_VALUE"
    SECOND_VALUE = "SECOND_VALUE"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def from_values(cls, *values: str) -> list["AnEnumWithNull"]:
        return [cls(value) for value in values]
