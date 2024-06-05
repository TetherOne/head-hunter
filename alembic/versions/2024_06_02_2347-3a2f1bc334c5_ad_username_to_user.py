"""ad username to user

Revision ID: 3a2f1bc334c5
Revises: 89615bad87f9
Create Date: 2024-06-02 23:47:27.197767

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "3a2f1bc334c5"
down_revision: Union[str, None] = "89615bad87f9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "username",
            sa.String(length=50),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_column(
        "users",
        "username",
    )
