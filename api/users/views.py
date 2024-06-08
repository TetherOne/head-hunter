from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.users import crud
from api.users.crud import get_user_by_email
from api.users.schemas import UserRegister, UserSchema, UserLogin
from core.models import db_helper

router = APIRouter(tags=["Users"])


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


@router.post(
    "/login/",
)
async def auth_token(
    user_login: UserLogin,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    pass


@router.get("/{email}")
async def read_user(
    email: str,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    return await get_user_by_email(email=email, session=session)
