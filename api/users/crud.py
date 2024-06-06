from sqlalchemy.ext.asyncio import AsyncSession

from api.users.schemas import UserRegister
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
