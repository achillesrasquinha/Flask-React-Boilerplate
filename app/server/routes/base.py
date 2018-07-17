# imports - third-party imports
from flask          import render_template

# imports - module imports
from app.server.app import app

@app.route("/")
def index():
    template = render_template("pages/index.html")
    return template