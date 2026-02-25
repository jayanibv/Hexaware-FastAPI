from fastapi import HTTPException
from app.repositories.job_repository import JobRepository


class JobService:

    def __init__(self):
        self.repo = JobRepository()


    def create_job(self, db, data):

        return self.repo.create_job(db, data)


    def get_job(self, db, id):

        job = self.repo.get_job(db, id)

        if not job:
            raise HTTPException(404, "Job not found")

        return job


    def get_jobs(self, db, skip, limit):

        return self.repo.get_all_jobs(db, skip, limit)