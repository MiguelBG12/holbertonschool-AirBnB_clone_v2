#!/usr/bin/python3
""" Script to start a Flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def storage_close(self):
    """Close the session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """ Shows the list of states"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template("7-states_list.html", states=sorted_states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """ Shows the list of cities in the id state"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template("9-states.html",
                           states=storage.all(State).get(f'State.{id}'))


if __name__ == '__main__':
    """ start the web app """
    app.run(host='0.0.0.0', port=5000)