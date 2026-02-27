from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.services.application_service import ApplicationService
from app.schemas.application_schema import ApplicationCreate, ApplicationUpdate, ApplicationResponse

router = APIRouter(prefix="/applications", tags=["Applications"])

# Dependency to get the ApplicationService with the DB session
def get_application_service(db: Session = Depends(get_db)):
    return ApplicationService(db)

@router.post("/register", response_model=ApplicationResponse)
def create_application(
    payload: ApplicationCreate,
    application_service: ApplicationService = Depends(get_application_service)
):
    return application_service.create_application(payload)

@router.get("/all", response_model=list[ApplicationResponse])
def get_all_applications(
    application_service: ApplicationService = Depends(get_application_service)
):
    return application_service.get_all_applications()

@router.get("/{application_id}", response_model=ApplicationResponse)
def get_application(
    application_id: int,
    application_service: ApplicationService = Depends(get_application_service)
):
    return application_service.get_application_by_id(application_id)

@router.put("/{application_id}", response_model=ApplicationResponse)
def update_application(
    application_id: int,
    payload: ApplicationUpdate,
    application_service: ApplicationService = Depends(get_application_service)
):
    return application_service.update_application(application_id, payload)

@router.delete("/{application_id}")
def delete_application(
    application_id: int,
    application_service: ApplicationService = Depends(get_application_service)
):
    application_service.delete_application(application_id)
    return {"message": "Application deleted successfully"}