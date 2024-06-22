from typing import Annotated

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.models.cache_helper import AsyncRedisCache
from src.api.vacancies import crud
from src.api.vacancies.dependencies import vacancy_by_id
from src.api.vacancies.schemas import VacancyCreate, VacancySchema, VacancyUpdate
from src.core.models import db_helper

router = APIRouter(
    tags=["Vacancies"],
)
cache = AsyncRedisCache()


@router.get(
    "/",
    response_model=list[VacancySchema],
    status_code=status.HTTP_200_OK,
)
async def get_vacancies(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    skip: int = Query(
        0,
        description="Skip vacancies",
    ),
    limit: int = Query(
        2,
        description="Limit the number of vacancies",
    ),
):
    cache_key = f"vacancies:{skip}:{limit}"
    cached_vacancies = await cache.get(cache_key)

    if cached_vacancies:
        print("From cache")
        return cached_vacancies

    vacancies = await crud.get_vacancies(session, skip, limit)
    vacancies_data = [VacancySchema.from_orm(vacancy).dict() for vacancy in vacancies]
    await cache.set(cache_key, vacancies_data)
    print("From db")
    return vacancies_data


@router.get(
    "/{contact_id}/",
    response_model=VacancySchema,
    status_code=status.HTTP_200_OK,
)
async def get_vacancy(
    vacancy: VacancySchema = Depends(vacancy_by_id),
):
    return vacancy


@router.post(
    "/create/",
    response_model=VacancyCreate,
    status_code=status.HTTP_201_CREATED,
)
async def create_vacancy(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    vacancy_create: VacancyCreate,
):
    return await crud.create_vacancy(
        vacancy_create=vacancy_create,
        session=session,
    )


@router.patch(
    "/update/{contact_id}/",
    status_code=status.HTTP_201_CREATED,
)
async def update_vacancy(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    vacancy_update: VacancyUpdate,
    vacancy: VacancySchema = Depends(vacancy_by_id),
):
    return await crud.update_vacancy(
        session=session,
        vacancy=vacancy,
        vacancy_update=vacancy_update,
    )


@router.delete(
    "/delete/{resume_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_contact(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    vacancy: VacancySchema = Depends(vacancy_by_id),
) -> None:
    await crud.delete_contact(
        session=session,
        vacancy=vacancy,
    )
