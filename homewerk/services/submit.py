from homewerk import models as m
from sqlalchemy import or_
from homewerk.services import Singleton
from homewerk.constants import SubmitStatus
from homewerk.utils import save_b64_file

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

        result = data.get('score')
        if result:
            submit.result = result
            submit.status = SubmitStatus.GRADED

        comment = data.get('comment')
        if comment:
            submit.comment = comment

        work_id = data.get('work_id')
        if work_id:
            file_data = data.get('file')
            if file_data:
                file_path = save_b64_file(file_data, work_id)
                work = m.Work.query.get(work_id)
                work.result_path = file_path

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