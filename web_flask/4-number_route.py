#!/usr/bin/python3
"""
Script that starts a Flask web application:
-Your web application must be listening on 0.0.0.0, port 5000
-Routes:
    /: display “Hello HBNB!”
You must use the option strict_slashes=False in your route definition
"""
from types import prepare_class
from flask import Flask, escape
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ Default method """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Default method """
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """ Default method """
    new = text.replace('_', ' ')
    return 'C %s' % escape(new)


@app.route('/python/')
@app.route('/python/<text>')
def python(text="is cool"):
    """ Default method """
    new = text.replace('_', ' ')
    return 'Python %s' % escape(new)


@app.route('/number/<n>')
def number(n):
    """ Default method """
    return '{:d} is a number'.format(int(n))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
