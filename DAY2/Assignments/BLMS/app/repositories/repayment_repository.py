from app.models.repayment import Repayment

class RepaymentRepository:

    def create(self, db, data):

        obj = Repayment(**data.dict())

        db.add(obj)

        db.commit()

        db.refresh(obj)

        return obj