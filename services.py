from models import db, User, Token, Recipes

# user
def create_user(username, password, confirm_password, role):
    user = User(username=username,password=password,role=role)
    db.session.add(token)
    db.session.commit()
    print('user created')

def user_login(username, password):
    db.query.filter_by(username=username,password=password).first()
    # set session if exists

def user_logout():
    # destory session
    print()

# token
def create_token(userid):
    token = Token(userid=userid)
    db.session.add(token)
    db.session.commit()
    print('token created')

# darknet
def detect():
    return ''

# recipes


# google map
