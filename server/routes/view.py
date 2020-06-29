from server import app
from flask import render_template, request, session

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/docs', methods = ['GET'])
def docs():
    return render_template('documentation.html')

@app.route('/demo', methods = ['GET'])
def demo():
    return render_template('demonstration.html')

@app.route('/apikey', methods = ['GET'])
def apikey():
    if session.get('user'):
        return render_template('apikey.html')
    else:
        return "Permission Denied"

@app.route('/user/manage', methods = ['GET'])
def manage_user():
    if session.get('user') and session.get('user')['role'] == 'admin':
        return render_template('manage_user.html')
    else:
        return "Permission Denied"

@app.errorhandler(404)
def not_found(e):
    ip = '';
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    print("404, url="+request.url+", remote_addr="+ip)
    return render_template("404.html")