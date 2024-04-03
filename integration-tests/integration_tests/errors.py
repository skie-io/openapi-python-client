"""Contains shared errors types that can be raised from API functions"""

from typing import Any

import httpx


class BaseError(Exception):
    pass


class PaginationError(BaseError):
    """Raised by api functions when the response status is not 200."""

    def __init__(self, model: Any, response: Any) -> None:
        self.response = response

        super().__init__(f"Pagination error: expected {model}, got {type(response)}")


class HTTPError(BaseError):
    def __init__(self, response: httpx.Response):
        self.response = response

        super().__init__(
            f"HTTP error: {self.response.status_code} {self.response.reason_phrase}\n"
            f"Response headers: {dict(self.response.headers)}\n"
            f"Response body: {self.response.text}"
        )


class UnexpectedStatus(HTTPError):
    """Raised by api functions when the response status an undocumented status."""


class InformationalResponse(HTTPError):
    """Raised when the response status is 1xx."""


class RedirectionError(HTTPError):
    """Raised when the response status is 3xx."""


class ClientError(HTTPError):
    """Raised when the response status is 4xx."""


class ServerError(HTTPError):
    """Raised when the response status is 5xx."""


class NotFoundError(ClientError):
    """Raised when the response status is 404."""


__all__ = ["UnexpectedStatus", "PaginationError", "NotFoundError", "ClientError"]
