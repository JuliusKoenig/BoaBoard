from pydantic import Field
from wiederverwendbar.singleton import Singleton
from wiederverwendbar.pydantic import ModelSingleton, FileConfig
from wiederverwendbar.logger import LoggerSettings
from wiederverwendbar.mongoengine import MongoengineSettings
from wiederverwendbar.uvicorn import UvicornServerSettings

from boaboard.core.environment import environment


class Settings(FileConfig, LoggerSettings, MongoengineSettings, UvicornServerSettings, metaclass=ModelSingleton):
    app_debug: bool = Field(default=False, description="App debug mode.")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # save settings at startup
        if environment().save_settings_at_startup:
            self.save()


def settings() -> Settings:
    try:
        return Singleton.get_by_type(Settings)
    except RuntimeError:
        return Settings(file_path="settings", init=True)
