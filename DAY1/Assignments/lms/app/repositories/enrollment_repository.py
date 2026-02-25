from app.core.db import enrollments_db
from app.models.enrollment_model import Enrollment

class EnrollmentRepository:

    def create(self, enrollment_data):
        new_id = len(enrollments_db) + 1
        enrollment = Enrollment(new_id, enrollment_data.student_id, enrollment_data.course_id)
        enrollments_db.append(enrollment)
        return enrollment

    def get_all(self):
        return enrollments_db

    def exists(self, student_id: int, course_id: int):
        for enrollment in enrollments_db:
            if enrollment.student_id == student_id and enrollment.course_id == course_id:
                return True
        return False