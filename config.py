from pydantic import BaseSettings
from functools import lru_cache

import os


class Settings(BaseSettings):
    tg_token: str = os.getenv("TG_TOKEN")

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
