from fastapi import HTTPException
from app.repositories.application_repository import ApplicationRepository
from app.repositories.job_repository import JobRepository


class ApplicationService:

    def __init__(self):

        self.repo = ApplicationRepository()

        self.job_repo = JobRepository()


    def apply_job(self, db, data):

        job = self.job_repo.get_job(db, data.job_id)

        if not job:
            raise HTTPException(404, "Job not found")

        return self.repo.create_application(db, data)