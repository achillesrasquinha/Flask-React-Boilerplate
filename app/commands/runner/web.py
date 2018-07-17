# imports - third-party imports
import click

# imports - module imports
from   app.server import app

@click.command("web")
@click.option("-h", "--host",
    default = "0.0.0.0",
    help    = "Host Name"
)
@click.option("-p", "--port",
    type    = int,
    default = 5000,
    help    = "Port Number"
)
@click.option("-m", "--mode",
    type    = click.Choice(["development", "production"]),
    default = "development",
    help    = "Mode Type"
)
def command(host = "0.0.0.0", port = 5000, mode = "development"):
    if mode == "development":
        app.run(host = host, port = port, debug = True)