from sqlalchemy import Column, Integer, String, Float
from app.database.base import Base

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    salary = Column(Float)
    company_name = Column(String)
    location = Column(String)