from server import app,config,is_authenticated
import requests, json
from flask import request, jsonify

@app.route('/place/search', methods = ['GET'])
def google_place_search():

    apikey = request.args.get('apikey', default="", type=str)
    if not is_authenticated(apikey,request.environ['HTTP_HOST']):
        return jsonify({"status":"error","message":"invalid api key."})

    foodkeyword = request.args.get('foodkeyword', default="", type=str)
    if foodkeyword == "":
        return jsonify({"status":"error","message":"foodkeyword is not presented"})

    latlong = request.args.get('latlng', default="22.280276,114.176953", type=str)
    radius = request.args.get('radius', default="1000", type=str)

    params={
        'query':foodkeyword,
        'key':config['GOOGLE_PLACE_API_KEY'],
        'fields':'place_id,name,formatted_address,opening_hours,rating,geometry,photos,url',
        'type':'restaurant',
        'location':latlong,
        radius:radius
    }
    res = json.loads(requests.get(config['GOOGLE_PLACE_API_ENDPOINT']+'/textsearch/json', params=params).content)
    return res

@app.route('/place/details', methods = ['GET'])
def google_place_details():

    apikey = request.args.get('apikey', default="", type=str)
    if not is_authenticated(apikey,request.environ['HTTP_HOST']):
        return jsonify({"status":"error","message":"invalid api key."})

    place_id = request.args.get('place_id', default="", type=str)
    if place_id == "":
        return jsonify({"status":"error","message":"place_id is not presented"})
        
    params={
        'place_id':place_id,
        'key':config['GOOGLE_PLACE_API_KEY'],
        'fields':'place_id,name,formatted_address,opening_hours,rating,geometry,photos,url'
    }
    res = json.loads(requests.get(config['GOOGLE_PLACE_API_ENDPOINT']+'/details/json', params=params).content)
    return res