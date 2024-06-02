from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.vacancies import crud
from core.models import Vacancy, db_helper


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

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Vacancy {vacancy_id} not found.",
    )
