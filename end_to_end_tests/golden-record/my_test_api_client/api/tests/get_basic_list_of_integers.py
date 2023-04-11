from http import HTTPStatus
from typing import Any, Dict, List, cast

import httpx
import orjson

from ... import errors
from ...client import Client
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/tests/basic_lists/integers",
    }

    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> List[int]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(List[int], orjson.loads(response.content))

        return response_200
    else:
        raise errors.UnexpectedStatus(response)


def _build_response(*, client: Client, response: httpx.Response) -> Response[List[int]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[List[int]]:
    """Get Basic List Of Integers

     Get a list of integers

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[int]]
    """

    kwargs = _get_kwargs()

    response = client.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
) -> List[int]:
    """Get Basic List Of Integers

     Get a list of integers

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List[int]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[List[int]]:
    """Get Basic List Of Integers

     Get a list of integers

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[int]]
    """

    kwargs = _get_kwargs()

    response = await client.async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
) -> List[int]:
    """Get Basic List Of Integers

     Get a list of integers

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List[int]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
