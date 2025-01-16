from typing import TYPE_CHECKING, Union

from fastapi import FastAPI
from fastapi.responses import RedirectResponse, PlainTextResponse

from boaboard import __title__, __description__, __version__, __author__, __author_email__, __license__
from boaboard.core.settings import settings

if TYPE_CHECKING:
    from boaboard.core.app import CoreApp


class ApiApp(FastAPI):
    def __init__(self, core_app: Union["CoreApp", "FastAPI"]) -> None:
        super().__init__(
            debug=settings().app_debug,
            title=__title__,
            summary=f"{__title__} API",
            description=__description__,
            version=__version__,
            terms_of_service="https://bastelqaurtier.de/terms",
            docs_url=settings().api_docs_path,
            redoc_url=settings().api_redoc_path,
            contact={"name": __author__, "email": __author_email__},
            license_info={"name": __license__, "url": "https://www.gnu.org/licenses/gpl-3.0.html"},
        )

        self.core_app = core_app

        # add api to core app
        self.core_app.mount(settings().api_prefix, self)

        # add root route
        self.add_api_route("/", self.root)

    async def root(self):
        if settings().api_docs_path is not None:
            return RedirectResponse(url=settings().api_prefix + settings().api_docs_path)
        if settings().api_redoc_path is not None:
            return RedirectResponse(url=settings().api_prefix + settings().api_redoc_path)
        return PlainTextResponse(f"{__title__} API v{__version__}")
