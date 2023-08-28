#!/usr/bin/python
"""
the previous task to a new script that 
starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


""" doc"""
@app.route("/", strict_slashes=False)  # route to the root of our site, "/"
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)  # route to the root of our site, "/"
def hello_hbnb():
    return "HBNB"


""" doc"""
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return "C " + text.replace('_', ' ')


""" doc"""
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def c_text(text):
    return  "Python " + text.replace('_', ' ')

""" doc"""
if __name__ == "__main__":
    """run the flask app"""
    app.run(host='0.0.0.0', port=5000)   # host is 'localhost'