from http import HTTPStatus
from typing import Any, Dict, List, cast

import httpx

from ... import errors
from ...client import Client
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    return {
        "method": "get",
        "url": "/tests/basic_lists/booleans",
    }


def _parse_response(*, client: Client, response: httpx.Response) -> List[bool]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(List[bool], response.json())

        return response_200
    else:
        raise errors.UnexpectedStatus(response)


def _build_response(*, client: Client, response: httpx.Response) -> Response[List[bool]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[List[bool]]:
    """Get Basic List Of Booleans

     Get a list of booleans

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[bool]]
    """

    kwargs = _get_kwargs()

    response = client.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
) -> List[bool]:
    """Get Basic List Of Booleans

     Get a list of booleans

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List[bool]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[List[bool]]:
    """Get Basic List Of Booleans

     Get a list of booleans

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[bool]]
    """

    kwargs = _get_kwargs()

    response = await client.async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
) -> List[bool]:
    """Get Basic List Of Booleans

     Get a list of booleans

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List[bool]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
