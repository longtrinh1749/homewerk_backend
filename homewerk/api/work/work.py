import os

import flask_restx as _fr
from flask import request, send_file
from werkzeug.utils import secure_filename

from homewerk.services import WorkService
from .schema import work_post_req_parser
from .schema import work_put_req_schema
from .schema import work_res_schema
from .schema import object_res_schema
from homewerk.utils import allowed_file, save_file
from homewerk.extensions.httpauth import token_auth

work_ns = _fr.Namespace(
    name='Work as individual image',
    path='/work'
)
service = WorkService.get_instance()

work_put_req_model = work_ns.model('WorkPutReq', work_put_req_schema)
object_res_model = work_ns.model('ObjectRes', object_res_schema)
work_res_model = work_ns.model('WorkRes', {
    'id': _fr.fields.Integer,
    'submit_id': _fr.fields.Integer,
    'image_path': _fr.fields.String,
    'result_path': _fr.fields.String,
    'priority': _fr.fields.Integer,
    'canvas_json': _fr.fields.String,
    'active': _fr.fields.Boolean,
    'objects': _fr.fields.List(_fr.fields.Nested(object_res_model))
})
works_res_model = work_ns.model('WorksRes', {
    'works': _fr.fields.List(_fr.fields.Nested(work_res_model))
})
@work_ns.route('', methods=['GET', 'POST', 'PUT'])
class Work(_fr.Resource):
    @work_ns.marshal_with(works_res_model)
    @work_ns.doc(params={'submit_id': 'Submit ID', 'assignment_id': 'Assignment ID', 'user_id': 'User ID'})
    @token_auth.login_required
    def get(self):
        data = request.args
        works = service.get_works(data)
        return {'works': works}

    # Chi post 1 work (current solution)
    @work_ns.marshal_with(work_res_model)
    @work_ns.expect(work_post_req_parser)
    @token_auth.login_required
    def post(self):
        if 'file' not in request.files:
            return 'not ok'
        file = request.files['file']
        if file.filename == '':
            return 'not ok no filename'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # path = save_file(file, filename)
            data = {
                'file': file,
                'filename': filename,
                'assignment_id': request.form.get('assignment_id'),
                'user_id': request.form.get('user_id'),
            }
            work = service.add_work(data)
        return work

    # @work_ns.marshal_with(work_res_model)
    @work_ns.expect(work_put_req_model)
    @token_auth.login_required
    def put(self):
        data = request.json
        work = service.put_work(data)
        return work
