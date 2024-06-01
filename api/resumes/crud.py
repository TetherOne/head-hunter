import os
import aiofiles
from typing import Sequence, Optional

from fastapi import UploadFile
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.resumes.schemas import ResumeCreate, ResumeUpdate
from core.config import settings
from core.models import Resume


async def get_resumes(
    session: AsyncSession,
) -> Sequence[Resume]:
    stmt = select(Resume).order_by(Resume.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_resume(
    session: AsyncSession,
    resume_id: int,
) -> Resume | None:
    return await session.get(Resume, resume_id)


async def image_upload(
    file: UploadFile,
) -> Optional[str]:
    if not file:
        return None

    upload_directory = settings.dir_save.resumes
    if not os.path.exists(upload_directory):
        os.makedirs(upload_directory)

    file_location = os.path.join(
        upload_directory,
        file.filename,
    )
    async with aiofiles.open(
        file_location,
        "wb+",
    ) as file_object:
        await file_object.write(await file.read())

    return file_location


async def create_resume(
    session: AsyncSession,
    resume_create: ResumeCreate,
    image: Optional[str],
) -> Resume:
    resume = Resume(
        **resume_create.dict(),
        image=image,
    )
    session.add(resume)
    await session.commit()
    await session.refresh(resume)
    return resume


async def update_resume(
    session: AsyncSession,
    resume: Resume,
    resume_update: ResumeUpdate,
):
    for name, value in resume_update.model_dump(
        exclude_unset=True,
    ).items():
        setattr(resume, name, value)
    await session.commit()
    await session.refresh(resume)
    return resume


async def delete_resume(
    session: AsyncSession,
    resume: Resume,
) -> None:
    await session.delete(resume)
    await session.commit()
