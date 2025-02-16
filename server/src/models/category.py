from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base


class Category(Base):
    """Модель Category в БД"""

    __tablename__ = "categories"
    name: Mapped[str] = mapped_column(String(225), unique=True, nullable=False)
    logo_url: Mapped[Optional[str]] = mapped_column(String(300), nullable=True)

    # Связь один-ко-многим c Product
    products: Mapped[list["Product"]] = relationship(
        "Product", back_populates="category", cascade="all, delete-orphan"
    )
