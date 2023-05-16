from __future__ import annotations

import datetime
import sys
from typing import Any, ClassVar

from attr import define

from ...utils import PythonIdentifier
from ..errors import PropertyError
from .protocol import PropertyProtocol, Value


@define
class DateTimeProperty(PropertyProtocol):
    """
    A property of type datetime.datetime
    """

    name: str
    required: bool
    default: Value | None
    python_name: PythonIdentifier
    description: str | None
    example: str | None

    _type_string: ClassVar[str] = "datetime.datetime"
    _json_type_string: ClassVar[str] = "str"
    template: ClassVar[str] = "datetime_property.py.jinja"

    @classmethod
    def build(
        cls,
        name: str,
        required: bool,
        default: Any,
        python_name: PythonIdentifier,
        description: str | None,
        example: str | None,
    ) -> DateTimeProperty | PropertyError:
        checked_default = cls.convert_value(default)
        if isinstance(checked_default, PropertyError):
            return checked_default

        return DateTimeProperty(
            name=name,
            required=required,
            default=checked_default,
            python_name=python_name,
            description=description,
            example=example,
        )

    @classmethod
    def convert_value(cls, value: Any) -> Value | None | PropertyError:
        if value is None or isinstance(value, Value):
            return value
        if isinstance(value, str):
            try:
                _check_datetime(value)  # make sure it's a valid value
            except ValueError as e:
                return PropertyError(f"Invalid datetime: {e}")
            return Value(f"str_to_datetime({value!r})", raw_value=value)
        return PropertyError(f"Cannot convert {value} to a datetime")

    def get_imports(self, *, prefix: str) -> set[str]:
        """
        Get a set of import strings that should be included when this property is used somewhere

        Args:
            prefix: A prefix to put before any relative (local) module names. This should be the number of . to get
            back to the root of the generated client.
        """
        imports = super().get_imports(prefix=prefix)
        imports.update({"import datetime", f"from {prefix}datetime import str_to_datetime", "from typing import cast"})
        return imports


if sys.version_info >= (3, 11):

    def _check_datetime(datetime_str: str) -> datetime.datetime:
        return datetime.datetime.fromisoformat(datetime_str)

else:

    def _check_datetime(datetime_str: str) -> datetime.datetime:
        return datetime.datetime.fromisoformat(datetime_str.replace("Z", "+00:00"))
