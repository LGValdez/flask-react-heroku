from backend.main import db
from backend.models.base.base import Base


class User(Base):
    name = db.Column(db.String(128), nullable=False)
    title = db.Column(db.String(128), nullable=True)
    about = db.Column(db.String())
