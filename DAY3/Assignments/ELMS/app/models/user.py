from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(String)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)