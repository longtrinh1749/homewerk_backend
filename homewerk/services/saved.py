from flask import g

from homewerk.models import db
from homewerk import models as m
from homewerk.services.base import Singleton
from homewerk.constants import SAVED_TYPE

class SavedService(Singleton):
    def create_saved(self, data):
        saved = m.Saved()
        user_id = data.get('user_id')
        user_id = g.user.id
        if user_id:
            saved.user_id = user_id

        type = data.get('type')
        if type and type in SAVED_TYPE:
            saved.type = type

        type_id = data.get('type_id')
        if type_id:
            saved.type_id = type_id

        description = data.get("description")
        if description:
            saved.description = description

        type_name = data.get('type_name')
        if type_name:
            saved.type_name = type_name

        if not (user_id and type and type_id):
            return
        else:
            old_saved = m.Saved.query.filter(m.Saved.type == type,
                                             m.Saved.type_id == type_id,
                                             m.Saved.user_id == user_id).first()
            if old_saved:
                return old_saved

            if saved.type == 'course':
                saved.path = {
                    'course': saved.type_id
                }
            elif saved.type == 'assignment':
                assignment = m.Assignment.query.filter(m.Assignment.id == type_id).first()
                saved.path = {
                    'course': assignment.course_id,
                    'assignment': saved.type_id
                }
            elif saved.type == 'submit':
                submit = m.Submit.query.filter(m.Submit.id == type_id).first()
                assignment = m.Assignment.query.filter(m.Assignment.id == submit.assignment_id).first()
                student = m.User.query.filter(m.User.id == submit.user_id).first()
                saved.path = {
                    'course': assignment.course_id,
                    'assignment': assignment.id,
                    'submit': saved.type_id,
                    'student': submit.user_id,
                }
                saved.type_name = f'{student.name}\'s submission for {assignment.name}'

        m.db.session.add(saved)
        m.db.session.commit()

        return saved

    def get_saved(self, data):
        query = m.Saved.query
        user_id = data.get('user_id')
        user_id = g.user.id
        if user_id:
            query = query.filter(m.Saved.user_id == user_id)

        type = data.get('type')
        if type:
            query = query.filter(m.Saved.type == type)

        type_id = data.get('type_id')
        if type_id:
            query = query.filter(m.Saved.type_id == type_id)

        saved = query.all()
        return saved

    def delete_saved(self, data):
        user_id = data.get('user_id')
        user_id = g.user.id
        type = data.get('type')
        type_id = data.get('type_id')
        all_saved = m.Saved.query.filter().all()
        m.Saved.query.filter(m.Saved.user_id == user_id,
                             m.Saved.type == type,
                             m.Saved.type_id == type_id).delete()

        m.db.session.commit()

        return True

