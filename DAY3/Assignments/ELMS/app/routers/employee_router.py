from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.leave_schema import LeaveCreate
from app.controllers import employee_controller
from app.dependencies.rbac import require_role

router = APIRouter(prefix="/employee", tags=["Employee"])

@router.post("/leave")
def apply_leave(
    data: LeaveCreate,
    db: Session = Depends(get_db),
    user = Depends(require_role("EMPLOYEE"))
):
    return employee_controller.apply_leave(db, data)