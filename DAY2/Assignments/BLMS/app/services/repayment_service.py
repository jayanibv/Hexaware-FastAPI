from fastapi import HTTPException
from app.repositories.repayment_repository import RepaymentRepository
from app.repositories.application_repository import ApplicationRepository


class RepaymentService:

    def __init__(
        self,
        repayment_repo: RepaymentRepository,
        application_repo: ApplicationRepository,
    ):

        self.repayment_repo = repayment_repo
        self.application_repo = application_repo


    def create_repayment(self, db, data):

        application = self.application_repo.get(db, data.loan_application_id)

        if not application:
            raise HTTPException(404, "Loan application not found")

        return self.repayment_repo.create(db, data)