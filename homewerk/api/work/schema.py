from flask_restx import fields, reqparse
from werkzeug.datastructures import FileStorage

work_post_req_parser  = reqparse.RequestParser()
work_post_req_parser.add_argument('file', location='files',
                                    type=FileStorage, required=True)
work_post_req_parser.add_argument('user_id', type=int)
work_post_req_parser.add_argument('assignment_id', type=int)

work_res_schema = {
    'id': fields.Integer,
    'submit_id': fields.Integer,
    'image_path': fields.String,
    'priority': fields.Integer,
    'canvas_json': fields.String,
    'active': fields.Boolean,
}

object_res_schema = {
    'work_id': fields.Integer,
    'type': fields.String,
    'top': fields.Float,
    'left': fields.Float,
    'width_size': fields.Float,
    'value': fields.String,
    'image': fields.Integer,
}

work_put_req_schema = {
    'id': fields.Integer,
    'active': fields.Boolean,
    'priority': fields.Integer,
    'canvas_json': fields.String,
}