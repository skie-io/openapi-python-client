from typing import Any, Dict, Optional

import httpx
from attrs import define, field

from .errors import ClientError, InformationalResponse, NotFoundError, RedirectionError, ServerError
from .json import add_json_headers, encode_json
from .jwt import AsyncJWTAuth, SyncJWTAuth


@define
class Client:
    """A class for keeping track of data related to the API

    The following are accepted as keyword arguments and will be used to construct httpx Clients internally:

        ``base_url``: The base URL for the API, all requests are made to a relative path to this URL

        ``headers``: A dictionary of headers to be sent with every request

        ``timeout``: The maximum amount of a time a request can take. API functions will raise
        httpx.TimeoutException if this is exceeded.

        ``pool_size``: The maximum number of connections to keep in a connection pool.

        ``httpx_args``: A dictionary of additional arguments to be passed to the ``httpx.Client`` and ``httpx.AsyncClient`` constructor.


    Attributes:
        raise_for_status: Raise an exception for any responses which are not a 2xx success code.
        key: The private key used to sign the JWT encoded with ES256.
        key_fingerprint: Key ID or fingerprint.
        jwt_expiration: Controls the expiration time for a JWT. 60 seconds by default.
    """

    raise_for_status: bool = field(default=True, kw_only=True)
    _base_url: str
    _headers: Dict[str, str] = field(factory=dict, kw_only=True)
    _timeout: float = field(default=30.0, kw_only=True)
    _pool_size: int = field(default=10, kw_only=True)
    _httpx_args: Dict[str, Any] = field(factory=dict, kw_only=True)
    _client: Optional[httpx.Client] = field(default=None, init=False)
    _async_client: Optional[httpx.AsyncClient] = field(default=None, init=False)
    _key: str = field(kw_only=True)
    _key_fingerprint: str = field(kw_only=True)
    _jwt_expiration: int = field(default=60, kw_only=True)

    def set_httpx_client(self, client: httpx.Client) -> "Client":
        """Manually the underlying httpx.Client

        **NOTE**: This will override any other settings on the client, including headers, and timeout.
        """
        self._client = client
        return self

    def get_httpx_client(self) -> httpx.Client:
        """Get the underlying httpx.Client, constructing a new one if not previously set"""
        if self._client is None:
            auth = SyncJWTAuth(key=self._key, kid=self._key_fingerprint, exp=self._jwt_expiration)

            self._client = httpx.Client(
                auth=auth,
                base_url=self._base_url,
                headers=self._headers,
                timeout=httpx.Timeout(self._timeout, pool=None),
                limits=httpx.Limits(max_connections=self._pool_size, max_keepalive_connections=self._pool_size),
                **self._httpx_args,
            )
        return self._client

    def __enter__(self) -> "Client":
        """Enter a context manager for self.client—you cannot enter twice (see httpx docs)"""
        self.get_httpx_client().__enter__()
        return self

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        """Exit a context manager for internal httpx.Client (see httpx docs)"""
        self.get_httpx_client().__exit__(*args, **kwargs)

    def set_async_httpx_client(self, async_client: httpx.AsyncClient) -> "Client":
        """Manually the underlying httpx.AsyncClient

        **NOTE**: This will override any other settings on the client, including headers, and timeout.
        """
        self._async_client = async_client
        return self

    def get_async_httpx_client(self) -> httpx.AsyncClient:
        """Get the underlying httpx.AsyncClient, constructing a new one if not previously set"""
        if self._async_client is None:
            auth = AsyncJWTAuth(key=self._key, kid=self._key_fingerprint, exp=self._jwt_expiration)

            self._async_client = httpx.AsyncClient(
                auth=auth,
                base_url=self._base_url,
                headers=self._headers,
                timeout=httpx.Timeout(self._timeout, pool=None),
                limits=httpx.Limits(max_connections=self._pool_size, max_keepalive_connections=self._pool_size),
                **self._httpx_args,
            )
        return self._async_client

    async def __aenter__(self) -> "Client":
        """Enter a context manager for underlying httpx.AsyncClient—you cannot enter twice (see httpx docs)"""
        await self.get_async_httpx_client().__aenter__()
        return self

    async def __aexit__(self, *args: Any, **kwargs: Any) -> None:
        """Exit a context manager for underlying httpx.AsyncClient (see httpx docs)"""
        await self.get_async_httpx_client().__aexit__(*args, **kwargs)

    def request(
        self,
        *,
        method: str,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        json: Optional[Any] = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> httpx.Response:
        if json is not None:
            headers = add_json_headers(headers)
            json = encode_json(json)

        response = self.get_httpx_client().request(
            method=method, url=url, data=data, files=files, content=json, params=params, headers=headers
        )

        if self.raise_for_status:
            self._check_response_status(response)

        return response

    async def async_request(
        self,
        *,
        method: str,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        json: Optional[Any] = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> httpx.Response:
        if json is not None:
            headers = add_json_headers(headers)
            json = encode_json(json)

        response = await self.get_async_httpx_client().request(
            method=method, url=url, data=data, files=files, content=json, params=params, headers=headers
        )

        if self.raise_for_status:
            self._check_response_status(response)

        return response

    def _check_response_status(self, response: httpx.Response) -> None:
        if response.is_success:
            return

        if response.status_code == 404:
            raise NotFoundError(response)

        if response.is_informational:
            raise InformationalResponse(response)

        if response.is_redirect:
            raise RedirectionError(response)

        if response.is_client_error:
            raise ClientError(response)

        if response.is_server_error:
            raise ServerError(response)
