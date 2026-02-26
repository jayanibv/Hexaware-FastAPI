from sqlalchemy.orm import Session
from app.models.asset_request import AssetRequest


class RequestRepository:

    def create(self, db: Session, request):
        db.add(request)
        db.commit()
        db.refresh(request)
        return request

    def get_by_id(self, db: Session, request_id: int):
        return db.query(AssetRequest).filter(
            AssetRequest.id == request_id
        ).first()

    def list_all(self, db: Session, offset: int = 0, limit: int = 10):
        return db.query(AssetRequest).offset(offset).limit(limit).all()

    def update(self, db: Session):
        db.commit()