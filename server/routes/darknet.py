from server import app
from flask import request
@app.route('/darknet', methods = ['GET'])
def darknet():
    return request.url