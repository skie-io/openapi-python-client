from http import HTTPStatus
from typing import Any, Dict, Union

import httpx

from ... import errors
from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    path_param: str,
    *,
    string_param: Union[Unset, None, str] = UNSET,
    integer_param: Union[Unset, None, int] = 0,
    header_param: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(header_param, Unset):
        headers["header param"] = header_param

    params: Dict[str, Any] = {}
    params["string param"] = string_param

    params["integer param"] = integer_param

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/parameter-references/{path_param}".format(
            path_param=path_param,
        ),
        "params": params,
        "headers": headers,
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
    path_param: str,
    *,
    client: Client,
    string_param: Union[Unset, None, str] = UNSET,
    integer_param: Union[Unset, None, int] = 0,
    header_param: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Test different types of parameter references

    Args:
        path_param (str):
        string_param (Union[Unset, None, str]):
        integer_param (Union[Unset, None, int]):
        header_param (Union[Unset, str]):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        path_param=path_param,
        string_param=string_param,
        integer_param=integer_param,
        header_param=header_param,
    )

    response = client.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    path_param: str,
    *,
    client: Client,
    string_param: Union[Unset, None, str] = UNSET,
    integer_param: Union[Unset, None, int] = 0,
    header_param: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Test different types of parameter references

    Args:
        path_param (str):
        string_param (Union[Unset, None, str]):
        integer_param (Union[Unset, None, int]):
        header_param (Union[Unset, str]):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        path_param=path_param,
        string_param=string_param,
        integer_param=integer_param,
        header_param=header_param,
    )

    response = await client.async_request(**kwargs)

    return _build_response(client=client, response=response)
