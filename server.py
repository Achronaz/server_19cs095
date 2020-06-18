from flask import Flask
import yaml

config = yaml.load(open('./config.yaml'),Loader=yaml.FullLoader)

app = Flask(__name__)

#import routes
from routes import *

if __name__ == '__main__':
    app.run(debug=True)

# from server import db, User, Token, Recipes
# user = User(userid=1, username="user1", password="user1", role="admin")
# db.session.add(user)
# db.session.commit()
# print(Recipes.query.filter_by(id=38).all()[0].id)