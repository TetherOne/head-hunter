from datetime import datetime

from pydantic import BaseModel


class FavoriteBase(BaseModel):
    vacancy_id: int
    user_id: int


class FavoriteSchema(FavoriteBase):
    id: int
    created_at: datetime
    updated_at: datetime


class FavoriteCreate(FavoriteBase):
    pass
