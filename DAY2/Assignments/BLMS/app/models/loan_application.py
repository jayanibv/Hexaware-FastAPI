from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.core.database import Base

class LoanApplication(Base):

    __tablename__ = "loan_applications"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    product_id = Column(Integer, ForeignKey("loan_products.id"))

    requested_amount = Column(Float)

    approved_amount = Column(Float, nullable=True)

    status = Column(String, default="pending")

    processed_by = Column(Integer, ForeignKey("users.id"), nullable=True)