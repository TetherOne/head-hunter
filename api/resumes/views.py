from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.resumes import crud
from api.resumes.dependencies import resume_by_id
from api.resumes.schemas import Resume, ResumeCreate
from core.models import db_helper

router = APIRouter(
    tags=["Resumes"],
)


@router.get(
    "/",
    response_model=list[Resume],
    status_code=status.HTTP_200_OK,
)
async def get_resumes(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    return await crud.get_resumes(
        session=session,
    )


@router.get(
    "/{resume_id}",
    response_model=Resume,
    status_code=status.HTTP_200_OK,
)
async def get_resume(
    resume: Resume = Depends(resume_by_id),
):
    return resume


@router.post(
    "/create/",
    response_model=ResumeCreate,
    status_code=status.HTTP_201_CREATED,
)
async def create_resume(
    resume_create: ResumeCreate,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    return await crud.create_resume(
        resume_create=resume_create,
        session=session,
    )
