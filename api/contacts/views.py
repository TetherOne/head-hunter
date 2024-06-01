from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.contacts import crud
from api.contacts.dependencies import contact_by_id
from api.contacts.schemas import Contact, ContactCreate, ContactUpdate
from core.models import db_helper

router = APIRouter(
    tags=["Resume contacts"],
)


@router.get(
    "/",
    response_model=list[Contact],
    status_code=status.HTTP_200_OK,
)
async def get_contacts(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    return await crud.get_contacts(
        session=session,
    )


@router.get(
    "/{contact_id}/",
    response_model=Contact,
    status_code=status.HTTP_200_OK,
)
async def get_contact(
    contact: Contact = Depends(contact_by_id),
):
    return contact


@router.post(
    "/create/",
    response_model=ContactCreate,
    status_code=status.HTTP_201_CREATED,
)
async def create_contact(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    contact_create: ContactCreate,
):
    return await crud.create_contact(
        contact_create=contact_create,
        session=session,
    )


@router.patch(
    "/update/{contact_id}/",
    status_code=status.HTTP_201_CREATED,
)
async def update_contact(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    contact_update: ContactUpdate,
    contact: Contact = Depends(contact_by_id),
):
    return await crud.update_contact(
        session=session,
        contact=contact,
        contact_update=contact_update,
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
    contact: Contact = Depends(contact_by_id),
) -> None:
    await crud.delete_contact(
        session=session,
        contact=contact,
    )
