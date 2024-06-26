from http import HTTPStatus
from typing import Any, Dict, List, Union, cast

import httpx
import orjson

from ... import errors
from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...types import File, Response


def _get_kwargs(
    *,
    multipart_data: List[File],
) -> Dict[str, Any]:
    multipart_multipart_data = []
    for multipart_data_item_data in multipart_data:
        multipart_data_item = multipart_data_item_data.to_tuple()

        multipart_multipart_data.append(multipart_data_item)

    return {
        "method": "post",
        "url": "/tests/upload/multiple",
        "files": multipart_multipart_data,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Union[Any, HTTPValidationError]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, orjson.loads(response.content))
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
    multipart_data: List[File],
) -> Response[Union[Any, HTTPValidationError]]:
    """Upload multiple files

     Upload several files in the same request

    Args:
        multipart_data (List[File]):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        multipart_data=multipart_data,
    )

    response = client.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    multipart_data: List[File],
) -> Union[Any, HTTPValidationError]:
    """Upload multiple files

     Upload several files in the same request

    Args:
        multipart_data (List[File]):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    multipart_data: List[File],
) -> Response[Union[Any, HTTPValidationError]]:
    """Upload multiple files

     Upload several files in the same request

    Args:
        multipart_data (List[File]):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        multipart_data=multipart_data,
    )

    response = await client.async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    multipart_data: List[File],
) -> Union[Any, HTTPValidationError]:
    """Upload multiple files

     Upload several files in the same request

    Args:
        multipart_data (List[File]):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
