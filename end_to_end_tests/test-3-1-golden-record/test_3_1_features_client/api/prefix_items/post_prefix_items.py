from http import HTTPStatus
from typing import Any, cast

import httpx
import orjson

from ... import errors
from ...client import Client
from ...models.post_prefix_items_body import PostPrefixItemsBody
from ...types import Response


def _get_kwargs(
    *,
    body: PostPrefixItemsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/prefixItems",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> str:
    if response.status_code == 200:
        response_200 = cast(str, orjson.loads(response.content))
        return response_200
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
    body: PostPrefixItemsBody,
) -> Response[str]:
    """
    Args:
        body (PostPrefixItemsBody):

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
    body: PostPrefixItemsBody,
) -> str:
    """
    Args:
        body (PostPrefixItemsBody):

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
    body: PostPrefixItemsBody,
) -> Response[str]:
    """
    Args:
        body (PostPrefixItemsBody):

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
    body: PostPrefixItemsBody,
) -> str:
    """
    Args:
        body (PostPrefixItemsBody):

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
