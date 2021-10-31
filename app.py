from flask import Flask
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin
from api.api import api

app = Flask(__name__, static_folder='frontend/build', static_url_path='')
CORS(app)

app.register_blueprint(api, url_prefix='/api')


@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run()
