import json

import flask_restx as _fr
from flask_restx import fields, marshal

from homewerk.api.course.schema import (
    get_course_request_model,
    get_courses_response_model,
    # get_courses_by_user_req_model,
    # add_course_user_req_model,
    # remove_course_user_req_model,
    update_course_request_model,
    create_course_request_model,
    get_courses_res_model
)
from homewerk.extensions.httpauth import token_auth

from homewerk.services.course import CourseService
from flask import request, abort

from homewerk.extensions.httpauth import token_auth
from flask import g

course_ns = _fr.Namespace(
    name='Courses',
    path='/courses'
)

service = CourseService.get_instance()

get_course_response_model = {
    'id': fields.Integer,
    'name': fields.String,
    'class': fields.String(attribute='clazz'),
    'school': fields.String,
    'school_year': fields.String(attribute='school_year_to_str'),
    'year': fields.String(attribute='school_year'),
    'created_by': fields.Integer,
    'active': fields.Boolean,
    'teacher': fields.Nested(course_ns.model('TeacherResData', {
        'name': fields.String,
    }), attribute='created_user'),
    'total': fields.Integer(attribute='total')
}
get_course_req_schema = course_ns.model('GetCourseRequest', get_course_request_model)
# get_courses_by_user_req_schema = course_ns.model('GetCourseByUserRequest', get_courses_by_user_req_model)
# get_courses_res_schema = fields.List(fields.Nested(course_ns.model('GetCoursesResponse', get_courses_response_model)))
create_course_req_schema = course_ns.model('PostCourseRequest', create_course_request_model)
update_course_req_schema = course_ns.model('PutCourseRequest', update_course_request_model)
get_course_res_schema = course_ns.model('GetCourseResponse', get_course_response_model)
# get_courses_res_schema = course_ns.model('GetCoursesResponse', get_courses_res_model) # Unable to swagger
get_courses_res_schema = course_ns.model('GetCoursesResponse', {
    'courses': fields.List(fields.Nested(course_ns.model('CoursesResponseData', get_course_response_model)))
})
# with user_course, may be create a new route?

@course_ns.route('', methods=['GET', 'POST', 'PUT'])
class Courses(_fr.Resource):
    @course_ns.marshal_with(get_courses_res_schema)
    @course_ns.doc(params={'id': 'Course ID', 'user_id': 'User ID'})
    @token_auth.login_required
    def get(self):
        data = request.args
        courses = service.get_courses(data)
        # abort(400)
        return {'courses': courses}

    @course_ns.marshal_with(get_course_res_schema)
    @course_ns.expect(create_course_req_schema)
    @token_auth.login_required(role='ROLE.TEACHER')
    def post(self):
        data = request.json
        course = service.create_course(data)
        return course

    @course_ns.marshal_with(get_course_res_schema)
    @course_ns.expect(update_course_req_schema)
    @token_auth.login_required(role='ROLE.TEACHER')
    def put(self):
        data = request.json
        course = service.update_course(data)
        return course
