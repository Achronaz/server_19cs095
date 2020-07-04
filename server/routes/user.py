from server import app, db, bcrypt
from flask import request, jsonify, session, redirect, url_for
from server.models.user import User
from server.models.apikey import ApiKey
import secrets
from sqlalchemy import exc

# util
def create_user(username,password,role):
    try:
        user = User(username=username, password=bcrypt.generate_password_hash(password), role=role)
        db.session.add(user)
        db.session.commit()
    except exc.SQLAlchemyError as ex:
        print(ex.args)
        return jsonify({'status':'error','message':'{}'.format(ex.args[0])})
    except Exception:
        return jsonify({'status':'error','message':'unknown error'})

    return jsonify({'status':'success','message':'user created.'})

@app.route('/user/signup', methods = ['POST'])
def user_signup():
    username = request.form.get("username", default="", type=str)
    password = request.form.get("password", default="", type=str)
    repassword = request.form.get("repassword", default="", type=str)
    if username == "" or password == "" or repassword == "":
        return jsonify({'status':'error','message':'username, password or repassword not presented'})
    if password != repassword:
        return jsonify({'status':'error','message':'password and repassword not match'})
    return create_user(username,password,'user')

@app.route('/user/signin', methods = ['POST'])
def user_signin():
    username = request.form.get("username", default="", type=str)
    password = request.form.get("password", default="", type=str)
    if username == "" or password == "":
        return jsonify({'status':'error','message':'username or password not presented'})
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

# need admin right
@app.route('/admin/add/user', methods = ['GET'])
def admin_add_user():
    return jsonify({'status':'success','message':'user added.'})

@app.route('/admin/edit/user', methods = ['GET'])
def admin_edit_user():
    return jsonify({'status':'success','message':'user updated.'})

@app.route('/admin/remove/user', methods = ['GET'])
def admin_remove_user():
    userid = request.form.get("userid", default="", type=str)
    
    return jsonify({'status':'success','message':'user removed.'})

