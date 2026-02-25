from app.models.loan_application import LoanApplication

class ApplicationRepository:

    def create(self, db, data):

        obj = LoanApplication(**data.dict())

        db.add(obj)

        db.commit()

        db.refresh(obj)

        return obj


    def get(self, db, id):

        return db.query(LoanApplication).filter_by(id=id).first()


    def update(self, db, obj):

        db.commit()

        db.refresh(obj)

        return obj