from wiederverwendbar.singleton import Singleton
from wiederverwendbar.uvicorn import UvicornServer

from boaboard.core.settings import Settings


class _Server(UvicornServer, metaclass=Singleton):
    def __init__(self):
        super().__init__(app="boaboard.core.app:CoreApp",
                         factory=True,
                         settings=Settings())


def _server() -> _Server:
    try:
        return Singleton.get_by_type(_Server)
    except RuntimeError:
        return _Server(init=True)


Server = _server
