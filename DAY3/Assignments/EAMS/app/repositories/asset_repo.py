from sqlalchemy.orm import Session
from app.models.asset import Asset


class AssetRepository:

    def create(self, db: Session, data):
        asset = Asset(**data.dict())
        db.add(asset)
        db.commit()
        db.refresh(asset)
        return asset

    def get_by_id(self, db: Session, asset_id: int):
        return db.query(Asset).filter(Asset.id == asset_id).first()

    def get_by_tag(self, db: Session, tag: str):
        return db.query(Asset).filter(Asset.asset_tag == tag).first()

    def list_all(self, db: Session, offset: int = 0, limit: int = 10):
        return db.query(Asset).offset(offset).limit(limit).all()

    def update_status(self, db: Session, asset: Asset, status: str):
        asset.status = status
        db.commit()
        db.refresh(asset)
        return asset