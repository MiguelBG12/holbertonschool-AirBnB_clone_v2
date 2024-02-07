#!usr/bin/python3
"""Script to start a Flask web"""

from flask import Flask

# Creating a Flask application instance
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    # Returns a simple greeting message
    return "Hello HBNB!"


if __name__ == '__main__':
    # Runs the Flask app on specified host and port, with debugging enabled
    app.run(host='0.0.0.0', port=5000, debug=True)
