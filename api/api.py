from flask import Blueprint, request
from flask_cors import CORS, cross_origin
from .me.me import about_me
from .projects.projects import get_projects

api = Blueprint('api', __name__)
CORS(api)


@api.route('')
@cross_origin()
def api_base():
    return {
        'message': "Congratulations you have accessed the api!"
    }

@api.route('/me', methods=['GET'])
@cross_origin()
def api_about_me():
    return about_me()

@api.route('/projects', methods=['GET'])
@cross_origin()
def projects_endpoint():
    params = request.args
    return get_projects(params=params)
