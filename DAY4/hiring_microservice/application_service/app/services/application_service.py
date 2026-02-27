from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.application_repositories import ApplicationRepository
from app.schemas.application_schema import (
    ApplicationCreate,
    ApplicationUpdate,
    ApplicationResponse,
)

class ApplicationService:

    def __init__(self, db: Session):
        self.db = db
        self.application_repo = ApplicationRepository(db)

    # CREATE APPLICATION
    def create_application(self, payload: ApplicationCreate) -> ApplicationResponse:
        existing_application = self.application_repo.get_application_by_title(payload.title)
        if existing_application:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Application already registered"
            )
        application = self.application_repo.create_job(payload.model_dump())

        return ApplicationResponse.model_validate(application)

    # GET ALL APPLICATIONS
    def get_all_applications(self) -> list[ApplicationResponse]:
        applications = self.application_repo.get_all_applications()
        return [ApplicationResponse.model_validate(application) for application in applications]

    # GET APPLICATION BY ID
    def get_application_by_id(self, application_id: int) -> ApplicationResponse:
        application = self.application_repo.get_application_by_id(application_id)

        if not application:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Application not found"
            )

        return ApplicationResponse.model_validate(job)


    # UPDATE APPLICATION (BY ID)
    def update_application(self, application_id: int, payload: ApplicationUpdate) -> ApplicationResponse:
        application = self.application_repo.get_application_by_id(application_id)

        if not application:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Application not found"
            )

        update_data = payload.model_dump(exclude_unset=True)

        updated_application = self.application_repo.update_application(application, update_data)

        return ApplicationResponse.model_validate(updated_application)


    # DELETE APPLICATION (BY ID)
    def delete_application(self, application_id: int):
        application = self.application_repo.get_application_by_id(application_id)

        if not application:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Application not found"
            )

        self.application_repo.delete_application(application)

        return {"message": "Application deleted successfully"}