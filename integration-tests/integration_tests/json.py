import importlib.util
from typing import Any, Dict, Optional

import orjson

ORJSON_OPTIONS = orjson.OPT_UTC_Z | orjson.OPT_SERIALIZE_NUMPY
IS_PANDAS_AVAILABLE = importlib.util.find_spec("pandas") is not None


def add_json_headers(headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    headers = {} if headers is None else headers
    headers = {**headers, "Content-Type": "application/json"}
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

else:

    def encode_json(json: Any) -> bytes:
        return orjson.dumps(json, option=ORJSON_OPTIONS)
