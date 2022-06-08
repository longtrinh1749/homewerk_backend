from homewerk import models as m
from homewerk.services import Singleton
from homewerk.services.score import ScoreService

score_service = ScoreService.get_instance()

class ExcelService(Singleton):
    def export_course_transcript(self, course_id):
        students = score_service.get_top_students_score_in_course(course_id=course_id, display=True)

        pass
