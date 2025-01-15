from pydantic import Field
from pydantic_settings import BaseSettings
from wiederverwendbar.pydantic.singleton import ModelSingleton

ENVIRONMENT_PREFIX = "BOABOARD_"


class Environment(BaseSettings, metaclass=ModelSingleton):
    save_settings_at_startup: bool = Field(default=False,
                                           alias=f"{ENVIRONMENT_PREFIX}SAVE_SETTINGS_AT_STARTUP",
                                           description="Save settings at startup.")
