from flask_restx import fields

get_assignment_res_model = {
    'id': fields.Integer,
    'name': fields.String,
    'course_id': fields.Integer,
    'active': fields.Boolean,
}

put_assignment_req_model = {
    'id': fields.Integer,
    'name': fields.String,
    'active': fields.Boolean,
    'due': fields.DateTime,
}