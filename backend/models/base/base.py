from datetime import datetime
from backend.main import db


class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.now)

    @staticmethod
    def prepare_values(values):
        return values

    def write(self, values):
        values = self.prepare_values(values)
        for key, value in values.items():
            setattr(self, key, value)
        db.session.commit()

    @classmethod
    def create(cls, values):
        values = cls.prepare_values(values)
        new_item = cls(**values)
        db.session.add(new_item)
        db.session.commit()
        return new_item

    @classmethod
    def unlink(cls, object_id):
        cls.query.filter_by(id=object_id).delete()
        db.session.commit()
