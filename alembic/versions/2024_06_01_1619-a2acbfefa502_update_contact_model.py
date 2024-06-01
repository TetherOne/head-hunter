"""update contact model

Revision ID: a2acbfefa502
Revises: 00f6096fcf6f
Create Date: 2024-06-01 16:19:27.120639

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2acbfefa502'
down_revision: Union[str, None] = '00f6096fcf6f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('contacts', 'phone',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('contacts', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)


def downgrade() -> None:
    op.alter_column('contacts', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('contacts', 'phone',
               existing_type=sa.VARCHAR(),
               nullable=False)
