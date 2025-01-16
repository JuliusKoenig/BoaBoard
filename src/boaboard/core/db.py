from wiederverwendbar.singleton import Singleton
from wiederverwendbar.mongoengine import MongoengineDbSingleton

from boaboard.core.settings import settings
from boaboard.core.logger import logger


def db() -> MongoengineDbSingleton:
    # initialize logger
    logger()

    try:
        return Singleton.get_by_type(MongoengineDbSingleton)
    except RuntimeError:
        return MongoengineDbSingleton(settings=settings(), init=True)
