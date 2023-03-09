from http import HTTPStatus
from typing import Any, Dict, List, Union

import httpx

from ... import errors
from ...client import Client
from ...models.paginated_result import PaginatedResult
from ...models.paginated_result_data_item import PaginatedResultDataItem
from ...models.paginated_result_error import PaginatedResultError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    next_page_token: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["next_page_token"] = next_page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/tests/paginated-with-multiple-responses",
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Union[PaginatedResult, PaginatedResultError]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedResult.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = PaginatedResultError.from_dict(response.json())

        return response_422
    else:
        raise errors.UnexpectedStatus(response)


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[PaginatedResult, PaginatedResultError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    next_page_token: Union[Unset, None, str] = UNSET,
) -> Response[Union[PaginatedResult, PaginatedResultError]]:
    """Endpoint with paginated results with multiple responses

    Args:
        next_page_token (Union[Unset, None, str]):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PaginatedResult, PaginatedResultError]]
    """

    kwargs = _get_kwargs(
        next_page_token=next_page_token,
    )

    response = client.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    next_page_token: Union[Unset, None, str] = UNSET,
) -> Union[PaginatedResult, PaginatedResultError]:
    """Endpoint with paginated results with multiple responses

    Args:
        next_page_token (Union[Unset, None, str]):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PaginatedResult, PaginatedResultError]
    """

    return sync_detailed(
        client=client,
        next_page_token=next_page_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    next_page_token: Union[Unset, None, str] = UNSET,
) -> Response[Union[PaginatedResult, PaginatedResultError]]:
    """Endpoint with paginated results with multiple responses

    Args:
        next_page_token (Union[Unset, None, str]):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PaginatedResult, PaginatedResultError]]
    """

    kwargs = _get_kwargs(
        next_page_token=next_page_token,
    )

    response = await client.async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    next_page_token: Union[Unset, None, str] = UNSET,
) -> Union[PaginatedResult, PaginatedResultError]:
    """Endpoint with paginated results with multiple responses

    Args:
        next_page_token (Union[Unset, None, str]):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PaginatedResult, PaginatedResultError]
    """

    return (
        await asyncio_detailed(
            client=client,
            next_page_token=next_page_token,
        )
    ).parsed


def fetch_all(
    *,
    client: Client,
) -> List["PaginatedResultDataItem"]:
    """Endpoint with paginated results with multiple responses

    Args:

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PaginatedResult, PaginatedResultError]
    """

    next_page_token = None
    data: List["PaginatedResultDataItem"] = []

    while True:
        page = sync(
            client=client,
            next_page_token=next_page_token,
        )

        if not isinstance(page, PaginatedResult):
            raise errors.PaginationError(PaginatedResult, page)

        data.extend(page.data)
        next_page_token = page.next_page_token

        if not next_page_token:
            break

    return data


async def async_fetch_all(
    *,
    client: Client,
) -> List["PaginatedResultDataItem"]:
    """Endpoint with paginated results with multiple responses

    Args:

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PaginatedResult, PaginatedResultError]
    """

    next_page_token = None
    data: List["PaginatedResultDataItem"] = []

    while True:
        page = await asyncio(
            client=client,
            next_page_token=next_page_token,
        )

        if not isinstance(page, PaginatedResult):
            raise errors.PaginationError(PaginatedResult, page)

        data.extend(page.data)
        next_page_token = page.next_page_token

        if not next_page_token:
            break

    return data
