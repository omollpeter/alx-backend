#!/usr/bin/env python3
"""
Contains a basic Flask app with a single route
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel, _


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


@babel.localeselector
def get_locale():
    """
    Matches the best language to be used in the application
    """
    if "locale" in request.args:
        return request.args.get("locale")
    return request.accept_languages.best_match(app.config["LANGUAGES"])


# babel = Babel(app, locale_selector=get_locale)


@app.context_processor
def inject_locale():
    """
    Injects get_locale function into template context
    """
    return dict(get_locale=get_locale)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """
    View function for the the index page
    """
    return render_template("4-index.html")


# if __name__ == "__main__":
#     app.run()
