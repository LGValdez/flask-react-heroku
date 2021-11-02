from flask import Blueprint
from flask_cors import CORS, cross_origin

api = Blueprint('api', __name__)
CORS(api)


@api.route('')
@cross_origin()
def api_base():
    return {
        'message': "Congratulations you have accessed the api!"
    }
