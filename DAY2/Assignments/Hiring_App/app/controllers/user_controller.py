from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user_schema import UserCreate, UserResponse
from app.services.user_service import UserService
from app.core.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

service = UserService()


@router.post("", response_model=UserResponse)
def create_user(data: UserCreate, db: Session = Depends(get_db)):

    return service.create_user(db, data)


@router.get("/{id}", response_model=UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):

    return service.get_user(db, id)


@router.get("", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):

    return service.get_users(db)