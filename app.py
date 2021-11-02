from flask_app.app import app, db
from api.api import api
from flask_migrate import Migrate
import os

migrate = Migrate(app, db)
app.register_blueprint(api, url_prefix='/api')


if __name__ == '__main__':
    db.create_all()
    os.system("flask db init")
    os.system("flask db migrate")
    os.system("flask db upgrade")
    app.run()
