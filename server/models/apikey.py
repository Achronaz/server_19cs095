from server import db
from datetime import datetime
class ApiKey(db.Model):
    __tablename__ = 'apikey'
    apikeyid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.userid'))
    apikey = db.Column(db.String(255), nullable=False)
    updated = db.Column(db.DateTime, default=datetime.now())
    user = db.relationship('User', backref="ApiKey")
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}