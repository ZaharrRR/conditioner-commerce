
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from db import Base


class ProductAttribute(Base):
    """Модель характеристик продукта в БД"""

    __tablename__ = "product_attributes"
    value: Mapped[str] = mapped_column(String(255), nullable=False)
    product_id: Mapped[UUID] = mapped_column(
        ForeignKey("products.id"), primary_key=True
    )
    attribute_id: Mapped[UUID] = mapped_column(
        ForeignKey("attributes.id"), primary_key=True
    )

    # Связи
    product: Mapped["Product"] = relationship("Product", back_populates="attributes")
    attribute: Mapped["Attribute"] = relationship(
        "Attribute", back_populates="products"
    )
