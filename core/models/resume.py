from typing import TYPE_CHECKING, Optional

from sqlalchemy.orm import Mapped, relationship

from core.models.base import Base

if TYPE_CHECKING:
    from core.models.contacts import Contact


class Resume(Base):
    image: Mapped[Optional[str]]
    job_tittle: Mapped[str]
    description: Mapped[str]
    salary: Mapped[int]
    contact: Mapped["Contact"] = relationship(
        back_populates="resume",
        uselist=False,
        cascade="all, delete-orphan",
    )
