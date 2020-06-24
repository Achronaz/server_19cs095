from server import app
from flask import render_template

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/docs', methods = ['GET'])
def docs():
    return render_template('docs.html')

@app.route('/demo', methods = ['GET'])
def demo():
    return render_template('demo.html')

@app.route('/register', methods = ['GET'])
def register():
    return render_template('register.html')