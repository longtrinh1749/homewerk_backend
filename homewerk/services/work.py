import uuid

from homewerk import models as m
from homewerk.services import Singleton
from sqlalchemy import or_
from homewerk.services.submit import SubmitService
from homewerk.constants import SubmitStatus
from homewerk.utils import save_file

submit_service = SubmitService.get_instance()

class WorkService(Singleton):
    def get_works(self, data):
        query = m.Work.query

        id = data.get('id')
        if id:
            query = query.filter(m.Work.id == id)

        submit_id = data.get('submit_id')
        if submit_id:
            query = query.filter(m.Work.submit_id == submit_id)

        user_id = data.get('user_id')
        if user_id:
            query = query.filter(m.Work.submit_id == m.Submit.id, m.Submit.user_id == user_id)

        assignment_id = data.get('assignment_id')
        if assignment_id:
            query = query.filter(m.Work.submit_id == m.Submit.id, m.Submit.assignment_id == assignment_id)

        return query.filter(m.Work.active == True).all()

    def add_work(self, data):
        user_id = data.get('user_id')
        assignment_id = data.get('assignment_id')
        submit = submit_service.get_submits({'user_id': user_id, 'assignment_id': assignment_id})
        if not submit:
            submit = m.Submit()
            submit.status = SubmitStatus.SUBMITTED
            submit.user_id = user_id
            submit.assignment_id = assignment_id
            m.db.session.add(submit)
            m.db.session.commit()
        else:
            submit = submit[0]

        file = data.get('file')
        filename = data.get('filename')
        exist_works = m.Work.query.filter(m.Work.submit_id == submit.id).all()
        new_work = m.Work()
        new_work.submit_id = submit.id
        path = save_file(file, uuid.uuid4(), 0)
        new_work.image_path = path
        new_work.priority = len(exist_works) + 1
        m.db.session.add(new_work)
        m.db.session.commit()
        # new_path = save_file(file, filename, new_work.id)
        # new_work.image_path = new_path
        # m.db.session.commit()
        return new_work

    def put_work(self, data):
        submit_id = data.get('submit_id')
        result = data.get('result')
        comment = data.get('comment')
        submit = m.Submit.query.get(submit_id)
        submit.result = result
        submit.comment = comment
        m.db.session.commit()
        id = data.get('id')
        if not id:
            return

        work = m.Work.query.filter(m.Work.id == id).first()
        active = data.get('active')
        if active is not None:
            work.active = active
        canvas_json = data.get('canvas_json')
        if canvas_json:
            work.canvas_json = canvas_json

        objects = m.WorkObject.query.filter(m.WorkObject.work_id == id).all()
        for o in objects:
            m.db.session.delete(o)

        objects = data.get('objects')
        if objects:
            objects = [o for o in objects if o]
            # current_objects = m.WorkObject(m.WorkObject.work_id == work.id).all()
            # for o in current_objects:
            #     m.db.session.delete(current_objects)
            # m.db.session.commit()
            work.objects = []
            for o in objects:
                new_object = m.WorkObject()
                new_object.work_id = o.get('workId')
                new_object.type = o.get('type')
                new_object.top = o.get('top')
                new_object.left = o.get('left')
                new_object.value = o.get('value')
                new_object.image = o.get('image')
                new_object.width_size = o.get('widthSize', 0)
                m.db.session.add(new_object)
                m.db.session.commit()

        m.db.session.commit()
        return work