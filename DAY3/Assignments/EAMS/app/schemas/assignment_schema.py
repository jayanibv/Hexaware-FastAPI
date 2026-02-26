from pydantic import BaseModel
from datetime import date
from typing import Optional


class AssignmentCreate(BaseModel):
    asset_id: int
    user_id: int
    assigned_date: date


class AssignmentReturn(BaseModel):
    returned_date: date
    condition_on_return: Optional[str] = None


class AssignmentResponse(BaseModel):
    id: int
    asset_id: int
    user_id: int
    assigned_date: date
    returned_date: Optional[date]
    condition_on_return: Optional[str]

    class Config:
        from_attributes = True