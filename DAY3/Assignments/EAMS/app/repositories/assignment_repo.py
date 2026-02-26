from sqlalchemy.orm import Session
from app.models.asset_assignment import AssetAssignment


class AssignmentRepository:

    def create(self, db: Session, assignment):
        db.add(assignment)
        db.commit()
        db.refresh(assignment)
        return assignment

    def get_active_by_asset(self, db: Session, asset_id: int):
        return db.query(AssetAssignment).filter(
            AssetAssignment.asset_id == asset_id,
            AssetAssignment.returned_date == None
        ).first()

    def get_by_id(self, db: Session, assignment_id: int):
        return db.query(AssetAssignment).filter(
            AssetAssignment.id == assignment_id
        ).first()

    def update(self, db: Session):
        db.commit()