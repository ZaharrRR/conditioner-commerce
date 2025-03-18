"""update nullable order_services

Revision ID: 30ed85ff82a6
Revises: 1a05ea88f4c6
Create Date: 2025-03-10 21:20:44.481808

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30ed85ff82a6'
down_revision: Union[str, None] = '1a05ea88f4c6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('order_services', 'order_id',
               existing_type=sa.UUID(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('order_services', 'order_id',
               existing_type=sa.UUID(),
               nullable=False)
    # ### end Alembic commands ###
