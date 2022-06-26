import copy

from flask import g

from homewerk.services import Singleton
from homewerk import models as m
from homewerk.constants import Role

class ScoreService(Singleton):
    def get_top_course_scores(self, student_id):
        student_id = g.user.id
        courses = m.Course.query.filter(m.Course.id == m.UserCourse.course_id,
                                        m.UserCourse.user_id == student_id).all()
        for c in courses:
            assignments = m.Assignment.query.filter(m.Assignment.course_id == c.id).all()
            assignment_ids = [a.id for a in assignments]
            submits = m.Submit.query.filter(m.Submit.assignment_id.in_(assignment_ids),
                                            m.Submit.user_id == student_id).all()
            total_score = 0
            for s in submits:
                try:
                    r = float(s.result) or 0
                except Exception:
                    r = 0
                total_score = total_score + r
            c.avg_score = total_score / len(assignment_ids)

        courses.sort(key=lambda c: c.avg_score)
        courses.reverse()

        return courses


    def get_top_assignment_score(self, course_id, student_id, display=False):
        assignments = m.Assignment.query.filter(m.Assignment.course_id == course_id).all()
        for a in assignments:
            submit = m.Submit.query.filter(m.Submit.assignment_id == a.id).first()
            a.score = submit.result if submit else 0

        if not display:
            assignments.sort(key=lambda a: a.score)

        return assignments


    def get_top_students_score_in_course(self, course_id, display=False):
        assignments = m.Assignment.query.filter(m.Assignment.course_id == course_id).all()
        students = m.User.query.filter(m.UserCourse.user_id == m.User.id,
                                       m.UserCourse.course_id == course_id,
                                       m.User.role == Role.Student).all()
        for student in students:
            assignment_ids = [a.id for a in assignments]
            submits = m.Submit.query.filter(m.Submit.assignment_id.in_(assignment_ids),
                                            m.Submit.user_id == student.id).all()
            total_score = 0
            for s in submits:
                asm = m.Assignment.query.get(s.assignment_id)
                try:
                    r = float(s.result) or 0
                except Exception:
                    r = 0
                total_score = total_score + r/asm.max_score
            student.avg_score = total_score / len(assignment_ids) * 10

            if display:
                new_assignments = copy.deepcopy(assignments)
                for a in new_assignments:
                    submit = m.Submit.query.filter(m.Submit.assignment_id == a.id, m.Submit.user_id == student.id).first()
                    if submit:
                        a.score = submit.result or 0
                        a.status = submit.status or ''
                    else:
                        a.score = 0
                student.assignments = new_assignments

        if not display:
            students.sort(key=lambda s: s.avg_score)
            students.reverse()

        return students
