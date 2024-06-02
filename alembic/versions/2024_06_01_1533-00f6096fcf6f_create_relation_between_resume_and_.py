"""create relation between resume and contact

Revision ID: 00f6096fcf6f
Revises: 1e638bd242b7
Create Date: 2024-06-01 15:33:27.261833

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "00f6096fcf6f"
down_revision: Union[str, None] = "1e638bd242b7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "contacts",
        sa.Column(
            "resume_id",
            sa.Integer(),
            nullable=False,
        ),
    )
    op.create_unique_constraint(
        None,
        "contacts",
        ["resume_id"],
    )
    op.create_foreign_key(
        None,
        "contacts",
        "resumes",
        ["resume_id"],
        ["id"],
    )


def downgrade() -> None:
    op.drop_constraint(
        None,
        "contacts",
        type_="foreignkey",
    )
    op.drop_constraint(
        None,
        "contacts",
        type_="unique",
    )
    op.drop_column(
        "contacts",
        "resume_id",
    )
