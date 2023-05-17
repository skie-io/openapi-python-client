from enum import Enum
from typing import List


class AnAllOfEnum(str, Enum):
    A_DEFAULT = "a_default"
    BAR = "bar"
    FOO = "foo"
    OVERRIDDEN_DEFAULT = "overridden_default"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def from_values(cls, *values: str) -> List["AnAllOfEnum"]:
        return [cls(value) for value in values]
