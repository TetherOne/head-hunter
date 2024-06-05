from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, mapped_column

from core.models import Base


class Favorite(Base):
    vacancy_id = mapped_column(
        ForeignKey("vacancies.id"),
    )
    user_id = mapped_column(
        ForeignKey("users.id"),
    )

    vacancy = relationship(
        "Vacancy",
        back_populates="favorites",
    )
    user = relationship(
        "User",
        back_populates="favorites",
    )

    __table_args__ = (
        UniqueConstraint(
            "vacancy_id",
            "user_id",
        ),
    )
