from homewerk.models import db
from homewerk import models as m
from sqlalchemy import String, Integer, DateTime, ForeignKey, Column, Text

class Work(db.Model, m.TimestampMixin):
    __tablename__ = 'works'

    submit_id = Column(Integer, ForeignKey('submits.id')) # submit includes many works (image)
    image_path = Column(Text, nullable=False)
    priority = Column(Integer, nullable=False) # priority: work order
    # TODO: co the bo sung next, previous_image cho tinh nang nop lai bai
    canvas_json = Column(Text)

    submit = db.relationship('Submit', backref='works')