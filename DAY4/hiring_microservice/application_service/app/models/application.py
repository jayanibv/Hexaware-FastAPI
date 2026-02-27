from sqlalchemy import Column, Integer, String
from app.database.base import Base

class Application(Base):
    __tablename__ = 'applications'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    job= Column(String)
    company_name = Column(String)
    location = Column(String)
    


    