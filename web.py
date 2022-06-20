from flask import Flask
from src import *
app = Flask(__name__)
app.run()

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/generate')
def generate():
    return '123'


@app.route("/generate/<username>")
def greet(username):
    return "Hello " + username + "!"