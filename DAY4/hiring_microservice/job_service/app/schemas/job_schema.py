from pydantic import BaseModel, ConfigDict
from typing import Optional

class JobCreate(BaseModel):
    title: str
    description: str
    location: str
    salary: float
    company_name: str

class JobUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    salary: Optional[float] = None
    company_name: Optional[str] = None
    
    model_config = ConfigDict(from_attributes=True)
    
class JobResponse(BaseModel):
    id: int
    title: str
    description: str
    location: str
    salary: float
    company_name: str
    
    model_config = ConfigDict(from_attributes=True)
        