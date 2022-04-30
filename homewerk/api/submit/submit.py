from flask import request
import flask_restx as _fr
from homewerk.services.submit import SubmitService
from .schema import (
    submit_post_req_schema,
    submit_res_schema,
    submit_put_req_schema,
    submit_post_req_parser
)

submit_ns = _fr.Namespace(
    name="Submiting Assignment API",
    path="/submits"
)

service = SubmitService.get_instance()
submit_res_model = submit_ns.model('SubmitResModel', submit_res_schema)
submits_res_model = submit_ns.model('SubmitsResModel', {
    'submits': _fr.fields.List(_fr.fields.Nested(submit_res_model))
})
submit_post_req_model = submit_ns.model('SubmitPostReqModel', submit_post_req_schema)
submit_put_req_model = submit_ns.model('SubmitPutReqModel', submit_put_req_schema)

@submit_ns.route('', methods=['GET', 'POST', 'PUT'])
class Submit(_fr.Resource):
    @submit_ns.marshal_with(submits_res_model)
    @submit_ns.doc({'id': 'ID', 'user_id': 'User ID', 'assignment_id': 'Assignment ID', 'status': 'Status'})
    def get(self):
        data = request.args
        submits = service.get_submits(data)
        return {'submits': submits}

    @submit_ns.marshal_with(submit_res_model)
    @submit_ns.expect(submit_post_req_parser)
    def post(self):
        # data = request.json
        # submit = service.add_submit(data)
        # return submit
        args = submit_post_req_parser.parse_args()
        data = request.json
        return 'ok'

    @submit_ns.marshal_with(submit_res_model)
    @submit_ns.expect(submit_post_req_model)
    def put(self):
        data = request.json
        submit = service.update_submit(data)
        return submit