import datetime

import flask
import flask_restx as _fr
from flask_restx import api, fields
from homewerk.api.user.schema import (
    get_user_request_model,
    get_user_response_model,
    post_user_request_model,
    put_user_request_model
)
from homewerk.constants import JWT_EXPIRED_HOURS

from homewerk.services.user import UserService
from flask import request, jsonify
from flask import g

from homewerk.extensions.httpauth import basic_auth, token_auth

user_ns = _fr.Namespace(
    name='User',
    path='/users'
)

service = UserService.get_instance()

get_user_request_schema = user_ns.model('GetUserRequest', get_user_request_model)
get_user_response_schema = user_ns.model('GetUserResponse', get_user_response_model)
post_user_request_schema = user_ns.model('PostUserRequest', post_user_request_model)
put_user_request_schema = user_ns.model('PutUserRequest', put_user_request_model)

@user_ns.route('', methods=['GET', 'POST', 'PUT'])
class Users(_fr.Resource):
    # @user_ns.expect(get_user_request_schema, location="query")
    @user_ns.marshal_with(get_user_response_schema)
    @user_ns.doc(params={'id': 'User ID', 'username': 'Username', 'password': 'Password'})
    @token_auth.login_required
    def get(self):
        data = request.args
        user = service.get_user(data)
        return user

    @user_ns.expect(post_user_request_schema)
    @user_ns.marshal_with(get_user_response_schema)
    def post(self):
        data = request.json
        return service.create_user(data)

    @user_ns.expect(put_user_request_schema)
    @user_ns.marshal_with(get_user_response_schema)
    @token_auth.login_required
    def put(self):
        data = request.json
        return service.update_user(data)

get_students_res_schema = user_ns.model('GetStudentsResponse', {
    'students': fields.List(fields.Nested(user_ns.model('StudentsResponseData', get_user_response_model)))
})

@user_ns.route('/account', methods=['PUT'])
class Account(_fr.Resource):
    @token_auth.login_required
    def put(self):
        data = request.json
        return service.update_password(data)

@user_ns.route('/course/students', methods=['GET'])
class CourseStudent(_fr.Resource):
    @user_ns.marshal_with(get_students_res_schema)
    @user_ns.doc(params={'course_id': 'Course ID'})
    @token_auth.login_required(role='ROLE.TEACHER')
    def get(self):
        data = request.args
        students = service.get_students_by_course(data)
        return {'students': students}

@user_ns.route('/token', methods=['GET', 'POST'])
class Token(_fr.Resource):
    @basic_auth.login_required
    def get(self):
        token = g.user.generate_auth_token()
        return jsonify({'token': token,
                        'expired_in': JWT_EXPIRED_HOURS,
                        'role': g.user.role,
                        'username': g.user.username})

    @token_auth.login_required
    def post(self):
        token = g.user.generate_auth_token()
        return jsonify({'token': token,
                        'expired_in': 7,
                        'role': g.user.role,
                        'username': g.user.username})

    @token_auth.login_required
    def put(self):
        token = g.user.generate_auth_token()
        return jsonify({'token': token,
                        'expired_in': 7,
                        'role': g.user.role,
                        'username': g.user.username})

