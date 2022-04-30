from flask_restx import Namespace, Model, marshal_with, fields
from flask import request
import flask_restx as _fr
from datetime import datetime

from homewerk.api.assignment.schema import (
    get_assignment_res_model,
    post_assignment_req_model,
    put_assignment_req_model,
)

from homewerk.services import AssignmentService

assignment_ns = _fr.Namespace(
    name='Assignments',
    path='/assignments'
)

service = AssignmentService.get_instance()

get_assignments_res_schema = assignment_ns.model('AssignmentsRes', {
    'assignments': fields.List(fields.Nested(assignment_ns.model('AssignmentRes', get_assignment_res_model)))
})
get_assignment_res_schema = assignment_ns.model('AssignmentRes', get_assignment_res_model)
post_assignment_req_schema = assignment_ns.model('PostAsmReq', post_assignment_req_model)
put_assignment_req_schema = assignment_ns.model('PutAsmReq', put_assignment_req_model)

@assignment_ns.route('', methods=['GET', 'POST', 'PUT'])
class Assignment(_fr.Resource):
    @assignment_ns.marshal_with(get_assignments_res_schema)
    @assignment_ns.doc(params={'id': 'ID', 'course_id': 'Course ID'})
    def get(self):
        data = request.args
        assignments = service.get_assignments(data)
        return {'assignments': assignments}

    @assignment_ns.marshal_with(get_assignment_res_schema)
    @assignment_ns.expect(post_assignment_req_schema)
    def post(self):
        data = request.json
        assignment = service.create_assignment(data)
        return assignment

    @assignment_ns.marshal_with(get_assignment_res_schema)
    @assignment_ns.expect(put_assignment_req_schema)
    def put(self):
        data = request.json
        assignment = service.update_assignment(data)
        return assignment