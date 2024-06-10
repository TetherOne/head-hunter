from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from api.users import crud
from api.users.schemas import UserRegister, UserSchema
from core.models import db_helper

router = APIRouter(tags=["Users"])
security = HTTPBasic()


@router.post(
    "/register/",
    response_model=UserSchema,
    status_code=status.HTTP_201_CREATED,
)
async def register_user(
    user_register: UserRegister,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    return await crud.register_user(
        user_register=user_register,
        session=session,
    )


@router.get(
    "/basic-auth/",
)
async def basic_auth(
    credentials: Annotated[
        HTTPBasicCredentials,
        Depends(security),
    ],
):
    return {
        "username": credentials.username,
        "password": credentials.password,
    }
