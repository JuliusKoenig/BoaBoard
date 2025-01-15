from wiederverwendbar.pydantic.singleton import ModelSingleton
from wiederverwendbar.pydantic.file_config import FileConfig
from wiederverwendbar.logger.settings import LoggerSettings
from wiederverwendbar.mongoengine.settings import MongoengineSettings
from wiederverwendbar.uvicorn.settings import UvicornServerSettings

from boaboard.core.environment import Environment


class Settings(FileConfig, LoggerSettings, MongoengineSettings, UvicornServerSettings, metaclass=ModelSingleton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # save settings at startup
        if Environment().save_settings_at_startup:
            self.save()
