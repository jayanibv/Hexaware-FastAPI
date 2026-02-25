from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:

    def create(self, db: Session, data):

        obj = User(**data.dict())

        db.add(obj)

        db.commit()

        db.refresh(obj)

        return obj


    def get(self, db, id):

        return db.query(User).filter(User.id == id).first()


    def get_all(self, db):

        return db.query(User).all()