import json
import mimetypes
from pathlib import Path

import yaml
from pydantic import BaseModel


class ClassOverride(BaseModel):
    """An override of a single generated class.

    See https://github.com/openapi-generators/openapi-python-client#class_overrides
    """

    class_name: str | None = None
    module_name: str | None = None


class Config(BaseModel):
    """Contains any configurable values passed by the user.

    See https://github.com/openapi-generators/openapi-python-client#configuration
    """

    class_overrides: dict[str, ClassOverride] = {}
    project_name_override: str | None = None
    package_name_override: str | None = None
    package_version_override: str | None = None
    use_path_prefixes_for_title_model_names: bool = True
    post_hooks: list[str] = [
        "ruff check --fix .",
        "black .",
    ]
    field_prefix: str = "field_"
    http_timeout: int = 5

    @staticmethod
    def load_from_path(path: Path) -> "Config":
        """Creates a Config from provided JSON or YAML file and sets a bunch of globals from it"""
        mime = mimetypes.guess_type(path.absolute().as_uri(), strict=True)[0]
        if mime == "application/json":
            config_data = json.loads(path.read_text())
        else:
            config_data = yaml.safe_load(path.read_text())
        config = Config(**config_data)
        return config
