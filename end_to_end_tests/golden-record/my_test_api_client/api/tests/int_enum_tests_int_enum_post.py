from http import HTTPStatus
from typing import Any, Dict, Union, cast

import httpx
import orjson

from ... import errors
from ...client import Client
from ...models.an_int_enum import AnIntEnum
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    int_enum: AnIntEnum,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    json_int_enum = int_enum.value

    params["int_enum"] = json_int_enum

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": "/tests/int_enum",
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Union[Any, HTTPValidationError]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, orjson.loads(response.content))
        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(orjson.loads(response.content))

        return response_422
    else:
        raise errors.UnexpectedStatus(response)


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    int_enum: AnIntEnum,
) -> Response[Union[Any, HTTPValidationError]]:
    """Int Enum

    Args:
        int_enum (AnIntEnum): An enumeration.

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        int_enum=int_enum,
    )

    response = client.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    int_enum: AnIntEnum,
) -> Union[Any, HTTPValidationError]:
    """Int Enum

    Args:
        int_enum (AnIntEnum): An enumeration.

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        int_enum=int_enum,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    int_enum: AnIntEnum,
) -> Response[Union[Any, HTTPValidationError]]:
    """Int Enum

    Args:
        int_enum (AnIntEnum): An enumeration.

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        int_enum=int_enum,
    )

    response = await client.async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    int_enum: AnIntEnum,
) -> Union[Any, HTTPValidationError]:
    """Int Enum

    Args:
        int_enum (AnIntEnum): An enumeration.

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            int_enum=int_enum,
        )
    ).parsed
