from http import HTTPStatus
from typing import Any, Dict, cast

import httpx
import orjson

from ... import errors
from ...client import Client
from ...types import Response


def _get_kwargs(
    *,
    body: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/config/content-type-override",
    }

    _body = body

    _kwargs["json"] = _body
    headers["Content-Type"] = "openapi/python/client"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> str:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(str, orjson.loads(response.content))
        return response_200
    else:
        raise errors.UnexpectedStatus(response)


def _build_response(*, client: Client, response: httpx.Response) -> Response[str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    body: str,
) -> Response[str]:
    """Content Type Override

    Args:
        body (str):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    body: str,
) -> str:
    """Content Type Override

    Args:
        body (str):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    body: str,
) -> Response[str]:
    """Content Type Override

    Args:
        body (str):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    body: str,
) -> str:
    """Content Type Override

    Args:
        body (str):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
