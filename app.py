from backend.main import app, db
from backend.api.api import api
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
