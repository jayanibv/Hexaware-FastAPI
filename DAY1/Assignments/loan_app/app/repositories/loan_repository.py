from app.models.loan_model import Loan
from app.models.loan_db import loan_db

class LoanRepository:
    def create_loan(self, loan_data):
        new_id = len(loan_db) + 1
        loan = Loan(new_id, loan_data.name, loan_data.email, loan_data.amount, loan_data.annual_income, loan_data.interest_rate, loan_data.duration)
        loan_db.append(loan)
        return loan

    def get_loan_by_id(self, loan_id: int):
        for loan in loan_db:
            if loan.id == loan_id:
                return loan
        return None
    
    def update_loan_status(self, loan_id: int, status: str):
        for loan in loan_db:
            if loan.id == loan_id:
                loan.status = status
                return loan
        return None
