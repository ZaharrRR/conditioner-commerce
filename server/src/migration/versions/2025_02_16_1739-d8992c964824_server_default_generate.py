"""server default generate

Revision ID: d8992c964824
Revises: 2d308130b7ca
Create Date: 2025-02-16 17:39:33.092608

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import UUID

# revision identifiers, used by Alembic.
revision: str = 'd8992c964824'
down_revision: Union[str, None] = '2d308130b7ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";')
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "attributes",
        "id",
        existing_type=UUID(as_uuid=True),
        server_default=sa.text("uuid_generate_v4()"),
    )
    op.alter_column(
        "brands",
        "id",
        existing_type=UUID(as_uuid=True),
        server_default=sa.text("uuid_generate_v4()"),
    )
    op.alter_column(
        "categories",
        "id",
        existing_type=UUID(as_uuid=True),
        server_default=sa.text("uuid_generate_v4()"),
    )
    op.alter_column(
        "product_attributes",
        "id",
        existing_type=UUID(as_uuid=True),
        server_default=sa.text("uuid_generate_v4()"),
    )
    op.alter_column(
        "product_images",
        "id",
        existing_type=UUID(as_uuid=True),
        server_default=sa.text("uuid_generate_v4()"),
    )
    op.alter_column(
        "products",
        "id",
        existing_type=UUID(as_uuid=True),
        server_default=sa.text("uuid_generate_v4()"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("DROP EXTENSION IF EXISTS \"uuid-ossp\";")
    op.alter_column("attributes", "id", existing_type=UUID(as_uuid=True), server_default=None)
    op.alter_column("brands", "id", existing_type=UUID(as_uuid=True), server_default=None)
    op.alter_column("categories", "id", existing_type=UUID(as_uuid=True), server_default=None)
    op.alter_column("product_attributes", "id", existing_type=UUID(as_uuid=True), server_default=None)
    op.alter_column("product_images", "id", existing_type=UUID(as_uuid=True), server_default=None)
    op.alter_column("products", "id", existing_type=UUID(as_uuid=True), server_default=None)
