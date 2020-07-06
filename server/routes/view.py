from server import app, db, rows2dicts
from flask import render_template, request, session
from server.models.apikey import ApiKey
from server.models.user import User

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
        apikeyList = []
        if session.get('user')['role'] == 'admin':
            apikeyList = db.session.query(ApiKey, User).join(User, User.userid==ApiKey.userid).all()
        else:
            apikeyList = db.session.query(ApiKey, User).join(User, User.userid==ApiKey.userid).filter(ApiKey.userid==session.get('user')['userid']).all()
        return render_template('apikey.html',apikeyList=apikeyList)
    else:
        return "Permission Denied"

@app.route('/user', methods = ['GET'])
def manage_user():
    if session.get('user') and session.get('user')['role'] == 'admin':
        userList = User.query.all()
        return render_template('user.html',userList=userList)
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