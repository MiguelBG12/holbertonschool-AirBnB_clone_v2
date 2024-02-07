#!/usr/bin/python3
"""Script to start a Flask web with 2 routes"""

from flask import Flask

# Creating a Flask application instance
app = Flask(__name__)


"""Defines a route '/' and the corresponding view function hello_route"""
@app.route('/', strict_slashes=False)
def hello_route():
    # Returns a simple greeting message
    return "Hello HBNB!"


"""Defines a route '/hbnb' and the corresponding view function hi_route"""
@app.route('/hbnb', strict_slashes=False)
def hi_route():
    # Returns a message "HBNB" when the route '/hbnb' is accessed
    return "HBNB"


if __name__ == '__main__':
    # Runs the Flask app on specified host and port, with debugging enabled
    app.run(host='0.0.0.0', port=5000, debug=True)
