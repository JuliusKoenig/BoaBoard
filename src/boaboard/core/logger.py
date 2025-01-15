from wiederverwendbar.singleton import Singleton
from wiederverwendbar.logger.singleton import LoggerSingleton as _LoggerSingleton

from boaboard import __module_name__
from boaboard.core.settings import Settings


def _logger() -> _LoggerSingleton:
    try:
        return Singleton.get_by_type(_LoggerSingleton)
    except RuntimeError:
        return _LoggerSingleton(name=__module_name__, settings=Settings(), init=True)


Logger = _logger
