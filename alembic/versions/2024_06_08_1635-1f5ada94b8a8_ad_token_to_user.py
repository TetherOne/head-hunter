"""ad token to user

Revision ID: 1f5ada94b8a8
Revises: bf6c4fb72c23
Create Date: 2024-06-08 16:35:00.208603

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1f5ada94b8a8"
down_revision: Union[str, None] = "bf6c4fb72c23"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "token",
            sa.String(),
            nullable=False,
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    op.drop_column(
        "users",
        "token",
    )
