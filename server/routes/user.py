from server import app, db, bcrypt
from flask import request, jsonify, session, redirect, url_for
from server.models.user import User
from server.models.token import Token
import secrets
from sqlalchemy import exc

@app.route('/user', methods = ['GET'])
def user():

    return secrets.token_hex()

@app.route('/user/signup', methods = ['POST'])
def user_register():

    username = request.form.get("username", default="", type=str)
    password = request.form.get("password", default="", type=str)
    repassword = request.form.get("repassword", default="", type=str)

    if username == "" or password == "" or repassword == "":
        return jsonify({'status':'error','message':'username, password or repassword not presented'})

    if password != repassword:
        return jsonify({'status':'error','message':'password and repassword not match'})

    try:
        user = User(username=username, password=bcrypt.generate_password_hash(password), role='user')
        db.session.add(user)
        db.session.commit()
    except exc.SQLAlchemyError as ex:
        print(ex.args)
        return jsonify({'status':'error','message':'{}'.format(ex.args[0])})
    except Exception:
        return jsonify({'status':'error','message':'unknown error'})

    return jsonify({'status':'success','message':'signup success'})

@app.route('/user/signin', methods = ['POST'])
def user_signin():

    username = request.form.get("username", default="", type=str)
    password = request.form.get("password", default="", type=str)

    if username == "" or password == "":
        return jsonify({'status':'error','message':'username or password not presented'})

    #select from db, compare hashed password
    user = User.query.filter_by(username=username).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({'status':'error','message':'username or password incorrect'})

    session['user'] = {
        "userid":user.userid,
        "username":user.username,
        "role":user.role
    }
    session.permanent = True

    return jsonify({'status':'success','message':'signin success'})

@app.route('/user/signout', methods = ['GET'])
def user_signout():
    session['user'] = False
    return jsonify({'status':'success','message':'signout success'})

@app.route('/user/add/token', methods = ['GET'])
def user_add_token():
    token = secrets.token_hex()
    token = Token(session['user'].userid, token)
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