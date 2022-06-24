from flask import Flask, render_template, Response, request, redirect, url_for
#from src import *
app = Flask(__name__, template_folder='pages')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    return render_template('generation.html')

@app.route("/generate/<username>")
def greet(username):
    return "Hello " + username + "!"


@app.route("/generate", methods=['POST', 'GET'])
def move_forward():
    if request.method == 'POST' or 'GET':
        return redirect(url_for('generate'))

app.run()