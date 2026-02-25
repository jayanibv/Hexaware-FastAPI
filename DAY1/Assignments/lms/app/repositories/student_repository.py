from app.core.db import students_db
from app.models.student_model import Student

class StudentRepository:

    def create(self, student_data):
        new_id = len(students_db) + 1
        student = Student(new_id, student_data.name, student_data.email)
        students_db.append(student)
        return student

    def get_by_id(self, student_id: int):
        for student in students_db:
            if student.id == student_id:
                return student
        return None