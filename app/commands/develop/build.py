# imports - third-party imports
import click

# imports - module imports
from   app.system import popen, which
import app

@click.command("build")
@click.option("-m", "--mode",
    type    = click.Choice(["development", "production"]),
    default = "development",
    help    = "Mode Type"
)
@click.option("-w", "--watch",
    is_flag = True,
    help    = "Watch"
)
def command(mode = "development", watch = False):
    popen("{yarn} run {command}".format(
        yarn    = which("yarn", raise_err = True),
        command = "build:{mode}".format(mode = "watch" if watch else mode)
    ))