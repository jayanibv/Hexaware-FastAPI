from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.controllers import manager_controller
from app.dependencies.rbac import require_role

router = APIRouter(prefix="/manager", tags=["Manager"])


@router.put("/leave/{leave_id}/approve")
def approve_leave(
    leave_id: int,
    db: Session = Depends(get_db),
    user=Depends(require_role("MANAGER"))
):
    return manager_controller.approve_leave(db, leave_id, user.id)