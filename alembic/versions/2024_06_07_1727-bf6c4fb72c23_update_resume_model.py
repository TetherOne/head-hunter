"""update resume model

Revision ID: bf6c4fb72c23
Revises: 28a34bbca858
Create Date: 2024-06-07 17:27:44.029515

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bf6c4fb72c23"
down_revision: Union[str, None] = "28a34bbca858"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("resumes", sa.Column("tittle", sa.String(), nullable=False))
    op.drop_column("resumes", "job_tittle")


def downgrade() -> None:
    op.add_column(
        "resumes",
        sa.Column("job_tittle", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.drop_column("resumes", "tittle")
