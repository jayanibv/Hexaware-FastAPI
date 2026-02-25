from fastapi import HTTPException
from app.schemas.loan_schema import LoanCreate

class LoanService:

    def __init__(self, repository):
        self.repository = repository

    def create_loan(self, loan_data: LoanCreate):

        if loan_data.amount > loan_data.annual_income * 10:
            raise HTTPException(
                status_code=400,
                detail="Loan amount cannot exceed 10 times annual income"
            )

        return self.repository.create_loan(loan_data)

    def get_loan_by_id(self, loan_id: int):
        loan = self.repository.get_loan_by_id(loan_id)

        if not loan:
            raise HTTPException(status_code=404, detail="Loan not found")

        return loan

    def update_loan_status(self, loan_id: int, new_status: str):

        loan = self.repository.get_loan_by_id(loan_id)

        if not loan:
            raise HTTPException(status_code=404, detail="Loan not found")

        if new_status == "APPROVED":

            if loan.status == "APPROVED":
                raise HTTPException(
                    status_code=400,
                    detail="Loan already approved"
                )

            if loan.status != "PENDING":
                raise HTTPException(
                    status_code=400,
                    detail="Only PENDING loans can be approved"
                )

        if loan.status == "APPROVED" and new_status == "PENDING":
            raise HTTPException(
                status_code=400,
                detail="Cannot revert approved loan to pending"
            )

        return self.repository.update_loan_status(loan_id, new_status)