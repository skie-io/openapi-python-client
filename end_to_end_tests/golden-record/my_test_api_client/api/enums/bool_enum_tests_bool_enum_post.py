from http import HTTPStatus
from typing import Any, Dict

import httpx

from ... import errors
from ...client import Client
from ...types import UNSET, Response


def _get_kwargs(
    *,
    bool_enum: bool,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["bool_enum"] = bool_enum

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/enum/bool",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> Any:
    if response.status_code == HTTPStatus.OK:
        return None
    else:
        raise errors.UnexpectedStatus(response)


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    bool_enum: bool,
) -> Response[Any]:
    """Bool Enum

    Args:
        bool_enum (bool):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        bool_enum=bool_enum,
    )

    response = client.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Client,
    bool_enum: bool,
) -> Response[Any]:
    """Bool Enum

    Args:
        bool_enum (bool):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        bool_enum=bool_enum,
    )

    response = await client.async_request(**kwargs)

    return _build_response(client=client, response=response)
