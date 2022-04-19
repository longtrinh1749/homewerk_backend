from sqlalchemy.orm import relationship, validates
from sqlalchemy import String, Integer, ForeignKey, Column, Text

import config
from homewerk import models as m
from homewerk.models import db

class User(db.Model, m.TimestampMixin):

    __tablename__ = 'users'

    name = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False, unique=True)
    password = Column(Text, nullable=False)
    role = Column(String(255), nullable=False) # enum ROLE.STUDENT or ROLE.TEACHER  # https://docs.sqlalchemy.org/en/14/core/type_basics.html#sqlalchemy.types.Enum #
    email = Column(String(255))
    address = Column(String(255))
    phone = Column(String(255))
    school = Column(String(255))
    clazz = Column(String(255))

    # @validates('email')
    # def validate_email(self, key, user):
    #     if '@' not in user:
    #         raise ValueError("failed simple email validation")
    #     return user

