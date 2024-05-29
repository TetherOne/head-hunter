from sqlalchemy.orm import Mapped

from core.models.base import Base


class Resume(Base):
    job_tittle: Mapped[str]
    description: Mapped[str]
    salary: Mapped[int]
