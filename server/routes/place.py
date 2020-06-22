from server import app,config
import requests, json

@app.route('/place/search/<input>', methods = ['GET'])
def google_place_search(input):
    params={
        'key':config['GOOGLE_PLACE_API_KEY'],
        'inputtype':'textquery',
        'fields':'photos,formatted_address,name,opening_hours,rating',
        'input':input
    }
    res = json.loads(requests.get(config['GOOGLE_PLACE_API_ENDPOINT'], params=params).content)
    return res