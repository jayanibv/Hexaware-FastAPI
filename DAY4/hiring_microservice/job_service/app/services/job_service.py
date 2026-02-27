from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.job_repositories import JobRepository
from app.schemas.job_schema import (
    JobCreate,
    JobUpdate,
    JobResponse,
)

class JobService:

    def __init__(self, db: Session):
        self.db = db
        self.job_repo = JobRepository(db)

    # CREATE JOB
    def create_job(self, payload: JobCreate) -> JobResponse:
        existing_job = self.job_repo.get_job_by_title(payload.title)
        if existing_job:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Job already registered"
            )
        job = self.job_repo.create_job(payload.model_dump())

        return JobResponse.model_validate(job)

    # GET ALL JOBS
    def get_all_jobs(self) -> list[JobResponse]:
        jobs = self.job_repo.get_all_jobs()
        return [JobResponse.model_validate(job) for job in jobs]

    # GET JOB BY ID
    def get_job_by_id(self, job_id: int) -> JobResponse:
        job = self.job_repo.get_job_by_id(job_id)

        if not job:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Job not found"
            )

        return JobResponse.model_validate(job)


    # UPDATE JOB (BY ID)
    def update_job(self, job_id: int, payload: JobUpdate) -> JobResponse:
        job = self.job_repo.get_job_by_id(job_id)

        if not job:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Job not found"
            )

        update_data = payload.model_dump(exclude_unset=True)

        updated_job = self.job_repo.update_job(job, update_data)

        return JobResponse.model_validate(updated_job)


    # DELETE JOB (BY ID)
    def delete_job(self, job_id: int):
        job = self.job_repo.get_job_by_id(job_id)

        if not job:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Job not found"
            )

        self.job_repo.delete_job(job)

        return {"message": "Job deleted successfully"}