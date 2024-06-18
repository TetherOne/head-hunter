from datetime import datetime

from pydantic import BaseModel


class VacancyBase(BaseModel):
    job_tittle: str
    description: str
    experience: str
    salary: int
    address: str | None = None
    phone: str | None = None
    email: str | None = None


class VacancySchema(VacancyBase):
    id: int
    created_at: datetime
    updated_at: datetime


class VacancyCreate(VacancyBase):
    pass


class VacancyUpdate(VacancyBase):
    job_tittle: str | None = None
    description: str | None = None
    experience: str | None = None
    salary: int | None = None
    address: str | None = None
    phone: str | None = None
    email: str | None = None
