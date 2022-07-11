import sqlalchemy.exc
from flask import g
from flask_restx import abort

from homewerk.constants import Role
from homewerk.services import Singleton
from homewerk import models as m
from homewerk import utils

class UserService(Singleton):
    def get_user(self, data):
        query = m.User.query
        if not data:
            return None
        if data.get('id'):
            query = query.filter(m.User.id == data.get('id'))
        else:
            query = query.filter(m.User.id == g.user.id)
        if data.get('username'):
            query = query.filter(m.User.username == data.get('username'))
        if data.get('password'):
            query = query.filter(m.User.password == data.get('password')) # TODO: ghep vao vs filter by username
        return query.first()

    def create_user(self, data):
        try:
            if not (data.get('username') and data.get('password')):
                abort(400)
            user = m.User()
            user.name = data.get('name')
            user.password = data.get('password')
            user.username = data.get('username')
            user.clazz = data.get('class')
            user.role = data.get('role')
            user.address = data.get('address')
            user.phone = data.get('phone')
            user.school = data.get('school')
            user.email = data.get('email')
            user.hash_password(data.get('password'))
            m.db.session.add(user)
            m.db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return None

        return user

    def update_user(self, data):
        user_id = g.user.id
        user = m.User.query.get(user_id)
        if not user:
            return None
        try:
            if (data.get('name')): user.name = data.get('name')
            if (data.get('class')): user.clazz = data.get('class')
            if (data.get('address')): user.address = data.get('address')
            if (data.get('phone')): user.phone = data.get('phone')
            if (data.get('school')): user.school = data.get('school')
            if (data.get('email')): user.email = data.get('email')
            m.db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return None

        return user

    def get_students_by_course(self, data):
        course_id = data.get('course_id')
        students = m.User.query.filter(m.User.id == m.UserCourse.user_id,
                                       m.UserCourse.course_id == course_id,
                                       m.UserCourse.active == True,
                                       m.User.role == Role.Student).all()
        assignment_id = data.get('assignment_id')
        for s in students:
            if assignment_id:
                submit = m.Submit.query.filter(m.Submit.user_id == s.id,
                                               m.Submit.assignment_id == assignment_id).first()
                if submit:
                    s.status = submit.status
                    s.score = submit.result

        return students

    def update_password(self, data):
        id = g.user.id
        user = m.User.query.get(id)
        old_password = data.get('old_password')
        if old_password != user.password:
            return "Wrong password"
        new_password = data.get('new_password')
        if new_password:
            user.password = new_password
            user.hash_password(new_password)

        m.db.session.commit()
        return "Success"

