from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.vacancies.schemas import VacancyCreate, VacancyUpdate, VacancySchema
from core.models import Vacancy


async def get_vacancies(
    session: AsyncSession,
    skip: int = 0,
    limit: int = 10,
) -> Sequence[Vacancy]:
    stmt = (
        select(Vacancy)
        .order_by(
            Vacancy.created_at.desc(),
        )
        .offset(skip)
        .limit(limit)
    )
    result = await session.execute(stmt)
    return result.scalars().all()


async def get_vacancy(
    vacancy_id: int,
    session: AsyncSession,
) -> Vacancy | None:
    return await session.get(Vacancy, vacancy_id)


async def create_vacancy(
    vacancy_create: VacancyCreate,
    session: AsyncSession,
):
    vacancy = Vacancy(**vacancy_create.dict())
    session.add(vacancy)
    await session.commit()
    await session.refresh(vacancy)
    return vacancy


async def update_vacancy(
    vacancy: VacancySchema,
    vacancy_update: VacancyUpdate,
    session: AsyncSession,
):
    for name, value in vacancy_update.dict(
        exclude_unset=True,
    ).items():
        setattr(vacancy, name, value)
    await session.commit()
    await session.refresh(vacancy)
    return vacancy


async def delete_contact(
    vacancy: VacancySchema,
    session: AsyncSession,
):
    await session.delete(vacancy)
    await session.commit()
