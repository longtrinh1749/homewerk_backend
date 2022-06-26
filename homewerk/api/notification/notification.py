import flask
import flask_restx as _fr
from flask_restx import api, fields

from homewerk.services.notification import NotificationService
from flask import request
from homewerk.extensions.httpauth import token_auth

notification_ns = _fr.Namespace(
    name='Notification',
    path='/notifications'
)

service = NotificationService.get_instance()
get_notification_schema = notification_ns.model(
        'GetNotificationResponse', {
            'id': fields.Integer,
            'scope': fields.String,
            'scope_id': fields.Integer,
            'path': fields.String,
            'trigger_id': fields.Integer,
            'action': fields.String,
            'description': fields.String,
            'type': fields.String,
        })
get_notifications_schema = notification_ns.model('GetNotificationsResponse', {
    'notifications': fields.List(fields.Nested(get_notification_schema))
})

update_notification_schema = notification_ns.model('UpdateNoti', {
    'id': fields.Integer,
    'read': fields.Boolean
})

@notification_ns.route('', methods=['GET', 'POST', 'PUT'])
class Notifications(_fr.Resource):
    @notification_ns.marshal_with(get_notifications_schema)
    @notification_ns.doc(params={'id': 'Notification ID', 'scope': 'Scope', 'path': 'Path', 'user_id': 'User ID'})
    @token_auth.login_required
    def get(self):
        data = request.args
        notifications = service.get_notifications_and_subcribe(data)
        return {'notifications': notifications}

    @notification_ns.expect(update_notification_schema)
    @notification_ns.marshal_with(get_notification_schema)
    @token_auth.login_required
    def put(self):
        data = request.json
        notifcation = service.update_notification(data)
        return notifcation

# TODO: add pub sub client to server to fcm