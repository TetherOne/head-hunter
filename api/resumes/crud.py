from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Sequence

from api.resumes.schemas import ResumeCreate
from core.models import Resume


async def get_resumes(
    session: AsyncSession,
) -> Sequence[Resume]:
    stmt = select(Resume).order_by(Resume.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_resume(
    resume_id: int,
    session: AsyncSession,
) -> Resume | None:
    return await session.get(Resume, resume_id)


async def create_resume(
    resume_create: ResumeCreate,
    session: AsyncSession,
) -> Resume:
    resume = Resume(**resume_create.model_dump())
    session.add(resume)
    await session.commit()
    await session.refresh(resume)
    return resume
