from pydantic import BaseModel
from datetime import date
from typing import Optional


class AssetCreate(BaseModel):
    asset_tag: str
    asset_type: str
    brand: str
    model: str
    purchase_date: date
    department_id: int


class AssetResponse(BaseModel):
    id: int
    asset_tag: str
    asset_type: str
    brand: str
    model: str
    purchase_date: date
    status: str
    department_id: int

    class Config:
        from_attributes = True