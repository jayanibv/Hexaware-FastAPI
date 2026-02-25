from pydantic import BaseModel

class ProductCreate(BaseModel):

    product_name: str

    interest_rate: float

    max_amount: float

    tenure_months: int

    description: str


class ProductResponse(ProductCreate):

    id: int

    class Config:
        from_attributes = True