from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base


class AssetRequest(Base):
    __tablename__ = "asset_requests"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    asset_type = Column(String, nullable=False)
    reason = Column(String, nullable=False)

    # PENDING | APPROVED | REJECTED
    status = Column(String, default="PENDING")

    approved_by = Column(Integer, ForeignKey("users.id"), nullable=True)

    # Relationships
    employee = relationship(
        "User",
        foreign_keys=[employee_id],
        back_populates="asset_requests"
    )