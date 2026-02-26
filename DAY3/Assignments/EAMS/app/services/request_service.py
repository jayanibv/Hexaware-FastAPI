from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.asset import Asset
from app.models.asset_request import AssetRequest
from app.repositories.request_repo import RequestRepository
from app.repositories.asset_repo import AssetRepository
from app.services.assignment_service import AssignmentService


class RequestService:

    def __init__(self):
        self.repo = RequestRepository()
        self.asset_repo = AssetRepository()
        self.assignment_service = AssignmentService()

    def create_request(self, db: Session, employee_id: int, data):
        request = AssetRequest(
            employee_id=employee_id,
            asset_type=data.asset_type,
            reason=data.reason
        )
        return self.repo.create(db, request)

    def approve_request(self, db: Session, request_id: int, approver_id: int):
        request = self.repo.get_by_id(db, request_id)
        if not request:
            raise HTTPException(404, "Request not found")

        if request.status != "PENDING":
            raise HTTPException(400, "Already processed")

        asset = db.query(Asset).filter(
            Asset.asset_type == request.asset_type,
            Asset.status == "AVAILABLE"
        ).first()

        if not asset:
            raise HTTPException(400, "No available asset of requested type")

        request.status = "APPROVED"
        request.approved_by = approver_id

        # assign automatically
        self.assignment_service.assign_asset(db, asset.id, request.employee_id)

        db.commit()
        return request