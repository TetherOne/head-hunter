"""update favorite table

Revision ID: fabd93e69c14
Revises: 208d2947c02b
Create Date: 2024-06-06 00:04:42.032471

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "fabd93e69c14"
down_revision: Union[str, None] = "208d2947c02b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "favorites",
        "vacancy_id",
        existing_type=sa.INTEGER(),
        nullable=True,
    )
    op.alter_column(
        "favorites",
        "user_id",
        existing_type=sa.INTEGER(),
        nullable=True,
    )


def downgrade() -> None:
    op.alter_column(
        "favorites",
        "user_id",
        existing_type=sa.INTEGER(),
        nullable=False,
    )
    op.alter_column(
        "favorites",
        "vacancy_id",
        existing_type=sa.INTEGER(),
        nullable=False,
    )
