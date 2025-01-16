from fastapi import FastAPI

from boaboard import __title__, __description__, __version__, __author__, __author_email__, __license__
from boaboard.core.settings import settings

api_app = FastAPI(
    debug=settings().app_debug,
    title=__title__,
    summary=f"{__title__} API",
    description=__description__,
    version=__version__,
    terms_of_service="https://bastelqaurtier.de/terms",
    contact={"name": __author__, "email": __author_email__},
    license_info={"name": __license__, "url": "https://www.gnu.org/licenses/gpl-3.0.html"},
)
