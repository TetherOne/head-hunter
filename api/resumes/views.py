from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    status,
    UploadFile,
    File,
)
from sqlalchemy.ext.asyncio import AsyncSession

from api.resumes import crud
from api.resumes.dependencies import resume_by_id
from api.resumes.schemas import Resume, ResumeCreate, ResumeUpdate
from core.models import db_helper
from core.s3_service.client import s3_client


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
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    resume_create: ResumeCreate = Depends(),
    file: UploadFile = File(None),
):
    image = await crud.image_upload(file)
    return await crud.create_resume(
        session=session,
        resume_create=resume_create,
        image=image,
    )


@router.patch(
    "/update/{resume_id}/",
    status_code=status.HTTP_201_CREATED,
)
async def update_qrcode(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    resume_update: ResumeUpdate,
    resume: Resume = Depends(resume_by_id),
):
    return await crud.update_resume(
        session=session,
        resume=resume,
        resume_update=resume_update,
    )


@router.delete(
    "/delete/{resume_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_resume(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    resume: Resume = Depends(resume_by_id),
) -> None:
    await crud.delete_resume(
        session=session,
        resume=resume,
    )


@router.get(
    "/image/{object_name}/{destination_path}",
    status_code=status.HTTP_200_OK,
)
async def get_image_view(
    object_name: str,
    destination_path: str,
):
    await s3_client.get_file(
        object_name,
        destination_path,
    )


@router.delete(
    "/delete/{image_name}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_resume_image(
    object_name: str,
) -> None:
    await s3_client.delete_file(
        object_name,
    )
