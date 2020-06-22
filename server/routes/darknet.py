import sys
sys.path.append('../../')
import GitHub.darknet as dn
from server import app
from flask import request
@app.route('/darknet', methods = ['GET'])
def darknet():
    return dn.detect()