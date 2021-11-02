from flask import jsonify
from ..api import api
from flask_cors import cross_origin


@api.route('/projects', methods=['GET'])
@cross_origin()
def get_projects(params=None):
    params = params or {}
    projects = [
        {
            "id": 1,
            "name": "eCommerce for Black Friday Sales",
            "company": "Confidential",
            "date_start": "July, 2021",
            "date_end": "Present",
            "technologies": ["Python", "JavaScript", "PostgreSQL"],
            "frameworks": ["Odoo", "jQuery", "PyCharm", "PGAdmin"],
            "description": """
                Customizations and performance improvements for Odoo eCommerce. 
                Integration with third-party email services via API calls.
            """
        },
        {
            "id": 2,
            "name": "Full Accounting Implementation",
            "company": "Confidential",
            "date_start": "June, 2021",
            "date_end": "Present",
            "technologies": ["Python", "JavaScript", "PostgreSQL"],
            "frameworks": ["Odoo", "jQuery", "PyCharm", "PGAdmin"],
            "description": """
                Implementation and customizations in Odoo for handling accounting,
                payroll, timesheet and assistance following the taxes, allowances and vacation
                rules in Puerto Rico.
            """
        },
        {
            "id": 3,
            "name": "Document Management System",
            "company": "Confidential",
            "date_start": "June, 2021",
            "date_end": "Present",
            "technologies": ["Python", "JavaScript", "PostgreSQL"],
            "frameworks": ["Odoo", "jQuery", "PyCharm", "PGAdmin"],
            "description": """
                Customizations in Odoo for handling Policies, SOP, contracts and
                other documents following the needs in Puerto Rico.
            """
        },
        {
            "id": 4,
            "name": "Improvements to Django and ReactJS",
            "company": "Confidential",
            "date_start": "July, 2021",
            "date_end": "September, 2021",
            "technologies": ["Python", "JavaScript", "PostgreSQL", "Docker"],
            "frameworks": ["Django", "ReactJS", "VSCode"],
            "description": """
                Improvements to a webpage in the United States that helps users
                track royalties and earnings given their registered wells and land ownerships.
            """
        }
    ]
    for key, value in params.items():
        projects = list(filter(lambda x: str(x[key]) == value, projects))
    return jsonify(projects)
