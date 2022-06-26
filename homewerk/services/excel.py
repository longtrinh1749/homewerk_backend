from homewerk import models as m
from homewerk.services import Singleton
from homewerk.services.score import ScoreService
from io import BytesIO
import xlsxwriter

score_service = ScoreService.get_instance()

class ExcelService(Singleton):
    def export_course_transcript(self, course_id):
        course = m.Course.query.get(course_id)
        students = score_service.get_top_students_score_in_course(course_id=course_id, display=True)
        output = BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        course_data_format = workbook.add_format({
            'bold': 1,
            'font_size': 12,
            'font_name': 'Times New Roman'
        })
        title_format = workbook.add_format({
            'bold': 1,
            'font_size': 14,
            'font_name': 'Times New Roman',
            'align': 'center',
            'valign': 'vcenter',
        })
        subtitle_format = workbook.add_format({
            'font_size': 14,
            'font_name': 'Times New Roman',
            'align': 'center',
            'valign': 'vcenter',
        })
        table_header_format = workbook.add_format({
            'bold': 1,
            'font_size': 12,
            'font_name': 'Times New Roman',
            'align': 'center',
            'valign': 'vcenter',
            'border': 1,
        })
        table_data_format = workbook.add_format({
            'font_size': 12,
            'font_name': 'Times New Roman',
            'align': 'center',
            'valign': 'vcenter',
            'border': 1,
        })
        worksheet.write(0, 0, course.school, course_data_format)
        worksheet.write(1, 0, course.clazz, course_data_format)
        worksheet.write(2, 0, course.name, course_data_format)
        worksheet.merge_range(4, 0, 4, len(students[0].assignments) + 2, 'BẢNG ĐIỂM HỌC PHẦN', title_format)
        worksheet.merge_range(5, 0, 5, len(students[0].assignments) + 2, f'MÔN: {course.name} - LỚP: {course.clazz} - NĂM HỌC: {course.school_year_to_str}', subtitle_format)

        worksheet.write(7, 0, 'STT', table_header_format)
        worksheet.write(7, 1, 'Họ và tên', table_header_format)
        worksheet.write(7, 2, 'Số điện thoại', table_header_format)

        for i, asm in enumerate(students[0].assignments):
            worksheet.write(7, i + 3, asm.name, table_header_format)


        for i, student in enumerate(students):
            worksheet.write(8 + i, 0, i, table_data_format)
            worksheet.write(8 + i, 1, student.name, table_data_format)
            worksheet.write(8 + i, 2, student.phone, table_data_format)
            for j, asm in enumerate(student.assignments):
                worksheet.write(i + 8, j + 3, asm.score, table_data_format)

        workbook.close()
        output.seek(0)

        return output, f'{course.name}'
