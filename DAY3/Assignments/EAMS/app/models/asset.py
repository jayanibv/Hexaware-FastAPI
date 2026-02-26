from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base


class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)

    asset_tag = Column(String, unique=True, nullable=False)
    asset_type = Column(String, nullable=False)  # Laptop, Monitor, License etc.
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    purchase_date = Column(Date, nullable=False)

    # AVAILABLE | ASSIGNED | MAINTENANCE | RETIRED
    status = Column(String, default="AVAILABLE")

    department_id = Column(Integer, ForeignKey("departments.id"))

    # Relationships
    department = relationship("Department", back_populates="assets")

    assignments = relationship("AssetAssignment", back_populates="asset")