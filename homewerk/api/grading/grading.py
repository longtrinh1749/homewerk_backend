from flask import request
import flask_restx as _fr
from homewerk.services.submit import SubmitService
from .schema import grading_post_req_parser



grading_ns = _fr.Namespace(
    name='Grading',
    path='/grading'
)

service = SubmitService.get_instance()

@grading_ns.route('', methods=['PUT'])
class Grading(_fr.Resource):
    @grading_ns.expect(grading_post_req_parser)
    def put(self):
        data = request.form
        service.update_submit(data)
        return 'ok'