from enum import Enum


class Role():
    Teacher = 'ROLE.TEACHER'
    Student = 'ROLE.STUDENT'

class SubmitStatus():
    SUBMITTED = 'submitted'
    HANDED_IN = 'handed in'
    GRADED = 'graded'