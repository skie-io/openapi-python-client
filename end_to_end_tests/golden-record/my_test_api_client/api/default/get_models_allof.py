from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import Client
from ...models.get_models_allof_response_200 import GetModelsAllofResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/models/allof",
    }

    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> GetModelsAllofResponse200:
    if response.status_code == 200:
        response_200 = GetModelsAllofResponse200.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response)


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetModelsAllofResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[GetModelsAllofResponse200]:
    """
    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetModelsAllofResponse200]
    """

    kwargs = _get_kwargs()

    response = client.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
) -> GetModelsAllofResponse200:
    """
    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetModelsAllofResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[GetModelsAllofResponse200]:
    """
    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetModelsAllofResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
) -> GetModelsAllofResponse200:
    """
    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetModelsAllofResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
