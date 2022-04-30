from homewerk.services.base import Singleton
from . import (
    user,
    course,
    course_user,
    submit,
    assignment,
    work
)

from .user import UserService
from .assignment import AssignmentService
from .work import WorkService
from .submit import SubmitService
