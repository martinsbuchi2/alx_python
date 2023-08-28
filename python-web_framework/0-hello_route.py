#!/usr/bin/python
"""
 script that starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)  # route to the root of our site, "/"
def hello():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)   # host is 'localhost'
