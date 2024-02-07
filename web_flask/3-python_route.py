#!/usr/bin/python3
"""Script that starts a Flask web with 4 routes"""
from flask import Flask

# Creating a Flask application instance
app = Flask(__name__)


# Defines a route '/' and the corresponding view function hello_route
@app.route('/', strict_slashes=False)
def hello_route():
    # Returns a simple greeting message
    return "Hello HBNB!"


# Defines a route '/hbnb' and the corresponding view function hi_route
@app.route('/hbnb', strict_slashes=False)
def hi_route():
    # Returns a message "HBNB" when the route '/hbnb' is accessed
    return "HBNB"


# Defines a route '/c/<text>' and the corresponding view function c_route
@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    # Replaces underscores with spaces in the text parameter
    text = text.replace("_", " ")
    # Returns a formatted message including the text parameter
    return f'C {text}'


# Defines routes with the view function python_route
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is_cool"):
    # Replaces underscores with spaces in the text parameter
    text = text.replace("_", " ")
    # Returns a formatted message including the text parameter
    return f'Python {text}'


if __name__ == '__main__':
    # Runs the Flask app on specified host and port, with debugging enabled
    app.run(host='0.0.0.0', port=5000, debug=True)
