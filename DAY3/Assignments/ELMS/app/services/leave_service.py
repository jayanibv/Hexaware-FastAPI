from datetime import date
from fastapi import HTTPException
from app.models.leave_request import LeaveRequest

class LeaveService:

    def apply_leave(self, db, data):
        if data.start_date > data.end_date:
            raise HTTPException(400, "Invalid dates")

        leave = LeaveRequest(**data.dict())
        db.add(leave)
        db.commit()
        db.refresh(leave)
        return leave

    def approve_leave(self, db, leave_id, manager_id):
        leave = db.query(LeaveRequest).filter(LeaveRequest.id == leave_id).first()
        if not leave:
            raise HTTPException(404, "Leave not found")

        if leave.status != "PENDING":
            raise HTTPException(400, "Already processed")

        leave.status = "APPROVED"
        leave.approved_by = manager_id
        db.commit()
        db.refresh(leave) 
        return leave