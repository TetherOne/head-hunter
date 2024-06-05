from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.favorites.schemas import FavoriteCreate
from core.models import Favorite


async def get_favorites(
    session: AsyncSession,
) -> Sequence[Favorite]:
    stmt = select(Favorite).order_by(
        Favorite.id,
    )
    result = await session.scalars(stmt)
    return result.all()


async def get_favorite(
    session: AsyncSession,
    favorite_id: int,
) -> Favorite | None:
    return await session.get(Favorite, favorite_id)


async def create_favorite(
    session: AsyncSession,
    favorite_create: FavoriteCreate,
) -> Favorite:
    favorite = Favorite(
        **favorite_create.dict(),
    )
    session.add(favorite)
    await session.commit()
    return favorite


async def delete_favorite(
    session: AsyncSession,
    favorite: Favorite,
) -> None:
    await session.delete(favorite)
    await session.commit()
