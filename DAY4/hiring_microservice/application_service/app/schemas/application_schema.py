from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

class ApplicationCreate(BaseModel):
    name: str
    email: EmailStr
    job: str
    company_name: str
    location: str

class ApplicationUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    job: Optional[str] = None
    company_name: Optional[str] = None
    location: Optional[str] = None
    
    model_config = ConfigDict(from_attributes=True)

    
class ApplicationResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    job: str
    company_name: str
    location: str
    
    model_config = ConfigDict(from_attributes=True)
        