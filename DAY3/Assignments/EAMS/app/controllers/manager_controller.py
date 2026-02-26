from sqlalchemy.orm import Session
from app.models.asset import Asset
from app.models.user import User


def view_department_assets(db: Session, department_id: int):
    return db.query(Asset).filter(
        Asset.department_id == department_id
    ).all()


def view_department_users(db: Session, department_id: int):
    return db.query(User).filter(
        User.department_id == department_id
    ).all()