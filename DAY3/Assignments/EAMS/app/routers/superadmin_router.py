from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.dependencies.rbac import require_roles
from app.controllers import superadmin_controller
from app.schemas.user_schema import UserCreate, UserResponse
from app.schemas.department_schema import DepartmentCreate, DepartmentResponse
from app.schemas.asset_schema import AssetCreate, AssetResponse

router = APIRouter(prefix="/superadmin", tags=["SuperAdmin"])


@router.post("/departments", response_model=DepartmentResponse)
def create_department(
    data: DepartmentCreate,
    db: Session = Depends(get_db),
    user=Depends(require_roles("SUPERADMIN"))
):
    return superadmin_controller.create_department(db, data)


@router.post("/users", response_model=UserResponse)
def create_user(
    data: UserCreate,
    db: Session = Depends(get_db),
):
    return superadmin_controller.create_user(db, data)


@router.post("/assets", response_model=AssetResponse)
def create_asset(
    data: AssetCreate,
    db: Session = Depends(get_db),
    user=Depends(require_roles("SUPERADMIN"))
):
    return superadmin_controller.create_asset(db, data)