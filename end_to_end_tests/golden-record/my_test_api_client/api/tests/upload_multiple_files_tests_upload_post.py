from http import HTTPStatus
from typing import Any, Dict, List, Union

import httpx
import orjson

from ... import errors
from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...types import File, Response


def _get_kwargs(
    *,
    body: List[File],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/tests/upload/multiple",
    }

    _body = []
    for body_item_data in body:
        body_item = body_item_data.to_tuple()

        _body.append(body_item)

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> Union[Any, HTTPValidationError]:
    if response.status_code == HTTPStatus.OK:
        response_200 = orjson.loads(response.content)
        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(orjson.loads(response.content))

        return response_422
    else:
        raise errors.UnexpectedStatus(response)


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    body: List[File],
) -> Response[Union[Any, HTTPValidationError]]:
    """Upload multiple files

     Upload several files in the same request

    Args:
        body (List[File]):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
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
    body: List[File],
) -> Union[Any, HTTPValidationError]:
    """Upload multiple files

     Upload several files in the same request

    Args:
        body (List[File]):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    body: List[File],
) -> Response[Union[Any, HTTPValidationError]]:
    """Upload multiple files

     Upload several files in the same request

    Args:
        body (List[File]):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    body: List[File],
) -> Union[Any, HTTPValidationError]:
    """Upload multiple files

     Upload several files in the same request

    Args:
        body (List[File]):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
