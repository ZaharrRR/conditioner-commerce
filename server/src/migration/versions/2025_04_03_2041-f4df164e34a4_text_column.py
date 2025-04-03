"""text column

Revision ID: f4df164e34a4
Revises: c239de277ed8
Create Date: 2025-04-03 20:41:23.439192

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f4df164e34a4'
down_revision: Union[str, None] = 'c239de277ed8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('products', 'description',
                    existing_type=sa.String(length=200),
                    type_=sa.Text(),
                    existing_nullable=True)
    op.alter_column('brands', 'description',
                    existing_type=sa.String(length=200),
                    type_=sa.Text(),
                    existing_nullable=True)


def downgrade() -> None:
    op.alter_column('products', 'description',
                    existing_type=sa.Text(),
                    type_=sa.String(200),
                    existing_nullable=True)
    op.alter_column('brands', 'description',
                    existing_type=sa.Text(),
                    type_=sa.String(200),
                    existing_nullable=True)
