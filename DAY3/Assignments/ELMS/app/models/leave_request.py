from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database.base import Base

class LeaveRequest(Base):
    __tablename__ = "leave_requests"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey("users.id"))
    start_date = Column(Date)
    end_date = Column(Date)
    reason = Column(String)
    status = Column(String, default="PENDING")
    approved_by = Column(Integer, nullable=True)