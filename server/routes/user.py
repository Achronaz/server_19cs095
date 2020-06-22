from server import app
from flask import request
@app.route('/user', methods = ['GET'])
def user():
    return request.url

@app.route('/user/register', methods = ['POST'])
def user_register():
    return request.url

@app.route('/user/login', methods = ['POST'])
def user_login():
    return request.url

@app.route('/user/logout', methods = ['GET'])
def user_logout():
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