from homewerk import models as m
from homewerk.models import db
from .base import TimestampMixin
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean


class Course(db.Model, TimestampMixin):
    __tablename__ = "courses"

    name = Column(String(255), nullable=False)
    clazz = Column('class', String(255))
    school = Column(String(255))
    school_year = Column(Integer)
    created_by = Column(Integer, ForeignKey('users.id'))
    created_user = db.relationship('User', backref='created_courses')
    active = Column(Boolean, nullable=False, default=True)

    @property
    def school_year_to_str(self):
        if self.school_year:
            ext_year = str(int(self.school_year) + 1)
            return str(self.school_year) + ' - ' + str(ext_year)