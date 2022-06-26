from flask_httpauth import HTTPTokenAuth, HTTPBasicAuth
from homewerk.models.user import User
from flask import g

token_auth = HTTPTokenAuth(scheme='Bearer')
basic_auth = HTTPBasicAuth()

@basic_auth.verify_password
def verify_password(username, password):
        # try to authenticate with username/password
    user = User.query.filter_by(username=username).first()
    if not user and not user.verify_password(password) and not user.password == password:
        return False
    g.user = user
    return True

@token_auth.verify_token
def verify_token(token):
    user = User.verify_auth_token(token)
    if not user:
        return False
    g.user = user
    return True

@token_auth.get_user_roles
def get_user_roles(auth):
    user = User.verify_auth_token(auth.get('token'))
    if not user:
        return None
    g.user = user
    return user.role