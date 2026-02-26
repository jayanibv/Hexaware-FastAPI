from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.dependencies.rbac import require_roles
from app.controllers import itadmin_controller
from app.schemas.asset_schema import AssetCreate, AssetResponse

router = APIRouter(prefix="/itadmin", tags=["IT Admin"])


@router.post("/assets", response_model=AssetResponse)
def create_asset(
    data: AssetCreate,
    db: Session = Depends(get_db),
    user=Depends(require_roles("IT_ADMIN"))
):
    return itadmin_controller.create_asset(db, data)


@router.put("/requests/{request_id}/approve")
def approve_request(
    request_id: int,
    db: Session = Depends(get_db),
    user=Depends(require_roles("IT_ADMIN"))
):
    return itadmin_controller.approve_request(db, request_id, user.id)


@router.post("/assign/{asset_id}/user/{user_id}")
def assign_asset(
    asset_id: int,
    user_id: int,
    db: Session = Depends(get_db),
    user=Depends(require_roles("IT_ADMIN"))
):
    return itadmin_controller.assign_asset(db, asset_id, user_id)


@router.put("/return/{assignment_id}")
def return_asset(
    assignment_id: int,
    condition: str,
    db: Session = Depends(get_db),
    user=Depends(require_roles("IT_ADMIN"))
):
    return itadmin_controller.return_asset(db, assignment_id, condition)