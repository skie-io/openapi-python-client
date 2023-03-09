from http import HTTPStatus
from typing import Any, Dict

import httpx

from ... import errors
from ...client import Client
from ...types import UNSET, Response


def _get_kwargs(
    param_path: str,
    *,
    param_query: str = "overridden_in_GET",
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["param"] = param_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/common_parameters_overriding/{param}".format(
            param=param_path,
        ),
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
    param_path: str,
    *,
    client: Client,
    param_query: str = "overridden_in_GET",
) -> Response[Any]:
    """Test that if you have an overriding property from `PathItem` in `Operation`, it produces valid code

    Args:
        param_path (str):
        param_query (str): A parameter with the same name as another. Default:
            'overridden_in_GET'. Example: an example string.

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        param_path=param_path,
        param_query=param_query,
    )

    response = client.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    param_path: str,
    *,
    client: Client,
    param_query: str = "overridden_in_GET",
) -> Response[Any]:
    """Test that if you have an overriding property from `PathItem` in `Operation`, it produces valid code

    Args:
        param_path (str):
        param_query (str): A parameter with the same name as another. Default:
            'overridden_in_GET'. Example: an example string.

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        param_path=param_path,
        param_query=param_query,
    )

    response = await client.async_request(**kwargs)

    return _build_response(client=client, response=response)
