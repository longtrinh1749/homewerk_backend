from homewerk import models as m
from homewerk.models import db
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean


class UserCourse(db.Model, m.TimestampMixin):
    __tablename__ = 'user_course'

    user_id = Column(Integer, ForeignKey('users.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    active = Column(Boolean, default=True)

    user = db.relationship('User', backref='user_course')
    course = db.relationship('Course', backref='course_user')