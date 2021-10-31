from flask import Blueprint
from flask_cors import CORS, cross_origin
from .me.me import about_me

api = Blueprint('api', __name__)
CORS(api)


@api.route('')
@cross_origin()
def api_base():
    return {
        'message': "Congratulations you have accessed the api!"
    }

@api.route('/me')
@cross_origin()
def api_about_me():
    return about_me()
