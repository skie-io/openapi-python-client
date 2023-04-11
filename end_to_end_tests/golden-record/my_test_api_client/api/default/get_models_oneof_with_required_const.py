from http import HTTPStatus
from typing import Any, Union

import httpx
import orjson

from ... import errors
from ...client import Client
from ...models.get_models_oneof_with_required_const_response_200_type_0 import (
    GetModelsOneofWithRequiredConstResponse200Type0,
)
from ...models.get_models_oneof_with_required_const_response_200_type_1 import (
    GetModelsOneofWithRequiredConstResponse200Type1,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/models/oneof-with-required-const",
    }

    return _kwargs


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Union["GetModelsOneofWithRequiredConstResponse200Type0", "GetModelsOneofWithRequiredConstResponse200Type1"]:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> Union[
            "GetModelsOneofWithRequiredConstResponse200Type0", "GetModelsOneofWithRequiredConstResponse200Type1"
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = GetModelsOneofWithRequiredConstResponse200Type0.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = GetModelsOneofWithRequiredConstResponse200Type1.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(orjson.loads(response.content))

        return response_200
    raise errors.UnexpectedStatus(response)


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[
    Union["GetModelsOneofWithRequiredConstResponse200Type0", "GetModelsOneofWithRequiredConstResponse200Type1"]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[
    Union["GetModelsOneofWithRequiredConstResponse200Type0", "GetModelsOneofWithRequiredConstResponse200Type1"]
]:
    """
    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['GetModelsOneofWithRequiredConstResponse200Type0', 'GetModelsOneofWithRequiredConstResponse200Type1']]
    """

    kwargs = _get_kwargs()

    response = client.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
) -> Union["GetModelsOneofWithRequiredConstResponse200Type0", "GetModelsOneofWithRequiredConstResponse200Type1"]:
    """
    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['GetModelsOneofWithRequiredConstResponse200Type0', 'GetModelsOneofWithRequiredConstResponse200Type1']
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[
    Union["GetModelsOneofWithRequiredConstResponse200Type0", "GetModelsOneofWithRequiredConstResponse200Type1"]
]:
    """
    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['GetModelsOneofWithRequiredConstResponse200Type0', 'GetModelsOneofWithRequiredConstResponse200Type1']]
    """

    kwargs = _get_kwargs()

    response = await client.async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
) -> Union["GetModelsOneofWithRequiredConstResponse200Type0", "GetModelsOneofWithRequiredConstResponse200Type1"]:
    """
    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['GetModelsOneofWithRequiredConstResponse200Type0', 'GetModelsOneofWithRequiredConstResponse200Type1']
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
