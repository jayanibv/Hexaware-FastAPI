from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    username: str
    email: str
    role: str
    password: str = Field(..., min_length=6, max_length=50)

class UserLogin(BaseModel):
    email: str
    password: str
