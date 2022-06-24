from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
#from src import *
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate')
def generate():
    return '123'


@app.route("/generate/<username>")
def greet(username):
    return "Hello " + username + "!"

app.run()