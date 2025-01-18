from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from models import Base


class Brand(Base):
    """Модель Brand в БД"""
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    photo_url: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
