#!/usr/bin/env python3

from flask import Flask, render_template
from flask_babel import Babel, _


app = Flask(__name__)
app.config["BABEL_DEFAULT_LOCALE"] = "es"
babel = Babel(app)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
