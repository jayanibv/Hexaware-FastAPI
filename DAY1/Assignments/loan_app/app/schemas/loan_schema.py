from pydantic import BaseModel

class LoanCreate(BaseModel):
    name: str
    email: str
    amount: int
    annual_income: int
    interest_rate: float
    duration: int

class LoanResponse(BaseModel):
    id: int
    name: str
    email: str
    amount: int
    annual_income: int
    interest_rate: float
    duration: int

class LoanStatusUpdate(BaseModel):
    status: str