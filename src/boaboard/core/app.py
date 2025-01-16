from starlette.applications import Starlette
from starlette.responses import HTMLResponse

from boaboard.api.app import api_app
from boaboard.core.logger import logger
from boaboard.core.settings import settings

# initialize logger (required for multi worker environments)
logger()


class CoreApp(Starlette):
    def __init__(self):
        super().__init__(debug=settings().app_debug)

        self.mount("/api", app=api_app)

        self.add_route("/", lambda r: HTMLResponse('<h1>Hello, world!</h1>'))
