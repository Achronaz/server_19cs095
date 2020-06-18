from server import app, config
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']

db = SQLAlchemy(app)

# from server import db, User, Token, Recipes
# user = User(userid=1, username="user1", password="user1", role="admin")
# db.session.add(user)
# db.session.commit()
# print(Recipes.query.filter_by(id=38).all()[0].id)

class User(db.Model):
    __tablename__ = 'user'
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(255), nullable=False)

class Token(db.Model):
    __tablename__ = 'token'
    tokenid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    token = db.Column(db.String(255), nullable=False)
    updated = db.Column(db.DateTime, default=datetime.now())

class Recipes(db.Model):
    __tablename__ = 'recipes'
    name = db.Column(db.Text)
    id = db.Column(db.Integer, primary_key=True)
    minutes = db.Column(db.Integer)
    contributor_id = db.Column(db.Integer)
    submitted = db.Column(db.DateTime)
    tags = db.Column(db.Text)
    nutrition = db.Column(db.Text)
    n_steps = db.Column(db.Integer)
    steps = db.Column(db.Text)
    description = db.Column(db.Text)
    ingredients = db.Column(db.Text)
    n_ingredients = db.Column(db.Integer)