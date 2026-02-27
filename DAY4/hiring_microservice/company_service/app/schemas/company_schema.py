from pydantic import BaseModel, ConfigDict
from typing import Optional

class CompanyCreate(BaseModel):
    name: str
    location: str

class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    
    model_config = ConfigDict(from_attributes=True)
    
class CompanyResponse(BaseModel):
    id: int
    name: str
    location: str
    
    model_config = ConfigDict(from_attributes=True)
        