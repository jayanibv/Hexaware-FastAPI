from fastapi import HTTPException
from app.repositories.user_repository import UserRepository


class UserService:

    def __init__(self, repository: UserRepository):
        self.repository = repository


    def create_user(self, db, data):

        # check duplicate email
        existing = db.query(self.repository.__class__.__name__)

        return self.repository.create(db, data)


    def get_user(self, db, user_id):

        user = self.repository.get(db, user_id)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return user


    def get_users(self, db):

        return self.repository.get_all(db)