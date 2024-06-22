from typing import Annotated

from fastapi import Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.resumes import crud
from src.core.models import Resume, db_helper
from utils.errors import NotFound


async def resume_by_id(
    resume_id: Annotated[int, Path],
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
) -> Resume:
    """
    Вспомогательная функция для
    получения Resume по id
    """
    resume = await crud.get_resume(
        session=session,
        resume_id=resume_id,
    )
    if resume is not None:
        return resume

    raise NotFound()
