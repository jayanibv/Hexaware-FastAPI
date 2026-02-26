from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import date
from app.models.asset_assignment import AssetAssignment
from app.repositories.assignment_repo import AssignmentRepository
from app.repositories.asset_repo import AssetRepository


class AssignmentService:

    def __init__(self):
        self.repo = AssignmentRepository()
        self.asset_repo = AssetRepository()

    def assign_asset(self, db: Session, asset_id: int, user_id: int):
        asset = self.asset_repo.get_by_id(db, asset_id)
        if not asset:
            raise HTTPException(404, "Asset not found")

        if asset.status != "AVAILABLE":
            raise HTTPException(400, "Asset not available")

        active = self.repo.get_active_by_asset(db, asset_id)
        if active:
            raise HTTPException(400, "Asset already assigned")

        assignment = AssetAssignment(
            asset_id=asset_id,
            user_id=user_id,
            assigned_date=date.today()
        )

        asset.status = "ASSIGNED"

        db.add(assignment)
        db.commit()
        db.refresh(assignment)

        return assignment

    def return_asset(self, db: Session, assignment_id: int, condition: str):
        assignment = self.repo.get_by_id(db, assignment_id)
        if not assignment:
            raise HTTPException(404, "Assignment not found")

        if assignment.returned_date:
            raise HTTPException(400, "Already returned")

        assignment.returned_date = date.today()
        assignment.condition_on_return = condition

        asset = assignment.asset
        asset.status = "AVAILABLE"

        db.commit()
        return assignment