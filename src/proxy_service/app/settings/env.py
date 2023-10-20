from __future__ import annotations

import os
import typing
from pathlib import Path

from decouple import Config as BaseConfig
from decouple import RepositoryEmpty, RepositoryEnv, undefined

if typing.TYPE_CHECKING:
    from collections.abc import Callable

    from decouple import Config as Undefined

BASE_DIR = Path(__file__).parent.parent
PROJECT_ROOT = BASE_DIR.parent

ENV_FILE = Path(os.getenv("APP_ENV_FILE", ""))


class Config(BaseConfig):
    def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        self.prefix = kwargs.pop("prefix", "")
        super().__init__(*args, **kwargs)

    def get(self, option: str, default: typing.Any = undefined, cast: Callable | Undefined = undefined) -> typing.Any:
        return super().get(self.prefix + option, default, cast)


config = Config(prefix="DJ_", repository=RepositoryEnv(str(ENV_FILE)) if ENV_FILE.is_file() else RepositoryEmpty())
