from datetime import datetime

from pydantic import BaseModel, EmailStr


class ContactBase(BaseModel):
    phone: str | None = None
    email: EmailStr | None = None
    telegram: str | None = None
    linkedin: str | None = None
    github: str | None = None
    gitlab: str | None = None


class Contact(ContactBase):
    id: int
    created_at: datetime
    updated_at: datetime


class ContactCreate(ContactBase):
    resume_id: int


class ContactUpdate(ContactBase):
    pass
