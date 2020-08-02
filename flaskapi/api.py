import predictor
import time
import os
import pathlib

from flask import Flask
from flask import request
from flask import abort


from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='../build', static_url_path='/')
#app = Flask(__name__)
# Max 128 mb file upload
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['MAX_CONTENT_LENGTH'] = 128 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = '/tmp/stop_sign_predict'
pathlib.Path(app.config['UPLOAD_FOLDER']).mkdir(parents=True, exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Serve the react files
# https://blog.miguelgrinberg.com/post/how-to-deploy-a-react--flask-project
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/time')
def get_current_time():
    print("hit the api")
    return {'time': time.time()}

# Prediction routes
# Requires enctype: multipart/form-data
# Inspired by https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/#uploading-files
# Currently just takes the uploaded file and saves it to /tmp/stop_sign_predict
@app.route('/predict_upload', methods=['POST'])
def predict_upload():
    print("hit the api")
    if 'file' not in request.files:
        abort(406)
    file = request.files['file']
    # if user does not select file, browser also
    # submits an empty part without filename
    if file.filename == '':
        abort(406)
    if file:
        filename = file.filename
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)
        return predictor.is_stopSign(path)
