from typing import Annotated

from fastapi import Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.vacancies import crud
from src.core.models import Vacancy, db_helper
from src.utils.errors import NotFound


async def vacancy_by_id(
    vacancy_id: Annotated[int, Path],
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
) -> Vacancy:
    """
    Вспомогательная функция для
    получения Resume по id
    """
    vacancy = await crud.get_vacancy(
        session=session,
        vacancy_id=vacancy_id,
    )
    if vacancy is not None:
        return vacancy

    raise NotFound()
