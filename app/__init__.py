# imports - standard imports
import os.path as osp

# imports - third-party imports
import addict

# imports - module imports
from app.__attr__  import (
    __name__,
    __version__
)
from app           import system
from app.logger    import get_logger
from app.exception import *

class Dict(addict.Dict):
    pass

path = Dict()
path.base      = system.pardir(__file__)
path.templates = osp.join(path.base, "templates")
path.public    = osp.join(path.base, "public")

log  = get_logger()