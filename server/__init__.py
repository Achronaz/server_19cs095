from flask import Flask, session, render_template
app = Flask(__name__,static_url_path='/static',static_folder='static',template_folder='templates')
app.config['UPLOAD_FOLDER'] = './upload'

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
import os
from datetime import timedelta
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)

from flask_cors import CORS
CORS(app)

# routes
from server.routes import *
