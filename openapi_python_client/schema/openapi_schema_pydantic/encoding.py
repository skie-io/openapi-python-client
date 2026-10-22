from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict

from .reference import Reference

if TYPE_CHECKING:  # pragma: no cover
    from .header import Header


class Encoding(BaseModel):
    """A single encoding definition applied to a single schema property.

    References:
        - https://swagger.io/docs/specification/describing-request-body/
        - https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#encodingObject
    """

    contentType: str | None = None
    headers: dict[str, Union["Header", Reference]] | None = None
    style: str | None = None
    explode: bool = False
    allowReserved: bool = False
    model_config = ConfigDict(
        # `Header` is an unresolvable forward reference, will rebuild in `__init__.py`:
        defer_build=True,
        extra="allow",
        json_schema_extra={
            "examples": [
                {
                    "contentType": "image/png, image/jpeg",
                    "headers": {
                        "X-Rate-Limit-Limit": {
                            "description": "The number of allowed requests in the current period",
                            "schema": {"type": "integer"},
                        }
                    },
                }
            ]
        },
    )
