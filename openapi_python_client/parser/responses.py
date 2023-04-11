__all__ = ["Response", "response_from_data"]

from http import HTTPStatus
from typing import Optional, Tuple, Union

from attrs import define

from openapi_python_client import utils

from .. import Config
from .. import schema as oai
from ..utils import PythonIdentifier
from .errors import ParseError, PropertyError
from .properties import AnyProperty, Property, Schemas, property_from_data


@define
class Response:
    """Describes a single response for an endpoint"""

    status_code: HTTPStatus
    prop: Property
    source: str


def _source_by_content_type(content_type: str) -> Optional[str]:
    content_type = utils.get_content_type(content_type)

    known_content_types = {
        "application/json": "orjson.loads(response.content)",
        "application/octet-stream": "response.content",
        "text/html": "response.text",
    }
    source = known_content_types.get(content_type)
    if source is None and content_type.endswith("+json"):
        # Implements https://www.rfc-editor.org/rfc/rfc6838#section-4.2.8 for the +json suffix
        source = "orjson.loads(response.content)"
    return source


def empty_response(
    *, status_code: HTTPStatus, response_name: str, config: Config, description: Optional[str]
) -> Response:
    """Return an untyped response, for when no response type is defined"""
    return Response(
        status_code=status_code,
        prop=AnyProperty(
            name=response_name,
            default=None,
            nullable=False,
            required=True,
            python_name=PythonIdentifier(value=response_name, prefix=config.field_prefix),
            description=description,
            example=None,
        ),
        source="None",
    )


def response_from_data(
    *,
    status_code: HTTPStatus,
    data: Union[oai.Response, oai.Reference],
    schemas: Schemas,
    parent_name: str,
    config: Config,
) -> Tuple[Union[Response, ParseError], Schemas]:
    """Generate a Response from the OpenAPI dictionary representation of it"""

    response_name = f"response_{status_code}"
    if isinstance(data, oai.Reference):
        return (
            empty_response(status_code=status_code, response_name=response_name, config=config, description=None),
            schemas,
        )

    content = data.content
    if not content:
        return (
            empty_response(
                status_code=status_code, response_name=response_name, config=config, description=data.description
            ),
            schemas,
        )

    for content_type, media_type in content.items():
        source = _source_by_content_type(content_type)
        if source is not None:
            schema_data = media_type.media_type_schema
            break
    else:
        return ParseError(data=data, detail=f"Unsupported content_type {content}"), schemas

    if schema_data is None:
        return (
            empty_response(
                status_code=status_code, response_name=response_name, config=config, description=data.description
            ),
            schemas,
        )

    prop, schemas = property_from_data(
        name=response_name,
        required=True,
        data=schema_data,
        schemas=schemas,
        parent_name=parent_name,
        config=config,
    )

    if isinstance(prop, PropertyError):
        return prop, schemas

    return Response(status_code=status_code, prop=prop, source=source), schemas
