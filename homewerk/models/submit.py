from homewerk.models import db
from homewerk import models as m
from sqlalchemy import String, Integer, ForeignKey, Column

class Submit(db.Model, m.TimestampMixin): # submit include many works (image)
    __tablename__ = 'submits'

    assignment_id = Column(Integer, ForeignKey('assignments.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    status = Column(String(255), nullable=False) # submitted, graded
    result = Column(Integer)