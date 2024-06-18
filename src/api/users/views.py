from typing import Annotated

import bcrypt
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.users import crud
from src.api.users.crud import get_user_by_email
from src.api.users.schemas import UserRegister, UserSchema, UserLogin
from src.api.users.utils import check_password
from src.core.models import db_helper

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


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8"),
    )


@router.post(
    "/login/",
    status_code=status.HTTP_201_CREATED,
)
async def authenticate_user(
    login_form: UserLogin,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    credentials: HTTPBasicCredentials = Depends(security),
):
    user = await get_user_by_email(login_form, session)

    await check_password(login_form, user)

    if credentials.username != user.email or not verify_password(
        credentials.password,
        user.password,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    return {"detail": "Login successful"}
