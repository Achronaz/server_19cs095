from server import app
from server.models.recipes import Recipes
from flask import request, jsonify

#utils
def rows2dicts(rows):
    return jsonify([row.as_dict() for row in rows])

@app.route('/recipe', methods = ['GET'])
def recipe():
    return request.url

@app.route('/recipe/test', methods = ['GET'])
def test():
    rows = rows2dicts(Recipes.query.limit(2).all())
    return rows