from homewerk import models as m
from homewerk.services import Singleton
from sqlalchemy import or_

class WorkService(Singleton):
    def get_works(self, data):
        query = m.Work.query

        id = data.get('id')
        if id:
            query = query.filter(m.Work.id == id)

        submit_id = data.get('submit_id')
        if submit_id:
            query = query.filter(m.Work.submit_id == submit_id)

        return query.all()

    def put_work(self, data):
        id = data.get('id')
        if not id:
            return

        work = m.Work.query.filter(m.Work.id == id).first()
        canvas_json = data.get('canvas_json')
        if canvas_json:
            work.canvas_json = canvas_json

        objects = data.get('objects')
        if objects:
            work.objects = objects

        m.db.session.commit()
        return work