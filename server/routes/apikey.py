from server import app, db, bcrypt
from flask import request, jsonify, session, redirect, url_for
from server.models.user import User
from server.models.token import Token
import secrets
from sqlalchemy import exc

#utils
def rows2dicts(rows):
    return jsonify([row.as_dict() for row in rows])

@app.route('/user/add/apikey', methods = ['GET'])
def user_add_apikey():
    if not session.get('user'):
        jsonify({'status':'error','message':'permission denied, please signin!'})

    user = session.get('user')
    try:
        apikey = Token(session.get('user')['userid'], secrets.token_hex())
        db.session.add(apikey)
        db.session.commit()
    except exc.SQLAlchemyError as ex:
        return jsonify({'status':'error','message':'{}'.format(ex.args[0])})
    except Exception:
        return jsonify({'status':'error','message':'unknown error'})
    return jsonify({'status':'success','message':'api key for '+user['username']+' created.'})

@app.route('/user/remove/apikey', methods = ['GET'])
def user_remove_apikey():
    tid = request.args.get("tid", default="", type=str)
    if tid == "":
        return jsonify({'status':'error','message':'tid not presented'})
    if not session.get('user'):
        return jsonify({'status':'error','message':'permission denied, please signin!'})
    user = session.get('user')
    target = Token.query.filter_by(tid=tid).first()

    if target is None:
        return jsonify({'status':'error','message':'apikey not found'})

    if(user['role'] != 'admin' and user['userid'] != target.userid):
        return jsonify({'status':'error','message':'permission denied: you don\'t have permission to remove this api key'})

    try:
        db.session.delete(target)
        db.session.commit()
    except exc.SQLAlchemyError as ex:
        return jsonify({'status':'error','message':'{}'.format(ex.args[0])})
    except Exception:
        return jsonify({'status':'error','message':'unknown error'})

    return jsonify({'status':'success','message':'api key for '+ user['username'] +' deleted.'})

@app.route('/user/list/apikey', methods = ['GET'])
def user_list_apikey():
    if not session.get('user'):
        return jsonify({'status':'error','message':'permission denied, please signin!'})
    user = session.get('user')
    if user['role'] == 'admin':
        return rows2dicts(Token.query.all())
    else:
        return rows2dicts(Token.query.filter_by(userid=user['userid']).all())


@app.route('/admin/add/apikey', methods = ['GET'])
def admin_add_apikey():
    if not session.get('user') and session.get('user')['role'] == 'admin':
        return jsonify({'status':'error','message':'permission denied, admin required.'})

    userid = request.args.get("userid", default="", type=str)
    if userid == "":
        return jsonify({'status':'error','message':'userid is not presented'})

    return request.url

@app.route('/admin/remove/apikey', methods = ['GET'])
def admin_remove_apikey():
    if not session.get('user') and session.get('user')['role'] == 'admin':
        return jsonify({'status':'error','message':'permission denied, admin required.'})

    tid = request.args.get("tid", default="", type=str)
    if tid == "":
        return jsonify({'status':'error','message':'tid is not presented'})

    return request.url

