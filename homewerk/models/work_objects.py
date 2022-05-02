from homewerk.models import db
from homewerk import models as m
from sqlalchemy import Text, Integer, String, Column, ForeignKey, Float

class WorkObject(db.Model, m.TimestampMixin):
    __tablename__ = 'work_objects'

    work_id = Column(Integer, ForeignKey('works.id'))
    type = Column(String(20), nullable=False)
    top = Column(Float, nullable=False)
    left = Column(Float, nullable=False)
    width_size = Column(Float, nullable=False) # width of image of work => to resize when render to fe
    value = Column(String(255))
    image = Column(Integer)

    work = db.relationship('Work', backref='objects')