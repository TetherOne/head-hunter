from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.users import crud
from api.users.crud import get_user_by_email
from api.users.schemas import UserRegister, UserSchema, UserLogin
from api.users.utils import generate_token, validate_password
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
    user = await get_user_by_email(
        session=session,
        email=user_login.email,
    )
    if user:
        if not validate_password(
            user_login.password,
            user.password,
        ):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid credentials",
            )
        else:
            user.token = generate_token()
            await session.commit()
            return {
                "bearer": user.token,
            }
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid credentials",
        )
