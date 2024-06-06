from typing import Optional, Sequence

from fastapi import UploadFile
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.resumes.schemas import ResumeCreate, ResumeUpdate
from core.models import Resume
from core.s3_service.client import s3_client


async def get_resumes(
    session: AsyncSession,
    skip: int,
    limit: int,
) -> Sequence[Resume]:
    stmt = (
        select(Resume)
        .order_by(
            Resume.created_at.desc(),
        )
        .offset(skip)
        .limit(limit)
    )
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

    object_name = file.filename
    async with s3_client.get_client() as client:
        await client.put_object(
            Bucket=s3_client.bucket_name,
            Key=object_name,
            Body=await file.read(),
        )
    return object_name


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
