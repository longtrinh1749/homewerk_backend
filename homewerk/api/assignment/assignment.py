from flask_restx import Namespace, Model, marshal_with, fields
from flask import request
import flask_restx as _fr
from datetime import datetime

from flask_restx.reqparse import RequestParser
from werkzeug.datastructures import FileStorage

from homewerk.api.assignment.schema import (
    get_assignment_res_model,
    post_assignment_req_model,
    put_assignment_req_model,
)

from homewerk.services import AssignmentService
from homewerk.extensions.httpauth import token_auth

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
    @token_auth.login_required
    def get(self):
        data = request.args
        assignments = service.get_assignments(data)
        return {'assignments': assignments}

    upload_param = RequestParser(bundle_errors=True)
    upload_param.add_argument('file', location='files',
                              type=FileStorage, required=True)
    upload_param.add_argument('course_id', default=False, type=int)
    upload_param.add_argument('name', default=False, type=str)
    upload_param.add_argument('due', default=False, type=str)
    upload_param.add_argument('instruction', default=False, type=str)
    @assignment_ns.marshal_with(get_assignment_res_schema)
    @assignment_ns.expect(upload_param)
    @token_auth.login_required(role='ROLE.TEACHER')
    def post(self):
        data = request.form
        assignment = service.create_assignment(data, request.files['file'])
        return assignment

    put_assignment_param = RequestParser(bundle_errors=True)
    put_assignment_param.add_argument('file', location='files',
                              type=FileStorage, required=True)
    put_assignment_param.add_argument('id', default=False, type=int)
    put_assignment_param.add_argument('name', default=False, type=str)
    put_assignment_param.add_argument('due', default=False, type=str)
    put_assignment_param.add_argument('instruction', default=False, type=str)
    @assignment_ns.marshal_with(get_assignment_res_schema)
    @assignment_ns.expect(put_assignment_param)
    @token_auth.login_required(role='ROLE.TEACHER')
    def put(self):
        data = request.form
        assignment = service.update_assignment(data, request.files.get('file'))
        return assignment