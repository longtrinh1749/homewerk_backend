from homewerk.services.saved import SavedService
import flask_restx as _fr
from flask_restx import fields
from flask import request

saved_ns = _fr.Namespace(
    name='Saved',
    path='/saved'
)

saved_service = SavedService.get_instance()

get_save_model = saved_ns.model('SaveModel', {
        'user_id': fields.Integer,
        'type': fields.String,
        'type_id': fields.Integer
    })
get_saves_model = saved_ns.model('GetSaveModel', {
    'saves': fields.List(fields.Nested(get_save_model))
})
delete_result_model = saved_ns.model('DeleteResult', {
    'result': fields.Boolean
})
@saved_ns.route('', methods=['GET', 'POST', 'DELETE'])
class Saved(_fr.Resource):

    @saved_ns.doc({'user_id': 'User ID'})
    @saved_ns.marshal_with(get_saves_model)
    def get(self):
        data = request.args
        saves = saved_service.get_saved(data)
        return saves

    @saved_ns.marshal_with(get_save_model)
    def post(self):
        data = request.json
        saved = saved_service.create_saved(data)
        return saved

    @saved_ns.marshal_with(delete_result_model)
    def delete(self):
        data = request.json
        result = saved_service.delete_saved(data)
        return result
