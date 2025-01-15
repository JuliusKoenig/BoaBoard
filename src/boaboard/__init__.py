from wiederverwendbar.logger.singleton import LoggerSingleton

from boaboard.core.environment import Environment
from boaboard.core.settings import Settings

__title__ = "boaboard"
__version__ = "0.1.0"
__author__ = "Julius Koenig"
__author_email__ = "info@bastelquartier.de"
__license__ = "GPL-3.0"

# initiate environment
Environment(init=True)

# initiate settings
Settings(file_path="settings", init=True)

# initiate logging
LoggerSingleton(name=__name__, settings=Settings(), init=True)
