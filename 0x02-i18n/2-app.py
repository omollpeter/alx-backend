#!/usr/bin/env python3
"""
Contains a basic Flask app with a single route
"""


from flask import Flask, render_template, request
from flask_babel import Babel
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config["LANGUAGES"])

@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """
    View function for the the index page
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
