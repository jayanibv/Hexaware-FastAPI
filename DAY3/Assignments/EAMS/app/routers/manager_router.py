from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.dependencies.rbac import require_roles
from app.controllers import manager_controller

router = APIRouter(prefix="/manager", tags=["Manager"])


@router.get("/department/assets")
def view_department_assets(
    db: Session = Depends(get_db),
    user=Depends(require_roles("MANAGER"))
):
    return manager_controller.view_department_assets(db, user.department_id)


@router.get("/department/users")
def view_department_users(
    db: Session = Depends(get_db),
    user=Depends(require_roles("MANAGER"))
):
    return manager_controller.view_department_users(db, user.department_id)