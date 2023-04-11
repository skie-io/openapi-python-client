from http import HTTPStatus
from typing import Any, Dict

import httpx
import orjson

from ... import errors
from ...client import Client
from ...models.post_naming_property_conflict_with_import_json_body import PostNamingPropertyConflictWithImportJsonBody
from ...models.post_naming_property_conflict_with_import_response_200 import (
    PostNamingPropertyConflictWithImportResponse200,
)
from ...types import Response


def _get_kwargs(
    *,
    json_body: PostNamingPropertyConflictWithImportJsonBody,
) -> Dict[str, Any]:
    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/naming/property-conflict-with-import",
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> PostNamingPropertyConflictWithImportResponse200:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostNamingPropertyConflictWithImportResponse200.from_dict(orjson.loads(response.content))

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
    json_body: PostNamingPropertyConflictWithImportJsonBody,
) -> Response[PostNamingPropertyConflictWithImportResponse200]:
    """
    Args:
        json_body (PostNamingPropertyConflictWithImportJsonBody):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostNamingPropertyConflictWithImportResponse200]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = client.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: PostNamingPropertyConflictWithImportJsonBody,
) -> PostNamingPropertyConflictWithImportResponse200:
    """
    Args:
        json_body (PostNamingPropertyConflictWithImportJsonBody):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostNamingPropertyConflictWithImportResponse200
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: PostNamingPropertyConflictWithImportJsonBody,
) -> Response[PostNamingPropertyConflictWithImportResponse200]:
    """
    Args:
        json_body (PostNamingPropertyConflictWithImportJsonBody):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostNamingPropertyConflictWithImportResponse200]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: PostNamingPropertyConflictWithImportJsonBody,
) -> PostNamingPropertyConflictWithImportResponse200:
    """
    Args:
        json_body (PostNamingPropertyConflictWithImportJsonBody):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostNamingPropertyConflictWithImportResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
