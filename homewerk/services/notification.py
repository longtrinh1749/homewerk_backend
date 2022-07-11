import sqlalchemy.exc
from flask import g

from homewerk.constants import Role, NotificationScopes, NotificationTypes, NotificationActions
from homewerk.services import Singleton
from homewerk import models as m
from homewerk import utils
from homewerk.biz.pub_sub import subcribe_notification

class NotificationService(Singleton):
    def get_notifications_and_subcribe(self, data):
        query = m.Notification.query
        if not data:
            return None
        if data.get('id'):
            query = query.filter(m.Notification.id == data.get('id'))
        if data.get('scope'):
            query = query.filter(m.Notification.scope == data.get('scope'))
        if data.get('path'):
            query = query.filter(m.Notification.path == data.get('path'))
        # if data.get('user_id'):
        #     user_id = data.get('user_id')
        if g.user.id:
            user_id = g.user.id
            query = query.filter(m.Notification.scope == m.NotificationSubcriber.scope,
                                 m.Notification.scope_id == m.NotificationSubcriber.scope_id,
                                 m.NotificationSubcriber.user_id == user_id,
                                 m.Notification.trigger_id != user_id
                                 )
            notifications_for_user = query.all()
            token = data.get('token')
            subcribe_notification(token, notifications_for_user)
        return query.all()

    def group_notifications(self, notifications):
        notifications = []


    def update_notification(self, data):
        notification = m.Notification.query.get(data['id'])
        notification.read = data['read']
        return notification

    # def get_course_notifications(self, user_id):
    #     user = m.User.query.filter(m.User.id == user_id).first()
    #     if user.role == Role.Student:
    #         relevant_courses = m.UserCourse.query.filter(m.UserCourse.user_id == user.id).all()
    #         relevant_course_ids = [c.id for c in relevant_courses]
    #         return m.Notification.query.filter(m.Notification.scope == NotificationScopes.COURSE,
    #                                            m.Notification.scope_id.in_(relevant_course_ids)).all()
    #     elif user.role == Role.Teacher:
    #         relevant_courses = m.Course.query.filter(m.Course.created_by == user.id).all()
    #         relevant_course_ids = [c.id for c in relevant_courses]
    #         return m.Notification.query.filter(m.Notification.scope == NotificationScopes.COURSE,
    #                                            m.Notification.scope_id.in_(relevant_course_ids)).all()
    #
    # def get_asm_notifications(self, user_id):
    #     user = m.User.query.filter(m.User.id == user_id).first()
    #     if user.role == Role.Student:
    #         relevant_submits = m.Submit.query.filter(m.Submit.user_id == user_id).all()
    #         relevant_submit_ids = [s.id for s in relevant_submits]
    #         return m.Notification.query.filter(m.Notification.scope == NotificationScopes.STUDENT_WORK,
    #                                            m.Notification.scope_id.in_(relevant_submit_ids))
    #         pass
    #     elif user.role == Role.Teacher:
    #         pass

    def create_notification(self, data):
        noti = m.Notification()
        noti.scope = data.get('scope')
        noti.scope_id = data.get('scope_id')
        noti.path = data.get('path')
        noti.action = data.get('action')
        noti.description = data.get('description')
        noti.trigger_id = data.get('trigger_id')

        m.db.session.add(noti)
        m.db.session.commit()
        return noti

    def create_assignment_notification(self, asm):
        noti = m.Notification()
        noti.scope = NotificationScopes.COURSE
        noti.type = NotificationTypes.ASSIGNMENT
        noti.path = {
            "course": asm.course_id,
        }
        noti.scope_id = asm.course_id
        noti.action = NotificationActions.CREATE_ASSIGNMENT
        course = m.Course.query.filter(m.Course.id == asm.course_id).first()
        noti.trigger_id = course.created_by
        noti.description = f'Teacher {course.created_user.name} has just created new assignment {asm.name} ' \
                           f'in course {course.name}'

        m.db.session.add(noti)
        m.db.session.commit()
        return noti

    def grade_assignment_notification(self, submit):
        noti = m.Notification()
        noti.scope = NotificationScopes.STUDENT_WORK
        noti.type = NotificationTypes.ASSIGNMENT
        assignment = m.Assignment.query.filter(m.Assignment.id == submit.assignment_id).first()
        noti.path = {
            "course": assignment.course_id,
            "assignment": submit.assignment_id,
        }
        noti.scope_id = submit.id
        noti.action = NotificationActions.UPDATE_ASSIGNMENT
        course = m.Course.query.filter(m.Course.id == assignment.course_id).first()
        noti.trigger_id = course.created_by
        noti.description = f'Teacher {course.created_user.name} has just graded your submit for assignment ' \
                           f'{assignment.name} in course {course.name}'

        m.db.session.add(noti)
        m.db.session.commit()
        return noti

    def submit_assignment_notification(self, submit):
        noti = m.Notification()

        noti.scope = NotificationScopes.ASSIGNMENT
        noti.type = NotificationTypes.ASSIGNMENT
        noti.action = NotificationActions.UPDATE_ASSIGNMENT
        assignment = m.Assignment.query.filter(m.Assignment.id == submit.assignment.id).first()
        noti.path = {
            "course": assignment.course_id,
            "assignment": submit.assignment_id,
        }
        noti.scope_id = submit.assignment_id
        course = m.Course.query.filter(m.Course.id == assignment.course_id).first()
        noti.trigger_id = submit.user_id
        student = m.User.query.filter(m.User.id == submit.user_id).first()
        noti.description = f'Student {student.name} have just submit their work for assignment ' \
                           f'{assignment.name} in course {course.name}'

        m.db.session.add(noti)
        m.db.session.commit()

        return noti

    def student_join_notification(self, course_user):
        noti = m.Notification()
        noti.scope = NotificationScopes.COURSE
        noti.type = NotificationTypes.COURSE
        noti.action = NotificationActions.STUDENT_JOIN
        noti.path = {
            "course": course_user.course_id
        }
        noti.scope_id = course_user.course_id
        noti.trigger_id = 0 # system
        student = m.User.query.filter(m.User.id == course_user.user_id).first()
        course = m.Course.query.filter(m.Course.id == course_user.course_id).first()
        noti.description = f'Student {student.name} has just joined your course {course.name}'

        return noti

    def subcribe_notification(self, scope=None, user_id=None, scope_id=None):
        subcription = m.NotificationSubcriber()
        subcription.scope = scope
        subcription.scope_id = scope_id
        subcription.user_id = user_id

        m.db.session.add(subcription)
        m.db.session.commit()

        return subcription
