"""update user model

Revision ID: 28a34bbca858
Revises: fabd93e69c14
Create Date: 2024-06-06 15:07:10.381606

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "28a34bbca858"
down_revision: Union[str, None] = "fabd93e69c14"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint(
        None,
        "users",
        ["username"],
    )
    op.create_unique_constraint(
        None,
        "users",
        ["email"],
    )


def downgrade() -> None:
    op.drop_constraint(
        None,
        "users",
        type_="unique",
    )
    op.drop_constraint(
        None,
        "users",
        type_="unique",
    )
