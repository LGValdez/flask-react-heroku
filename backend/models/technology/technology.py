from backend.main import db
from backend.models.base.base import Base


class Technology(Base):
    name = db.Column(db.String(128), nullable=False)
    tech_type = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"{self.name} ({self.tech_type})"