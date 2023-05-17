from enum import Enum


class AnAllOfEnum(str, Enum):
    A_DEFAULT = "a_default"
    BAR = "bar"
    FOO = "foo"
    OVERRIDDEN_DEFAULT = "overridden_default"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def from_values(cls, *values: str) -> list["AnAllOfEnum"]:
        return [cls(value) for value in values]
