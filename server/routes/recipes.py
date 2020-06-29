from server import app
from server.models.recipes import Recipes
from flask import request, jsonify

#utils
def rows2dicts(rows):
    return jsonify([row.as_dict() for row in rows])

@app.route('/recipes/search', methods = ['GET'])
def recipe_search():
    foodkeyword = request.args.get('foodkeyword', default="", type=str)
    if foodkeyword == "":
        return jsonify({"status":"error","message":"foodkeyword is not presented"})

    rows = rows2dicts(Recipes.query.filter(Recipes.name.like('%'+foodkeyword+'%') | Recipes.tags.like('%'+foodkeyword+'%')).limit(10).all())
    return rows