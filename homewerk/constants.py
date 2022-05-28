from enum import Enum


class Role:
    Teacher = 'ROLE.TEACHER'
    Student = 'ROLE.STUDENT'

class SubmitStatus:
    SUBMITTED = 'submitted'
    HANDED_IN = 'handed in'
    GRADED = 'graded'

class NotificationScopes:
    COURSE = 'course'
    ASSIGNMENT = 'assignment'
    STUDENT_WORK = 'student'

class NotificationTypes:
    CHAT = 'chat'
    WORK = 'work'

class NotificationActions:
    CREATE_ASSIGNMENT = 'create assignment'
    UPDATE_ASSIGNMENT = 'update assignment'
    STUDENT_JOIN = 'student join'