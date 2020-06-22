from server import db
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
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    