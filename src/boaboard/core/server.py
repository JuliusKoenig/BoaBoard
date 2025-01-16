from wiederverwendbar.uvicorn import UvicornServer

from boaboard.core.settings import Settings


class Server(UvicornServer):
    def __init__(self):
        super().__init__(app="boaboard.core.app:CoreApp",
                         factory=True,
                         settings=Settings())


