from sqlalchemy.ext.asyncio import AsyncSession

from .dependencies import user_by_id
from core.models import db_helper

from fastapi import APIRouter
from fastapi import Depends

from .schemas import User

from . import crud



user_router = APIRouter(tags=['Users'])



@user_router.get('/', response_model=list[User])
async def get_users(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.get_users(session=session)



@user_router.get('/{user_id}', response_model=User)
async def get_user(
    user: User = Depends(user_by_id),
):
    return user