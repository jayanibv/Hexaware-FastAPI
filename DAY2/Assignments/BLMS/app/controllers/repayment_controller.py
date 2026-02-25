from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.repayment_schema import (
    RepaymentCreate,
    RepaymentResponse,
)

from app.repositories.repayment_repository import RepaymentRepository
from app.repositories.application_repository import ApplicationRepository

from app.services.repayment_service import RepaymentService

from app.core.database import get_db

router = APIRouter(prefix="/repayments", tags=["Repayments"])


repayment_repo = RepaymentRepository()
application_repo = ApplicationRepository()

service = RepaymentService(
    repayment_repo,
    application_repo
)


@router.post("", response_model=RepaymentResponse)
def create_repayment(
    data: RepaymentCreate,
    db: Session = Depends(get_db),
):
    return service.create_repayment(db, data)