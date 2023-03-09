from http import HTTPStatus
from typing import Any, Dict

import httpx

from ... import errors
from ...client import Client
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client_query: str,
    url_query: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["client"] = client_query

    params["url"] = url_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/naming/reserved-parameters",
        "params": params,
    }


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
    client_query: str,
    url_query: str,
) -> Response[Any]:
    """
    Args:
        client_query (str):
        url_query (str):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client_query=client_query,
        url_query=url_query,
    )

    response = client.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Client,
    client_query: str,
    url_query: str,
) -> Response[Any]:
    """
    Args:
        client_query (str):
        url_query (str):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client_query=client_query,
        url_query=url_query,
    )

    response = await client.async_request(**kwargs)

    return _build_response(client=client, response=response)
