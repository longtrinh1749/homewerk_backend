from homewerk.services import Singleton
from homewerk import models as m

class AssignmentService(Singleton):
    def get_assignments(self, data):
        query = m.Assignment.query

        id = data.get('id')
        if id:
            query = query.filter(m.Assignment.id == id)
        course_id = data.get('course_id')
        if course_id:
            query = query.filter(m.Assignment.course_id == course_id)

        return query.all()

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



