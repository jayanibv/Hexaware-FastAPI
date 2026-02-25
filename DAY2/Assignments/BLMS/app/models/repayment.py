from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.core.database import Base

class Repayment(Base):

    __tablename__ = "repayments"

    id = Column(Integer, primary_key=True)

    loan_application_id = Column(Integer, ForeignKey("loan_applications.id"))

    amount_paid = Column(Float)

    payment_status = Column(String)