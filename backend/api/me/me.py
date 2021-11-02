from backend.api.api import api
from flask_cors import cross_origin
from backend.models.user.user import User
from flask import request, Response
from flask import jsonify

USER_FIELDS = ('id', 'create_date', 'name', 'title', 'about')

def get_single_user_data(user):
    data = {}
    for field in USER_FIELDS:
        data[field] = getattr(user, field)
    return data


@api.route('/me', methods=['GET', 'POST'])
@cross_origin()
def about_me():
    if request.method == 'GET':
        users = User.query.all()
        results = [get_single_user_data(user) for user in users]
        return jsonify(results)

    if request.method == 'POST':
        User.create(request.values)
        return Response(status=200)


@api.route('/me/<user_id>', methods=['GET', 'DELETE'])
@cross_origin()
def about_me_with_id(user_id):
    if request.method == 'GET':
        user = User.query.filter_by(id=user_id).first()
        results = get_single_user_data(user)
        return jsonify(results)

    if request.method == 'DELETE':
        User.unlink(user_id)
        return Response(status=200)
