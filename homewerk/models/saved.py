from homewerk.models import db
from sqlalchemy import Integer, String, Boolean, Column, ForeignKey
from homewerk.models.base import TimestampMixin

class Saved(db.Model, TimestampMixin):
    __tablename__ = 'saved'

    user_id = Column(Integer, ForeignKey('users.id'))
    type = Column(String(100), nullable=False) # assignment, assignment, submit
    type_id = Column(Integer, nullable=False)
    type_name = Column(String(255), nullable=False)
    path = Column(String(255), nullable=False)
    description = Column(String(255))
