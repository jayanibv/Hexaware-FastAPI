from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.dependencies.rbac import require_roles
from app.controllers import employee_controller
from app.schemas.request_schema import RequestCreate

router = APIRouter(prefix="/employee", tags=["Employee"])


@router.post("/request")
def request_asset(
    data: RequestCreate,
    db: Session = Depends(get_db),
    user=Depends(require_roles("EMPLOYEE"))
):
    return employee_controller.request_asset(db, user.id, data)


@router.get("/my-assets")
def view_my_assets(
    db: Session = Depends(get_db),
    user=Depends(require_roles("EMPLOYEE"))
):
    return employee_controller.view_my_assets(db, user.id)