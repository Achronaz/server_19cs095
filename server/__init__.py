import os
from flask import Flask, session, render_template, jsonify
app = Flask(__name__,static_url_path='/static',static_folder='static',template_folder='templates')
app.config['UPLOAD_FOLDER'] = os.path.dirname(os.path.realpath(__file__)) + '/upload'

# bcrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# config
import yaml
config = yaml.load(open('config.yaml'),Loader=yaml.FullLoader)

# database
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']
db = SQLAlchemy(app)

# session
from datetime import timedelta
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)

from flask_cors import CORS
CORS(app)

# routes
@app.context_processor
def inject_global():
    return dict(server_endpoint=config['SERVER_ENDPOINT'])

# utils
def rows2dicts(rows):
    return jsonify([row.as_dict() for row in rows])

from server.models.apikey import ApiKey
def is_authenticated(apikey,origin):
    if origin in ['localhost:5000','api.achronaz.com']:
        return True
    apikey = ApiKey.query.filter_by(apikey=apikey).first()
    return apikey is not None

from server.routes import *
