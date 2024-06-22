from typing import Annotated

from fastapi import Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.contacts import crud
from src.core.models import Contact, db_helper
from src.utils.errors import NotFound


async def contact_by_id(
    contact_id: Annotated[int, Path],
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
) -> Contact:
    """
    Вспомогательная функция для
    получения Contact по id
    """
    contact = await crud.get_contact(
        session=session,
        contact_id=contact_id,
    )
    if contact is not None:
        return contact

    raise NotFound()
