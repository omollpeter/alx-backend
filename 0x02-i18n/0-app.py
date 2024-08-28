#!/usr/bin/env python3
"""
Contains a basic Flask app with a single route
"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    title = "Welcome to Holberton"
    header = "Hello world"
    return render_template("0-index.html", title=title, header=header)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
