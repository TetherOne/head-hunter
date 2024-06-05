from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import relationship

from core.models import Base


class Favorite(Base):
    vacancy_id = Column(
        Integer,
        ForeignKey("vacancies.id"),
        primary_key=True,
    )
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        primary_key=True,
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
