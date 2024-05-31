from datetime import datetime

from pydantic import BaseModel


class ResumeBase(BaseModel):
    job_tittle: str
    description: str
    salary: int


class Resume(ResumeBase):
    id: int
    created_at: datetime
    updated_at: datetime


class ResumeCreate(ResumeBase):
    pass
