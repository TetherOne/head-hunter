from typing import Annotated, Optional

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.favorites import crud
from src.api.favorites.dependencies import favorite_by_id
from src.api.favorites.schemas import FavoriteCreate, FavoriteSchema
from src.core.models import Favorite, db_helper

router = APIRouter(
    tags=["Favorites"],
)


@router.get(
    "/",
    response_model=list[FavoriteSchema],
    status_code=status.HTTP_200_OK,
)
async def get_favorites(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    user_id: Optional[int] = None,
    vacancy_id: Optional[int] = None,
):
    return await crud.get_favorites(
        session=session,
        user_id=user_id,
        vacancy_id=vacancy_id,
    )


@router.post(
    "/create/",
    response_model=FavoriteCreate,
    status_code=status.HTTP_201_CREATED,
)
async def create_favorite(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    favorite_create: FavoriteCreate,
):
    return await crud.create_favorite(
        session=session,
        favorite_create=favorite_create,
    )


@router.delete(
    "/delete/{favorite_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_favorite(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    favorite: Favorite = Depends(favorite_by_id),
) -> None:
    await crud.delete_favorite(
        session=session,
        favorite=favorite,
    )
