from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.models.user import User
from app.exceptions.custom_exceptions import (
    UserNotFoundException,
    DuplicateUserException
)


class UserService:

    def __init__(self):

        self.repo = UserRepository()


    def create_user(self, db: Session, data):

        # check duplicate email properly
        existing = db.query(User).filter(
            User.email == data.email
        ).first()

        if existing:

            raise DuplicateUserException(data.email)

        return self.repo.create_user(db, data)


    def get_user(self, db: Session, user_id: int):

        user = self.repo.get_user(db, user_id)

        if not user:

            raise UserNotFoundException(user_id)

        return user


    def get_users(self, db: Session):

        return self.repo.get_users(db)