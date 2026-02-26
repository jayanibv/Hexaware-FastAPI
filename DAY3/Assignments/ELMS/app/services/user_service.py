from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User
from app.core.security import hash_password
from app.repositories.user_repo import UserRepository


class UserService:

    def __init__(self):
        self.repo = UserRepository()

    def create_user(self, db: Session, data):
        existing = self.repo.get_by_email(db, data.email)
        if existing:
            raise HTTPException(status_code=400, detail="Email already registered")

        data.password = hash_password(data.password)
        return self.repo.create(db, data)

    def get_all_users(self, db: Session):
        return db.query(User).all()