from fastapi import HTTPException

class CourseService:

    def __init__(self, repository):
        self.repository = repository

    def create_course(self, course_data):
        return self.repository.create(course_data)

    def get_all_courses(self):
        return self.repository.get_all()

    def get_course(self, course_id: int):
        course = self.repository.get_by_id(course_id)
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")
        return course