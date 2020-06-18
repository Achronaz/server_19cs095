from server import app
from services import *

@app.route('/')
def index():
    return 'Flask'