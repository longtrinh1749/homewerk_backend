from sqlalchemy.orm import relationship
from sqlalchemy import String, Integer, ForeignKey, Column, Text

import config
from homewerk import models as m
from homewerk.models import db

class User(db.Model, m.TimestampMixin):

    __tablename__ = 'users'

    name = Column(String(255), nullable=False)
    phonenumber = Column(String(255), nullable=True)