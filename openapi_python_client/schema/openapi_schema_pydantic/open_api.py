from typing import Literal

from pydantic import BaseModel, ConfigDict

from .components import Components
from .external_documentation import ExternalDocumentation
from .info import Info
from .paths import Paths
from .security_requirement import SecurityRequirement
from .server import Server
from .tag import Tag


class OpenAPI(BaseModel):
    """This is the root document object of the OpenAPI document.

    References:
        - https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#oasObject
        - https://swagger.io/docs/specification/basic-structure/
    """

    info: Info
    servers: list[Server] = [Server(url="/")]
    paths: Paths
    components: Components | None = None
    security: list[SecurityRequirement] | None = None
    tags: list[Tag] | None = None
    externalDocs: ExternalDocumentation | None = None
    openapi: Literal["3.0.0"] | Literal["3.0.1"] | Literal["3.0.2"] | Literal["3.0.3"]
    model_config = ConfigDict(
        # `Components` is not built yet, will rebuild in `__init__.py`:
        defer_build=True,
        extra="allow",
    )
