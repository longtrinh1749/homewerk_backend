from flask import g
from sqlalchemy import or_

from homewerk.services import Singleton
from homewerk import models as m
from homewerk.constants import SubmitStatus, NotificationScopes
from homewerk.services.notification import NotificationService

noti_service = NotificationService.get_instance()

class AssignmentService(Singleton):
    def get_assignments(self, data):
        query = m.Assignment.query

        id = data.get('id')
        if id:
            query = query.filter(m.Assignment.id == id)
        course_id = data.get('course_id')
        if course_id:
            query = query.filter(m.Assignment.course_id == course_id)

        user_id = data.get('user_id')
        user_id = g.user.id

        assignments = query.all()
        for a in assignments:
            total_submit = len(m.Submit.query.filter(m.Submit.assignment_id == a.id,
                                                 or_(m.Submit.status == SubmitStatus.HANDED_IN,
                                                     m.Submit.status == SubmitStatus.GRADED)).all())
            total_graded = len(m.Submit.query.filter(m.Submit.assignment_id == a.id,
                                                 m.Submit.status == SubmitStatus.GRADED).all())
            a.total_submit = total_submit
            a.total_graded = total_graded
            if user_id:
                submit = m.Submit.query.filter(m.Submit.assignment_id == a.id,
                                               m.Submit.user_id == user_id).first()
                if submit:
                    a.status = submit.status
                else:
                    a.status = ''


        return assignments

    def create_assignment(self, data):
        asm = m.Assignment()
        course_id = data.get('course_id')
        if course_id:
            asm.course_id = course_id

        due = data.get('due')
        if due:
            asm.due = due

        name = data.get('name')
        if name:
            asm.name = name

        instruction = data.get('instruction')
        if instruction:
            asm.instruction = instruction

        m.db.session.add(asm)
        m.db.session.commit()
        course = m.Course.query.filter(m.Course.id == asm.course_id).first()
        noti_service.create_assignment_notification(asm)
        noti_service.subcribe_notification(scope=NotificationScopes.ASSIGNMENT,
                                           scope_id=asm.id,
                                           user_id=course.created_by)
        return asm


    def update_assignment(self, data):
        id = data.get('id')
        assignment = m.Assignment.query.filter(m.Assignment.id == id).first()

        name = data.get('name')
        if name:
            assignment.name = name

        due = data.get('due')
        if due:
            assignment.due = due

        active = data.get('active')
        if active:
            assignment.active = active

        instruction = data.get('instruction')
        if instruction:
            assignment.instruction = instruction

        m.db.session.commit()
        return assignment



