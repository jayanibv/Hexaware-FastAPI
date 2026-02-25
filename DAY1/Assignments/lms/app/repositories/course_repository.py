from app.core.db import courses_db
from app.models.course_model import Course

class CourseRepository:

    def create(self, course_data):
        new_id = len(courses_db) + 1
        course = Course(new_id, course_data.title, course_data.duration)
        courses_db.append(course)
        return course

    def get_all(self):
        return courses_db

    def get_by_id(self, course_id: int):
        for course in courses_db:
            if course.id == course_id:
                return course
        return None