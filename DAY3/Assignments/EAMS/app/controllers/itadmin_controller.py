from sqlalchemy.orm import Session
from app.services.asset_service import AssetService
from app.services.assignment_service import AssignmentService
from app.services.request_service import RequestService

asset_service = AssetService()
assignment_service = AssignmentService()
request_service = RequestService()


def create_asset(db: Session, data):
    return asset_service.create_asset(db, data)


def approve_request(db: Session, request_id: int, approver_id: int):
    return request_service.approve_request(db, request_id, approver_id)


def assign_asset(db: Session, asset_id: int, user_id: int):
    return assignment_service.assign_asset(db, asset_id, user_id)


def return_asset(db: Session, assignment_id: int, condition: str):
    return assignment_service.return_asset(db, assignment_id, condition)