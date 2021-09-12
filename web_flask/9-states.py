#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def states_id(id=None):
    """ Default method """
    states = storage.all(State)
    if (id):
        return render_template('9-states.html', states=states, id=id)
    return render_template('9-states.html', states=states)


@app.teardown_appcontext
def close(self):
    """function that remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
