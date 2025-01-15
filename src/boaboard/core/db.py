from wiederverwendbar.singleton import Singleton
from wiederverwendbar.mongoengine.singleton import MongoengineDbSingleton as MongoengineDbSingleton

from boaboard.core.settings import Settings


def _db() -> MongoengineDbSingleton:
    try:
        return Singleton.get_by_type(MongoengineDbSingleton)
    except RuntimeError:
        return MongoengineDbSingleton(settings=Settings(), init=True)


Db = _db
