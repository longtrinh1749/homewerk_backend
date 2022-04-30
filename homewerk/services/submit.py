from homewerk import models as m
from sqlalchemy import or_
from homewerk.services import Singleton

class SubmitService(Singleton):
    def get_submits(self, data):
        query = m.Submit.query

        id = data.get('id')
        if id:
            query = query.filter(m.Submit.id == id)

        assignment_id = data.get('assignment_id')
        if assignment_id:
            query = query.filter(m.Submit.assignment_id == assignment_id)

        user_id = data.get('user_id')
        if user_id:
            query = query.filter(m.Submit.user_id == user_id)

        status = data.get('status')
        if status:
            query = query.filter(m.Submit.status == status)

        return query.all()

    def update_submit(self, data):
        id = data.get('id')
        if not id:
            return

        submit = m.Submit.query.filter(m.Submit.id == id).first()
        status = data.get('status')
        if status:
            submit.status = status

        result = data.get('result')
        if result:
            submit.result = result

        m.db.session.commit()
        return submit

    def add_submit(self, data):
        submit = m.Submit()
        submit.status = 'submitted'
        user_id = data.get('user_id')
        if not user_id:
            return
        submit.user_id = user_id
        assignment_id = data.get('assignment_id')
        if not assignment_id:
            return
        submit.assignment_id = assignment_id
        m.db.session.add(submit)
        m.db.session.commit()

        return submit