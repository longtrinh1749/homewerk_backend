from marshmallow import fields as mfields, Schema
from flask_restx import fields

class GetUserRequest(Schema):
    id = mfields.Integer()

get_user_request_model = {
    'id': fields.Integer
}

get_user_response_model = {
    'id': fields.Integer,
    'name': fields.String,
    'username': fields.String,
    'password': fields.String,
    'role': fields.String,
    'email': fields.String,
    'address': fields.String,
    'phone': fields.String,
    'school': fields.String,
    'class': fields.String(attribute='clazz'),
}

post_user_request_model = {
    'name': fields.String,
    'username': fields.String,
    'password': fields.String,
    'role': fields.String,
    'email': fields.String,
    'address': fields.String,
    'phone': fields.String,
    'school': fields.String,
    'class': fields.String(attribute='clazz'),
}

put_user_request_model = {
    'id': fields.Integer,
    'name': fields.String,
    'username': fields.String,
    'password': fields.String,
    'role': fields.String,
    'email': fields.String,
    'address': fields.String,
    'phone': fields.String,
    'school': fields.String,
    'class': fields.String(attribute='clazz'),
}
