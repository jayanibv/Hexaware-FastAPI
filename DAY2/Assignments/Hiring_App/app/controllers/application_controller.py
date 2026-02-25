from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.application_schema import ApplicationCreate, ApplicationResponse
from app.services.application_service import ApplicationService
from app.core.database import get_db

router = APIRouter(prefix="/applications", tags=["Applications"])

service = ApplicationService()


@router.post("", response_model=ApplicationResponse)
def apply(data: ApplicationCreate, db: Session = Depends(get_db)):

    return service.apply_job(db, data)