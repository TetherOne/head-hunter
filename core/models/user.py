from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base


class User(Base):
    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
    )
    email: Mapped[str] = mapped_column(
        unique=True,
    )
    password: Mapped[str]
    token: Mapped[str | None]
    favorites = relationship(
        "Favorite",
        back_populates="user",
    )
