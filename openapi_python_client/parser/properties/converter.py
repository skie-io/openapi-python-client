"""Utils for converting default values into valid Python"""

__all__ = ["convert", "convert_chain"]

import datetime
from collections.abc import Callable, Iterable
from typing import Any

from ... import utils
from ..errors import ValidationError


def convert(type_string: str, value: Any) -> Any | None:
    """
    Used by properties to convert some value into a valid value for the type_string.

    Args:
        type_string: The string of the actual type that this default will be in the generated client.
        value: The default value to try to convert.

    Returns:
        The converted value if conversion was successful, or None of the value was None.

    Raises:
        ValidationError if value could not be converted for type_string.
    """
    if value is None:
        return None
    if type_string not in _CONVERTERS:
        raise ValidationError()
    try:
        return _CONVERTERS[type_string](value)
    except (KeyError, ValueError, AttributeError) as err:
        raise ValidationError from err


def convert_chain(type_strings: Iterable[str], value: Any) -> Any | None:
    """
    Used by properties which support multiple possible converters (Unions).

    Args:
        type_strings: Iterable of all the supported type_strings.
        value: The default value to try to convert.

    Returns:
        The converted value if conversion was successful, or None of the value was None.

    Raises:
        ValidationError if value could not be converted for type_string.
    """
    for type_string in type_strings:
        try:
            val = convert(type_string, value)
            return val
        except ValidationError:
            continue
    raise ValidationError()


def _convert_string(value: Any) -> str | None:
    if isinstance(value, str):
        value = utils.remove_string_escapes(value)
    return repr(value)


def _convert_datetime(value: str) -> str | None:
    datetime.datetime.fromisoformat(value)  # Make sure it works
    return f"datetime.datetime.fromisoformat({value!r})"


def _convert_date(value: str) -> str | None:
    datetime.date.fromisoformat(value)
    return f"datetime.date.fromisoformat({value!r})"


_CONVERTERS: dict[str, Callable[[Any], Any | None]] = {
    "str": _convert_string,
    "datetime.datetime": _convert_datetime,
    "datetime.date": _convert_date,
    "float": float,
    "int": int,
    "bool": bool,
}
