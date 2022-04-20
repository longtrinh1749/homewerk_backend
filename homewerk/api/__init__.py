import flask_restx as _fr
from flask import Blueprint
from . import (
    user,
    course
)

api_bp = Blueprint('api', __name__)
api = _fr.Api(
    app=api_bp,
    version='1.0',
)

def init_app(app, **kwargs):
    app.register_blueprint(api_bp)
    api.add_namespace(user.user_ns)
    api.add_namespace(course.course_ns)
    api.add_namespace(course.course_user_ns)