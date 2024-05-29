"""update vacansy to vacansies

Revision ID: 6aaeaf2097ec
Revises: 4ed76849369d
Create Date: 2024-05-29 19:54:14.125226

"""

from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "6aaeaf2097ec"
down_revision: Union[str, None] = "4ed76849369d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "vacancies",
        sa.Column("job_tittle", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("address", sa.String(), nullable=True),
        sa.Column("phone", sa.String(), nullable=True),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_table("vacancys")


def downgrade() -> None:
    op.create_table(
        "vacancys",
        sa.Column("job_tittle", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("description", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("address", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("phone", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("email", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name="vacancys_pkey"),
    )
    op.drop_table("vacancies")
