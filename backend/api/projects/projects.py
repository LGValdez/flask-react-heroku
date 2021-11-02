from flask import jsonify
from backend.api.api import api
from backend.models.project.project import Project
from flask_cors import cross_origin
from flask import request, Response
from backend.main import db

PROJECT_FIELDS = (
    'id', 'create_date', 'name', 'company', 'role', 'date_start',
    'date_end', 'technologies', 'description')


def get_single_project_data(project):
    data = {}
    for field in PROJECT_FIELDS:
        if field == 'technologies':
            data[field] = [{
                'name': tech.name,
                'type': tech.tech_type,
            } for tech in getattr(project, field)]
        else:
            data[field] = getattr(project, field)
    return data


@api.route('/me/<user_id>/projects', methods=['GET', 'POST'])
@cross_origin()
def user_projects(user_id, params=None):
    params = params or {}
    if request.method == 'GET':
        params['user_id'] = user_id
        projects = Project.query.filter_by(**params)
        results = [get_single_project_data(project) for project in projects]
        return jsonify(results)

    if request.method == 'POST':
        values = request.values.copy()
        values['user_id'] = user_id
        Project.create(values)
        return Response(status=200)


@api.route('/me/<user_id>/projects/<project_id>', methods=['GET', 'PATCH', 'DELETE'])
@cross_origin()
def user_projects_with_id(user_id, project_id, params=None):
    project = Project.query.filter_by(id=project_id, user_id=user_id).first()
    if request.method == 'GET':
        result = get_single_project_data(project)
        return jsonify(result)

    if request.method == 'PATCH':
        values = request.values.copy()
        project.write(values)
        return Response(status=200)

    if request.method == 'DELETE':
        project.technologies = []
        Project.unlink(project.id)
        return Response(status=200)
