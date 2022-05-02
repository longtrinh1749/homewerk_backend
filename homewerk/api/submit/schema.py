from flask_restx import fields, reqparse
from werkzeug.datastructures import FileStorage

submit_res_schema = {
    'id': fields.Integer,
    'assignment_id': fields.Integer,
    'user_id': fields.Integer,
    'status': fields.String,
    'result': fields.String,
    'comment': fields.String,
}

submit_post_req_schema = {
    'assignment_id': fields.Integer,
    'user_id': fields.Integer,
}

submit_put_req_schema = {
    'assignment_id': fields.Integer,
    'user_id': fields.Integer,
    'id': fields.Integer,
    'status': fields.String,
    'result': fields.Integer
}

submit_post_req_parser = reqparse.RequestParser()
submit_post_req_parser.add_argument('works', location='files',
                                    type=FileStorage, required=True)