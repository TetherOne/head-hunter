"""update vacansy table

Revision ID: 89615bad87f9
Revises: a2acbfefa502
Create Date: 2024-06-02 22:17:15.003798

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "89615bad87f9"
down_revision: Union[str, None] = "a2acbfefa502"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "vacancies",
        sa.Column(
            "experience",
            sa.String(),
            nullable=False,
        ),
    )
    op.add_column(
        "vacancies",
        sa.Column(
            "salary",
            sa.Integer(),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_column(
        "vacancies",
        "salary",
    )
    op.drop_column(
        "vacancies",
        "experience",
    )
