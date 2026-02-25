from fastapi import APIRouter, Depends
from app.services.loan_service import LoanService
from app.dependencies.loan_dependency import get_loan_service
from app.schemas.loan_schema import LoanCreate, LoanResponse, LoanStatusUpdate

router = APIRouter()

@router.post("/loans", response_model=LoanResponse)
async def create_loan(loan_data: LoanCreate, loan_service: LoanService = Depends(get_loan_service)):
    return loan_service.create_loan(loan_data)

@router.get("/loans/{loan_id}", response_model=LoanResponse)
async def get_loan_by_id(loan_id: int, loan_service: LoanService = Depends(get_loan_service)):
    return loan_service.get_loan_by_id(loan_id)

@router.put("/loans/{loan_id}", response_model=LoanResponse)
async def update_loan_status(loan_id: int, loan_status: LoanStatusUpdate, loan_service: LoanService = Depends(get_loan_service)):
    return loan_service.update_loan_status(loan_id, loan_status.status)
