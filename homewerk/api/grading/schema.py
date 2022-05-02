from flask_restx import fields, reqparse
from werkzeug.datastructures import FileStorage

grading_post_req_parser  = reqparse.RequestParser()
grading_post_req_parser.add_argument('file', location='files',
                                    type=FileStorage, required=True)
grading_post_req_parser.add_argument('submit_id', type=str)
grading_post_req_parser.add_argument('comment', type=str)
grading_post_req_parser.add_argument('score', type=str)