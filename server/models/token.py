from server import db
from datetime import datetime
class Token(db.Model):
    __tablename__ = 'token'
    tokenid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    token = db.Column(db.String(255), nullable=False)
    updated = db.Column(db.DateTime, default=datetime.now())
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}