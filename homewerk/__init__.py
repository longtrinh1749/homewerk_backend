import flask
import os
from . import api, models, services
from homewerk.extensions import httpauth
import config
from flask_cors import CORS


def create_app():

    def load_app_config(app):
        app.config.from_object(config)

    app = flask.Flask(__name__)
    load_app_config(app)
    app.config['SECRET_KEY'] = 'hardsecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/homewerk'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['CORS_SUPPORTS_CREDENTIALS'] = True
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['CORS_EXPOSE_HEADERS'] = 'Content-Disposition'
    app.config['UPLOAD_FOLDER'] = config.ROOT_DIR + '/data'

    models.init_app(app)
    api.init_app(app)
    CORS(app)

    return app

app = create_app()

@app.teardown_appcontext
def shutdown_session(exception=None):
    models.db.session.remove()

from . import biz
