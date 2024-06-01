from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base

if TYPE_CHECKING:
    from core.models.resume import Resume


class Contact(Base):
    phone: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=True)
    telegram: Mapped[str] = mapped_column(nullable=True)
    linkedin: Mapped[str] = mapped_column(nullable=True)
    github: Mapped[str] = mapped_column(nullable=True)
    gitlab: Mapped[str] = mapped_column(nullable=True)
    resume_id: Mapped[int] = mapped_column(
        ForeignKey("resumes.id"),
    )
    resume: Mapped["Resume"] = relationship(
        back_populates="contact",
    )

    __table_args__ = (UniqueConstraint("resume_id"),)
