from homewerk.models import db
import homewerk.models as m
from homewerk.constants import Role

def get_top_course_scores(student_id):
    courses = m.Course.query.filter(m.Course.id == m.UserCourse.course_id,
                                    m.UserCourse.user_id == student_id).all()
    for c in courses:
        assignments = m.Assignment.query.filter(m.Assignment.course_id == c.id).all()
        assignment_ids = [a.id for a in assignments]
        submits = m.Submit.query.filter(m.Submit.assignment_id.in_(assignment_ids)).all()
        total_score = 0
        for s in submits:
            total_score = total_score + s.result
        c.avg_score = total_score / len(assignment_ids)

    courses.sort(key=lambda c: c.avg_score)

    return courses


def get_top_assignment_score(course_id, student_id):
    assignments = m.Assignment.query.filter(m.Assignment.course_id == course_id).all()
    for a in assignments:
        submit = m.Submit.query.filter(m.Submit.assignment_id == a.id).first()
        a.score = submit.result or 0

    assignments.sort(key=lambda a: a.score)

    return assignments


def get_top_students_score_in_course(course_id):
    assignments = m.Assignment.query.filter(m.Assignment.course_id == course_id).all()
    students = m.User.query.filter(m.UserCourse.user_id == m.User.id,
                                   m.UserCourse.course_id == course_id,
                                   m.User.role == Role.Student).all()
    for s in students:
        assignment_ids = [a.id for a in assignments]
        submits = m.Submit.query.filter(m.Submit.assignment_id.in_(assignment_ids),
                                        m.Submit.user_id == s.id).all()
        total_score = 0
        for s in submits:
            total_score = total_score + s.result
        s.avg_score = total_score / len(assignment_ids)

    students.sort(key=lambda s: s.avg_score)

    return students
