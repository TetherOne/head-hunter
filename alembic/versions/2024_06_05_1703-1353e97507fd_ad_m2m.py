"""ad m2m

Revision ID: 1353e97507fd
Revises: fe8c01363430
Create Date: 2024-06-05 17:03:31.257507

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "1353e97507fd"
down_revision: Union[str, None] = "fe8c01363430"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "favorites",
        sa.Column(
            "vacancy_id",
            sa.Integer(),
            nullable=False,
        ),
    )
    op.add_column(
        "favorites",
        sa.Column(
            "user_id",
            sa.Integer(),
            nullable=False,
        ),
    )
    op.create_foreign_key(
        None,
        "favorites",
        "vacancies",
        ["vacancy_id"],
        ["id"],
    )
    op.create_foreign_key(
        None,
        "favorites",
        "users",
        ["user_id"],
        ["id"],
    )


def downgrade() -> None:
    op.drop_constraint(
        None,
        "favorites",
        type_="foreignkey",
    )
    op.drop_constraint(
        None,
        "favorites",
        type_="foreignkey",
    )
    op.drop_column(
        "favorites",
        "user_id",
    )
    op.drop_column(
        "favorites",
        "vacancy_id",
    )
