from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.department import Department
from app.repositories.department_repo import DepartmentRepository


class DepartmentService:

    def __init__(self):
        self.repo = DepartmentRepository()

    def create_department(self, db: Session, data):
        return self.repo.create(db, data)

    def get_all_departments(self, db: Session):
        return db.query(Department).all()