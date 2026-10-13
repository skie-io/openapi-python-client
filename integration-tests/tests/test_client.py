from datetime import datetime, timezone
from typing import Any, Dict

import httpx
import jwt
import orjson
import ormsgpack
import pytest

from integration_tests.api.parameters import post_parameters_header
from integration_tests.client import Client
from integration_tests.models.post_parameters_header_response_200 import PostParametersHeaderResponse200

_test_key = """-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIIVEl1i9xtby2IlXDjrlvRNHcNkRXh3U1TNU99sb7uvaoAoGCCqGSM49
AwEHoUQDQgAE3Ez3CzfCzPo3xHaVf/hYDnGrA+aV+iz0kwixt+CN+hyxsgmo7GZ6
t2dglgM+cLzvkhzq1ULE5xoT6JI2/D5NRQ==
-----END EC PRIVATE KEY-----"""
_test_key_fingerprint = "143edb698bd97dff684bf6b21b4ea18436930914"
_test_body = {"time": datetime(2024, 3, 15, 12, 30, tzinfo=timezone.utc)}
_test_header_data = {"boolean": True, "string": "a test string", "number": 1.1, "integer": 1}


def _echo_authorization(request: httpx.Request) -> httpx.Response:
    return httpx.Response(200, text=request.headers.get("Authorization", ""))


def _negotiate_header_data(request: httpx.Request) -> httpx.Response:
    if request.headers["Accept"] == "application/msgpack":
        content = ormsgpack.packb(_test_header_data)
        return httpx.Response(200, headers={"Content-Type": "application/msgpack"}, content=content)

    return httpx.Response(200, json=_test_header_data)


def _make_client(**kwargs: Any) -> Client:
    return Client(
        "http://localhost:3000",
        httpx_args={"transport": httpx.MockTransport(_echo_authorization)},
        **kwargs,
    )


def _assert_signed_jwt(authorization: str) -> None:
    scheme, token = authorization.split(" ")

    assert scheme == "Bearer"
    assert jwt.get_unverified_header(token)["kid"] == _test_key_fingerprint
    jwt.decode(token, key=_test_key, algorithms=["ES256"], audience="api")


def test_token() -> None:
    client = _make_client(token="opaque-token")

    response = client.request(method="GET", url="/")

    assert response.text == "Bearer opaque-token"


@pytest.mark.asyncio
async def test_token_async() -> None:
    client = _make_client(token="opaque-token")

    response = await client.async_request(method="GET", url="/")

    assert response.text == "Bearer opaque-token"


def test_jwt() -> None:
    client = _make_client(key=_test_key, key_fingerprint=_test_key_fingerprint)

    response = client.request(method="GET", url="/")

    _assert_signed_jwt(response.text)


@pytest.mark.asyncio
async def test_jwt_async() -> None:
    client = _make_client(key=_test_key, key_fingerprint=_test_key_fingerprint)

    response = await client.async_request(method="GET", url="/")

    _assert_signed_jwt(response.text)


@pytest.mark.parametrize(
    "credentials",
    [
        {},
        {"key": "key"},
        {"key_fingerprint": "fingerprint"},
        {"token": "opaque-token", "key": "key"},
        {"token": "opaque-token", "key": "key", "key_fingerprint": "fingerprint"},
    ],
)
def test_invalid_credentials(credentials: Dict[str, Any]) -> None:
    with pytest.raises(ValueError):
        Client("http://localhost:3000", **credentials)


def test_json() -> None:
    client = _make_client(token="opaque-token")

    response = client.request(method="POST", url="/", json=_test_body)

    assert response.request.headers["Accept"] == "*/*"
    assert response.request.headers["Content-Type"] == "application/json"
    assert orjson.loads(response.request.content) == {"time": "2024-03-15T12:30:00Z"}


def test_msgpack() -> None:
    client = _make_client(token="opaque-token", msgpack=True)

    response = client.request(method="POST", url="/", json=_test_body)

    assert response.request.headers["Accept"] == "application/msgpack"
    assert response.request.headers["Content-Type"] == "application/msgpack"
    assert ormsgpack.unpackb(response.request.content) == {"time": "2024-03-15T12:30:00Z"}


@pytest.mark.asyncio
async def test_msgpack_async() -> None:
    client = _make_client(token="opaque-token", msgpack=True)

    response = await client.async_request(method="POST", url="/", json=_test_body)

    assert response.request.headers["Accept"] == "application/msgpack"
    assert response.request.headers["Content-Type"] == "application/msgpack"
    assert ormsgpack.unpackb(response.request.content) == {"time": "2024-03-15T12:30:00Z"}


def test_msgpack_without_body() -> None:
    client = _make_client(token="opaque-token", msgpack=True)

    response = client.request(method="GET", url="/")

    assert response.request.headers["Accept"] == "application/msgpack"
    assert "Content-Type" not in response.request.headers


@pytest.mark.parametrize(
    "msgpack, content_type",
    [
        (True, "application/msgpack"),
        (False, "application/json"),
    ],
)
def test_parse_response(msgpack: bool, content_type: str) -> None:
    client = Client(
        "http://localhost:3000",
        token="opaque-token",
        msgpack=msgpack,
        httpx_args={"transport": httpx.MockTransport(_negotiate_header_data)},
    )

    response = post_parameters_header.sync_detailed(
        client=client,
        boolean_header=True,
        string_header="a test string",
        number_header=1.1,
        integer_header=1,
    )

    assert response.headers["Content-Type"] == content_type
    assert response.parsed == PostParametersHeaderResponse200(
        boolean=True, string="a test string", number=1.1, integer=1
    )
