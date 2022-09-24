import logging
from functools import lru_cache
from typing import List
from decouple import config
from pydantic import BaseSettings

log = logging.getLogger("uvicorn")


class Setting(BaseSettings):
    APP_VERSION: str = config("APP_VERSION", default="0.0.1")
    APP_DESCRIPTION: str = config("APP_DESCRIPTION", default="API")
    APP_NAME: str = config("APP_NAME", default="FastApi Boilerplate")
    APP_PORT: int = config("APP_PORT", default=8000, cast=int)
    ROOT_PATH: str = config("ROOT_PATH", default="/")
    ENVIRONMENT: str = config("ENVIRONMENT", default="dev")
    TESTING: bool = config("TESTING", default=False, cast=bool)
    DB_URL = config("DB_URL")
    DB_TEST_URL = config("DB_TEST_URL")
    PASSWORD_ADMIN = config("PASSWORD_ADMIN")
    EMAIL_ADMIN = config("EMAIL_ADMIN")
    GENERATE_SCHEMAS = config("GENERATE_SCHEMAS")
    NEO4J_ACCESS = config("NEO4J_ACCESS")
    ALLOW_HEADERS: List = ["*"]
    ALLOW_METHODS: List = ["*"]
    ORIGINS: List = ["*"]
    MODELS: List = [
        "aerich.models",
        "app.modules.user.model",
    ]


@lru_cache()
def get_settings():
    log.info("Loading Config Application.")
    return Setting()
