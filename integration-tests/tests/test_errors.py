import httpx
import ormsgpack

from integration_tests.errors import HTTPError

_test_error = {"code": 404, "message": "Not found"}


def test_msgpack_body() -> None:
    content = ormsgpack.packb(_test_error)
    response = httpx.Response(404, headers={"Content-Type": "application/msgpack"}, content=content)

    assert str(HTTPError(response)).endswith("Response body: {'code': 404, 'message': 'Not found'}")


def test_invalid_msgpack_body() -> None:
    response = httpx.Response(404, headers={"Content-Type": "application/msgpack"}, content=b"\xc1")

    assert str(HTTPError(response)).endswith(f"Response body: {response.text}")


def test_json_body() -> None:
    response = httpx.Response(404, json=_test_error)

    assert str(HTTPError(response)).endswith(f"Response body: {response.text}")
