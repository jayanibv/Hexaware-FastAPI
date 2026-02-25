from sqlalchemy.orm import Session
from app.models.user import User


class UserRepository:

    def create_user(self, db: Session, data):

        user = User(**data.dict())

        db.add(user)
        db.commit()
        db.refresh(user)

        return user


    def get_user(self, db, user_id):

        return db.query(User).filter(User.id == user_id).first()


    def get_users(self, db):

        return db.query(User).all()