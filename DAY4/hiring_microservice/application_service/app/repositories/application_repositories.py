from sqlalchemy.orm import Session
from app.models.application import Application

class ApplicationRepository:

    def __init__(self, db: Session):
        self.db = db
        
    def create_application(self, application_data: dict) -> Application:
        application = Application(**application_data)
        self.db.add(application)
        self.db.commit()
        self.db.refresh(application)
        return application
    
    def get_application_by_title(self, title: str) -> Application | None:
        return self.db.query(Application).filter(Application.title == title).first()
    
    def get_application_by_id(self, application_id: int) -> Application | None:
        return self.db.query(Application).filter(Application.id == application_id).first()

    def update_application(self, application: Application, update_data: dict) -> Application:
        for key, value in update_data.items():
            setattr(application, key, value)
        self.db.commit()
        self.db.refresh(application)
        return application

    def delete_application(self, application: Application):
        self.db.delete(application)
        self.db.commit()