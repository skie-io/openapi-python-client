from enum import Enum


class ModelWithMergedPropertiesStringToEnum(str, Enum):
    A = "a"
    B = "b"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def from_values(cls, *values: str) -> list["ModelWithMergedPropertiesStringToEnum"]:
        return [cls(value) for value in values]
