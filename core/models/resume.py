from typing import Optional

from sqlalchemy.orm import Mapped

from core.models.base import Base


class Resume(Base):
    image: Mapped[Optional[str]]
    job_tittle: Mapped[str]
    description: Mapped[str]
    salary: Mapped[int]
