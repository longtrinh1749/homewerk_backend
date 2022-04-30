from homewerk.models import db
from homewerk import models as m
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Boolean


class Assignment(db.Model, m.TimestampMixin):
    __tablename__ = 'assignments'

    name = Column(String(155), nullable=False)
    due = Column(DateTime)
    course_id = Column(Integer, ForeignKey('courses.id'))
    active = Column(Boolean, default=True)
    instruction = Column(String(500))

    course = db.relationship('Course', backref='assignments')