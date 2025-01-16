from typing import TYPE_CHECKING, Union

from nicegui import app as ui_app, ui
from fastapi.responses import RedirectResponse

from boaboard.core.settings import settings
from boaboard.ui.dashboard import dashboard_router

if TYPE_CHECKING:
    from fastapi import FastAPI
    from boaboard.core.app import CoreApp


class UiApp:
    def __init__(self, core_app: Union["CoreApp", "FastAPI"]) -> None:
        self.core_app = core_app

        # include the dashboard router
        ui_app.include_router(dashboard_router)

        # add root route
        ui.page("/")(self.root)

        # initialize nicegui
        ui.run_with(
            app=self.core_app,
            title=settings().ui_title,
            viewport=settings().ui_viewport,
            favicon=settings().ui_favicon,
            dark=settings().ui_dark,
            language=settings().ui_language,
            reconnect_timeout=settings().ui_reconnect_timeout,
            mount_path=settings().ui_prefix,
            prod_js=settings().ui_prod_js,
            storage_secret=settings().ui_storage_secret,
        )

    async def root(self):
        return RedirectResponse(url=settings().ui_prefix + dashboard_router.prefix)
