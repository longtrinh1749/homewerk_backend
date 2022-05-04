from homewerk.services import Singleton
from homewerk import models as m
from homewerk.constants import SubmitStatus

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

        assignments = query.all()
        for a in assignments:
            total_submit = len(m.Submit.query.filter(m.Submit.assignment_id == a.id,
                                                 m.Submit.status == SubmitStatus.HANDED_IN).all())
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

        m.db.session.commit()
        return assignment



