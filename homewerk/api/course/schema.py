from flask_restx import fields

get_course_request_model = {
    'id': fields.Integer
}

get_course_response_model = {
    'id': fields.Integer,
    'name': fields.String,
    'class': fields.String(attribute='clazz'),
    'school': fields.String,
    'school_year': fields.String(attribute='school_year_to_str'),
    'year': fields.String(attribute='school_year'),
    'created_by': fields.Integer,
}

get_courses_res_model = {
    'courses': fields.List(fields.Nested(get_course_response_model))
    # 'courses': fields.String,
}

get_courses_response_model = {
    'courses': fields.Nested(model=get_course_response_model)
}

# get_courses_response_model = {
#     'course': [{
#         'name': fields.String,
#         'class': fields.String,
#         'school': fields.String,
#         'school_year': fields.Integer,
#         'user_id': fields.Integer,
#     }]
# }

get_courses_by_user_req_model = {
    'user_id': fields.Integer
}

create_course_request_model = {
    'name': fields.String,
    'class': fields.String,
    'school': fields.String,
    'school_year': fields.Integer,
    'user_id': fields.Integer,
}

update_course_request_model = {
    'id': fields.Integer,
    'class': fields.String,
    'school': fields.String,
    'school_year': fields.Integer,
}

# TODO: create route to use
add_course_user_req_model = {
    'course_id': fields.Integer,
    'user_id': fields.Integer,
}

# TODO: create route to use
remove_course_user_req_model = {
    'course_id': fields.Integer,
    'user_id': fields.Integer,
}

course_user_res_model = {
    'result': fields.Boolean,
}