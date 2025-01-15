from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route

from boaboard.api.app import api_app
from boaboard.core.logger import Logger
from boaboard.core.settings import Settings

# initiate logging (needed if uvicorn workers equals 1)
Logger()


class CoreApp(Starlette):
    def __init__(self):
        super().__init__(debug=Settings().app_debug)

        self.mount("/api", app=api_app)

        self.add_route("/", lambda r: HTMLResponse('<h1>Hello, world!</h1>'))
