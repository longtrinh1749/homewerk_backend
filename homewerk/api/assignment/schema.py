from flask_restx import fields

get_assignment_res_model = {
    'id': fields.Integer,
    'name': fields.String,
    'course_id': fields.Integer,
    'active': fields.Boolean,
    'due': fields.String,
    'instruction': fields.String,
    'submit': fields.Integer(attribute='total_submit'),
    'graded': fields.Integer(attribute='total_graded'),
    'status': fields.String(attribute='status'),
    'attachment': fields.String,
    'score': fields.Integer,
}

post_assignment_req_model = {
    'course_id': fields.Integer,
    'name': fields.String,
    'due': fields.DateTime,
    'instruction': fields.String,
}

put_assignment_req_model = {
    'id': fields.Integer,
    'name': fields.String,
    'active': fields.Boolean,
    'due': fields.DateTime,
    'instruction': fields.String,
}