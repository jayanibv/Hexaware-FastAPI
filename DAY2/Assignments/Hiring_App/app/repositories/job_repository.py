from app.models.job import Job
from sqlalchemy.orm import Session

class JobRepository:

    def create_job(self, db: Session, data):

        job = Job(**data.dict())

        db.add(job)
        db.commit()
        db.refresh(job)

        return job


    def get_job(self, db, job_id):

        return db.query(Job).filter(Job.id == job_id).first()


    def get_all_jobs(self, db):

        return db.query(Job).all()