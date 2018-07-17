# imports - standard imports
import sys
from   subprocess     import list2cmdline

# imports - third-party imports
import click
from   honcho.manager import Manager

# imports - module imports
from   app.util       import list_filter
import app

@click.command("start")
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
        daemons   = [
            app.Dict({
                    "name": "web",
                "command": ["app", "run", "web",
                    "--host", host, "--port", port, "--mode", mode
                ]
            }),
            app.Dict({
                    "name": "build",
                "command": list_filter(["app", "build",
                    "--mode",  mode,
                    "--watch" if mode == "development" else ""
                ], bool)
            })
        ]

        manager  = Manager()
        for daemon in daemons:
            name = "{name}".format(
                name  = daemon.name
            )
            command = list2cmdline([str(arg) for arg in daemon.command])
            manager.add_process(
                name,
                command
            )

        code = manager.loop()

        sys.exit(code)