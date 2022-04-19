from homewerk.services import Singleton
from homewerk import models as m
from sqlalchemy import desc

class CourseService(Singleton):
    def get_all_courses(self):
        return m.Course.query.all()

    def get_courses(self, data):
        query = m.Course.query
        if not data:
            return self.get_all_courses()
        if data.get('id'):
            query = query.filter(m.Course.id == data.get('id'))
        if data.get('user_id'):
            query = query.filter(m.UserCourse.user_id == data.get('user_id'))
        courses = query.order_by(desc(m.Course.id)).all()
        return courses

    def create_course(self, data):
        course = m.Course()
        course.name = data.get('name')
        course.clazz = data.get('class')
        course.school = data.get('school')
        course.school_year = data.get('school_year')
        course.created_by = data.get('user_id')
        m.db.session.add(course)
        m.db.session.flush()
        self.add_course_user(course.id, course.created_by)
        m.db.session.commit()
        return course

    def update_course(self, data):
        course = m.Course.query.get(data.get('id'))
        if not course:
            return None
        course.clazz = data.get('class')
        course.school = data.get('school')
        course.school_year = data.get('school_year')
        m.db.session.commit()
        return course

    def remove_course_user(self, course_id, user_id):
        course_user = m.UserCourse.query.filter(m.UserCourse.user_id == user_id,
                                                m.UserCourse.course_id == course_id).first()

        m.db.session.delete(course_user)
        m.db.session.commit
        return course_user.course

    def add_course_user(self, course_id, user_id):
        course_user = m.UserCourse()
        course_user.course_id = course_id
        course_user.user_id = user_id
        m.db.session.add(course_user)
        m.db.session.commit()

        return course_user.course
