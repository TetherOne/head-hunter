from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from api.users.schemas import UserRegister, UserLogin
from api.users.utils import hash_password
from core.models import User


async def register_user(
    user_register: UserRegister,
    session: AsyncSession,
) -> User:
    password = user_register.password
    hashed_password = hash_password(password)
    user = User(
        username=user_register.username,
        email=user_register.email,
        password=hashed_password,
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def get_user_by_email(
    login_form: UserLogin,
    session: AsyncSession,
) -> User:
    result = await session.execute(select(User).filter(User.email == login_form.email))
    user = result.scalars().first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user
