from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserBase(UserSchema):
    id: int
    created_at: datetime
    updated_at: datetime


class UserRegister(UserSchema):
    pass


class UserUpdate(UserRegister):
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None
