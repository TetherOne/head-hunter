from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.resumes import crud
from api.resumes.schemas import Resume
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
