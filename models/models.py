from app.app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    title = db.Column(db.String(128), nullable=True)
    about = db.Column(db.String())

    @staticmethod
    def create(values):
        new_user = User(**values)
        db.session.add(new_user)
        db.session.commit()

    @staticmethod
    def unlink(user_id):
        User.query.filter_by(id=user_id).delete()
        db.session.commit()
