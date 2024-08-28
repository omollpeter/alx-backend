#!/usr/bin/env python3
"""
Contains a basic Flask app with a single route
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz


class Config:
    """
    Defines configuration settings for the Flask App
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


# babel = Babel(app)


# @babel.localeselector
def get_locale():
    """
    Matches the best language to be used in the application
    """
    if "locale" in request.args:
        return request.args.get("locale")
    if g.user:
        if g.user and g.user["locale"] in app.config["LANGUAGES"]:
            return g.user["locale"]
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_timezone():
    """
    Matches the best language to be used in the application
    """
    try:
        if "timezone" in request.args:
            timezone = pytz.timezone(request.args.get("timezone"))
        elif g.user:
            timezone = pytz.timezone(g.user["timezone"])
        else:
            timezone = pytz.timezone(app.config["BABEL_DEFAULT_TIMEZONE"])
    except pytz.exceptions.UnknownTimeZoneError:
        timezone = pytz.timezone(app.config["BABEL_DEFAULT_TIMEZONE"])
    finally:
        return timezone


babel = Babel(app, locale_selector=get_locale)


@app.context_processor
def inject_locale():
    """
    Injects get_locale function into template context
    """
    return dict(get_locale=get_locale, get_timezone=get_timezone)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Uses the login ID passed in the parameter to return the specific
    user
    """
    if "login_as" in request.args:
        id = request.args.get("login_as")
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """
    The function is run before any other function
    Sets user on flask.g.user if any
    """
    g.user = get_user()


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """
    View function for the the index page
    """
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run()
