from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.application_schema import (
    ApplicationCreate,
    ApplicationResponse,
    ApplicationStatusUpdate,
)

from app.repositories.application_repository import ApplicationRepository
from app.repositories.product_repository import ProductRepository

from app.services.application_service import ApplicationService

from app.core.database import get_db

router = APIRouter(prefix="/applications", tags=["Loan Applications"])


application_repo = ApplicationRepository()
product_repo = ProductRepository()

service = ApplicationService(application_repo, product_repo)


@router.post("", response_model=ApplicationResponse)
def create_application(
    data: ApplicationCreate,
    db: Session = Depends(get_db),
):
    return service.create(db, data)


@router.put("/{application_id}", response_model=ApplicationResponse)
def update_application_status(
    application_id: int,
    data: ApplicationStatusUpdate,
    db: Session = Depends(get_db),
):
    return service.update_status(
        db,
        application_id,
        data.status,
        data.approved_amount,
    )