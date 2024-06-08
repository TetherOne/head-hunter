from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserSchema(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime


class UserRegister(UserBase):
    pass


class UserUpdate(UserRegister):
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str
