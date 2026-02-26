from pydantic import BaseModel
from datetime import date

class LeaveCreate(BaseModel):
    employee_id: int
    start_date: date
    end_date: date
    reason: str

class LeaveResponse(BaseModel):
    id: int
    employee_id: int
    status: str

    class Config:
        from_attributes = True