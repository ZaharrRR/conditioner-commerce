from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, func, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(AsyncAttrs, DeclarativeBase):
    """Декларативный базовый класс"""

    __abstract__ = True

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid4,
        server_default=func.uuid_generate_v4()
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=text("timezone('UTC-5', now())"), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=text("timezone('UTC-5', now())"), onupdate=text("timezone('UTC-5', now())")
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"
