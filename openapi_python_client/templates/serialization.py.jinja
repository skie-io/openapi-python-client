import importlib.util
from typing import Any, Dict, Optional

import httpx
import orjson
import ormsgpack

ORJSON_OPTIONS = orjson.OPT_UTC_Z | orjson.OPT_SERIALIZE_NUMPY
ORMSGPACK_OPTIONS = ormsgpack.OPT_UTC_Z | ormsgpack.OPT_SERIALIZE_NUMPY
MSGPACK_CONTENT_TYPES = ("application/msgpack", "application/x-msgpack", "application/vnd.msgpack")
IS_PANDAS_AVAILABLE = importlib.util.find_spec("pandas") is not None


def add_json_headers(headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    headers = {} if headers is None else headers
    headers = {**headers, "Content-Type": "application/json"}
    return headers


def add_msgpack_headers(headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    headers = {} if headers is None else headers
    headers = {**headers, "Content-Type": "application/msgpack"}
    return headers


def add_msgpack_accept_header(headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    headers = {} if headers is None else headers
    headers = {**headers, "Accept": "application/msgpack"}
    return headers


if IS_PANDAS_AVAILABLE:
    from pandas import Timestamp  # type: ignore

    def encode_pandas(obj: Any) -> Any:
        if isinstance(obj, Timestamp):
            return obj.to_pydatetime()
        else:
            return obj

    def encode_json(json: Any) -> bytes:
        return orjson.dumps(json, option=ORJSON_OPTIONS, default=encode_pandas)

    def encode_msgpack(data: Any) -> bytes:
        return ormsgpack.packb(data, option=ORMSGPACK_OPTIONS, default=encode_pandas)

else:

    def encode_json(json: Any) -> bytes:
        return orjson.dumps(json, option=ORJSON_OPTIONS)

    def encode_msgpack(data: Any) -> bytes:
        return ormsgpack.packb(data, option=ORMSGPACK_OPTIONS)


def is_msgpack(response: httpx.Response) -> bool:
    content_type = response.headers.get("Content-Type", "").split(";")[0].strip().lower()
    return content_type in MSGPACK_CONTENT_TYPES


def decode_response(response: httpx.Response) -> Any:
    """Decodes the response body as MessagePack or JSON, according to its Content-Type"""
    if is_msgpack(response):
        return ormsgpack.unpackb(response.content)

    return orjson.loads(response.content)
