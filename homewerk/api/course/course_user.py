import flask_restx as _fr
from flask_restx import fields

from homewerk.api.course.schema import (
    add_course_user_req_model,
    remove_course_user_req_model,
    course_user_res_model
)

from homewerk.services.course_user import CourseUserService
from flask import request

course_user_ns = _fr.Namespace(
    name='CourseUser',
    path='/course'
)

service = CourseUserService.get_instance()

post_course_user_schema = course_user_ns.model('Add', add_course_user_req_model)
delete_course_user_schema = course_user_ns.model('Remove', remove_course_user_req_model)
response_schema = course_user_ns.model('Res', course_user_res_model)

@course_user_ns.route('', methods=['POST', 'DELETE'])
class Course(_fr.Resource):
    @course_user_ns.marshal_with(response_schema)
    @course_user_ns.expect(post_course_user_schema)
    def post(self):
        data = request.json
        result = service.add_user_to_course(data)
        return result

    @course_user_ns.marshal_with(response_schema)
    @course_user_ns.expect(delete_course_user_schema)
    @course_user_ns.expect(delete_course_user_schema)
    def delete(self):
        data = request.json
        result = service.remove_user_from_course(data)
        return result