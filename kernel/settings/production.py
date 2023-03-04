from decouple import config

from .base import *
from .services import *
from .packages import *

DEBUG = config('DEBUG', cast=bool, default=False)
