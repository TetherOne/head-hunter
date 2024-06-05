"""ad uniq

Revision ID: 208d2947c02b
Revises: 1353e97507fd
Create Date: 2024-06-05 17:11:10.857306

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "208d2947c02b"
down_revision: Union[str, None] = "1353e97507fd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint(
        None,
        "favorites",
        ["vacancy_id", "user_id"],
    )


def downgrade() -> None:
    op.drop_constraint(
        None,
        "favorites",
        type_="unique",
    )
