from http import HTTPStatus
from typing import Any, Dict

import httpx

from ... import errors
from ...client import Client
from ...models.test_inline_objects_json_body import TestInlineObjectsJsonBody
from ...models.test_inline_objects_response_200 import TestInlineObjectsResponse200
from ...types import Response


def _get_kwargs(
    *,
    json_body: TestInlineObjectsJsonBody,
) -> Dict[str, Any]:
    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/tests/inline_objects",
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> TestInlineObjectsResponse200:
    if response.status_code == HTTPStatus.OK:
        response_200 = TestInlineObjectsResponse200.from_dict(response.json())

        return response_200
    else:
        raise errors.UnexpectedStatus(response)


def _build_response(*, client: Client, response: httpx.Response) -> Response[TestInlineObjectsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: TestInlineObjectsJsonBody,
) -> Response[TestInlineObjectsResponse200]:
    """Test Inline Objects

    Args:
        json_body (TestInlineObjectsJsonBody):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TestInlineObjectsResponse200]
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
    json_body: TestInlineObjectsJsonBody,
) -> TestInlineObjectsResponse200:
    """Test Inline Objects

    Args:
        json_body (TestInlineObjectsJsonBody):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TestInlineObjectsResponse200
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: TestInlineObjectsJsonBody,
) -> Response[TestInlineObjectsResponse200]:
    """Test Inline Objects

    Args:
        json_body (TestInlineObjectsJsonBody):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TestInlineObjectsResponse200]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: TestInlineObjectsJsonBody,
) -> TestInlineObjectsResponse200:
    """Test Inline Objects

    Args:
        json_body (TestInlineObjectsJsonBody):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TestInlineObjectsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
