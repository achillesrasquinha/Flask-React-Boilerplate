# imports - third-party imports
import click

# imports - standard imports
import app
from   app.commands.util import group_commands

@click.group(app.__name__)
@click.version_option(app.__version__,
    message = "%(version)s"
)
def group():
    """
    App
    """
    pass

command = group_commands(group, (
    "app.commands.develop.build",
    
    "app.commands.runner",
    "app.commands.runner.start",
))