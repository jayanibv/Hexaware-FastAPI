from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.user_schema import UserCreate
from app.schemas.department_schema import DepartmentCreate
from app.controllers import admin_controller
from app.dependencies.rbac import require_role

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/users")
def create_user(
    data: UserCreate,
    db: Session = Depends(get_db)
):
    return admin_controller.create_user(db, data)

@router.get("/users")
def get_users(
    db: Session = Depends(get_db),
    user=Depends(require_role("ADMIN"))
):
    return admin_controller.get_users(db)


@router.post("/departments")
def create_department(
    data: DepartmentCreate,
    db: Session = Depends(get_db),
    user=Depends(require_role("ADMIN"))
):
    return admin_controller.create_department(db, data)