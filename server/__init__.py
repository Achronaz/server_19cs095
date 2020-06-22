from flask import Flask
app = Flask(__name__)

import yaml
config = yaml.load(open('config.yaml'),Loader=yaml.FullLoader)

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']
db = SQLAlchemy(app)

from server.routes import *