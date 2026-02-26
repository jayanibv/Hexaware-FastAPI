from sqlalchemy.orm import Session
from app.models.department import Department


class DepartmentRepository:

    def create(self, db: Session, data):
        department = Department(**data.dict())
        db.add(department)
        db.commit()
        db.refresh(department)
        return department

    def get_by_id(self, db: Session, dept_id: int):
        return db.query(Department).filter(Department.id == dept_id).first()

    def list_all(self, db: Session):
        return db.query(Department).all()