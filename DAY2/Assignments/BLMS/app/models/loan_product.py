from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base

class LoanProduct(Base):

    __tablename__ = "loan_products"

    id = Column(Integer, primary_key=True, index=True)

    product_name = Column(String)

    interest_rate = Column(Float)

    max_amount = Column(Float)

    tenure_months = Column(Integer)

    description = Column(String)