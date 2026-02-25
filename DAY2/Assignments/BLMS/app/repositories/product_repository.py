from app.models.loan_product import LoanProduct

class ProductRepository:

    def create(self, db, data):

        obj = LoanProduct(**data.dict())

        db.add(obj)

        db.commit()

        db.refresh(obj)

        return obj


    def get(self, db, id):

        return db.query(LoanProduct).filter_by(id=id).first()


    def get_all(self, db, skip, limit):

        return db.query(LoanProduct).offset(skip).limit(limit).all()