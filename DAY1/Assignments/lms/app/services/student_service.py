from fastapi import HTTPException

class StudentService:

    def __init__(self, repository):
        self.repository = repository

    def create_student(self, student_data):
        return self.repository.create(student_data)

    def get_student(self, student_id: int):
        student = self.repository.get_by_id(student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        return student