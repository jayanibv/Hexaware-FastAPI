# app/routers/auth_router.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.controllers.auth_controller import AuthController
from app.schemas.user_schema import UserCreate, UserResponse, UserLogin


router = APIRouter(prefix="/auth", tags=["Authentication"])


# -----------------------------
# Register
# -----------------------------

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return AuthController.register(db, user.dict())


# -----------------------------
# Login
# -----------------------------

@router.post("/login")
def login(
    login_data: UserLogin,
    db: Session = Depends(get_db)
):
    return AuthController.login(
        db,
        {
            "email": login_data.email,
            "password": login_data.password
        }
    )