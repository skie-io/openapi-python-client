import typing

from httpx import Auth, Request, Response


class TokenAuth(Auth):
    """Sends an opaque token as is"""

    def __init__(self, token: str):
        self.token = token

    def auth_flow(self, request: Request) -> typing.Generator[Request, Response, None]:
        request.headers["Authorization"] = f"Bearer {self.token}"

        yield request
