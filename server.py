from flask import Flask
app = Flask(__name__)

import yaml
config = yaml.load(open('./config.yaml'),Loader=yaml.FullLoader)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
