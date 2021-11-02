from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from backend.main import db
from backend.models.base.base import Base
from backend.models.technology.technology import Technology

project_technologies_rel = db.Table(
    'project_technologies_rel', Base.metadata,
    db.Column('project_id', ForeignKey('project.id')),
    db.Column('technology_id', ForeignKey('technology.id'))
)


class Project(Base):
    name = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    company = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(128), nullable=False)
    date_start = db.Column(db.String(128), nullable=False)
    date_end = db.Column(db.String(128), nullable=False)
    technologies = relationship("Technology", secondary=project_technologies_rel)
    description = db.Column(db.String(), nullable=False)

    @staticmethod
    def prepare_values(values):
        if "technologies" in values:
            technologies = []
            for technology in values["technologies"].split(","):
                tech = Technology.query.filter_by(name=technology).first()
                if not tech:
                    tech = Technology.create({
                        'name': technology,
                        'tech_type': 'Others'
                    })
                technologies.append(tech)
            values["technologies"] = technologies
        return values

    def __repr__(self):
        return f"{self.name}"
