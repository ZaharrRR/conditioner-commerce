from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base


class Attribute(Base):
    """Модель Attribute в БД"""

    name: Mapped[str] = mapped_column(String(500), unique=True, nullable=False)

    # Связь
    products: Mapped[list["ProductAttribute"]] = relationship(
        "ProductAttribute", back_populates="attribute", cascade="all, delete-orphan"
    )
