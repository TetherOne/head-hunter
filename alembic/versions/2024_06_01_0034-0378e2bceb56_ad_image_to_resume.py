"""ad image to resume

Revision ID: 0378e2bceb56
Revises: ac9ade60440c
Create Date: 2024-06-01 00:34:33.097463

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0378e2bceb56'
down_revision: Union[str, None] = 'ac9ade60440c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('resumes', sa.Column('image', sa.String(), nullable=True,))


def downgrade() -> None:
    op.drop_column('resumes', 'image',)
