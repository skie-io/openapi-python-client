from http import HTTPStatus
from typing import Any, Dict

import httpx

from ... import errors
from ...client import Client
from ...models.post_naming_property_conflict_with_import_body import PostNamingPropertyConflictWithImportBody
from ...models.post_naming_property_conflict_with_import_response_200 import (
    PostNamingPropertyConflictWithImportResponse200,
)
from ...types import Response


def _get_kwargs(
    *,
    body: PostNamingPropertyConflictWithImportBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/naming/property-conflict-with-import",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> PostNamingPropertyConflictWithImportResponse200:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostNamingPropertyConflictWithImportResponse200.from_dict(response.json())

        return response_200
    else:
        raise errors.UnexpectedStatus(response)


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PostNamingPropertyConflictWithImportResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    body: PostNamingPropertyConflictWithImportBody,
) -> Response[PostNamingPropertyConflictWithImportResponse200]:
    """
    Args:
        body (PostNamingPropertyConflictWithImportBody):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostNamingPropertyConflictWithImportResponse200]
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
    body: PostNamingPropertyConflictWithImportBody,
) -> PostNamingPropertyConflictWithImportResponse200:
    """
    Args:
        body (PostNamingPropertyConflictWithImportBody):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostNamingPropertyConflictWithImportResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    body: PostNamingPropertyConflictWithImportBody,
) -> Response[PostNamingPropertyConflictWithImportResponse200]:
    """
    Args:
        body (PostNamingPropertyConflictWithImportBody):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostNamingPropertyConflictWithImportResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    body: PostNamingPropertyConflictWithImportBody,
) -> PostNamingPropertyConflictWithImportResponse200:
    """
    Args:
        body (PostNamingPropertyConflictWithImportBody):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostNamingPropertyConflictWithImportResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
