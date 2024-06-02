from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.vacancies import crud
from api.vacancies.dependencies import vacancy_by_id
from api.vacancies.schemas import Vacancy, VacancyCreate, VacancyUpdate
from core.models import db_helper


router = APIRouter(
    tags=["Vacancies"],
)


@router.get(
    "/",
    response_model=list[Vacancy],
    status_code=status.HTTP_200_OK,
)
async def get_vacancies(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    return await crud.get_vacancies(
        session=session,
    )


@router.get(
    "/{contact_id}/",
    response_model=Vacancy,
    status_code=status.HTTP_200_OK,
)
async def get_contact(
    vacancy: Vacancy = Depends(vacancy_by_id),
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
    vacancy: Vacancy = Depends(vacancy_by_id),
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
    vacancy: Vacancy = Depends(vacancy_by_id),
) -> None:
    await crud.delete_contact(
        session=session,
        vacancy=vacancy,
    )
