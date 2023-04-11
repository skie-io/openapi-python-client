from http import HTTPStatus
from typing import Any

import httpx
import orjson

from ... import errors
from ...client import Client
from ...models.a_model import AModel
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/responses/reference",
    }

    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> AModel:
    if response.status_code == 200:
        response_200 = AModel.from_dict(orjson.loads(response.content))

        return response_200
    raise errors.UnexpectedStatus(response)


def _build_response(*, client: Client, response: httpx.Response) -> Response[AModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[AModel]:
    """Endpoint using predefined response

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AModel]
    """

    kwargs = _get_kwargs()

    response = client.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
) -> AModel:
    """Endpoint using predefined response

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AModel
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[AModel]:
    """Endpoint using predefined response

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AModel]
    """

    kwargs = _get_kwargs()

    response = await client.async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
) -> AModel:
    """Endpoint using predefined response

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AModel
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
