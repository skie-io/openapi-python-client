from http import HTTPStatus
from typing import Any, Dict, Union

import httpx
import orjson

from ... import errors
from ...client import Client
from ...models.post_body_multipart_body import PostBodyMultipartBody
from ...models.post_body_multipart_response_200 import PostBodyMultipartResponse200
from ...models.public_error import PublicError
from ...types import Response


def _get_kwargs(
    *,
    body: PostBodyMultipartBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/body/multipart",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> Union[PostBodyMultipartResponse200, PublicError]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostBodyMultipartResponse200.from_dict(orjson.loads(response.content))

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = PublicError.from_dict(orjson.loads(response.content))

        return response_400
    else:
        raise errors.UnexpectedStatus(response)


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[PostBodyMultipartResponse200, PublicError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    body: PostBodyMultipartBody,
) -> Response[Union[PostBodyMultipartResponse200, PublicError]]:
    """
    Args:
        body (PostBodyMultipartBody):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostBodyMultipartResponse200, PublicError]]
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
    body: PostBodyMultipartBody,
) -> Union[PostBodyMultipartResponse200, PublicError]:
    """
    Args:
        body (PostBodyMultipartBody):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostBodyMultipartResponse200, PublicError]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    body: PostBodyMultipartBody,
) -> Response[Union[PostBodyMultipartResponse200, PublicError]]:
    """
    Args:
        body (PostBodyMultipartBody):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostBodyMultipartResponse200, PublicError]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    body: PostBodyMultipartBody,
) -> Union[PostBodyMultipartResponse200, PublicError]:
    """
    Args:
        body (PostBodyMultipartBody):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostBodyMultipartResponse200, PublicError]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
