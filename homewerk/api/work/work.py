import flask_restx as _fr
from flask import request
from homewerk.services import WorkService

work_ns = _fr.Namespace(
    name='Work as individual image',
    path='/work'
)
service = WorkService.get_instance()

@work_ns.route('', methods=['GET', 'PUT'])
class Work(_fr.Resource):
    def get(self):
        data = request.args
        works = service.get_works(data)
        return {'works': works}

    def put(self):
        data = request.json
        work = service.put_work(data)
        return work
