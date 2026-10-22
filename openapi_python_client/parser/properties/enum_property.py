__all__ = ["EnumProperty"]

from typing import Any, ClassVar, cast

from attrs import define, field

from ... import schema as oai
from ... import utils
from .property import Property
from .schemas import Class

ValueType = str | int


@define
class EnumProperty(Property):
    """A property that should use an enum"""

    values: dict[str, ValueType]
    class_info: Class
    value_type: type[ValueType]
    default: Any | None = field()

    template: ClassVar[str] = "enum_property.py.jinja"

    _allowed_locations: ClassVar[set[oai.ParameterLocation]] = {
        oai.ParameterLocation.QUERY,
        oai.ParameterLocation.PATH,
        oai.ParameterLocation.COOKIE,
        oai.ParameterLocation.HEADER,
    }

    def get_base_type_string(self, *, quoted: bool = False) -> str:
        return self.class_info.name

    def get_base_json_type_string(self, *, quoted: bool = False) -> str:
        return self.value_type.__name__

    def get_imports(self, *, prefix: str) -> set[str]:
        """
        Get a set of import strings that should be included when this property is used somewhere

        Args:
            prefix: A prefix to put before any relative (local) module names. This should be the number of . to get
            back to the root of the generated client.
        """
        imports = super().get_imports(prefix=prefix)
        imports.add(f"from {prefix}models.{self.class_info.module_name} import {self.class_info.name}")
        return imports

    @staticmethod
    def values_from_list(values: list[str] | list[int]) -> dict[str, ValueType]:
        """Convert a list of values into dict of {name: value}, where value can sometimes be None"""
        output: dict[str, ValueType] = {}

        for i, value in enumerate(values):
            value = cast(str | int, value)
            if isinstance(value, int):
                if value < 0:
                    output[f"VALUE_NEGATIVE_{-value}"] = value
                else:
                    output[f"VALUE_{value}"] = value
                continue
            if value and value[0].isalpha():
                key = value.upper()
            else:
                key = f"VALUE_{i}"
            if key in output:
                raise ValueError(f"Duplicate key {key} in Enum")
            sanitized_key = utils.snake_case(key).upper()
            output[sanitized_key] = utils.remove_string_escapes(value)
        return output
