from fastapi import APIRouter, Depends
from app.schemas.student_schema import StudentCreate
from app.dependencies.dependencies import get_student_service
from app.services.student_service import StudentService

router = APIRouter()

@router.post("/students", status_code=201)
def create_student(student: StudentCreate,
                   service: StudentService = Depends(get_student_service)):
    return service.create_student(student)

@router.get("/students/{student_id}")
def get_student(student_id: int,
                service: StudentService = Depends(get_student_service)):
    return service.get_student(student_id)