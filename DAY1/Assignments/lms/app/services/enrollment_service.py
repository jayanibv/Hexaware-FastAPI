from fastapi import HTTPException

class EnrollmentService:

    def __init__(self, enrollment_repo, student_repo, course_repo):
        self.enrollment_repo = enrollment_repo
        self.student_repo = student_repo
        self.course_repo = course_repo

    def enroll(self, enrollment_data):

        student = self.student_repo.get_by_id(enrollment_data.student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        course = self.course_repo.get_by_id(enrollment_data.course_id)
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")

        if self.enrollment_repo.exists(enrollment_data.student_id, enrollment_data.course_id):
            raise HTTPException(status_code=400, detail="Already enrolled")

        return self.enrollment_repo.create(enrollment_data)

    def get_all_enrollments(self):
        return self.enrollment_repo.get_all()