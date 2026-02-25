from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.job_schema import JobCreate, JobResponse
from app.services.job_service import JobService
from app.core.database import get_db

router = APIRouter(prefix="/jobs", tags=["Jobs"])

service = JobService()


@router.post("", response_model=JobResponse)
def create_job(data: JobCreate, db: Session = Depends(get_db)):

    return service.create_job(db, data)


@router.get("/{id}", response_model=JobResponse)
def get_job(id: int, db: Session = Depends(get_db)):

    return service.get_job(db, id)


@router.get("", response_model=list[JobResponse])
def get_jobs(db: Session = Depends(get_db)):

    return service.get_jobs(db)