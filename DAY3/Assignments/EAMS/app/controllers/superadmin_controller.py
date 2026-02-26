from sqlalchemy.orm import Session
from app.repositories.department_repo import DepartmentRepository
from app.repositories.user_repo import UserRepository
from app.services.asset_service import AssetService
from app.core.security import hash_password

dept_repo = DepartmentRepository()
user_repo = UserRepository()
asset_service = AssetService()


def create_department(db: Session, data):
    return dept_repo.create(db, data)


def create_user(db: Session, data):
    data.password = hash_password(data.password)
    return user_repo.create(db, data)


def create_asset(db: Session, data):
    return asset_service.create_asset(db, data)