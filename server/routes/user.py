from server import app, db
from flask import request, jsonify, session
from server.models.user import User
from server.models.token import Token

# utils
def hash(content):
    return content

@app.route('/user', methods = ['GET'])
def user():
    return request.url

@app.route('/user/register', methods = ['POST'])
def user_register():

    username = request.form.get("username", default=None, type=str)
    password = request.form.get("password", default=None, type=str)
    repassword = request.form.get("repassword", default=None, type=str)

    if username is None or password is None or repassword is None:
        return jsonify({'status':'error','message':'username, password or repassword not presented'})

    if password != repassword:
        return jsonify({'status':'error','message':'password and repassword not match'})

    user = User(name=username, password=hash(password), role='user')
    db.session.add(user)
    db.session.commit()

    return jsonify({'status':'success','message':'register success'})

@app.route('/user/login', methods = ['POST'])
def user_login():
    
    username = request.form.get("username", default=None, type=str)
    password = request.form.get("password", default=None, type=str)

    if username is None or password is None:
        return jsonify({'status':'error','message':'username or password not presented'})
    
    #select from db, compare hashed password

    session['username'] = username
    session.permanent = True

    # redirect
    return request.url

@app.route('/user/logout', methods = ['GET'])
def user_logout():
    session['username'] = False

    # redirect
    return request.url

@app.route('/user/add/token', methods = ['GET'])
def user_add_token():
    return request.url

@app.route('/user/remove/token', methods = ['GET'])
def user_remove_token():
    return request.url

# need admin right
@app.route('/admin/add/user', methods = ['GET'])
def admin_add_user():
    return request.url

@app.route('/admin/edit/user', methods = ['GET'])
def admin_edit_user():
    return request.url

@app.route('/admin/remove/user', methods = ['GET'])
def admin_remove_user():
    return request.url

@app.route('/admin/add/token', methods = ['GET'])
def admin_add_token():
    return request.url

@app.route('/admin/remove/token', methods = ['GET'])
def admin_remove_token():
    return request.url