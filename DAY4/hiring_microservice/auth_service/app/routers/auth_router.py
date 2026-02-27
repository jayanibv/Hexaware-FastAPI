from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.auth_schema import RegisterSchema, LoginSchema, TokenResponse
from app.services.auth_service import AuthService
from app.database.session import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(payload: RegisterSchema, db: Session = Depends(get_db)):
    user = AuthService.register(db, payload.email, payload.password, payload.role)
    return {"message": "User created", "id": user.id}

@router.post("/login", response_model=TokenResponse)
def login(payload: LoginSchema, db: Session = Depends(get_db)):
    token = AuthService.login(db, payload.email, payload.password)
    return {"access_token": token}