from .base import (
    init_app,
    db,
    migrate,
    TimestampMixin
)

from .user import User
from .course import Course
from .user_course import UserCourse