from pydantic import BaseModel
from typing import Optional


class DepartmentCreate(BaseModel):
    name: str
    manager_id: Optional[int] = None


class DepartmentResponse(BaseModel):
    id: int
    name: str
    manager_id: Optional[int]

    class Config:
        from_attributes = True