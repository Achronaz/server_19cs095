from server import app, rows2dicts, is_authenticated
from server.models.recipes import Recipes
from flask import request, jsonify

@app.route('/recipes/search', methods = ['GET'])
def recipe_search():

    apikey = request.args.get('apikey', default="", type=str)
    if not is_authenticated(apikey):
        return jsonify({"status":"error","message":"invalid api key."})

    foodkeyword = request.args.get('foodkeyword', default="", type=str)
    if foodkeyword == "":
        return jsonify({"status":"error","message":"foodkeyword is not presented"})

    rows = rows2dicts(Recipes.query.filter(Recipes.name.like('%'+foodkeyword+'%') | Recipes.tags.like('%'+foodkeyword+'%')).limit(10).all())
    return rows