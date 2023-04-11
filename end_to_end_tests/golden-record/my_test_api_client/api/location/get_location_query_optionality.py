import datetime
from http import HTTPStatus
from typing import Any, Dict, Union

import httpx

from ... import errors
from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    not_null_required: datetime.datetime,
    null_required: Union[None, datetime.datetime],
    null_not_required: Union[None, Unset, datetime.datetime] = UNSET,
    not_null_not_required: Union[Unset, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_not_null_required = not_null_required
    params["not_null_required"] = json_not_null_required

    json_null_required: Union[None, datetime.datetime]
    if isinstance(null_required, datetime.datetime):
        json_null_required = null_required
    else:
        json_null_required = null_required
    params["null_required"] = json_null_required

    json_null_not_required: Union[None, Unset, datetime.datetime]
    if isinstance(null_not_required, Unset):
        json_null_not_required = UNSET
    elif isinstance(null_not_required, datetime.datetime):
        json_null_not_required = null_not_required
    else:
        json_null_not_required = null_not_required
    params["null_not_required"] = json_null_not_required

    json_not_null_not_required: Union[Unset, datetime.datetime] = UNSET
    if not isinstance(not_null_not_required, Unset):
        json_not_null_not_required = not_null_not_required
    params["not_null_not_required"] = json_not_null_not_required

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/location/query/optionality",
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
    not_null_required: datetime.datetime,
    null_required: Union[None, datetime.datetime],
    null_not_required: Union[None, Unset, datetime.datetime] = UNSET,
    not_null_not_required: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Any]:
    """
    Args:
        not_null_required (datetime.datetime):
        null_required (Union[None, datetime.datetime]):
        null_not_required (Union[None, Unset, datetime.datetime]):
        not_null_not_required (Union[Unset, datetime.datetime]):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        not_null_required=not_null_required,
        null_required=null_required,
        null_not_required=null_not_required,
        not_null_not_required=not_null_not_required,
    )

    response = client.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Client,
    not_null_required: datetime.datetime,
    null_required: Union[None, datetime.datetime],
    null_not_required: Union[None, Unset, datetime.datetime] = UNSET,
    not_null_not_required: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Any]:
    """
    Args:
        not_null_required (datetime.datetime):
        null_required (Union[None, datetime.datetime]):
        null_not_required (Union[None, Unset, datetime.datetime]):
        not_null_not_required (Union[Unset, datetime.datetime]):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        not_null_required=not_null_required,
        null_required=null_required,
        null_not_required=null_not_required,
        not_null_not_required=not_null_not_required,
    )

    response = await client.async_request(**kwargs)

    return _build_response(client=client, response=response)
