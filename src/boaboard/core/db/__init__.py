from wiederverwendbar.singleton import Singleton as _Singleton
from wiederverwendbar.mongoengine import MongoengineDbSingleton as _MongoengineDbSingleton

from boaboard.core.settings import settings as _settings
from boaboard.core.logger import logger as _logger
from boaboard.core.db.employee import EmployeeDocument
from boaboard.core.db.location import LocationDocument
from boaboard.core.db.attendance import AttendanceDocument


def db() -> _MongoengineDbSingleton:
    # initialize logger
    _logger()

    try:
        return _Singleton.get_by_type(_MongoengineDbSingleton)
    except RuntimeError:
        return _MongoengineDbSingleton(settings=_settings(), init=True)