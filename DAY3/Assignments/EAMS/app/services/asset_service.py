from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.asset_repo import AssetRepository


class AssetService:

    def __init__(self):
        self.repo = AssetRepository()

    def create_asset(self, db: Session, data):
        existing = self.repo.get_by_tag(db, data.asset_tag)
        if existing:
            raise HTTPException(400, "Asset tag already exists")

        return self.repo.create(db, data)

    def list_assets(self, db: Session, offset: int, limit: int):
        return self.repo.list_all(db, offset, limit)