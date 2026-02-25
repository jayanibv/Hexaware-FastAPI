from fastapi import APIRouter, Depends
from app.schemas.enrollment_schema import EnrollmentCreate
from app.dependencies.dependencies import get_enrollment_service
from app.services.enrollment_service import EnrollmentService

router = APIRouter()

@router.post("/enrollments", status_code=201)
def enroll(enrollment: EnrollmentCreate,
           service: EnrollmentService = Depends(get_enrollment_service)):
    return service.enroll(enrollment)

@router.get("/enrollments")
def get_enrollments(service: EnrollmentService = Depends(get_enrollment_service)):
    return service.get_all_enrollments()