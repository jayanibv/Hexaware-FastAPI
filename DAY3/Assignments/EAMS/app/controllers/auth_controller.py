from sqlalchemy.orm import Session
from app.services.auth_service import AuthService

auth_service = AuthService()


def login(db: Session, email: str, password: str):
    return auth_service.login(db, email, password)