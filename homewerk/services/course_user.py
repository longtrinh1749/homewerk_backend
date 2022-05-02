from homewerk.services import Singleton
from homewerk import models as m
from homewerk.constants import Role

class CourseUserService(Singleton):
    def add_user_to_course(self, data):
        course_user = m.UserCourse()
        course_user.course_id = data.get('course_id')
        course_user.user_id = data.get('user_id')

        m.db.session.add(course_user)
        m.db.session.commit()
        return {'result': True}

    def remove_user_from_course(self, data):
        user_id = data.get('user_id')
        course_id = data.get('course_id')
        course_user = m.UserCourse.query.filter(m.UserCourse.course_id == course_id,
                                                m.UserCourse.user_id == user_id).first()
        if course_user:
            course_user.active = False
            # m.db.session.delete(course_user)
            m.db.session.commit()
            return {'result': True}

        return {'result': False}