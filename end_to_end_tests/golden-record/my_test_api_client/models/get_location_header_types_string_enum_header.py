from enum import Enum


class GetLocationHeaderTypesStringEnumHeader(str, Enum):
    ONE = "one"
    THREE = "three"
    TWO = "two"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def from_values(cls, *values: str) -> list["GetLocationHeaderTypesStringEnumHeader"]:
        return [cls(value) for value in values]
