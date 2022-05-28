import flask_sqlalchemy as _fs
import flask_migrate as _fm
import sqlalchemy as _sa
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.types import DateTime, TypeDecorator
from datetime import timedelta
from sqlalchemy import func

class BaseTimestamp(TypeDecorator):
    impl = DateTime()

    def process_result_value(self, value, dialect):
        if value is not None:
            return value + timedelta(hours=7)
        return value

class TimestampMixin(object):

    @declared_attr
    def id(self):
        return _sa.Column(_sa.Integer, primary_key=True, autoincrement=True)

    @declared_attr
    def created_at(self):
        return _sa.Column(BaseTimestamp, server_default=func.now(),
                          default=func.now(), nullable=False)

    @declared_attr
    def updated_at(self):
        return _sa.Column(
            BaseTimestamp, server_default=func.now(),
            default=func.now(), nullable=False,
            onupdate=func.now())


db = _fs.SQLAlchemy()
migrate = _fm.Migrate(db=db, compare_type=True)

def init_app(app, **kwargs):

    db.app = app
    db.init_app(app)
    migrate.init_app(app)
