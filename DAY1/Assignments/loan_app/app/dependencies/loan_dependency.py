from app.services.loan_service import LoanService
from app.repositories.loan_repository import LoanRepository

loan_repo = LoanRepository()

def get_loan_service():
    return LoanService(loan_repo)

def get_loan_repository():
    return loan_repo