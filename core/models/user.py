from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base


class User(Base):
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str]
    password: Mapped[str]
    favorites = relationship(
        "Favorite",
        back_populates="vacancy",
    )
