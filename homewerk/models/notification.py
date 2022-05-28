from homewerk import models as m
from homewerk.models import db
from .base import TimestampMixin
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean

class Notification(db.Model, TimestampMixin):
    __tablename__ = 'notifications'

    scope = Column(String(255), nullable=False)
    scope_id = Column(Integer, nullable=False)
    path = Column(String(255), nullable=False) # ClassID/AssignmentID/StudentID {class: , assignment:, student: }
    trigger_id = Column(Integer, nullable=False) # user_id or system
    action = Column(String(255), nullable=False) # mention, submit, due, etc
    description = Column(String(255))
    type = Column(String(100))
