from server import app
from flask import request
@app.route('/user', methods = ['GET'])
def user():
    return request.url