# imports - third-party imports
from   flask import Flask

# imports - module imports
import app

app = Flask(__name__,
    static_folder   = app.path.public,
    template_folder = app.path.templates
)