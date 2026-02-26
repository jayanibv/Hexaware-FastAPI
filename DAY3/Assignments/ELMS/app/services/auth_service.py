from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.user_repo import UserRepository
from app.core.security import verify_password, create_access_token


class AuthService:

    def __init__(self):
        self.repo = UserRepository()

    def login(self, db: Session, email: str, password: str):
        user = self.repo.get_by_email(db, email)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        if not verify_password(password, user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        token = create_access_token({"user_id": user.id})
        return {"access_token": token, "token_type": "bearer"}