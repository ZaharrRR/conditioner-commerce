"""Update price type

Revision ID: b45a09c6fbce
Revises: ec52c2d2e94c
Create Date: 2025-01-26 21:54:57.731197

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "b45a09c6fbce"
down_revision: Union[str, None] = "ec52c2d2e94c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "products",
        "price",
        existing_type=sa.DOUBLE_PRECISION(precision=53),
        type_=sa.Numeric(precision=10, scale=2),
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "products",
        "price",
        existing_type=sa.Numeric(precision=10, scale=2),
        type_=sa.DOUBLE_PRECISION(precision=53),
        existing_nullable=False,
    )
    # ### end Alembic commands ###
