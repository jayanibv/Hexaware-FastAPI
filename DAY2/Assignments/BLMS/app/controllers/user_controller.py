from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user_schema import UserCreate, UserResponse
from app.repositories.user_repository import UserRepository
from app.core.database import get_db

router = APIRouter(prefix="/users")

repo = UserRepository()

@router.post("", response_model=UserResponse)

def create(data: UserCreate, db: Session = Depends(get_db)):

    return repo.create(db, data)


@router.get("/{id}", response_model=UserResponse)

def get(id: int, db: Session = Depends(get_db)):

    return repo.get(db, id)