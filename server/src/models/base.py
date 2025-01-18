from uuid import uuid4, UUID
from datetime import datetime

from sqlalchemy import func, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(AsyncAttrs, DeclarativeBase):
    """Декларативный базовый класс"""
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid4
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = (mapped_column(
        DateTime(timezone=True), onupdate=func.now()
    )

    @declared_attr.directive)
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'