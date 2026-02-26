from pydantic import BaseModel
from typing import Optional


class RequestCreate(BaseModel):
    asset_type: str
    reason: str


class RequestResponse(BaseModel):
    id: int
    employee_id: int
    asset_type: str
    reason: str
    status: str
    approved_by: Optional[int]

    class Config:
        from_attributes = True