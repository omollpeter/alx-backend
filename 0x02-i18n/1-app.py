#!/usr/bin/env python3
"""
Contains a basic Flask app with a single route
"""


from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Defines configuration settings for the Flask App
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


babel = Babel(app)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """
    View function for the the index page
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
