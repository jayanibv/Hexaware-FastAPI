from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.base import Base

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    manager_id = Column(Integer, ForeignKey("users.id"))