from pathlib import Path
from typing import Literal

from pydantic import Field
from wiederverwendbar.singleton import Singleton
from wiederverwendbar.pydantic import ModelSingleton, FileConfig
from wiederverwendbar.logger import LoggerSettings
from wiederverwendbar.mongoengine import MongoengineSettings
from wiederverwendbar.uvicorn import UvicornServerSettings

from boaboard.core.environment import environment


class Settings(FileConfig, LoggerSettings, MongoengineSettings, UvicornServerSettings, metaclass=ModelSingleton):
    # app
    app_debug: bool = Field(default=False, description="App debug mode.")

    # api
    api_prefix: str = Field(default="/api", description="API prefix.")
    api_docs_path: str | None = Field(default="/docs", description="API docs path. If None, no docs are served.")
    api_redoc_path: str | None = Field(default="/redoc", description="API redoc path. If None, no redoc is served.")

    # ui
    ui_prefix: str = Field(default="/ui", description="UI prefix.")
    ui_title: str = Field(default="BoaBoard", description="UI title.")
    ui_viewport: str = Field(default="width=device-width, initial-scale=1", description="Viewport meta tag.")
    ui_favicon: str | Path | None = Field(default=None, description="Favicon path.")
    ui_dark: bool = Field(default=False, description="Dark mode.")
    ui_language: Literal["ar", "ar-TN", "az-Latn", "bg", "bn", "ca", "cs", "da", "de", "el", "en-GB", "en-US",
    "eo", "es", "et", "eu", "fa", "fa-IR", "fi", "fr", "gn", "he", "hr", "hu", "id", "is", "it", "ja",
    "kk", "km", "ko-KR", "kur-CKB", "lt", "lu", "lv", "ml", "mm", "ms", "my", "nb-NO", "nl", "pl", "pt",
    "pt-BR", "ro", "ru", "sk", "sl", "sm", "sr", "sr-CYR", "sv", "ta", "th", "tr", "ug", "uk", "uz-Cyrl",
    "uz-Latn", "vi", "zh-CN", "zh-TW"] = Field(default="en-US", description="Language.")
    ui_reconnect_timeout: float = Field(default=3.0, description="Reconnect timeout.")
    ui_prod_js: bool = Field(default=True, description="Use production JavaScript.")
    ui_storage_secret: str = Field(default="pick your private secret here", description="Storage secret.")

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
