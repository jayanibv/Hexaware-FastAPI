from app.models.application import Application


class ApplicationRepository:

    def create_application(self, db, data):

        app = Application(**data.dict())

        db.add(app)
        db.commit()
        db.refresh(app)

        return app


    def get_application(self, db, id):

        return db.query(Application).filter(
            Application.id == id
        ).first()