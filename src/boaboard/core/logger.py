from wiederverwendbar.singleton import Singleton
from wiederverwendbar.logger import LoggerSingleton

from boaboard import __name__ as __module_name__
from boaboard.core.settings import settings


def logger() -> LoggerSingleton:
    try:
        return Singleton.get_by_type(LoggerSingleton)
    except RuntimeError:
        return LoggerSingleton(name=__module_name__,
                               settings=settings(),
                               ignored_loggers_like=["pymongo", "asyncio", "parso", "engineio", "socketio"],
                               init=True)
