#!/usr/bin/python3
"""Module used to start a Flask web application
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    """Added function to root route, that displays greetings
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Function that displays "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>')
def c_post(text):
    """Function takes input parameter and renders it to user
    """
    formatted_text = text.replace('_', ' ')
    return "C {}".format(formatted_text)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
