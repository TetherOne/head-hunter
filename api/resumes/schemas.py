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


class ResumeUpdate(ResumeCreate):
    job_tittle: str | None = None
    description: str | None = None
    salary: int | None = None
