from typing import Dict

import httpx
import orjson
import ormsgpack
import pytest

from integration_tests.serialization import decode_response

_test_data = {"name": "Alice", "scopes": ["dashboard", "api"]}


@pytest.mark.parametrize(
    "content_type",
    [
        "application/msgpack",
        "application/x-msgpack",
        "application/vnd.msgpack",
        "application/msgpack; charset=utf-8",
    ],
)
def test_decode_msgpack(content_type: str) -> None:
    response = httpx.Response(200, headers={"Content-Type": content_type}, content=ormsgpack.packb(_test_data))

    assert decode_response(response) == _test_data


@pytest.mark.parametrize(
    "headers",
    [
        {"Content-Type": "application/json"},
        {},
    ],
)
def test_decode_json(headers: Dict[str, str]) -> None:
    response = httpx.Response(200, headers=headers, content=orjson.dumps(_test_data))

    assert decode_response(response) == _test_data
