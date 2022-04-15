import flask
import flask_restx as _fr
from homewerk.services.user import UserService
from flask import g
from flask import request

user_ns = _fr.Namespace(
    name='User',
    path='/users'
)

service = UserService.get_instance()

@user_ns.route('', methods=['GET', 'POST'])
class Users(_fr.Resource):
    def get(self):
        user = service.get_user()
        return user

    def post(self):
        data = request.json
        return service.create_user(data)
