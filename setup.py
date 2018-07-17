import sys
import os.path as osp

from   setuptools import setup, find_packages

import pip

try:
    from pip._internal.req import parse_requirements # pip 10
except ImportError:
    from pip.req           import parse_requirements # pip 9

with open(osp.join("app", "__attr__.py")) as f:
    content = f.read()
    exec(content)

def get_dependencies(type_ = None):
    path         = osp.abspath("requirements.txt")
    requirements = [str(ir.req) for ir in parse_requirements(path, session = "hack")]
    
    return requirements

setup(
    name                 = __name__,
    version              = __version__,
    url                  = __url__,
    author               = __author__,
    author_email         = __email__,
    description          = __description__,
    packages             = find_packages(),
    entry_points         = {
        "console_scripts": [
            "{name} = {name}.__main__:command".format(name = __name__)
        ]
    },
    install_requires     = get_dependencies(),
    include_package_data = True
)