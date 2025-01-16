from pydantic import Field
from pydantic_settings import BaseSettings
from wiederverwendbar.singleton import Singleton
from wiederverwendbar.pydantic import ModelSingleton

ENVIRONMENT_PREFIX = "BOABOARD_"


class Environment(BaseSettings, metaclass=ModelSingleton):
    save_settings_at_startup: bool = Field(default=False,
                                           alias=f"{ENVIRONMENT_PREFIX}SAVE_SETTINGS_AT_STARTUP",
                                           description="Save settings at startup.")


def environment() -> Environment:
    try:
        return Singleton.get_by_type(Environment)
    except RuntimeError:
        return Environment(init=True)
