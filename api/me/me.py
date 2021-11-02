from ..api import api
from flask_cors import cross_origin
from models.models import User
from flask import request, Response
from flask import jsonify


@api.route('/me', methods=['GET', 'POST'])
@cross_origin()
def about_me():
    if request.method == 'GET':
        users = User.query.all()
        results = [{
            'id': user.id,
            'about': user.about,
            'title': user.title,
            'name': user.name
        } for user in users]
        return jsonify(results)

    if request.method == 'POST':
        User.create(request.args)
        return Response(status=200)


@api.route('/me/<user_id>', methods=['GET', 'DELETE'])
@cross_origin()
def about_me_with_id(user_id):
    if request.method == 'GET':
        user = User.query.filter_by(id=user_id).first()
        results = {
            'id': user.id,
            'about': user.about,
            'title': user.title,
            'name': user.name
        }
        return jsonify(results)

    if request.method == 'DELETE':
        User.unlink(user_id)
        return Response(status=200)
