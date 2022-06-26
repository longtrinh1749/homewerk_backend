import datetime

from sqlalchemy.orm import relationship, validates
from sqlalchemy import String, Integer, ForeignKey, Column, Text
from homewerk.constants import JWT_EXPIRED_HOURS

import config
from homewerk import models as m
from homewerk.models import db

from passlib.apps import custom_app_context as pwd_context
from itsdangerous import URLSafeSerializer as Serializer, BadSignature, SignatureExpired

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
    password_hash = Column(String(255))

    # @validates('email')
    # def validate_email(self, key, user):
    #     if '@' not in user:
    #         raise ValueError("failed simple email validation")
    #     return user

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):
        from homewerk import app
        s = Serializer(app.config['SECRET_KEY'])
        return s.dumps(
            {'id': self.id,
             'expired_in': str(datetime.datetime.now() + datetime.timedelta(hours=JWT_EXPIRED_HOURS)),
             'role': self.role
             }
        )

    @staticmethod
    def verify_auth_token(token):
        from homewerk import app
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
            if data.get('expired_in') < str(datetime.datetime.now()):
                return None
        except BadSignature:
            return None

        user = User.query.get(data.get('id'))
        return user

