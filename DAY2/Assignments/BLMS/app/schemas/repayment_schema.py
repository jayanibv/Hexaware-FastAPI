from pydantic import BaseModel

class RepaymentCreate(BaseModel):

    loan_application_id: int

    amount_paid: float

    payment_status: str


class RepaymentResponse(RepaymentCreate):

    id: int

    class Config:
        from_attributes = True