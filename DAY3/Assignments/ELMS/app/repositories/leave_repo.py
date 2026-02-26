from sqlalchemy.orm import Session
from app.models.leave_request import LeaveRequest

class LeaveRepository:

    def create(self, db: Session, data):
        leave = LeaveRequest(**data.dict())
        db.add(leave)
        db.commit()
        db.refresh(leave)
        return leave