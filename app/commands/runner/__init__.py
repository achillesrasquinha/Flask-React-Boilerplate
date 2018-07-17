# imports - third-party imports
import click

# imports - module imports
from   app.commands.util import group_commands

@click.group("run")
def group():
    """
    Run Processes
    """
    pass

command = group_commands(group, (
    "app.commands.runner.web",
))