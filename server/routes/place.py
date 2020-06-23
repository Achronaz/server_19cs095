from server import app,config
import requests, json

@app.route('/place/search/<input>', methods = ['GET'])
def google_place_search(input):
    params={
        'query':input,
        'key':config['GOOGLE_PLACE_API_KEY'],
        'fields':'place_id,name,formatted_address,opening_hours,rating,geometry,photos,url',
        'type':'restaurant'
    }
    res = json.loads(requests.get(config['GOOGLE_PLACE_API_ENDPOINT']+'/textsearch/json', params=params).content)
    return res

@app.route('/place/details/<place_id>', methods = ['GET'])
def google_place_details(place_id):
    params={
        'place_id':place_id,
        'key':config['GOOGLE_PLACE_API_KEY'],
        'fields':'place_id,name,formatted_address,opening_hours,rating,geometry,photos,url'
    }
    res = json.loads(requests.get(config['GOOGLE_PLACE_API_ENDPOINT']+'/details/json', params=params).content)
    return res