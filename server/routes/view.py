from server import app
from flask import render_template, request

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/documentation', methods = ['GET'])
def docs():
    return render_template('documentation.html')

@app.route('/demonstration', methods = ['GET'])
def demo():
    return render_template('demonstration.html')

@app.route('/register', methods = ['GET'])
def register():
    return render_template('register.html')

@app.errorhandler(404)
def not_found(e):
    ip = '';
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    print("404, url="+request.url+", remote_addr="+ip)
    return render_template("404.html")