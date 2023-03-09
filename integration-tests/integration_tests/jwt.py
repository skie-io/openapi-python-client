import secrets
import time
import typing
from asyncio import Lock
from datetime import datetime, timedelta, timezone
from threading import RLock

import jwt
from httpx import Auth, Request, Response


class BaseJWTAuth(Auth):
    def __init__(self, key: str, kid: str, exp: int):
        self.key = key
        self.kid = kid
        self.exp = exp

        self._expires: float = 0
        self._jwt: str = ""

        # generate a new token 10 seconds earlier than the 'exp' header to give
        # enough time for the request to be made
        self._expires_leeway = 10

    def needs_refresh(self) -> bool:
        return not self._jwt or self._expires < time.monotonic()

    def generate(self) -> None:
        jti = secrets.token_hex(16)
        now = datetime.now(tz=timezone.utc)
        exp = now + timedelta(seconds=self.exp)

        payload = {"jti": jti, "nbf": now, "exp": exp, "iat": now, "aud": "api"}
        headers = {"kid": self.kid}

        self._expires = time.monotonic() + self.exp - self._expires_leeway

        if self._expires < 0:
            self._expires = 0

        self._jwt = jwt.encode(payload=payload, headers=headers, algorithm="ES256", key=self.key)


class SyncJWTAuth(BaseJWTAuth):
    def __init__(self, key: str, kid: str, exp: int):
        super().__init__(key=key, kid=kid, exp=exp)

        self._lock = RLock()

    def sync_auth_flow(self, request: Request) -> typing.Generator[Request, Response, None]:
        if self.needs_refresh():
            with self._lock:
                self.generate()

        request.headers["Authorization"] = f"Bearer {self._jwt}"

        yield request


class AsyncJWTAuth(BaseJWTAuth):
    def __init__(self, key: str, kid: str, exp: int):
        super().__init__(key=key, kid=kid, exp=exp)

        self._lock = Lock()

    async def async_auth_flow(self, request: Request) -> typing.AsyncGenerator[Request, Response]:
        if self.needs_refresh():
            async with self._lock:
                self.generate()

        request.headers["Authorization"] = f"Bearer {self._jwt}"

        yield request
