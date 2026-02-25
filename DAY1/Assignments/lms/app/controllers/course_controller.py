from fastapi import APIRouter, Depends
from app.schemas.course_schema import CourseCreate
from app.dependencies.dependencies import get_course_service
from app.services.course_service import CourseService

router = APIRouter()

@router.post("/courses", status_code=201)
def create_course(course: CourseCreate,
                  service: CourseService = Depends(get_course_service)):
    return service.create_course(course)

@router.get("/courses")
def get_courses(service: CourseService = Depends(get_course_service)):
    return service.get_all_courses()

@router.get("/courses/{course_id}")
def get_course(course_id: int,
               service: CourseService = Depends(get_course_service)):
    return service.get_course(course_id)