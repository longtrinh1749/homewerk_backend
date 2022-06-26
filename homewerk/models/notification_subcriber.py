from homewerk import models as m
from homewerk.models import db
from .base import TimestampMixin
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean

class NotificationSubcriber(db.Model, TimestampMixin):
    __tablename__ = 'notification_subcriber'

    user_id = Column(Integer, nullable=False)
    scope = Column(String(100), nullable=False)
    scope_id = Column(Integer, nullable=False)
    active = Column(Boolean, default=True)
    read = Column(Boolean, default=True)
