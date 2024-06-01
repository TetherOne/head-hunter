from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.contacts.schemas import ContactCreate, ContactUpdate
from core.models import Contact


async def get_contacts(
    session: AsyncSession,
) -> Sequence[Contact]:
    stmt = select(Contact).order_by(Contact.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_contact(
    contact_id: int,
    session: AsyncSession,
) -> Contact | None:
    return await session.get(Contact, contact_id)


async def create_contact(
    contact_create: ContactCreate,
    session: AsyncSession,
):
    contact = Contact(**contact_create.dict())
    session.add(contact)
    await session.commit()
    await session.refresh(contact)
    return contact


async def update_contact(
    contact: Contact,
    contact_update: ContactUpdate,
    session: AsyncSession,
):
    for name, value in contact_update.dict(
        exclude_unset=True,
    ).items():
        setattr(contact, name, value)
    await session.commit()
    await session.refresh(contact)
    return contact


async def delete_contact(
    contact: Contact,
    session: AsyncSession,
):
    await session.delete(contact)
    await session.commit()
