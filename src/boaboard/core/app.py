from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import RedirectResponse

from boaboard.core.logger import logger
from boaboard.core.settings import settings
from boaboard.api.app import ApiApp
from boaboard.ui.app import UiApp

# initialize logger (required for multi worker environments)
logger()


class CoreApp(Starlette):
    def __init__(self):
        super().__init__(debug=settings().app_debug)

        # initialize the API app
        self.api_app = ApiApp(core_app=self)

        # initialize the UI app
        self.ui_app = UiApp(core_app=self)

        # add root route
        self.add_route("/", self.root)

    async def root(self, request: Request):
        return RedirectResponse(url=settings().ui_prefix)
