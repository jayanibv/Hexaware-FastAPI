from pydantic import BaseModel


class JobCreate(BaseModel):

    title: str
    description: str
    salary: float
    company_id: int


class JobResponse(JobCreate):

    id: int

    class Config:
        from_attributes = True