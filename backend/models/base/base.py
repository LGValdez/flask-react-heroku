from datetime import datetime
from backend.main import db


class Base(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.now)

    @classmethod
    def create(cls, values):
        new_item = cls(**values)
        db.session.add(new_item)
        db.session.commit()

    @classmethod
    def unlink(cls, object_id):
        cls.query.filter_by(id=object_id).delete()
        db.session.commit()
