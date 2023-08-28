#!/usr/bin/python
"""
the previous task to a new script that starts a Flask web application:
/number/<n>: display “n is a number” only if n is an integer
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)  # route to the root of our site, "/"
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)  # route to the root of our site, "/"
def hello_hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return "C " + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)   # host is 'localhost'
