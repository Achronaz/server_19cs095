from server import app
from server.models.recipes import Recipes
from flask import request, jsonify

#utils
def rows2dicts(rows):
    return jsonify([row.as_dict() for row in rows])

@app.route('/recipe/search/<input>', methods = ['GET'])
def recipe_search(input):
    rows = rows2dicts(Recipes.query.filter(Recipes.name.like('%'+input+'%') | Recipes.tags.like('%'+input+'%')).limit(10).all())
    return rows