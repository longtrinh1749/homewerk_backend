from flask import request, send_file
import flask_restx as _fr
from flask_restx import fields

from homewerk.services.submit import SubmitService
from .schema import grading_post_req_parser
from homewerk.services.score import ScoreService
from homewerk.services.excel import ExcelService
from homewerk.extensions.httpauth import token_auth


grading_ns = _fr.Namespace(
    name='Grading',
    path='/grading'
)

service = SubmitService.get_instance()
score_service = ScoreService.get_instance()
excel_service = ExcelService.get_instance()

@grading_ns.route('', methods=['PUT'])
class Grading(_fr.Resource):
    @grading_ns.expect(grading_post_req_parser)
    @token_auth.login_required(role='ROLE.TEACHER')
    def put(self):
        data = request.form
        service.update_submit(data)
        return 'ok'


get_assignments_res_schema = grading_ns.model('AssignmentsRes', {
    'assignments': fields.List(fields.Nested(grading_ns.model('AssignmentRes', {
        'id': fields.Integer,
        'name': fields.String,
        'course_id': fields.Integer,
        'active': fields.Boolean,
        'due': fields.String,
        'instruction': fields.String,
        'submit': fields.Integer(attribute='total_submit'),
        'graded': fields.Integer(attribute='total_graded'),
        'status': fields.String(attribute='status'),
        'score': fields.String,
    })))
})

get_courses_res_schema = grading_ns.model('CoursesRes', {
    'courses': fields.List(fields.Nested(grading_ns.model('CourseRes', {
        'id': fields.Integer,
        'name': fields.String,
        'class': fields.String(attribute='clazz'),
        'school': fields.String,
        'school_year': fields.String(attribute='school_year_to_str'),
        'year': fields.String(attribute='school_year'),
        'created_by': fields.Integer,
        'active': fields.Boolean,
        'teacher': fields.Nested(grading_ns.model('TeacherResData', {
            'name': fields.String,
        }), attribute='created_user'),
        'total': fields.Integer(attribute='total'),
        'avg_score': fields.Float
    })))
})

get_students_res_schema = grading_ns.model('StudentsRes', {
    'students': fields.List(fields.Nested(grading_ns.model('StudentRes', {
        'id': fields.Integer,
        'name': fields.String,
        'avg_score': fields.Float,
        'assignments': fields.List(fields.Nested(grading_ns.model('AssignmentRes', {
            'id': fields.Integer,
            'name': fields.String,
            'course_id': fields.Integer,
            'active': fields.Boolean,
            'due': fields.String,
            'instruction': fields.String,
            'submit': fields.Integer(attribute='total_submit'),
            'graded': fields.Integer(attribute='total_graded'),
            'status': fields.String(attribute='status'),
            'score': fields.String,
        }))),
    })))
})

@grading_ns.route('/courses', methods=['GET'])
class CoursesScore(_fr.Resource):
    @grading_ns.doc(params={'student_id': 'Student ID'})
    @grading_ns.marshal_with(get_courses_res_schema)
    @token_auth.login_required
    def get(self):
        data = request.args
        courses = score_service.get_top_course_scores(data['student_id'])
        return {'courses': courses}


@grading_ns.route('/assignments', methods=['GET'])
class AssignmentsScore(_fr.Resource):
    @grading_ns.doc(params={'course_id': 'Course ID', 'display': 'Display', 'excel': 'Excel file return'})
    @grading_ns.marshal_with(get_assignments_res_schema)
    @token_auth.login_required(role='ROLE.TEACHER')
    def get(self):
        data = request.args
        assignments = score_service.get_top_assignment_score(data['course_id'], 0, display=data['display'])
        if data['excel']:
            output, filename = excel_service.export_course_transcript(data['course_id'])
            return send_file(output, attachment_filename=f"{filename}.xlsx", as_attachment=True)
        return {'assignments': assignments}


@grading_ns.route('/excel', methods=['GET'])
class Export(_fr.Resource):
    @grading_ns.doc(params={'course_id': 'Course ID'})
    @token_auth.login_required(role='ROLE.TEACHER')
    def get(self):
        data = request.args
        output, filename = excel_service.export_course_transcript(data['course_id'])
        return send_file(output, attachment_filename=f"{filename}.xlsx", as_attachment=True)


@grading_ns.route('/students', methods=['GET'])
class StudentssScore(_fr.Resource):
    @grading_ns.doc(params={'course_id': 'Course ID', 'display': 'Display'})
    @grading_ns.marshal_with(get_students_res_schema)
    @token_auth.login_required(role='ROLE.TEACHER')
    def get(self):
        data = request.args
        students = score_service.get_top_students_score_in_course(data['course_id'], display=True)
        return {'students': students}
