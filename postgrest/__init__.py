from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    __version__ = "dev"

from .client import Client, Error
from .filters import *
from .model import Model
from .model_client import ModelClient
