from sqlalchemy.orm import Session
from app.services.request_service import RequestService
from app.models.asset_assignment import AssetAssignment

request_service = RequestService()


def request_asset(db: Session, employee_id: int, data):
    return request_service.create_request(db, employee_id, data)


def view_my_assets(db: Session, user_id: int):
    return db.query(AssetAssignment).filter(
        AssetAssignment.user_id == user_id,
        AssetAssignment.returned_date == None
    ).all()