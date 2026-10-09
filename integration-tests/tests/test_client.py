from typing import Any, Dict

import httpx
import jwt
import pytest

from integration_tests.client import Client

_test_key = """-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIIVEl1i9xtby2IlXDjrlvRNHcNkRXh3U1TNU99sb7uvaoAoGCCqGSM49
AwEHoUQDQgAE3Ez3CzfCzPo3xHaVf/hYDnGrA+aV+iz0kwixt+CN+hyxsgmo7GZ6
t2dglgM+cLzvkhzq1ULE5xoT6JI2/D5NRQ==
-----END EC PRIVATE KEY-----"""
_test_key_fingerprint = "143edb698bd97dff684bf6b21b4ea18436930914"


def _echo_authorization(request: httpx.Request) -> httpx.Response:
    return httpx.Response(200, text=request.headers.get("Authorization", ""))


def _make_client(**credentials: Any) -> Client:
    return Client(
        "http://localhost:3000",
        httpx_args={"transport": httpx.MockTransport(_echo_authorization)},
        **credentials,
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
