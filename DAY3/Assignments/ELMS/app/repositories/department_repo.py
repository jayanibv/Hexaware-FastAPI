from sqlalchemy.orm import Session
from app.models.department import Department

class DepartmentRepository:

    def create(self, db: Session, data):
        dept = Department(**data.dict())
        db.add(dept)
        db.commit()
        db.refresh(dept)
        return dept