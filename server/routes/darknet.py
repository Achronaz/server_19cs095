import sys, os
sys.path.append('../../darknet')
import darknet.darknet as dn

from server import app
from flask import request, render_template

# load YOLOv4 model
MODEL_CFG = 'darknet/custom5-512.cfg'
MODEL_WEIGHTS = 'darknet/custom5-512.weights'
MODEL_DATA = 'darknet/custom5-512.data'

net = dn.load_net_custom(
    str.encode(MODEL_CFG),
    str.encode(MODEL_WEIGHTS), 0, 1)
meta = dn.load_meta(str.encode(MODEL_DATA))

# start Flask Server
from flask import Flask, jsonify ,request, render_template
from werkzeug.utils import secure_filename
from flask_cors import CORS
import uuid
from PIL import Image

UPLOAD_FOLDER = os.getcwd() + "../upload/"
ALLOWED_EXTENSIONS = {'png', 'jpg'}

#utils
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def predict(filepath):
    predictions = dn.detect(net, meta, str.encode(filepath))
    temp = []
    img = Image.open(filepath)
    width = img.size[0]
    height = img.size[1]
    for prediction in predictions:
        label = prediction[0]
        similarity = prediction[1]
        cx = prediction[2][0]
        cy = prediction[2][1]
        w = prediction[2][2]
        h = prediction[2][3]
        x1 = cx - w / 2
        y1 = cy - h / 2
        x2 = cx + w / 2
        y2 = cy + h / 2
        temp.append({'label':label,'similarity':similarity,'x1':x1,'y1':y1,'x2':x2,'y2':y2})
    return jsonify(temp)

@app.route('/darknet/detect', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request.files)
        if 'file' not in request.files:
            return jsonify({'msg':'no file part'})
        file = request.files['file']
        if file.filename == '':
            return jsonify({'msg':'no selected file'})
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            base, ext = os.path.splitext(filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], str(uuid.uuid4()) + ext )
            file.save(filepath)
            return predict(filepath)
    return render_template('documentation.html')
