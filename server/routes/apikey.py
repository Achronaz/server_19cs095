from server import app, db, bcrypt, rows2dicts
from flask import request, jsonify, session, redirect, url_for
from server.models.user import User
from server.models.apikey import ApiKey
import secrets
from sqlalchemy import exc

# utils
def create_apikey(userid):
    try:
        apikey = ApiKey(userid=userid, apikey=secrets.token_hex())
        db.session.add(apikey)
        db.session.commit()
    except exc.SQLAlchemyError as ex:
        return jsonify({'status':'error','message':'{}'.format(ex.args[0])})
    except Exception:
        return jsonify({'status':'error','message':'unknown error'})
    return jsonify({'status':'success','message':'api key for user '+str(userid)+' created.'})

@app.route('/user/apikey/create', methods = ['GET'])
def user_apikey_create():
    if not session.get('user'):
        return jsonify({'status':'error','message':'please signin with user account.'})
    return create_apikey(session.get('user')['userid'])

@app.route('/admin/apikey/create', methods = ['GET'])
def admin_apikey_create():
    if not session.get('user') and session.get('user')['role'] == 'admin':
        return jsonify({'status':'error','message':'please signin with admin account.'})
    userid = request.args.get("userid", default=-1, type=int)
    if userid == -1:
        return jsonify({'status':'error','message':'userid is not presented'})
    return create_apikey(userid)

@app.route('/apikey/delete', methods = ['GET'])
def apikey_delete():
    if not session.get('user'):
        return jsonify({'status':'error','message':'please signin with user account.'})
    
    apikeyid = request.args.get("apikeyid", default="", type=str)
    if apikeyid == "":
        return jsonify({'status':'error','message':'apikeyid is not presented.'})

    user = session.get('user')
    target = ApiKey.query.filter_by(apikeyid=apikeyid).first()

    if target is None:
        return jsonify({'status':'error','message':'apikey '+ str(apikeyid) +' not found'})

    if(user['role'] != 'admin' and user['userid'] != target.userid):
        return jsonify({'status':'error','message':'permission denied: you don\'t have permission to delete this api key'})

    try:
        db.session.delete(target)
        db.session.commit()
    except exc.SQLAlchemyError as ex:
        return jsonify({'status':'error','message':'{}'.format(ex.args[0])})
    except Exception:
        return jsonify({'status':'error','message':'unknown error'})

    return jsonify({'status':'success','message':'api key '+ str(apikeyid) +' deleted.'})

