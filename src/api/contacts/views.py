from typing import Annotated

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.contacts import crud
from src.api.contacts.dependencies import contact_by_id
from src.api.contacts.schemas import ContactCreate, ContactSchema, ContactUpdate
from src.core.models import db_helper

router = APIRouter(
    tags=["Resume contacts"],
)


@router.get(
    "/",
    response_model=list[ContactSchema],
    status_code=status.HTTP_200_OK,
)
async def get_contacts(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    resume_id: int = Query(None, description="Filter contacts by resume_id"),
    skip: int = Query(0, description="Skip contacts"),
    limit: int = Query(2, description="Limit the number of contact"),
):
    return await crud.get_contacts(
        session=session,
        resume_id=resume_id,
        skip=skip,
        limit=limit,
    )


@router.get(
    "/{contact_id}/",
    response_model=ContactSchema,
    status_code=status.HTTP_200_OK,
)
async def get_contact(
    contact: ContactSchema = Depends(contact_by_id),
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
    contact: ContactSchema = Depends(contact_by_id),
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
    contact: ContactSchema = Depends(contact_by_id),
) -> None:
    await crud.delete_contact(
        session=session,
        contact=contact,
    )
