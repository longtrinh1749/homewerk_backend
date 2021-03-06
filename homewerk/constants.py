from enum import Enum

JWT_EXPIRED_HOURS = 10
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
    COURSE = 'Course'
    ASSIGNMENT = 'Assignment'

class NotificationActions:
    CREATE_ASSIGNMENT = 'create assignment'
    UPDATE_ASSIGNMENT = 'update assignment'
    STUDENT_JOIN = 'student join'

SAVED_TYPE = ['assignment', 'course', 'submit']